# JeffGeerling.com Drupal Codebase

![CI](https://github.com/geerlingguy/jeffgeerling-com/workflows/CI/badge.svg?branch=master&event=push)

This is the Drupal codebase that powers JeffGeerling.com.

## Local Environment

Make sure you have Docker and DDEV installed, then run the following commands (in the same directory as this README file):

    ddev restart

After setup is complete (assuming the site is installed), visit http://jeffgeerling-com.ddev.site/ to see the Drupal site.

### Installing Drupal

You can install Drupal using the install wizard, but we like to use Drush for more automation:

    ddev exec drush site:install minimal --db-url="mysql://db:db@ddev-jeffgeerling-com-db/drupal" --site-name="Jeff Geerling" --existing-config -y

> **Note**: It's preferred you store the database connection details in a separate `settings.local.php` file; otherwise, Drupal will try to stuff the connection details into the main `settings.php` file. Sensitive information like database passwords should _not_ be stored in this repository's `settings.php`.

### Migrating Content

First, make sure you have a local copy of the Drupal 7 database available; see the [drupal7db README](drupal7db/README.md) for setup instructions.

When you're ready to migrate content from the `drupal7` site database, run:

    ddev exec drush migrate-import --group=migrate_drupal_7

To update the migration configuration (basically reset the entire migration process):

  1. Delete all the `migrate*` files inside `config/sync`.
  2. Reinstall the site (see 'Installing Drupal' above).
  3. Run:

     ```
     ddev exec drush migrate-upgrade --legacy-db-key=drupal7 --legacy-root=https://www.jeffgeerling.com --configure-only
     ```

### Updating Configuration

Any time configuration is changed or any modules or Drupal is upgraded, you should export the site's configuration using the command:

    ddev exec drush config:export -y

And then push any changes to the Git repository before deploying the latest code to the site.
