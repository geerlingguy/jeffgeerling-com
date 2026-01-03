---
draft: true
date: '{{ .Date }}'
# lastmod: '{{ .Date }}'
# tags: ['tag_here']
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
slug: '{{ replace .File.ContentBaseName " " "-" | strings.ToLower }}'
# description: 'description_here'
---
