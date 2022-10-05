---
title: "Dynamic Programming"
date: 2022-10-05T12:30:00+08:00
lastmod: 2022-10-06T09:20:00+08:00
draft: true
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "LeetCode 746. Min Cost Climbing Stairs | Dynamic Programming | Python | Time O(n) Space O(1) Question"
resources:
- name: "featured-image"
  src: "featured-image.jpeg"
tags: ["Python", "Dynamic Programming", "Leetcode", "Leetcode Easy", "Bottom Up Approach"]
toc:
  enable: true
zhtw: false
---
# Dynamic Programming
## Advantages
Addresses problems with exponantial time complexity to Polynomial (sometimes even linear)
$O(c^n)$ -> $O(n^c)$ -> $O(n)$
### When to Use
When we don't want to recalculate things. We want to rely on existing solutions.

## Requirments
### Properties
1. Optimal Substructure
Use $X_1$ to solve $X_2$ to solve $X_3$ etc. to solve the entire problem.
2. Overlapping Subprolems
**Fibonacci**
$Fib(5) = Fib(4) + Fib(3)$
$Fib(4) = Fib(3) + Fib(2)$
...
Overlapping part: $Fib(3)$, $Fib(2)$, $Fib(1)$ *(Memoized/Cached Results)*

## Types of Problems
1. Combinatoric -> Ans: **How many...?**
2. Optimization -> Ans: **Minimum/Maximum** of steps/ways/paths...
$$1+2+3+4+5+...+R=\sum_{i=1}^n i$$
$n=1$, $F(1)=1$
$n=2$, $F(2)=F(1)+2=3$
$n=3$, $F(3)=F(2)+3=6$
...
$F(n)=F(n-1)+n$
### Go Implementation
```go
func nSum(n int) int {
	dp := make([]int, n+1)
	dp[0] = 0 // in case n==0
	for i:=1; i<=n; i++ {
		dp[i] = dp[i-1] + i
	}
	return dp[n]
}
```

## Framework for Solving DP Problems
1. Express our goal as an objective functions

> Example: **Climbing Stairs Problem**

$F(i)$ is the number of distinct ways to reach the i-th stair 
2. Identify **Base cases** (to solve bondary problems)

> $F(2)=2$ 
> $F(1)=1$ 
> $F(0)=1$ 
> $$F(n)=F(n-1)+F(n-2)$$

3. Recurrence relation
4. Order of computation
5. Location of the answer

> $F(n)$