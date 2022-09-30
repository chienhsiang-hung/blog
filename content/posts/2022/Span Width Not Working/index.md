---
title: "Span Width Not Working"
date: 2022-08-04T04:00:00+08:00
lastmod: 2022-08-04T04:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Span is an inline element. It has no width or height."
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["HTML", "Span", "Span Width", "CSS", "Style"]
toc:
  enable: false
zhtw: false
---
Span is an inline element. It has no width or height.
```html
<div id='box' style='  
  background: black;  
  border-radius: 15px;  
  top: 4%;  
  left: 2%;  
  width: 96%;  
  height: 94%;  
  position: absolute;  
'><span style='color:white; width:100%; text-align:right;'>test</span></div>
```
Things like this won’t work. You need to change the style of a  `span`  to something like below.
```html
<div id='box' style='  
  background: black;  
  border-radius: 15px;  
  top: 4%;  
  left: 2%;  
  width: 96%;  
  height: 94%;  
  position: absolute;  
'><span style='color:white; width:100%; **display:inline-block;** text-align:right;'>test</span></div>
```
![](https://miro.medium.com/max/1400/1*QShqdyN82RpVk6iUD09Sww.png)

And it worked!

According to  [Basheer AL-MOMANI](https://stackoverflow.com/users/4251431/basheer-al-momani)  ([css — Does height and width not apply to span? — Stack Overflow](https://stackoverflow.com/questions/2491068/does-height-and-width-not-apply-to-span/2491072#2491072)): You could turn it into a block-level element, then it will accept your dimension directives.

contact me  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)