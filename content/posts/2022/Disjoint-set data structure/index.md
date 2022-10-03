---
title: "Disjoint-set data structure"
date: 2022-09-28
lastmod: 2022-09-28
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "In computer science, a disjoint-set data structure, also called a union–find data structure or merge–find set, is a data structure that…"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Dsu", "Disjoint Set", "Union Find", "Leetcode Medium", "Graph"]
toc:
  enable: false
zhtw: false
---
In  [computer science](https://en.wikipedia.org/wiki/Computer_science), a disjoint-set data structure, also called a union–find data structure or merge–find set, is a  [data structure](https://en.wikipedia.org/wiki/Data_structure)  that stores a collection of  [disjoint](https://en.wikipedia.org/wiki/Disjoint_sets)  (non-overlapping)  [sets](https://en.wikipedia.org/wiki/Set_(mathematics)). Equivalently, it stores a  [partition of a set](https://en.wikipedia.org/wiki/Partition_of_a_set)  into disjoint  [subsets](https://en.wikipedia.org/wiki/Subset). It provides operations for adding new sets, merging sets (replacing them by their  [union](https://en.wikipedia.org/wiki/Union_(set_theory))), and finding a representative member of a set. The last operation makes it possible to find out efficiently if any two elements are in the same or different sets.

While there are several ways of implementing disjoint-set data structures, in practice they are often identified with a particular implementation called a disjoint-set forest. This is a specialized type of  [forest](https://en.wikipedia.org/wiki/Forest_(graph_theory))  which performs unions and finds in near-constant  [amortized time](https://en.wikipedia.org/wiki/Amortized_analysis). To perform a sequence of m addition, union, or find operations on a disjoint-set forest with n nodes requires total time  [_O_](https://en.wikipedia.org/wiki/Big_O_notation)(_m_α(_n_)), where α(_n_) is the extremely slow-growing  [inverse Ackermann function](https://en.wikipedia.org/wiki/Inverse_Ackermann_function). Disjoint-set forests do not guarantee this performance on a per-operation basis. Individual union and find operations can take longer than a constant times α(_n_) time, but each operation causes the disjoint-set forest to adjust itself so that successive operations are faster. Disjoint-set forests are both  [asymptotically optimal](https://en.wikipedia.org/wiki/Asymptotically_optimal)  and practically efficient.

Disjoint-set data structures play a key role in  [Kruskal’s algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)  for finding the  [minimum spanning tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree)  of a graph. The importance of minimum spanning trees means that disjoint-set data structures underlie a wide variety of algorithms. In addition, disjoint-set data structures also have applications to symbolic computation, as well in compilers, especially for  [register allocation](https://en.wikipedia.org/wiki/Register_allocation)  problems.

![](https://miro.medium.com/max/1400/0*_i5cUsi_8mBblwqc)

`MakeSet`  creates 8 singletons.

![](https://miro.medium.com/max/1400/0*GbhhczNi4I0LSWxF)

After some operations of  `Union`, some sets are grouped together.

# [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/)

You are given an array of strings  `equations`  that represent relationships between variables where each string  `equations[i]`  is of length  `4`  and takes one of two different forms:  `"xi==yi"`  or  `"xi!=yi"`.Here,  `xi`  and  `yi`  are lowercase letters (not necessarily different) that represent one-letter variable names.

Return  `true`  _if it is possible to assign integers to variable names so as to satisfy all the given equations, or_  `false`  _otherwise_.

Example 1:

Input: equations = [“a==b”,”b!=a”] Output: false Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second. There is no way to assign the variables to satisfy both equations.

Example 2:

Input: equations = [“b==a”,”a==b”] Output: true Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

# [Union Find](https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/2624959/C%2B%2B-or-Union-Find-or-Related-Problems)

Approach ([kiranpalsingh1806](https://leetcode.com/kiranpalsingh1806))

-   We will store variables in same component if they are equal.
-   Then we will check non-equality equtions, if both variables in any of those equation are in same component, we return false.

Let’s take one example —  `a==b`,  `b==c`,  `a!=d`,  `d==e`,  `e!=f`,  `a!=c`.

![](https://miro.medium.com/max/1400/0*-ZXe0G7mDzz5fhed)

How Union Find works ?

![](https://miro.medium.com/max/1400/0*1twoV4OLllkRdWXK)

# [Disjoint Set Union (dsu) aka Union Find](https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/2625039/LeetCode-The-Hard-Way-Explained-Line-By-Line)

> for dsu tutorial, please check out  [https://wingkwong.github.io/leetcode-the-hard-way/tutorials/graph-theory/disjoint-set-union](https://wingkwong.github.io/leetcode-the-hard-way/tutorials/graph-theory/disjoint-set-union)  ([wingkwong](https://leetcode.com/wingkwong))

A set is a collection of elements. If two sets have no common elements, then they are called disjoint sets. For example, {1, 2} and {3, 4} are disjoint sets while {1, 2} and {1, 3} are not because they have a common element 1.

Disjoint Set Union (or DSU or Union Find) is a data structure that allows us to combine any two sets into one. Let’s say we have 10 elements and we initialise an array rootroot with a size of 10. Here we have 10 sets and each individual element in the set is the parent.
```c
vector<int> root(10);  
for(int i = 0; i < 10; i++) root[i] = i;
```
If we join the first element 1 and 2 together, we first check if they belong to the same parent. If they do, it means they have already in the same set. Otherwises, we can point one to another and update rootroot like  `root[2] = 1`  which means the root of element 2 is 1. We can make it more flexible to check if they are already in the same set or not simply by returning a boolean value.

> _What’s the intuition behind union find?_

Based on the property of  `==`. If you see  `==`  in the equation, then we can put those numbers under the same group due to the following properties.

-   if a == b, then b == a
-   if a == b, b == c, then a == c

In other word, x != y means x is not in the same group as y.

So we need a data structure to handle the connected relationship and use contradiction to find out the false cases. Then DSU comes to mind. If we can see them as a graph. For the case  `a == b, b == c`, we may first think of a -> b -> c which may lead us to think about a DFS solution. However, we can compress the path like a -> b and a -> c where a is the root. By doing so, we compress b and c into the same level so that we don't need to walk all the nodes between the root and the source to achieve O(logN) per call on average.

# Solution

[Satisfiability of Equality Equations.py at main · chienhsiang-hung](https://github.com/chienhsiang-hung/Data-Structures-and-Algorithms-in-Python/blob/main/Sorting%20and%20Searching/Satisfiability%20of%20Equality%20Equations/Satisfiability%20of%20Equality%20Equations.py)
```python
class Solution:  
    def equationsPossible(self, equations: List[str]) -> bool:  
        # ["a==b","b!=a"] False  
        # ["b==a","a==b"] True  
        # ["a==b","b==c","c!=a"] False  
        # ["a!=a"] False  
        # ["a==b","a==c","c!=b"] False  
        # ["a==b","c==a","c!=b"] False  
          
          
        parent = [i for i in range(26)]  
          
        def find(x):  
            if parent[x] == x:  
                return x  
            return find(parent[x])  
          
        for e in equations:  
            a = ord(e[0]) % 97  
            b = ord(e[3]) % 97  
            eq = e[1]  
            if eq == '=':  
                parent[find(a)] = find(b)  
          
        for e in equations:  
            a = ord(e[0]) % 97  
            b = ord(e[3]) % 97  
            eq = e[1]  
            if eq == '!' and find(a) == find(b):  
                return False  
          
        return True# time: O(Nlog(N)), space: O(1)
```
Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)