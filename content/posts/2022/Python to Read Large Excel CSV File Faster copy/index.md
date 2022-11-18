---
title: ""
date: 2022-11-18T11:19:00+08:00
lastmod: 2022-11-18T11:19:00+08:00
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
## Classic DFS
At first, I came oup with a classic DFS solution.
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
Now you need to look closer to the problem and draw the routes. For example `[[24],[3,6,11,14,22],[1,23,24],[0,6,14],[1,3,8,11,20]]` the first 4 rounds should be:

    20 -> 1 -> 3  -> 8
          1 -> 23 -> 24
               3  -> 6

We need to utilize `queue` to achieve the transfer record like. How? By **traversing the same route first then other branches**. So that queue would be like `[20,1,3,8,11,23,6...]`.

*What if we have multiple stop to transfer at the first stop?* Let's say `[[24,20],[3,6,11,14,22],[1,23,24],[0,6,14],[1,3,8,11,20]]`. Then you need to know where they are by tagging their `bus_num` in the `adj_list`.
## Remember The Bus Number
```python
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        adj_map = defaultdict(list)
        visited_map = defaultdict(lambda: False)

        # travers the routes to build a Adj List
        for bus_num in range(len(routes)):
            for n_stop in range(len(routes[bus_num])):
                next_stop_i = (n_stop +1) % len(routes[bus_num])
                next_stop = routes[bus_num][next_stop_i]

                adj_map[ routes[bus_num][n_stop] ].append( (next_stop, bus_num) )
        
        # Example of adj_map
        # {
        #   1: [(23, 2), (3, 4)],
        # }
        stop_queue = deque([
            ( source, adj_map[source][0][1] )
        ])
        buses = set()
        while stop_queue:
            current, cur_bus_num = stop_queue.popleft()
            if visited_map[current]: continue

            visited_map[current] = True
            buses.add(cur_bus_num)
            if current == target: return len(buses)

            for next_stop, next_bus_num in adj_map[current]:
                if next_bus_num == cur_bus_num:
                    stop_queue.appendleft(
                        (next_stop, next_bus_num)
                    )
                else:
                    stop_queue.append(
                        (next_stop, next_bus_num)
                    )
        return -1     
```
Failed at **Input**:

`[[1,9,12,20,23,24,35,38],[10,21,24,31,32,34,37,38,43],[10,19,28,37],[8],[14,19],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]]` ,`source=37`, `target=28`

Dry run the code you will find the issue here: **How can we find the shortest route (in terms of number of transfer needed)?** *(Since the output was 4 and expected is 1.)*
## Find The Shortest Route (Transfer)
You will need to divide the searching route and record it and find the `min`.
```python
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        adj_map = defaultdict(list)
        visited_map = defaultdict(lambda: False)

        # travers the routes to build a Adj List
        for bus_num in range(len(routes)):
            for n_stop in range(len(routes[bus_num])):
                next_stop_i = (n_stop +1) % len(routes[bus_num])
                next_stop = routes[bus_num][next_stop_i]

                adj_map[ routes[bus_num][n_stop] ].append( (next_stop, bus_num) )


        transfers = []
        def search(current, current_bus_num, target, n_transfer=1):
            if current == target:
                transfers.append(n_transfer)
                return

            if visited_map[current]:
                return
            visited_map[current] = True

            for next_stop, next_bus_num in adj_map[current]:
                if current_bus_num == next_bus_num:
                    search(next_stop, next_bus_num, target, n_transfer)
                else:
                    search(next_stop, next_bus_num, target, n_transfer+1)


        visited_map[source] = True
        for next_stop, bus_num in adj_map[source]:
            search(next_stop, bus_num, target)

        return -1 if not transfers else min(transfers)
```
Then I proposed the new solution with **num of transfers recorded** while failed at case like `[[10,21,24,31,32,34,37],[10,19,28,37],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]]`, `output=2`, `expected=1`. You need to be careful of adapting **1D visited record or 2D**.
## 2D Visited Matrix
```python
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        adj_map = defaultdict(list)
        # prepare a 2-d visited matrix
        visited_map = [
            [False] * len(routes[i]) for i in range(len(routes))
        ]

        # travers the routes to build a Adj List
        for bus_num in range(len(routes)):
            for n_stop in range(len(routes[bus_num])):
                next_stop_i = (n_stop +1) % len(routes[bus_num])
                next_stop = routes[bus_num][next_stop_i]

                adj_map[ routes[bus_num][n_stop] ].append( (next_stop, bus_num, n_stop) )

                # init source visited
                if n_stop == source:
                    visited_map[bus_num][n_stop] = True


        transfers = []
        def search(current, current_bus_num, n_stop, target, n_transfer=1):
            if current == target:
                transfers.append(n_transfer)
                return

            if visited_map[current_bus_num][n_stop]:
                return
            visited_map[current_bus_num][n_stop] = True

            for next_stop, next_bus_num, n_stop in adj_map[current]:
                if current_bus_num == next_bus_num:
                    search(next_stop, next_bus_num, n_stop, target, n_transfer)
                else:
                    search(next_stop, next_bus_num, n_stop, target, n_transfer+1)


        for next_stop, bus_num, n_stop in adj_map[source]:
            search(next_stop, bus_num, n_stop, target)

        return -1 if not transfers else min(transfers)
```
With the *2-d visited matrix*, still I got the wrong output. After a further examination, I've found I've might been using the wrong technique. I should have adopted **BFS** instead of **DFS** which made my visited matrix useless here (sine it needs to be updated on each branch).