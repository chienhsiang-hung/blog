---
title: "Embed Medium Blog On Website w/ RWD"
date: 2022-07-13
lastmod: 2022-07-13
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "In the last post Embed Medium Blog On Website. This is a free and simple guide through… | by 洪健翔 Hung, Chien-hsiang | Jul, 2022 | Medium…"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Responsive Web Design", "Medium", "Front End Development", "Website", "JavaScript"]
toc:
  enable: false
zhtw: false
---
In the last post  [Embed Medium Blog On Website. This is a free and simple guide through… | by 洪健翔 Hung, Chien-hsiang | Jul, 2022 | Medium](https://hungchienhsiang.medium.com/embed-medium-blog-on-website-880dc0d75062), I’ve shown you how to embed your medium post into your website with Zero Cost and Absolute Customized. But it doesn’t seem perfect enough, does it? So here we are, with some simple customization of adjustment, let’s modernize your embedded medium post with some simple responsive web design technique.

# How It Works

# [DEMO](https://chienhsiang-hung.github.io/embed-medium-blog-on-website/RWD)

![](https://miro.medium.com/max/1400/0*Rsqcy3rR9WOMIebA.png)

# [CSS](https://github.com/chienhsiang-hung/embed-medium-blog-on-website/blob/RWD/asset/cs/EmbeddingMedium.css)
```css
.medium-card span {
padding: 8px 8px 8px 8px;
}
/* https://stackoverflow.com/questions/11552380/how-to-automatically-crop-and-center-an-image */
.medium-card img {
width: 200px;
height: 200px;
object-fit: cover; /* https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit */
object-position: center; /* Center the image within the element */
min-height: 100%;
min-width: 100%;
}
.medium-card img {
transition: all 0.5s;
}
.medium-card:hover img {
transform: scale(1.2);
}
```
# [JS](https://github.com/chienhsiang-hung/embed-medium-blog-on-website/blob/RWD/asset/js/EmbeddingMedium.js)
```javascript
/* Sometimes it's also useful to use window.innerWidth (not typically found on mobile devices) instead of screen width

when dealing with desktop browsers where the window size is often less than the device screen size. */

var width = (window.innerWidth > 0) ? window.innerWidth : screen.width;
```

and
```javascript
pageSize  =  (width  <  768) ? 1 : 3;
```
in  `promise.then()`

# In  [HTML](https://github.com/chienhsiang-hung/embed-medium-blog-on-website/blob/RWD/index.html)

We put  `<meta name="viewport" content="width=device-width, initial-scale=1">`  this in  `<head>`  tag

GitHub:  [chienhsiang-hung/embed-medium-blog-on-website at RWD (github.com)](https://github.com/chienhsiang-hung/embed-medium-blog-on-website/tree/RWD)

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)