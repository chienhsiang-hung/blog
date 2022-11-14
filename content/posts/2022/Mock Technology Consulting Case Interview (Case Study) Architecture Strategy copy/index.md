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

The `heap[0]` element also returns the smallest element each time. Let’s see various Operations on the heap in  [Python](https://www.geeksforgeeks.org/python-programming-language/).

### Creating a simple heap

The `heap.heapify(iterable)` function is used to **convert the iterable into a heap**  data structure. i.e. in heap order.

<script src="https://gist.github.com/chienhsiang-hung/e533d937f4db749dde5cf918785869af.js"></script>

In this notebook I've showed:
1. how heapq affects the original `list`
2. how to `push` and `pop`
3. `push` and `pop` simultaneously with `heapq.heappushpop(list, item)` and `heapq.heapreplace(list, item)`
4. `nlargest(n, list)` and `nsmallest(n, list)`

## Resources
- [Heap queue (or heapq) in Python - GeeksforGeeks](https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/)