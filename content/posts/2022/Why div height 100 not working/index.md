---
title: "Why div height 100 not working?"
date: 2022-08-17
lastmod: 2022-08-17
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "In order for a percentage value to work for height, the parent’s height must be determined. The only exception is the root element \u003Chtml\u003E…"
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["CSS", "HTML", "Div Height", "Screen Height", "Height 100"]
toc:
  enable: false
zhtw: false
---
![](https://miro.medium.com/max/1400/0*4HIOoTmqaDQUOh0n)

Photo by  [Maik Jonietz](https://unsplash.com/@der_maik_?utm_source=medium&utm_medium=referral)  on  [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

In order for a percentage value to work for height, the parent’s height must be determined. The only exception is the  **root**  element  `<html>`, which can be a percentage height. .

So, you’ve given all of your elements height, except for the  `<html>`, so what you should do is add this:
```html
html {  
    height: 100%;  
}
```
And your code should work fine.
```html
* { padding: 0; margin: 0; }  
html, body, #fullheight {  
    min-height: 100% !important;  
    height: 100%;  
}  
#fullheight {  
    width: 250px;  
    background: blue;  
}<div id=fullheight>  
  Lorem Ipsum          
</div>
```
[**JsFiddle example**](http://jsfiddle.net/MadaraUchiha/KfjGU/). By:  [**Madara’s Ghost**](https://stackoverflow.com/users/871050/madaras-ghost)  From  [html — Why doesn’t height: 100% work to expand divs to the screen height? — Stack Overflow](https://stackoverflow.com/questions/7049875/why-doesnt-height-100-work-to-expand-divs-to-the-screen-height)

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)