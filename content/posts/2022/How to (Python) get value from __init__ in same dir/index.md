---
title: "How to (Python) get value from __init__ in same dir"
date: 2022-08-24
lastmod: 2022-08-24
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "If you get"
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Python", "Class", "Modules", "Import", "Variables"]
toc:
  enable: false
zhtw: true
---
![](https://miro.medium.com/max/1400/0*F3Yp9KVm6pBl-Pps)

Photo by  [Chris Ried](https://unsplash.com/@cdr6934?utm_source=medium&utm_medium=referral)  on  [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

If you get

`ImportError: attempted relative import with no known parent package`

when you do like
```python
import . from something
```
especially from the script executed, just try
```python
from __init__ import something
```
Even though it could be problematic when there are many  `__init__.py`s in  `sys.path`, it would be helpful in some simple situaions.

by  [ghchoi](https://stackoverflow.com/users/4227175/ghchoi)

# [How to import from the __init__.py in the same directory?](https://stackoverflow.com/questions/42862042/how-to-import-from-the-init-py-in-the-same-directory)

I see ‘import from parent module’ as an anti-pattern in Python. Imports should be the other way around. Importing from modules’s  `__init__.py`  is especially problematic. As you noticed, importing module  `foo.bar`  from  `foo/bar.py`  involves importing  `foo/__init__.py`  first, and you may end up with a circular dependency. Adding a  `print("Importing", __name__)`  to your init files helps see the sequence and understand the problem.

I’d suggest that you moved the code you want to import in  `conditions.py`  from  `__init__.py`  to a separate lower-level module, and just import some names from that module in  `__init__.py`  to expose it at higher level.

Let’s suppose that you had some  `class Bar`  in your  `__init__.py`. I'd reorganize it the following way.

`__init__.py`:
```python
from bar import Bar  # exposed at the higher level, as it used to be.
```
`bar.py`:
```python
class Bar(object): ...
```
`conditions.py`:
```python
from . import Bar  # Now it works.
```
Ideally an  `__init__.py`  should contain nothing but imports from lower-level modules, or nothing at all.

by  [9000](https://stackoverflow.com/users/223424/9000)

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)