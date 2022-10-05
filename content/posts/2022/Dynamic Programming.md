---
title: ""
date: 2022-10-05T12:30:00+08:00
lastmod: 2022-10-06T09:20:00+08:00
draft: true
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "LeetCode 746. Min Cost Climbing Stairs | Dynamic Programming | Python | Time O(n) Space O(1) Question"
resources:
- name: "featured-image"
  src: "featured-image.jpeg"
tags: ["Python", "Dynamic Programming", "Leetcode", "Leetcode Easy", "Bottom Up Approach"]
toc:
  enable: true
zhtw: false
---
# Dynamic Programming
## Advantages
Addresses problems with exponantial time complexity to Polynomial (sometimes even linear)
$O(c^n)$ -> $O(n^c)$ -> $O(n)$

## Requirments
### Properties
1. Optimal Substructure
Use $X_1$ to solve $X_2$ to solve $X_3$ etc. to solve the entire problem.
2. Overlapping Subprolems
**Fibonacci**
$Fib(5) = Fib(4) + Fib(3)$
$Fib(4) = Fib(3) + Fib(2)$
...
Overlapping part: $Fib(3)$, $Fib(2)$, $Fib(1)$