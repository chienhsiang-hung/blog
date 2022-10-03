---
title: "CSS Bottom to The Parent | PowerApps HtmlText"
date: 2022-09-20T00:00:00+08:00
lastmod: 2022-09-20T00:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "How to achieve something like the example above? This should work well in most browsers but Power Apps."
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["CSS", "Display", "Position", "Relative", "Absolute"]
toc:
  enable: true
zhtw: false
---
![](https://miro.medium.com/max/1400/1*X_Ayku5urkIfVkQq8RA4ww.png)

How to achieve something like the example above? This should work well in most browsers but Power Apps.

*(notice `calc(100% — 3em);` syntex, put `-` between spaces)* (# css height 100% — upper div)
```html
<div style='  
     position: relative;  
     width: 100%;  
     height: calc(100% - 100px);  
     max-width: 640px;  
     margin-left: auto;  
     margin-right: auto;  
    '>  
        <h2 style='  
        position: absolute;  
        bottom: 0;  
        right: 20px;  
        color: white;  
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.5);  
        text-align: right;  
    '><u>Skip</u></h2>
```
But because the inner div is positioned absolutely, you’ll always have to worry about other content in the outer div overlapping it (and you’ll always have to set fixed heights). by  [Jon Smock](https://stackoverflow.com/users/25538/jon-smock),  [j08691](https://stackoverflow.com/users/616443/j08691)

[css — How can I send an inner \<div> to the bottom of its parent \<div>? — Stack Overflow](https://stackoverflow.com/questions/2147303/how-can-i-send-an-inner-div-to-the-bottom-of-its-parent-div)

## In Power Apps you need to change it to:
```html
<div style='  
    position: relative;  
    width: 100%;  
    max-width: 740px;  
    height: "&Parent.Height&"px;  
    margin-left: auto;  
    margin-right: auto;  
'>  
    <h3 style='  
        position: absolute;  
        bottom: 20px;  
        right: 20px;  
        color: white;  
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.5);  
        font-family: "&Char(34)&"Montserrat"&Char(34)&", sans-serif;  
        text-align: right;  
        cursor: pointer;  
    '>  
        <u>Skip</u>  
    </h3>  
</div>
```
![](https://miro.medium.com/max/1132/1*wt-sBUKF01gLAHycsk_N2Q.png)

The major difference is  `height: calc(100% — 100px);`  to  `height: “&Parent.Height&”px;`  due to the limitation in Power Apps  **HtmlText.**

![](https://miro.medium.com/max/968/1*gddI2Nv-EBAxi8BPYgds4Q.png)

It works well after the change!

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)