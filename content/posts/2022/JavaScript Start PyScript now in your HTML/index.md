---
title: "JavaScript? Start PyScript now in your HTML"
date: 2022-07-22
lastmod: 2022-07-22
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "PyScript is a meta project that aims to combine multiple open technologies into a framework that allows users to create sophisticated browser applications with Python. It integrates seamlessly with the way the DOM works in the browser and allows users to add Python logic in a way that feels natural both to web and Python developers."
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Pyscript", "JavaScript", "Python", "HTML", "Website"]
toc:
  enable: true
zhtw: false
---
## PyScript is a meta project that aims to combine multiple open technologies into a framework that allows users to create sophisticated browser applications with Python. It integrates seamlessly with the way the DOM works in the browser and allows users to add Python logic in a way that feels natural both to web and Python developers.

# Try PyScript

To try PyScript, import the appropriate pyscript files to your html page with:
```html
<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />  
<script defer src="https://pyscript.net/alpha/pyscript.js"></script>
```
You can then use PyScript components in your html page. PyScript currently implements the following elements:

-   `<py-script>`: can be used to define python code that is executable within the web page. The element itself is not rendered to the page and is only used to add logic
-   `<py-repl>`: creates a REPL component that is rendered to the page as a code editor and allows users to write executable code

_From official doc_

Check out the  [pyscriptjs/examples](https://github.com/chienhsiang-hung/pyscript/tree/main/pyscriptjs/examples)  folder for more examples on how to use it, all you need to do is open them in Chrome.

# New Version Has a Better Initialization EX

![](https://miro.medium.com/max/1400/1*dZZKcNOqrxHZeKpJD4NSqg.png)

You can do basically everything even  **import a CSV file**  and read it with Pandas just like that.

## HTML
```html
<div id="temp_test">  
      <h3>wait</h3>  
    </div>
```
## PyScript
```html
 <py-script output="temp_test">  
import pandas as pd  
a = pd.read_csv('./test.csv')  
a  
    </py-script>
```
Just put this in to your <head> in HTML
```html
<link rel="stylesheet" href="[https://pyscript.net/alpha/pyscript.css](https://pyscript.net/alpha/pyscript.css)" />  
    <script defer src="[https://pyscript.net/alpha/pyscript.js](https://pyscript.net/alpha/pyscript.js)"></script>  
    <py-env>  
        - pandas  
        - paths:  
          - ./test.csv  
    </py-env>
```
or you can output just like how you always do in  **Jupyter Notebook**
```html
<py-script>  
from datetime import datetime  
now = datetime.now()  
now  
    </py-script>
```
_*import package from inside `<py-script>`*_

All mentioned are done in a  [demo](https://chienhsiang-hung.github.io/pyscript/)

Finally you can even have a  [**Python Online IDE**](https://chienhsiang-hung.github.io/pyscript/pyscript-hello-world)  for yourself. Use this:
```html
<div>  
        <py-repl id="my-repl" auto-generate="true"></py-repl>  
    </div>
```
Let’s go [try out](https://github.com/chienhsiang-hung/pyscript) then!

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)