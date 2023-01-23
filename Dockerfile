ARG DRUPAL_BASE_IMAGE=geerlingguy/drupal:latest-arm64

# PHP Dependency install via Composer.
FROM composer as vendor

# Build the Docker image for Drupal.
FROM $DRUPAL_BASE_IMAGE

# TODO: Change this.
ENV DRUPAL_MD5 aedc6598b71c5393d30242b8e14385e5

# Copy precompiled codebase into the container.
COPY --from=vendor /app/ /var/www/html/

# Download mhsendmail and use it for PHP's sendmail_path.
RUN curl -OL https://github.com/mailhog/mhsendmail/releases/download/v0.2.0/mhsendmail_linux_amd64 \
 && chmod +x mhsendmail_linux_amd64 \
 && mv mhsendmail_linux_amd64 /usr/local/bin/mhsendmail
RUN sed -i '\|sendmail_path|c\sendmail_path = "/usr/local/bin/mhsendmail --smtp-addr=mailhog:1025"' /etc/php/8.1/apache2/php.ini
RUN sed -i '\|sendmail_path|c\sendmail_path = "/usr/local/bin/mhsendmail --smtp-addr=mailhog:1025"' /etc/php/8.1/cli/php.ini

# Add Drush Launcher.
RUN curl -OL https://github.com/drush-ops/drush-launcher/releases/download/0.10.0/drush.phar \
 && chmod +x drush.phar \
 && mv drush.phar /usr/local/bin/drush

# Adjust the Apache docroot.
ENV APACHE_DOCUMENT_ROOT=/var/www/html/web

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
