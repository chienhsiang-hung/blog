---
title: "Median of Two Sorted Arrays in Python (LeetCode Hard)"
date: 2023-01-19T03:00:00+08:00
lastmod: 2023-01-19T03:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Given an integer array nums and an integer k, return the number of good subarrays of nums."
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Python", "Sliding Windows", "Sliding Window Algorithm", "Leetcode", "Leetcode Medium"]
toc:
  enable: true
---
## Solution
Most Python solution you can find usding either this or kth solution they slice the `nums1` and `nums2` for loop and it makes the time complexity from $O(Logn)$ $O(nLogn)$. Here I share a solution using pointer to avoid such the problem.

{{< youtube LPFhl65R7ww >}}

If you don't understand the concept please have a look at the above video first by [@tusharroy2525](https://www.youtube.com/@tusharroy2525/about). 