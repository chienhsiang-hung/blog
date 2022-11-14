---
title: "Heap Queue (heapq) in Python | LeetCode Example Last Stone Weight"
date: 2022-11-14T10:46:00+08:00
lastmod: 2022-11-14T10:46:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Heap data structure is mainly used to represent a priority queue. In Python, it is available using the “heapq” module. The property of this data structure in Python is that each time the smallest heap element is popped(min-heap)."
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Python", "Heapq", "Priority Queue", "Heap", "Leetcode"]
toc:
  enable: true
---
![featured-image.jpg](featured-image.jpg "img source: https://unsplash.com/photos/n0CTq0rroso")
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

### Example
[Last Stone Weight - LeetCode](https://leetcode.com/problems/last-stone-weight/)
```python
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-item for item in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            big1 = heapq.heappop(stones)
            big2 = heapq.heappop(stones)
            heapq.heappush(stones, big1-big2)
        
        return -stones[0]
```
#### Approach
Turn all `int` to negative so that we can properly use `Heap`.
1. `pop` the largest 2 and crash them then `push` them back
2. till the end

With
> `heapq` is a *binary heap*, with $O(log n)$ `push` and $O(log n)$ `pop`.[^heapqtc]

we know that with our approach we will have $O(nlog n)$ Time Complexity and $O(1)$ Space Complexity.
## Resources
- [Heap queue (or heapq) in Python - GeeksforGeeks](https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/)

[^heapqtc]: [python - What's the time complexity of functions in heapq library - Stack Overflow](https://stackoverflow.com/questions/38806202/whats-the-time-complexity-of-functions-in-heapq-library#:~:text=heapq%20is%20a%20binary%20heap,O(n%20log%20n).)