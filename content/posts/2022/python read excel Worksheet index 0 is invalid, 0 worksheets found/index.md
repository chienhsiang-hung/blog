---
title: "python read excel Worksheet index 0 is invalid, 0 worksheets found"
date: 2022-07-26
lastmod: 2022-07-26
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "A simple solution to python — Pandas: ValueError: Worksheet index 0 is invalid, 0 worksheets found — Stack Overflow"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Python", "Pandas", "Excel", "Worksheet", "Read Excel File"]
toc:
  enable: false
zhtw: false
---
![](https://miro.medium.com/max/1400/1*FAGWIm_mhdqVz-CXtEWhHg.png)

A simple solution to  [python — Pandas: ValueError: Worksheet index 0 is invalid, 0 worksheets found — Stack Overflow](https://stackoverflow.com/questions/69948897/pandas-valueerror-worksheet-index-0-is-invalid-0-worksheets-found)

1.  Check your target file
2.  find the sheet’s name

![](https://miro.medium.com/max/726/1*LVZ0ZWG2UxYfXUbeAq8OeA.png)

3. launch a new blank excel

4. find the sheet’s name

![](https://miro.medium.com/max/738/1*_87mu4KBYmV9bRIfIc4t_A.png)

If they have a different default worksheet name, close all Excels, and regenerate the target excel. (The default worksheet name would be switched back to normal)

Now re  `pd.read_excel`  again. It’ll be successful.

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)