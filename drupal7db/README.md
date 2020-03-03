# Drupal 7 Database migration Docker Compose file

This directory contains a Docker Compose file that starts a MySQL instance running locally on port 3307 that can be used for the migration of the JeffGeerling.com Drupal 7 database.

Start this instance with:

    docker-compose up -d

See the environment variables in `docker-compose.yml` for database connection details.

## Why a separate docker-compose?

Well, during migration, this will be useful, but after the migration is complete, we can basically throw this away. Easier to delete this directory than to untangle anything from the main `docker-compose.yml` file.
