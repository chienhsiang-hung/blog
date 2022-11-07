---
title: "Topological Sorting | LeetCode Course Schedule I/II | Graph, DFS, BFS"
date: 2022-11-07T10:50:00+08:00
lastmod: 2022-11-07T10:50:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: ""
resources:
- name: "featured-image"
  src: ""
tags: ["Tcp Ip", "Tcp", "Internet Protocol", "Udp", "Communication Protocol"]
toc:
  enable: true
zhtw: false
---
## What's Topological Sorting
Topological sorting for **Directed Acyclic Graph (DAG)** is a linear ordering of vertices such that for every directed edge u v, **vertex u comes before v** in the ordering.[^topological-sorting]

**Note:** Topological Sorting for a graph is not possible if the graph is not a DAG. (i.e. If there is a loop/cycle in the Graph)

*Below is the implementation of the above approach:*
<script src="https://gist.github.com/chienhsiang-hung/c468ece14fd0fee5af4ec24edf39e134.js"></script>

[^topological-sorting]: [Topological Sorting - GeeksforGeeks](https://www.geeksforgeeks.org/topological-sorting/)
