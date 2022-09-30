---
title: "Simple JavaScript Language Switcher"
date: 2022-07-26T10:00:00+08:00
lastmod: 2022-07-26T10:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "A simple solution to python — Pandas: ValueError: Worksheet index 0 is invalid, 0 worksheets found — Stack Overflow"
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["JavaScript", "Language Switcher", "Website", "Multilingualism", "Jquery"]
toc:
  enable: false
zhtw: false
---
![](https://miro.medium.com/max/1400/0*GH3zuK_2sRtvh66b)

Photo by  [KOBU Agency](https://unsplash.com/@kobuagency?utm_source=medium&utm_medium=referral)  on  [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

# javascript-language-switcher

after quite a bit of searching, I decided to create a naive one

you can just fork it to use it

simple  [demo](https://chienhsiang-hung.github.io/javascript-language-switcher/)

HTML
```html
<h1 class="en">JavaScript Language Switcher</h1>  
    <h1 class="tw">JS語言切換</h1>  
    <span class='en' onclick="switch_lang('.en', '.tw')">中文</span><span class='tw' onclick="switch_lang('.tw', '.en')">EN</span>
```
JS
```javascript
window.onload = switch_lang('.tw', '.en');function switch_lang(hide_lan, show_lan){  
  $(hide_lan).hide();  
  $(show_lan).show();  
}
```
Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)