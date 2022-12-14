---
title: "LeetCode [Hard] Bus Routes | Algorithm - BFS"
date: 2022-11-20T06:43:00+08:00
lastmod: 2022-11-20T06:43:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "We need to re-think the problem, how do we walk through the routes? Or in other words, how do we travel from a to b by bus if we have no maps?"
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Algorithms", "Leetcode", "Bfs", "Breadth First Search", "Python"]
toc:
  enable: true
---
## Question
[Bus Routes - LeetCode](https://leetcode.com/problems/bus-routes/)
## Attempts
### Classic DFS
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
### Remember The Bus Number
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
### Find The Shortest Route (Transfer)
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
### 2D Visited Matrix
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
With the *2-d visited matrix*, still I got the wrong output. After a further examination, I've found I've might been using the wrong technique. I should have adopted **BFS** instead of **DFS** which made my visited matrix useless here (sine it needs to be updated/re-initialized on each branch).

**You need to do BFS simultaniously.**
![Bus Routes 0](Bus%20Routes%200.jpg "Bus Routes 0")
To record the visited-matrix in order to determine whether to stop or not.
```python
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        if source == target:
            return 0
            
        adj_map = defaultdict(list)

        # traverse the routes to build a Adj List
        for bus_num in range(len(routes)):
            for n_stop in range(len(routes[bus_num])):
                next_stop_i = (n_stop +1) % len(routes[bus_num])
                next_stop = routes[bus_num][next_stop_i]

                adj_map[ routes[bus_num][n_stop] ].append( (next_stop, bus_num) )


        transfers = []
        def search(current, current_bus_num, visited, target, n_transfer=1):
            if current == target:
                transfers.append(n_transfer)
                return

            elif visited[current]:
                return
            visited[current] = True

            # Traverse
            for next_stop, next_bus_num in adj_map[current]:
                if current_bus_num == next_bus_num:
                    search(next_stop, next_bus_num, visited.copy(), target, n_transfer)
                else:
                    search(next_stop, next_bus_num, visited.copy(), target, n_transfer+1)

        for next_stop, bus_num in adj_map[source]:
            visited = defaultdict(lambda: False)
            visited[source] = True
            search(next_stop, bus_num, visited, target)
        
        return -1 if not transfers else min(transfers)
```
Still failed, at
```python
# failed at 
test1 = [[3,16,33,45,59,79,103,135],[3,35,39,54,56,78,96,101,120,132,146,148],[13,72,98],[37,70,107],[0,12,31,37,41,68,78,94,100,101,113,123],[11,32,52,85,135],[43,50,128],[0,13,49,51,53,55,60,65,66,80,82,87,92,99,112,118,120,125,128,131,137],[15,19,34,37,45,52,56,97,108,123,142],[7,9,20,28,29,33,34,38,43,46,47,48,53,59,65,72,74,80,88,92,110,111,113,119,135,140],[15,41,64,83],[7,13,26,31,57,85,101,108,110,115,119,124,149],[47,61,67,70,74,75,77,84,92,101,124,132,133,142,147],[0,2,5,6,12,18,34,37,47,58,77,98,99,109,112,131,135,149],[6,7,8,9,14,17,21,25,33,40,45,50,56,57,58,60,68,92,93,100,108,114,130,149],[7],[5,16,22,48,77,82,108,114,124],[34,71],[8,16,32,48,104,108,116,134,145],[3,10,16,19,35,45,64,74,89,101,116,149],[1,5,7,10,11,18,40,45,50,51,52,54,55,69,71,81,82,83,85,89,96,100,114,115,124,134,138,148],[0,2,3,5,6,9,15,52,64,103,108,114,146],[5,33,39,40,44,45,66,67,68,69,84,102,106,115,120,128,133],[17,26,49,50,55,58,60,65,88,90,102,121,126,130,137,139,144],[6,12,13,37,41,42,48,50,51,55,64,65,68,70,73,102,106,108,120,123,126,127,129,135,136,149],[6,7,12,33,37,41,47,53,54,80,107,121,126],[15,75,91,103,107,110,125,139,142,149],[18,24,30,52,61,64,75,79,85,95,100,103,105,111,128,129,142],[3,14,18,32,45,52,57,63,68,78,85,91,100,104,111,114,142],[4,7,11,20,21,31,32,33,48,61,62,65,66,73,80,92,93,97,99,108,112,116,136,139]]
# 85
# 112
# output=4, expected=2
```
We need to re-think the problem, how do we walk through the routes? Or in other words, how do we travel from a to b by bus if we have no maps?
## Why BFS
In order to record the right process. Imagine you're taking a bus, you have tried all the bus on that specific station. Would you come back again before you reach the end given the condition that you have travelled all the possible routes starts from this station? *(Inspired by [zippysphinx](https://leetcode.com/zippysphinx/)'s [Solution](https://leetcode.com/problems/bus-routes/solutions/1072394/python-bfs-solution/).)*
![bus by bus](featured-image.jpg "bus by bus")
```python
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        transfers = 0
        if source == target:
            return transfers

        # create a stop-to-buses map
        stop_to_bus = defaultdict(set)
        for bus_num in range(len(routes)):
            for i in range(len(routes[bus_num])):
                stop_to_bus[routes[bus_num][i]].add(bus_num)
        
        visited_buses = [False] * len(routes)
        bus_queue = deque([
            stop_to_bus[source] # set of buses
        ])
        while bus_queue[0]:
            current_buses = bus_queue.popleft()
            
            transfers += 1
            bus_queue.append(set())
            for bus in current_buses:
                visited_buses[bus] = True
                for stop in routes[bus]:
                    if stop == target:
                        return transfers

                    # add new bus to visit
                    for next_bus in stop_to_bus[stop]:
                        if not visited_buses[ next_bus ]:
                            bus_queue[-1].add( next_bus )
        return -1
```
