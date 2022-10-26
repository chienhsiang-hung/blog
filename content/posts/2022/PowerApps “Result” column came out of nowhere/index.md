---
title: "PowerApps “Result” column came out of nowhere"
date: 2022-10-26T10:36:00+08:00
lastmod: 2022-10-26T10:36:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Column does not exist. The column with the most similar name is …"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Powerapps", "Sharepoint", "Patch", "Connecting To Data", "Collection"]
toc:
  enable: true
zhtw: false
---
## Column does not exist. The column with the most similar name is …

When I tried to  `Patch()`  a collection to SharePoint, It kept showing

> Column does not exist. The column with the most similar name is …

in which the collection is collected by  `Defaults(someSharePoint)`. And I never add or delete any column in the collection. So this error seems nonsense to me.  **Though, when I check the collection, the extra column does appear somehow**.

![](https://miro.medium.com/max/646/1*7Fh0Wy9iy8dZ1HoOEJu3bQ.png)

[Solved: Fail to recognize column, but its there — Power Platform Community (microsoft.com)](https://powerusers.microsoft.com/t5/Building-Power-Apps/Fail-to-recognize-column-but-its-there/td-p/554530)

Usually, when this happens, we just reconnect the SharePoint or check the real field name by looking into the list setting.

![](https://miro.medium.com/max/700/1*AUCDtibw8z7yQTg7fZGfuw.png)

But this time, it just wouldn’t wrok. It even popped up a new problem.

![](https://miro.medium.com/max/351/1*3ee_SSy-uS4uwB5rtzmOEg.png)

## Check the Collection

So, I checked the collection and found this very “Result” column came out of nowhere.

![](https://miro.medium.com/max/700/1*j13oMjyzxXKXQd5mhsxbcA.png)

## Just Remove It

Brute force solution. I tried to just simply remove it but failed again. Somehow it appeared after  `ClearCollect()`.

![](https://miro.medium.com/max/700/1*dINSIO20a6HymoJIzAdkNQ.png)

So the final solution came clear, we need to make the collection

## Placed Directly in Where You Need it

![](https://miro.medium.com/max/700/1*ON4onbs-FSmVCmZTXP6erQ.png)

No error messages shown and it’s running flawlessly!