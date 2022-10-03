---
title: "Power Automate List Rows Column Null (List Rows Filter Empty update)"
date: 2022-09-08
lastmod: 2022-09-08
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "According to out last tutorial - Power Automate List Rows Filter Empty and Update Row NotFound. | by 洪健翔 Hung, Chien-hsiang | Sep, 2022 |…"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Power Automate", "List Rows", "Column Null", "Filter Empty", "Check Null Value"]
toc:
  enable: false
zhtw: false
---
According to out last tutorial -  [Power Automate List Rows Filter Empty and Update Row NotFound. | by 洪健翔 Hung, Chien-hsiang | Sep, 2022 | Medium](https://hungchienhsiang.medium.com/power-automate-list-rows-filter-empty-and-update-row-notfound-cecd4ec37bf6), we stated that we can use  `ColumnName ne ‘’`  to filter the empty row. Though sometimes it doesn’t work. Here is a simple solution.

![](https://miro.medium.com/max/1400/0*0qxPfU3z3fc0-go-.png)

**Just change** `**ColumnName ne ‘’**` **to** `**ColumnName ne null**` **it worked!**

![](https://miro.medium.com/max/1254/0*iAqGhs2syxbppVDo.png)

[How To Check Null Value In ODATA Filter Of Get Items Action In FLOW (c-sharpcorner.com)](https://www.c-sharpcorner.com/blogs/how-to-check-null-value-in-odata-filter-of-get-items-action-in-flow)  by  [Sarvesh Shinde](https://www.c-sharpcorner.com/members/sarvesh-shinde2)

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)