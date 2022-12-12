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
*Use [Best HTML Viewer, HTML Beautifier, HTML Formatter and to Test / Preview HTML Output (codebeautify.org)](https://codebeautify.org/htmlviewer) beautifier to view `html`.*

We can simply use `Pandas.read_html()` to read the tables inside a given `html`.

> If you ever faced the problem `UnicodeDecodeError: 'cp950' codec can't decode byte 0xe2 in position 4204: illegal multibyte sequence`
>
> Simply add a parameter `encoding="utf-8"` to the `open`.[^how-do-i-fix-this-cp950-illegal-multibyte-sequence-unicodedecodeerror-when-rea]

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
## Transpose/Transform
![Transpose-or-Transform-the-table](Transpose-or-Transform-the-table.png "Transpose-or-Transform-the-table.png")

A simple and intuitive approach will be


[^how-do-i-fix-this-cp950-illegal-multibyte-sequence-unicodedecodeerror-when-rea]: [python - How do I fix this cp950 "illegal multibyte sequence" UnicodeDecodeError when reading a text file? - Stack Overflow](https://stackoverflow.com/questions/49021589/how-do-i-fix-this-cp950-illegal-multibyte-sequence-unicodedecodeerror-when-rea)