# JeffGeerling.com Drupal Codebase

This is the Drupal codebase that powers JeffGeerling.com.

## Local Environment

Make sure you have Docker installed, then run the following commands (in the same directory as this README file):

  1. Build the local Drupal docker image:

     ```
     docker build -t jeffgeerling-com:latest .
     ```

  2. Start the local development environment with Docker Compose:

     ```
     docker-compose up -d
     ```

After the environment is running, you can visit http://localhost/ and see the Drupal site.

### Installing Drupal

You can install Drupal using the install wizard, but we like to use Drush for more automation:

    docker-compose exec drupal bash -c 'drush site:install minimal --db-url="mysql://drupal:$DRUPAL_DATABASE_PASSWORD@$DRUPAL_DATABASE_HOST/drupal" --site-name="Jeff Geerling" --existing-config -y'

### Migrating Content

When you're ready to migrate content from the `drupal7` site database, run:

    docker-compose exec drupal bash -c 'drush migrate-import --group=migrate_drupal_7'

### Updating Configuration

Any time configuration is changed or any modules or Drupal is upgraded, you should export the site's configuration using the command:

    docker-compose exec drupal bash -c 'drush config:export -y'

And then push any changes to the Git repository before deploying the latest code to the site.
