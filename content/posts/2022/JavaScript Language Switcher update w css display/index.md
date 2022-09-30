---
title: "JavaScript Language Switcher update w/ css display"
date: 2022-08-09
lastmod: 2022-08-09
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Simple JavaScript Language Switcher, use javascript switch language."
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["JavaScript", "Jquery", "Multilingual Websites", "Language Switcher", "CSS"]
toc:
  enable: false
zhtw: false
---
Simple JavaScript Language Switcher, use javascript switch language.

![](https://miro.medium.com/max/1400/0*2egHHaPC7kdekiEf)

Photo by  [Markus Winkler](https://unsplash.com/@markuswinkler?utm_source=medium&utm_medium=referral)  on  [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

after quite a bit of searching, I decided to create a naive one

you can just  [fork](https://github.com/chienhsiang-hung/javascript-language-switcher/fork)  it to use it

simple  [demo](https://chienhsiang-hung.github.io/javascript-language-switcher/)

# jQuery Hide & Show

At the first I thought I can use jQuery’s  `.hide()`  and  `.show()`  to achieve the result I want.

# First Naive Version

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
Then I quickly found that the user with javascript disabled or slow load in would result in seeing the  [original HTML](https://chienhsiang-hung.github.io/javascript-language-switcher/)  w/ multiple langs not being hidden.

So I’ve tried to initialize the hidden lang by set CSS  `visible`  to  `hidden`.

# CSS Visibility
```css
.tw {visibility: hidden;}  
.en {visibility: visible;}
```
But it resulted in a  [disordered layout](https://chienhsiang-hung.github.io/javascript-language-switcher/css-visible.html).(You can regard it as what when we set the  `colour: white;`  to cover something up)  
Finally with the help of another style attribution,  `display`, I am able to achieve what I want - to set up a multilingual site and handle the error when users have a low load-in speed or JS disabled.

# CSS Display
```css
.tw {display: none;}
```
Result:  [Simple JavaScript Language Switcher w/ css display (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/javascript-language-switcher/css-display.html)

# How to use it

_The example was shown for TW-EN site._

Set up your HTML like  [this](https://chienhsiang-hung.github.io/javascript-language-switcher/css-display.html):
```html
<h1  class="mt-5 en">Simple JavaScript Language Switcher w/ css display</h1>  
<h1  class="mt-5 tw">藉由CSS實現簡易JS語言切換</h1>  
<span  class='en'  onclick="switch_lang('.en', '.tw')">中文</span><span  class='tw'  onclick="switch_lang('.tw', '.en')">EN</span>
```
Put this in  `<head>`  part of your HTML:
```html
<link href="https://chienhsiang-hung.github.io/javascript-language-switcher/src/css/switch-lang-display.css" rel="stylesheet">
```
And this in  `<body>`  part of you HTML:
```html
<script src='https://chienhsiang-hung.github.io/javascript-language-switcher/src/js/switch-lang-no-onload.js'></script>
```
# Support

It’s always appreciated if you would like to  [buy me a cofee](https://ko-fi.com/chienhsianghung)  to support this API. Thank you :)

contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)