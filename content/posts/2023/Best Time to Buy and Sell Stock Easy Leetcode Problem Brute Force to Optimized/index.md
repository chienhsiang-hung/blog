---
title: "Best Time to Buy and Sell Stock Easy Leetcode Problem Brute Force to Optimized"
date: 2023-05-24T05:01:00+08:00
lastmod: 2023-05-24T05:01:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
images: ["posts/2023/best-time-to-buy-and-sell-stock-easy-leetcode-problem/Best%20Time%20to%20Buy%20and%20Sell%20Stock.png"]
featuredimage: Best%20Time%20to%20Buy%20and%20Sell%20Stock.png
tags: ["Leetcode", "Leetcode Easy", "Brute Force", "Optimization", "Data Structure Algorithm"]
toc:
  enable: true
---
## Problem
[Best Time to Buy and Sell Stock - LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

You are given an array  `prices`  where  `prices[i]`  is the price of a given stock on the  `ith`  day.

You want to maximize your profit by choosing a  **single day**  to buy one stock and choosing a  **different day in the future**  to sell that stock.

Return  _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return  `0`.

**Example 1:**

**Input:** prices = [7,1,5,3,6,4]
**Output:** 5
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2:**

**Input:** prices = [7,6,4,3,1]
**Output:** 0
**Explanation:** In this case, no transactions are done and the max profit = 0.

**Constraints:**

-   `1 <= prices.length <= 105`
-   `0 <= prices[i] <= 104`
## Brute Force to Optimized
![alt Best%20Time%20to%20Buy%20and%20Sell%20Stock.png](Best%20Time%20to%20Buy%20and%20Sell%20Stock.png "Best Time to Buy and Sell Stock")
```python
# prices = [7,1,5,3,6,4]

min_ = prices[0]
profit = 0
for p in prices[1:]:
  profit = max(profit, p-min_)
  min_ = min(min_, p)
return profit
```
