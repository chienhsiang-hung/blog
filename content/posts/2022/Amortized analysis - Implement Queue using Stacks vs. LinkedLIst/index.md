---
title: "Amortized analysis - Implement Queue using Stacks vs. LinkedLIst"
date: 2022-12-17T02:17:00+08:00
lastmod: 2022-12-17T02:17:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: ""
resources:
- name: "featured-image"
  src: ""
tags: [""]
toc:
  enable: true
---
## What's Amortized Analysis
The motivation for amortized analysis is that looking at the worst-case run time can be too pessimistic. Instead, amortized analysis averages the **running times of operations in a sequence over that sequence**.[^Amortized_analysis]

## Example
### Implement Queue
#### Linked LIst
```python
class QNode:
    def __init__(self, v=0, _next=None):
        self.value = v
        self.next = _next


class MyQueue:
    def __init__(self):
        self.root = None
        self.tail = None

    def push(self, x: int) -> None:
        if not self.root:
            self.root = QNode(x)
            self.tail = self.root
        else:
            self.tail.next = QNode(x)
            self.tail = self.tail.next
        
    def pop(self) -> int:
        output = self.root.value
        self.root = self.root.next
        return output

    def peek(self) -> int:
        return self.root.value

    def empty(self) -> bool:
        return not self.root
```
Each operation takes exact O(1) time complexity to execute.

What if we are not allowed to use linked list but **2 stacks** instead. It would be impossible to achieve right? Though with Amortized Analysis, **amortized O(1)** is acceptable. We can still try to make some tricks.

[^Amortized_analysis]: [Amortized analysis - Wikipedia](https://en.wikipedia.org/wiki/Amortized_analysis)
