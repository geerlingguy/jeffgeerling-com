# Drupal Export to Hugo

See: https://github.com/geerlingguy/jeffgeerling-com/issues/158

## Migration Steps

First make sure you have an updated dump of the entire production database running locally, accessible to the `mariadb` or `mysql` cli.

### 1 - Export Blog Posts to CSV

Run `drupal_export.py` to export the all blog posts to a CSV file:

```
pip3 install pymysql --break-system-packages
python3 drupal_export.py > blog_export.csv
```

### 2 - Process Blog Posts (convert to Hugo Markdown)

Run the `csv_to_hugo.py` Python script to generate blog entries:

```
pip3 install markdownify html2text --break-system-packages
python3 csv_to_hugo.py --csv blog_export.csv --out ./hugo_content
```

This will take a while the first time it runs, as it needs to download all images referenced in the posts.

### 3 - Download referenced files (non-image)

Run the `hugo_file_refs_dl.py` script:

```
pip3 install requests --break-system-packages
./hugo_file_refs_dl.py --dry-run
```

Run again without `--dry-run` if you want to actually download files and update the text in the Hugo posts.
