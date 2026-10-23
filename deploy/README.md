# Deploy

`deploy-site.sh` builds the site on the webserver and deploys it to `/var/www/www.jeffgeerling.com`.

It pulls `master`, builds with Hugo into a staging directory, runs a sanity check, rsyncs changed files to the webroot, then purges Cloudflare.

## Usage

```
git push && ssh sshjg.jeffgeerling.com ./deploy-site.sh
```

| Option | Effect |
| --- | --- |
| `--force` | Skip the size/file-count gate |
| `--no-purge` | Skip Cloudflare purge |
| `--rollback` | Restore the site as it was before the last deploy |
| `--rebuild` | Deploy even if the commit is already live |
| `https://...` | Extra URL(s) to purge |

## Server setup (one-time)

The `mm` Ansible playbook should already set this stuff up, but here are some manual commands if needed:

```
sudo apt install -y git rsync curl
sudo chown -R geerlingguy:geerlingguy /var/www/www.jeffgeerling.com
install -m 700 deploy-site.sh ~/deploy-site.sh
install -m 600 /dev/null ~/.config/jeffgeerling-deploy.env
```

Contents of `~/.config/jeffgeerling-deploy.env`:

```
CLOUDFLARE_ZONE_ID=...
CLOUDFLARE_PURGE_TOKEN=...   # token with cache_purge permission
HUGO_VERSION=0.xxx.x         # match local `hugo version`
```

Run the script as the deploy user, not root. Hugo extended is installed automatically if it's missing (this step uses `sudo`).

## Safety checks

- Nothing is deployed if the build fails or is missing `index.html`, `blog/index.html`, `blog.xml` or `sitemap.xml`.
- Nothing is deployed if total size changes by more than 15% or the file count by more than 10% (override these with `MAX_SIZE_DELTA_PCT` and `MAX_COUNT_DELTA_PCT`).
- If `origin/master` matches the last deployed commit (stored in `~/.jeffgeerling-deployed-commit`), the script exits immediately.
- `.well-known/` in the webroot is never touched.
- The checkout in `~/jeffgeerling-com` is hard-reset on every run, so don't edit files there.