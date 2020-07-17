ARG DRUPAL_BASE_IMAGE=geerlingguy/drupal:latest

# PHP Dependency install via Composer.
FROM composer as vendor

# TODO: For production, copy composer files and web dir.
# COPY composer.json composer.json
# COPY composer.lock composer.lock
# COPY web/ web/

# TODO: For production, install dependencies inside container.
# RUN composer install \
#     --ignore-platform-reqs \
#     --no-interaction \
#     --no-dev \
#     --prefer-dist

# Build the Docker image for Drupal.
FROM $DRUPAL_BASE_IMAGE

# TODO: Change this.
ENV DRUPAL_MD5 aedc6598b71c5393d30242b8e14385e5

# Copy precompiled codebase into the container.
COPY --from=vendor /app/ /var/www/html/

# TODO: For production, copy config in place.
# Copy other required configuration into the container.
# COPY config/ /var/www/html/config/
# COPY load.environment.php /var/www/html/load.environment.php
# COPY jeffgeerling.settings.php /var/www/html/web/sites/default/settings.php

# TODO: For production, set file permissions properly.
# Make sure file ownership is correct on the document root.
# RUN chown -R www-data:www-data /var/www/html/web

# TODO: Only do this in development, not production.
# Download mhsendmail and use it for PHP's sendmail_path.
RUN curl -OL https://github.com/mailhog/mhsendmail/releases/download/v0.2.0/mhsendmail_linux_amd64 \
 && chmod +x mhsendmail_linux_amd64 \
 && mv mhsendmail_linux_amd64 /usr/local/bin/mhsendmail
RUN sed -i '\|sendmail_path|c\sendmail_path = "/usr/local/bin/mhsendmail --smtp-addr=mailhog:1025"' /etc/php/7.4/apache2/php.ini
RUN sed -i '\|sendmail_path|c\sendmail_path = "/usr/local/bin/mhsendmail --smtp-addr=mailhog:1025"' /etc/php/7.4/cli/php.ini

# Add Drush Launcher.
RUN curl -OL https://github.com/drush-ops/drush-launcher/releases/download/0.6.0/drush.phar \
 && chmod +x drush.phar \
 && mv drush.phar /usr/local/bin/drush

# Adjust the Apache docroot.
ENV APACHE_DOCUMENT_ROOT=/var/www/html/web

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
