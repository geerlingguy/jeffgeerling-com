#!/usr/bin/env bash
#
# Build and deploy www.jeffgeerling.com on the webserver.
#
# Usage:
#   deploy-site.sh [--force] [--no-purge] [extra URLs to purge...]
#   deploy-site.sh --rollback
#
#   --force     Skip the size/file-count sanity gate (required files still checked).
#   --no-purge  Don't purge Cloudflare cache.
#   --rollback  Restore the site as it was before the last deploy.
#   --rebuild   Build and deploy even if the commit is already deployed.
#
# Config/secrets are read from $ENV_FILE (default ~/.config/jeffgeerling-deploy.env).
# Run as the deploy user (not root).

set -euo pipefail

ENV_FILE="${ENV_FILE:-$HOME/.config/jeffgeerling-deploy.env}"
# shellcheck source=/dev/null
[[ -r "$ENV_FILE" ]] && source "$ENV_FILE"

REPO_URL="${REPO_URL:-https://github.com/geerlingguy/jeffgeerling-com.git}"
BRANCH="${BRANCH:-master}"
SRC_DIR="${SRC_DIR:-$HOME/jeffgeerling-com}"
BUILD_DIR="${BUILD_DIR:-$HOME/jeffgeerling-com-build}"
PREV_DIR="${PREV_DIR:-$HOME/jeffgeerling-com-prev}"   # Snapshot of last live site.
STATE_FILE="${STATE_FILE:-$HOME/.jeffgeerling-deployed-commit}"
WEB_ROOT="${WEB_ROOT:-/var/www/www.jeffgeerling.com}"
HUGO_VERSION="${HUGO_VERSION:-}"   # Pin to match `hugo version` on your Mac.
MAX_SIZE_DELTA_PCT="${MAX_SIZE_DELTA_PCT:-15}"
MAX_COUNT_DELTA_PCT="${MAX_COUNT_DELTA_PCT:-10}"
REQUIRED_FILES=(index.html blog/index.html blog.xml sitemap.xml)

CLOUDFLARE_ZONE_ID="${CLOUDFLARE_ZONE_ID:-}"
CLOUDFLARE_PURGE_TOKEN="${CLOUDFLARE_PURGE_TOKEN:-}"
PURGE_URLS=(
  https://www.jeffgeerling.com
  https://www.jeffgeerling.com/
  https://www.jeffgeerling.com/blog/
  https://www.jeffgeerling.com/blog.xml
)

FORCE=0; PURGE=1; ROLLBACK=0; REBUILD=0
for arg in "$@"; do
  case "$arg" in
    --force) FORCE=1 ;;
    --no-purge) PURGE=0 ;;
    --rollback) ROLLBACK=1 ;;
    --rebuild) REBUILD=1 ;;
    http*://*) PURGE_URLS+=("$arg") ;;
    *) echo "Unknown argument: $arg" >&2; exit 2 ;;
  esac
done

log() { printf '[%s] %s\n' "$(date +%T)" "$*"; }
die() { log "ERROR: $*" >&2; exit 1; }

[[ $EUID -ne 0 ]] || die "Run as the deploy user, not root (keeps ownership sane)."
for cmd in git rsync curl flock; do
  command -v "$cmd" >/dev/null 2>&1 || die "Missing '$cmd' (sudo apt install -y $cmd)."
done
[[ -d "$WEB_ROOT" && -w "$WEB_ROOT" ]] || die "$WEB_ROOT missing or not writable by $(whoami)."

# Only one deploy at a time.
exec 9>"${XDG_RUNTIME_DIR:-/tmp}/jeffgeerling-deploy.lock"
flock -n 9 || die "Another deploy is already running."

sync_to_webroot() {
  # --checksum: Hugo rewrites every file, so mtimes are useless; only copy
  # files whose content changed (keeps mtimes/ETags stable for caching).
  rsync -a --delete --checksum --chmod=D755,F644 \
    --exclude '.well-known/' \
    "$1"/ "$WEB_ROOT"/
}

purge_cloudflare() {
  [[ $PURGE -eq 1 ]] || { log "Skipping Cloudflare purge."; return; }
  if [[ -z "$CLOUDFLARE_ZONE_ID" || -z "$CLOUDFLARE_PURGE_TOKEN" ]]; then
    log "WARNING: Cloudflare vars not set in $ENV_FILE; skipping purge."
    return
  fi
  local json
  json=$(printf '"%s",' "${PURGE_URLS[@]}")
  json="{\"files\":[${json%,}]}"
  log "Purging Cloudflare cache for ${#PURGE_URLS[@]} URLs..."
  curl -fsS -X POST \
    "https://api.cloudflare.com/client/v4/zones/${CLOUDFLARE_ZONE_ID}/purge_cache" \
    -H "Authorization: Bearer ${CLOUDFLARE_PURGE_TOKEN}" \
    -H "Content-Type: application/json" \
    --data "$json" | grep -q '"success":[[:space:]]*true' \
    || die "Cloudflare purge failed."
}

if [[ $ROLLBACK -eq 1 ]]; then
  [[ -f "$PREV_DIR/index.html" ]] || die "No previous build at $PREV_DIR."
  log "Rolling back to snapshot taken before the last deploy..."
  sync_to_webroot "$PREV_DIR"
  purge_cloudflare
  rm -f "$STATE_FILE"   # Next normal run will redeploy.
  log "Rollback complete."
  exit 0
fi

# --- 1. Install Hugo (extended) if missing ---------------------------------
if ! command -v hugo >/dev/null 2>&1; then
  if [[ -z "$HUGO_VERSION" ]]; then
    HUGO_VERSION=$(curl -fsSL https://api.github.com/repos/gohugoio/hugo/releases/latest \
      | grep -oP '"tag_name":\s*"v\K[^"]+')
    log "HUGO_VERSION not pinned; using latest (${HUGO_VERSION})."
  fi
  arch=$(dpkg --print-architecture)
  deb="/tmp/hugo_extended_${HUGO_VERSION}_linux-${arch}.deb"
  log "Installing Hugo extended ${HUGO_VERSION} (${arch})..."
  curl -fsSL -o "$deb" \
    "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-${arch}.deb"
  sudo dpkg -i "$deb"
  rm -f "$deb"
elif [[ -n "$HUGO_VERSION" ]] && ! hugo version | grep -q "v${HUGO_VERSION}"; then
  log "WARNING: installed Hugo ($(hugo version | awk '{print $2}')) != pinned v${HUGO_VERSION}."
fi

# --- 2. Get latest source ---------------------------------------------------
if [[ ! -d "$SRC_DIR/.git" ]]; then
  log "Cloning $REPO_URL..."
  git clone --branch "$BRANCH" "$REPO_URL" "$SRC_DIR"
fi
log "Updating source to origin/$BRANCH..."
git -C "$SRC_DIR" fetch --quiet origin "$BRANCH"
new_commit=$(git -C "$SRC_DIR" rev-parse "origin/$BRANCH")
if [[ $REBUILD -eq 0 && -f "$STATE_FILE" && "$(cat "$STATE_FILE")" == "$new_commit" ]]; then
  log "${new_commit:0:7} is already deployed; nothing to do (use --rebuild to force)."
  exit 0
fi
git -C "$SRC_DIR" reset --hard --quiet "origin/$BRANCH"
git -C "$SRC_DIR" clean -fdq
if [[ -f "$SRC_DIR/.gitmodules" ]]; then
  git -C "$SRC_DIR" submodule update --init --recursive --quiet
fi
log "At $(git -C "$SRC_DIR" log -1 --format='%h %s')"

# --- 3. Build into a staging dir (never straight into the webroot) ----------
log "Building site..."
(cd "$SRC_DIR" && hugo --gc --minify --cleanDestinationDir --destination "$BUILD_DIR") \
  || die "Hugo build failed; nothing deployed."

# --- 4. Sanity gate ---------------------------------------------------------
for f in "${REQUIRED_FILES[@]}"; do
  [[ -s "$BUILD_DIR/$f" ]] || die "Build is missing $f; nothing deployed."
done

new_size=$(du -sb "$BUILD_DIR" | cut -f1)
new_count=$(find "$BUILD_DIR" -type f | wc -l)
old_size=$(du -sb --exclude='.well-known' "$WEB_ROOT" | cut -f1)
old_count=$(find "$WEB_ROOT" -type f -not -path '*/.well-known/*' | wc -l)

pct_delta() { # abs % change from $1 (old) to $2 (new)
  awk -v o="$1" -v n="$2" 'BEGIN { if (o == 0) { print 0; exit } d = (n - o) * 100 / o; printf "%.1f", (d < 0 ? -d : d) }'
}
size_delta=$(pct_delta "$old_size" "$new_size")
count_delta=$(pct_delta "$old_count" "$new_count")
log "Size:  $(numfmt --to=iec "$old_size") -> $(numfmt --to=iec "$new_size") (${size_delta}%)"
log "Files: ${old_count} -> ${new_count} (${count_delta}%)"

if [[ $old_count -gt 0 && $FORCE -eq 0 ]]; then
  awk -v a="$size_delta" -v b="$MAX_SIZE_DELTA_PCT" 'BEGIN { exit !(a > b) }' \
    && die "Size changed more than ${MAX_SIZE_DELTA_PCT}%; re-run with --force if expected."
  awk -v a="$count_delta" -v b="$MAX_COUNT_DELTA_PCT" 'BEGIN { exit !(a > b) }' \
    && die "File count changed more than ${MAX_COUNT_DELTA_PCT}%; re-run with --force if expected."
fi

# --- 5. Deploy --------------------------------------------------------------
log "Snapshotting live site to $PREV_DIR (for --rollback)..."
rsync -a --delete --exclude '.well-known/' "$WEB_ROOT"/ "$PREV_DIR"/
log "Syncing build to $WEB_ROOT..."
sync_to_webroot "$BUILD_DIR"

echo "$new_commit" > "$STATE_FILE"

purge_cloudflare
log "Deploy complete."
