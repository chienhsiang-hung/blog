---
title: "binary tree random node python"
date: 2022-10-03T03:40:00+08:00
lastmod: 2022-10-03T04:10:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "isnanx commented on 30 Apr 2019"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Hugo", "Word Count", "Chinese", "Blog", "Post"]
toc:
  enable: true
zhtw: false
---
# Random Node
From the book - **Cracking the Coding Interview** (*4.11*).
Build a **binary tree class** along with the **insert**, **delete**, **find** and the **getRandomNode** method which returns a random node in the tree. (All nodes shall have the same possibility to be returned.)

## Brute Force
> The intuition brute force solution would be to traverse all nodes and collect them into an array/list then randomly choose one of them out of Uniform Distribution.
> 
> Time: O(n)
>
> Space: O(1)

## Optimized
Though **it would be nicer if we can give a O(1) method. Since we are given the ownership of the whole class (generated from the scratch)**, we can simply record the size in order to produce a uniform random choice.

### Record the Size in Node
```python
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.size = 1
```

Then update the insert and the delete function. *The delete function would be a bit tricky to implement*.

The solution provided by the book outsource github isn't quite right on [the delete function](https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_04/p11_random_node.py#L52). (The size property wasn't being taken care of quite right.)
```python
def delete_helper(self, node, key):

    if node is None:
        return node

    if key < node.key:
        node.left = self.delete_helper(node.left, key)

    elif key > node.key:
        node.right = self.delete_helper(node.right, key)

    else:
        if node.left is None:
            temp, node = node.right, None
            return temp

        elif node.right is None:
            temp, node = node.left, None
            return temp

        temp = min_val_node(node.right)
        node.key = temp.key
        node.right = self.delete_helper(node.right, temp.key)

    node.size -= 1
    return node
```