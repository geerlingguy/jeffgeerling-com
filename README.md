# JeffGeerling.com Drupal Codebase

![CI](https://github.com/geerlingguy/jeffgeerling-com/workflows/CI/badge.svg?branch=master&event=push)

This is the Drupal codebase that powers JeffGeerling.com.

## Local Environment

The first time you start using this project, you need to create your local settings file:

    cp web/sites/default/example.settings.local.php web/sites/default/settings.local.php

Make sure you have Docker installed, then run the following command (in the same directory as this README file):

    docker-compose up -d

Visit http://localhost/ to see the Drupal installation.

> Note: This `docker-compose.yml` configuration uses an NFS mount for better performance on macOS. You need to ensure [NFS is configured properly on your Mac](https://github.com/geerlingguy/jeffgeerling-com/issues/22#issuecomment-597891217) or you'll get errors when you build the environment.
> 
> If you're on Linux or want to skip configuring NFS, you can use the `docker-compose.override.yml` file inside `.github/` instead of the one included in the root of the repo.

### Installing Drupal

You can install Drupal using the install wizard, but we like to use Drush for more automation:

    docker-compose exec drupal bash -c 'drush site:install minimal --db-url="mysql://drupal:$DRUPAL_DATABASE_PASSWORD@$DRUPAL_DATABASE_HOST/drupal" --site-name="Jeff Geerling" --existing-config -y'

> **Note**: It's preferred you store the database connection details in a separate `settings.local.php` file; otherwise, Drupal will try to stuff the connection details into the main `settings.php` file. Sensitive information like database passwords should _not_ be stored in this repository's `settings.php`.

### Migrating Content

First, make sure you have a local copy of the Drupal 7 database available; see the [drupal7db README](drupal7db/README.md) for setup instructions.

When you're ready to migrate content from the `drupal7` site database, run:

    docker-compose exec drupal bash -c 'drush migrate-import --group=migrate_drupal_7'

To update the migration configuration (basically reset the entire migration process):

  1. Delete all the `migrate*` files inside `config/sync`.
  2. Reinstall the site (see 'Installing Drupal' above).
  3. Run:

     ```
     docker-compose exec drupal bash -c 'drush migrate-upgrade --legacy-db-key=drupal7 --legacy-root=https://www.jeffgeerling.com --configure-only'
     ```

### Updating Configuration

Any time configuration is changed or any modules or Drupal is upgraded, you should export the site's configuration using the command:

    docker-compose exec drupal bash -c 'drush config:export -y'

And then push any changes to the Git repository before deploying the latest code to the site.
