---
title: "Python Extract HTML Table (Convert to Pandas DataFrame) Tutorial"
date: 2022-12-12T08:21:00+08:00
lastmod: 2022-12-12T08:21:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: ""
resources:
- name: "featured-image"
  src: ""
tags: [""]
toc:
  enable: true
---
## Examine the HTML
We can simply use `Pandas.read_html()` to read the tables inside a given `html`.

But, what if we have a `HTML` body that has **nested tables**.
```html
<table ...>
  <th>
    <table ...>
      ...
```
![nested tables](featured-image.png "nested tables")

We can play with the string by finding the n-th occurence `'<table'` to filter out the unwanted `<table>`. Then use the `header` parameter to anchor the right header.

But how can we transform the table to the format we want?