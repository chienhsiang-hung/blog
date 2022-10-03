---
title: "Understand Python Path — Import Variable From __init__.py (update)"
date: 2022-09-06T10:00:00+08:00
lastmod: 2022-09-06T10:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "This is an update for How to (Python) get value from __init__ in same dir | by 洪健翔 Hung, Chien-hsiang | Aug, 2022 | Medium. Make sure you…"
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Python", "Import", "Path", "Variables", "Modules"]
toc:
  enable: false
zhtw: true
---
This is an update for  [How to (Python) get value from \_\_init\_\_ in same dir | by 洪健翔 Hung, Chien-hsiang | Aug, 2022 | Medium](https://hungchienhsiang.medium.com/hot-to-python-get-value-from-init-in-same-dir-ab3982589500). Make sure you have read the previous one. Let’s get started!

![](https://miro.medium.com/max/1400/0*u0-PawlvltYTMdx-)

Photo by  [AltumCode](https://unsplash.com/@altumcode?utm_source=medium&utm_medium=referral)  on  [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Dir Structure:

—ModuleName

| — \_\_init\_\_.py

| — bar.py

`__init__.py`:
```python
colour_map_earth_tone = ['#E8D0A9', '#B7AFA3', '#C1DAD6', '#b7baba', '#ACD1E9', '#6D929B']
```
`bar.py`:
```python
if __name__ == '__main__': 
  from __init__ import colour_map_earth_tone
else: 
  from . import colour_map_earth_tone
```
This way you can successfully import the var from \_\_init\_\_.py when both testing and production using.

_original q:_ [_Can I use \_\_init\_\_.py to define global variables?_](https://stackoverflow.com/questions/1383239/can-i-use-init-py-to-define-global-variables)

Contact Me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)