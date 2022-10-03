---
title: "binary tree random node python"
date: 2022-10-03T03:40:00+08:00
lastmod: 2022-10-03T03:45:00+08:00
draft: true
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
# Random Node
From the book - **Cracking the Coding Interview** (*4.11*).
Build a **binary tree class** along with the **insert**, **delete**, **find** and the **getRandomNode** method which returns a random node in the tree. (All nodes shall have the same possibility to be returned.)

## Brute Force
> The intuition brute force solution would be to traverse all nodes and collect them into an array/list then randomly choose one of them out of Uniform Distribution.
> 
> Time: O(n)
>
> Space: O(1)

Though **it would be nicer if we can give a O(1) method. Since we are given the ownership of the whole class (generated from the scratch)**, we can simply record the size in order to produce a uniform random choice.

## Optimized
The solution provided by the book outsource github isn't quite right on the [delete function](https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_04/p11_random_node.py#L52). (The size property wasn't being taken care of quite right.)