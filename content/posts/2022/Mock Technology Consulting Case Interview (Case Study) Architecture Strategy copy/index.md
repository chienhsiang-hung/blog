---
title: "Heap Queue (heapq) in Python | LeetCode Example Last Stone Weight"
date: 2022-11-14T09:20:00+08:00
lastmod: 2022-11-14T09:20:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Architecture Strategy: Federal Finance Agency Practice Case from Deloitte and Christine Wong. Our client is a small division of a large Federal Finance Agency that is in charge of administering and enforcing economic and trade sanctions determined by US foreign policy and national security goals."
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Tech Consulting", "Case Study", "Management Consulting", "Banking Technology", "Case Interview"]
toc:
  enable: true
zhtw: false
---
## Heap
[Heap data structure is mainly used to represent a **priority queue**.](https://www.geeksforgeeks.org/applications-of-heap-data-structure/) In Python, it is available using the “`heapq`” module. The property of this data structure in Python is that **each time the smallest heap element is popped(min-heap)**.
> Whenever elements are pushed or popped, heap structure is maintained.
> 
The `heap[0]` element also returns the smallest element each time. Let’s see various Operations on the heap in  [Python](https://www.geeksforgeeks.org/python-programming-language/).

### Creating a simple heap

The  `heapify(iterable)`:- This function is used to **convert the iterable into a heap**  data structure. i.e. in heap order.