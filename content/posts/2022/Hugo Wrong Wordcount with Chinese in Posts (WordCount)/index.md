---
title: "Hugo | Wrong Wordcount with Chinese in Posts (#.WordCount)"
date: 2022-09-29
lastmod: 2022-09-29
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "isnanx commented on 30 Apr 2019"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Hugo", "Word Count", "Chinese", "Blog", "Post"]
toc:
  enable: true
zhtw: false
---
[isnanx](https://github.com/isnanx)  commented  [on 30 Apr 2019](https://github.com/gohugoio/hugo/issues/5913#issue-438712365)

Hi, as I write both Chinese and English in my posts, I found it that Chinese characters were not included when counting the words, I doubt if there is something wrong of my usage or it’s truly not supported by now, any reference? Thanks.

[Chinese characters may not supported by variable Wordcount · Issue #5913 · gohugoio/hugo (github.com)](https://github.com/gohugoio/hugo/issues/5913)

# Solution Found

It’s really simple. Just configure the value of  `hasCJKLanguage`  to  `true`  (default is  `false`  ).

> hasCJKLanguage
> 
> **Default value:**  false
> 
> If true, auto-detect Chinese/Japanese/Korean Languages in the content. This will make  `.Summary`  and  `.WordCount`  behave correctly for CJK languages.

![](https://miro.medium.com/max/1400/1*YPAsbSKUwYEIV98Y2YZ3vw.png)

Example:  [新南向國家見實習-新飛菲律賓遊學行銷企劃 HsinFei intern in The Philippines — Hung, Chien-Hsiang 洪健翔 | Blog (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/blog/posts/%E6%96%B0%E5%8D%97%E5%90%91%E5%9C%8B%E5%AE%B6%E8%A6%8B%E5%AF%A6%E7%BF%92-%E6%96%B0%E9%A3%9B%E8%8F%B2%E5%BE%8B%E8%B3%93%E9%81%8A%E5%AD%B8%E8%A1%8C%E9%8A%B7%E4%BC%81%E5%8A%83-hsinfei-intern-in-the-philippines/)

See:  [Configure Hugo | Hugo (gohugo.io)](https://gohugo.io/getting-started/configuration/#hascjklanguage)

When we work with strings in Hugo, we often want to get some basic information like its length. We can then show that information in our theme for readers or use it with other string operations. Let’s see how we can measure the length of text in Hugo.

## [3 ways to get the length of a string of text in Hugo](https://kodify.net/hugo/strings/string-length/)

## More

[Hugo’s word count is wrong in the HTML content written in Japanese even if hasCJKLanguage is true. · Issue #9335 · gohugoio/hugo (github.com)](https://github.com/gohugoio/hugo/issues/9335)