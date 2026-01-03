---
draft: true
date: '{{ .Date }}'
# lastmod: '{{ .Date }}'
# tags:
# - tag1
# - tag2
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
slug: '{{ replace .File.ContentBaseName " " "-" | strings.ToLower }}'
# description: 'description_here'
---
