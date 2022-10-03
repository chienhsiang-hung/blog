---
title: "Is BFS/DFS a Greedy Algorithm? What’s The Difference Between Greedy and Heuristic Algorithm?"
date: 2022-09-22
lastmod: 2022-09-22
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Is BFS\u002FDFS a Greedy Algorithm and Why?"
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Greedy Algorithms", "Heuristic Search", "Bfs", "DFS", "Trees And Graphs"]
toc:
  enable: false
zhtw: false
---
![](https://miro.medium.com/max/1400/0*23Lg7cs2V8LRNlvY)

Photo by  [Kevin Ku](https://unsplash.com/@ikukevk?utm_source=medium&utm_medium=referral)  on  [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

# Is BFS/DFS a Greedy Algorithm and Why?

Though, the simple answer could be YES. To better understand this I would suggest reading on greedy vs heuristics algorithm.

> _Greedy algorithms supply an exact solution! Heuristic algorithms use probability and statistics in order to avoid running through all the possibilities and provide an “estimated best solution” (which means that if a better solution exists, it will be only slightly better)._

A greedy algorithms follow locally optimal solution at each stage. While searching for the best solution, the best so far solution is only updated if the search finds a better solution. Whereas this is not always the case with heuristic algorithms (e.g. genetic, evolutionary, Tabu search, ant search, and so forth). Heuristic algorithms may update the best so far even if it’s worse than the best so far to avoid getting trapped in a local optimal solution.

_Therefore, in nutshell BFS/DFS generally fall under greedy algorithms._

# [Breadth First Search vs Greedy Algorithm](https://stackoverflow.com/questions/62665126/breadth-first-search-vs-greedy-algorithm#:~:text=The%20term%20%22greedy%20algorithm%22%20refers,it%20to%20an%20optimization%20problem.)

The term “greedy algorithm” refers to algorithms that solve optimization problems.

> _BFS is not specifically for solving optimization problems, so it doesn’t make sense (i.e., it’s not even wrong) to say that BFS is a greedy algorithm unless you are applying it to an optimization problem. In that case, the statement is true or not depending on how it is applied._

The “reputable algorithm book” probably refers to BFS in the context of a specific optimization problem, and is probably correct to say that it is a greedy algorithm in that context… which you have omitted in your question.

# [Greedy Algorithms](https://www.geeksforgeeks.org/greedy-algorithms/)

Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. So the problems where choosing locally optimal also leads to global solution are the best fit for Greedy.

A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage. In many problems, a greedy strategy does not produce an optimal solution, but a greedy heuristic can yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.

For example, a greedy strategy for the  [travelling salesman problem](https://en.wikipedia.org/wiki/Greedy_algorithm)  (which is of high computational complexity) is the following heuristic: “At each step of the journey, visit the nearest unvisited city.” This heuristic does not intend to find the best solution, but it terminates in a reasonable number of steps; finding an optimal solution to such a complex problem typically requires unreasonably many steps. In mathematical optimization, greedy algorithms optimally solve combinatorial problems having the properties of matroids and give constant-factor approximations to optimization problems with the submodular structure.

# [Heuristic Algorithms](https://optimization.mccormick.northwestern.edu/index.php/Heuristic_algorithms)

A heuristic algorithm is one that is designed to solve a problem in a faster and more efficient fashion than traditional methods by sacrificing optimality, accuracy, precision, or completeness for speed. Heuristic algorithms often times used to solve NP-complete problems, a class of decision problems. In these problems, there is no known efficient way to find a solution quickly and accurately although solutions can be verified when given. Heuristics can produce a solution individually or be used to provide a good baseline and are supplemented with optimization algorithms. Heuristic algorithms are most often employed when approximate solutions are sufficient and exact solutions are necessarily computationally expensive.

# Traveling Salesmen Problem

A well-known example of a heuristic algorithm is used to solve the common Traveling Salesmen Problem. The problem is as follows: given a list of cities and the distances between each city, what is the shortest possible route that visits each city exactly once? A heuristic algorithm used to quickly solve this problem is the nearest neighbor (NN) algorithm (also known as the Greedy Algorithm). Starting from a randomly chosen city, the algorithm finds the closest city. The remaining cities are analyzed again, and the closest city is found.

![](https://miro.medium.com/max/786/0*YMp1sYH--NsPsvZv)

Figure 1: Example of how the nearest neighbor algorithm functions.

These are the steps of the NN algorithm:

1.  Start at a random vertex
2.  Determine the shortest distance connecting the current vertex and an unvisited vertex V
3.  Make the current vertex the unvisited vertex V
4.  Make V visited
5.  Record the distance traveled
6.  Terminate if no other unvisited vertices remain
7.  Repeat step 2.5

This algorithm is heuristic in that it does not take into account the possibility of better steps being excluded due to the selection process. For n cities, the NN algorithm creates a path that is approximately 25% longer than the most optimal solution.

# [What’s the difference between greedy and heuristic algorithm?](https://stackoverflow.com/questions/21537028/whats-the-difference-between-greedy-and-heuristic-algorithm)

> _their main characteristic is to choose the best (local) option at each iteration_

Not at all true for heuristics. Heuristic algorithms are making choices that are know to be suboptimal in theory, but have been proved in practice to produce reasonable results.  [Heuristics](http://en.wikipedia.org/wiki/Heuristic_%28computer_science%29)  usually find an  _approximate_  solution:

> _In computer science, artificial intelligence, and mathematical optimization, a heuristic is a technique designed for solving a problem more quickly when classic methods are too slow, or for finding an approximate solution when classic methods fail to find any exact solution. This is achieved by trading optimality, completeness, accuracy, or precision for speed._

Greedy is an example of heuristic (make the best local choice and hope for the optimal global result), but that does not mean heuristics are greedy. There are many heuristics completely unrelated to greedy, eg.  [genetic algorithms are considered heuristic](http://en.wikipedia.org/wiki/Genetic_algorithm):

> _In the computer science field of artificial intelligence, a genetic algorithm (GA) is a search heuristic that mimics the process of natural selection._

Wrapping up…

-   Are all Heuristics, Greedy Algorithms — No
-   Are all Greedy Algorithms, Heuristics — In general, yes.

Trees and Graphs:  [Data-Structures-and-Algorithms-in-Python/Trees and Graphs at main · chienhsiang-hung/Data-Structures-and-Algorithms-in-Python (github.com)](https://github.com/chienhsiang-hung/Data-Structures-and-Algorithms-in-Python/tree/main/Trees%20and%20Graphs)

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)