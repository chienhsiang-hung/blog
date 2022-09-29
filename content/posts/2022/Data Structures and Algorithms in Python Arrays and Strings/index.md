---
title: "Data Structures and Algorithms in Python | Arrays and Strings"
date: 2022-07-24
lastmod: 2022-07-24
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "In this series and in the next few weeks, I will show you Data Structures and Algorithms in Python by some classic interview solutions…"
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Data Structures", "Algorithms", "Python", "Arrays", "String"]
toc:
  enable: false
zhtw: false
---
In this series and in the next few weeks, I will show you Data Structures and Algorithms in Python by some classic interview solutions. Please take a pen, whiteboard, and your laptop. Let’s start learning!

![](https://miro.medium.com/max/1400/0*KETX-BIADtDFfUP1.jpg)

Cheat sheet to  [Arrays and Strings](https://github.com/chienhsiang-hung/Data-Structures-and-Algorithms-in-Python/tree/main/Arrays%20and%20Strings). And some heads up for you.

# Creating a Matrix in Python without numpy
```python
new_matrix  = [ [None]*height ] *  width

This way, all the inner list will be pointed to the same address, i.e.

test_list = [[]]*5  
id(test_list[0]) == id(test_list[1])

Do something like this instead.

new_matrix = []  
i = 0  
while i < width:  
    new_matrix.append([]) # add a row  
    j = height - 1  
    while j >= 0:  
        new_matrix[i].append(matrix[j][i])
```
See example  [Data-Structures-and-Algorithms-in-Python/Rotate Matrix.py at main · chienhsiang-hung/Data-Structures-and-Algorithms-in-Python (github.com)](https://github.com/chienhsiang-hung/Data-Structures-and-Algorithms-in-Python/blob/main/Arrays%20and%20Strings/Rotate%20Matrix.py)

# Unittest Heads Up

# ‘in-place’ function

When doing unittest for ‘in-place’ function, remember to deepcopy the test set for looping tests, i.e.
```python
from copy import deepcopyfor (_input, _output) in  self.test_cases:  
    _input = deepcopy(_input) # don't forget this line, because it changes original input that make your right answer to be wrong
```
or
```python
for text, expected in self.test_cases:  
    _input = deepcopy(text) # don't forget this line, because it changes original input that make your right answer to be wrong  
    for func in self.testable_functions:  
        start = time.perf_counter()  
        func(_input)  
        assert(  
            _input == expected  
        ), f'{func.__name__} failed for value: {text}, output={_input}, expected={expected}'
```
or
```python
for (_input, _output) in test_cases:  
    _input_copy = _input.copy()  
    assert zero_matrix(_input_copy) == _output
```
See example

-   [Data-Structures-and-Algorithms-in-Python/Rotate Matrix.py at main · chienhsiang-hung/Data-Structures-and-Algorithms-in-Python (github.com)](https://github.com/chienhsiang-hung/Data-Structures-and-Algorithms-in-Python/blob/main/Arrays%20and%20Strings/Rotate%20Matrix.py)
-   [Data-Structures-and-Algorithms-in-Python/Zero Matrix.py at main · chienhsiang-hung/Data-Structures-and-Algorithms-in-Python (github.com)](https://github.com/chienhsiang-hung/Data-Structures-and-Algorithms-in-Python/blob/main/Arrays%20and%20Strings/Zero%20Matrix.py)

Test your script:  [Hsiang | PyScript Hello World (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/pyscript/pyscript-hello-world)

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)