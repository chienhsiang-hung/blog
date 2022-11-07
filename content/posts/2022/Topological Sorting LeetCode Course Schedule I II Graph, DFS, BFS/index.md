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

## Examples
### Course Schedule
**LeetCode 207. Course Schedule**[^course-schedule] *[Medium]*

There are a total of  `numCourses`  courses you have to take, labeled from  `0`  to  `numCourses - 1`. You are given an array  `prerequisites`  where  `prerequisites[i] = [ai, bi]`  indicates that you  **must**  take course  `bi`  first if you want to take course  `ai`.

-   For example, the pair  `[0, 1]`, indicates that to take course  `0`  you have to first take course  `1`.

Return  `true`  if you can finish all courses. Otherwise, return  `false`.

**Example 1:**

> **Input:** numCourses = 2, prerequisites = [[1,0]]
>
> **Output:** true
>
> **Explanation:** There are a total of 2 courses to take. 
>
> To take course 1 you should have finished course 0. So it is possible.

**Example 2:**

> **Input:** numCourses = 2, prerequisites = [[1,0],[0,1]]
> 
> **Output:** false
> 
> **Explanation:** There are a total of 2 courses to take. 
> 
> To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

**Constraints:**

-   `1 <= numCourses <= 2000`
-   `0 <= prerequisites.length <= 5000`
-   `prerequisites[i].length == 2`
-   `0 <= ai, bi < numCourses`
-   All the pairs prerequisites[i] are  **unique**.

### Course Schedule II
**LeetCode 210. Course Schedule II**[^course-schedule-ii]

[^topological-sorting]: [Topological Sorting - GeeksforGeeks](https://www.geeksforgeeks.org/topological-sorting/)
[^course-schedule]: [Course Schedule - LeetCode](https://leetcode.com/problems/course-schedule/)
[^course-schedule-ii]: [Course Schedule II - LeetCode](https://leetcode.com/problems/course-schedule-ii/)
