---
title: ""
date: 2022-11-17T11:24:00+08:00
lastmod: 2022-11-17T11:24:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: ""
resources:
- name: "featured-image"
  src: ""
tags: []
toc:
  enable: true
---
## 
At first, I came oup with a classic BFS solution.
```python
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj_map = defaultdict(list)
        visited_map = defaultdict(lambda: False)

        # travers the routes to build a Adj List
        for r in routes:
            for i in range(len(r)):
                # reach the end
                if i == len(r)-1:
                    adj_map[r[i]].append(r[0])
                else:
                    adj_map[r[i]].append(r[i+1])

        stack = deque([
            (source, 1)
        ])
        while stack:
            current, n_bus = stack.popleft()
            if current == target:
                return n_bus

            if visited_map[current]:
                continue
            visited_map[current] = True
            
            # BFS
            for i in range( len(adj_map[current]) ):
                # Same bus
                if i == 0:
                    stack.append(
                        (adj_map[current][i], n_bus)
                    )
                # Transfer
                else:
                    stack.append(
                        (adj_map[current][i], n_bus+1)
                    )
        return -1
```
Which failed at case like `[[24],[3,6,11,14,22],[1,23,24],[0,6,14],[1,3,8,11,20]], 20, 8` where you need to know which bus you're at i.e. stop-1.

Because the part I used `i == 0` to determine if that's a **transfer** doesn't quite fit for case like above.
```python
# BFS
for i in range( len(adj_map[current]) ):
    # Same bus
    if i == 0:
        stack.append(
            (adj_map[current][i], n_bus)
        )
    # Transfer
    else:
        stack.append(
            (adj_map[current][i], n_bus+1)
        )
```
Now you need to look closer to the problem and draw the routes. For example ``[[24],[3,6,11,14,22],[1,23,24],[0,6,14],[1,3,8,11,20]]` the first 4 rounds should be:

    20 -> 1 -> 3  -> 8
          1 -> 23 -> 24
               3  -> 6

We need to utilize `queue` to achieve the transfer record like. How? By **traversing the same route first then other branches**.