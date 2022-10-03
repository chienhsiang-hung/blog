---
title: "Javascript Interview Questions: Pagination, Memoization, Event Bubbling"
date: 2022-09-20T10:00:00+08:00
lastmod: 2022-09-20T10:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "1. What is pagination?"
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["JavaScript", "Memoization", "Event Bubbling", "Pagination", "Interview"]
toc:
  enable: true
zhtw: false
---
![](https://miro.medium.com/max/1400/0*VTfHv6-FuDxthMJO)

Photo by  [Claudio Schwarz](https://unsplash.com/@purzlbaum?utm_source=medium&utm_medium=referral)  on  [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

# 1. What is pagination?

[What is Pagination? And How to Implement it on Your Website — SEOptimer](https://www.seoptimer.com/blog/what-is-pagination/)

Pagination is a sequence of pages which are connected and have similar content. It is important to note that even when the content on a section of a page is split into distinct pages, we will still define that as pagination.

## Why use pagination?

1.  Better user experience
2.  Easier navigation

**Real-Time Scenario:**  Let’s take the amazon website or Flipkart website for displaying available products in their database. Let suppose they have 1 million products with them. If they are trying to show all the items at a time, the customer must wait more time like one day to see all the product lists.

## Introduction to Pagination in JavaScript

JavaScript Pagination concept is applied for moving among the pages with First, Next, Previous and Last buttons or links. Pagination’s main motto is to move among the content immediately by clicking links or buttons. Pagination has multiple links or buttons provided for access First, Next, Previous and Last content. Create First, Next, Previous and Last buttons in JavaScript we have used different JavaScript functions.

## How Should we Tackle this Situation?

Instead of showing all the items at a time, we can show them 50 to 100 items at a time by using a list of link buttons. If the first 50 to 100 items do not fulfil the need of a client, we then move to the next 50 to 100.

[**The syntax for Pagination:**](https://www.educba.com/pagination-in-javascript/)
```javascript
//function for creating page list  
function prepareList() {  
for (count = 0; count < 100; count++)  
//add iteration elements to an array  
createPages= getPageNumber();//user defined function  
}  
//function per creating pages  
function preparePages() {  
var start= ((presentPage - 1) * countPerEachPage);  
var end = start+ countPerEachPage;  
listPage= list.slice(start, end);  
//call some user defined methods to pagination functionality  
}
```
## Example:

[Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)

![](https://miro.medium.com/max/1400/1*bBkOxZtY13fP6wMMeiEUPQ.png)

[Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)
```javascript
// make Pagination  
    mediumPromise.then(function() {  
        // make Pagination reponsive  
        pageSize = (width < 768) ? 1 : 3;  
        var pageCount = $(".medium-card").length / pageSize;$("#pagin").append(`<a class="page-link" href="javascript:void(0);">&laquo;</a>`);  
        for (var i = 0; i < pageCount; i++) {  
            $("#pagin").append(`<a class="page-link" href="javascript:void(0);">${(i + 1)}</a>`);  
        }  
        $("#pagin").append(`<a class="page-link" href="javascript:void(0);">&raquo;</a>`);$("#pagin a:nth-child(2)").addClass("active");showPage = function (page) {  
            $(".medium-card").hide();  
            $(".medium-card").each(  
                function (n) {  
                    if (n >= pageSize * (page - 1) && n < pageSize * page)  
                        $(this).show();  
                }  
            );  
        }  
        showPage(1);var pageNum = 1;  
        $("#pagin a").click(function () {if ($(this).text() == "«") {  
                // pre button error handling  
                pageNum--;  
                if (pageNum < 1) {  
                    pageNum++;  
                    return false;  
                }  
                else {  
                    showPage(pageNum)  
                }  
            } else if ($(this).text() == "»"){  
                // nex button error handling  
                pageNum++;  
                if (pageNum > pageCount) {  
                    pageNum--;  
                    return false;  
                }  
                else {  
                    showPage(pageNum)  
                }  
            } else {  
                pageNum = parseInt($(this).text());  
                showPage(pageNum)  
            }// refresh the pagebutton <a>  
            $("#pagin a").removeClass("active");  
            $(`#pagin a:nth-child(${pageNum+1})`).addClass("active");  
              
        });  
    });
```
[chienhsiang-hung.github.io/EmbeddingMedium.js at main · chienhsiang-hung/chienhsiang-hung.github.io](https://github.com/chienhsiang-hung/chienhsiang-hung.github.io/blob/main/assets/js/EmbeddingMedium.js)

# 2. What is Memoization?

In programming,  [**memoization is an optimization technique**](https://www.freecodecamp.org/news/memoization-in-javascript-and-react/)  that makes applications more efficient and hence faster. It does this by storing computation results in cache, and retrieving that same information from the cache the next time it’s needed instead of computing it again.

In simpler words, it consists of storing in  **cache**  the output of a function, and making the function check if each required computation is in the cache before computing it.

A  **cache**  is simply a temporary data store that holds data so that future requests for that data can be served faster.

Memoization is a simple but powerful trick that can help speed up our code, especially when dealing with repetitive and heavy computing functions.

# 3. Bubbling and capturing

## [Bubbling](https://javascript.info/bubbling-and-capturing#bubbling)

The bubbling principle is simple.

**When an event happens on an element, it first runs the handlers on it, then on its parent, then all the way up on other ancestors.**

Let’s say we have 3 nested elements  `FORM > DIV > P`  with a handler on each of them:
```html
<style>  
  body * {  
    margin: 10px;  
    border: 1px solid blue;  
  }  
</style><form onclick="alert('form')">FORM  
  <div onclick="alert('div')">DIV  
    <p onclick="alert('p')">P</p>  
  </div>  
</form>
```
## A click on the inner  `<p>`  first runs  `onclick`:

1.  On that  `<p>`.
2.  Then on the outer  `<div>`.
3.  Then on the outer  `<form>`.
4.  And so on upwards till the  `document`  object.

So if we click on  `<p>`, then we’ll see 3 alerts:  `p`  →  `div`  →  `form`.

The process is called “bubbling”, because events “bubble” from the inner element up through parents like a bubble in the water.

> **_Almost_  all events bubble.**
> 
> The key word in this phrase is “almost”.
> 
> For instance, a  `focus`  event does not bubble. There are other examples too, we’ll meet them. But still it’s an exception, rather than a rule, most events do bubble.

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)