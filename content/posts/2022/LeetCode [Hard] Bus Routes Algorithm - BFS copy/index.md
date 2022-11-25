---
title: "PowerApps HtmlText Common CSS Adjustments"
date: 2022-11-25T10:31:00+08:00
lastmod: 2022-11-25T10:31:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "css div full screen, css center horizontally and vertically, css button width based on char count, css style not working, Background Opacity CSS"
resources:
- name: "featured-image"
  src: ""
tags: ["Algorithms", "Leetcode", "Bfs", "Breadth First Search", "Python"]
toc:
  enable: true
---
## Dcoration
### Div Full Screen
css div full screen `position: absolute;`[^css-make-a-div-height-full-screen]
```css
.box {
  background:red;
  position:absolute;
  top:0px;
  right:0px;
  bottom:0px;
  left:0px;
}
```
### Center Horizontally and Vertically
css center horizontally and vertically[^centering-vertically-and-horizontally-with-CSS]

- **not so good methods (won't work on PowerApps)**

    **Using tables**
    ```html
    <table>
        <tr>
            <td>
            Centered content
            </td>
        </tr>
    </table>
    ```
    ```css
    table {
        width: 100%;
        height: 100%;
    }

    td {
        vertical-align: center;
        text-align: center;
    }
    ```
    **Using FlexBox**
    ```html
    <div>Centered content</div>
    ```
    ```css
    div {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    ```
- **Suggested method which works on Powerapps correctly:**

    **Using translations**
    ```html
    <div>Centered content</div>
    ```
    ```css
    div {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    ```
### Button Width Fit to The Text
css button width based on char count

as simple as `width: fit-content;`

*If you are developing to a modern browser. https://caniuse.com/#search=fit%20content [^make-button-width-fit-to-the-text]*
### Troubleshooting CSS
css style not working[^how-to-troubleshoot-css-not-working]

i.e. if you put the style below to button in `HtmeText` control, things below the `font-family: "JetBrains Mono",monospace;` won't applied
```css
/* CSS */
.button-30 {
  align-items: center;
  appearance: none;
  background-color: #FCFCFD;
  border-radius: 4px;
  border-width: 0;
  box-shadow: rgba(45, 35, 66, 0.4) 0 2px 4px,rgba(45, 35, 66, 0.3) 0 7px 13px -3px,#D6D6E7 0 -3px 0 inset;
  box-sizing: border-box;
  color: #36395A;
  cursor: pointer;
  display: inline-flex;
  font-family: "JetBrains Mono",monospace;
  height: 48px;
  justify-content: center;
  line-height: 1;
  list-style: none;
  overflow: hidden;
  padding-left: 16px;
  padding-right: 16px;
  position: relative;
  text-align: left;
  text-decoration: none;
  transition: box-shadow .15s,transform .15s;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
  will-change: box-shadow,transform;
  font-size: 18px;
}
```
since you need to change `"` to `'` which you need to use `Char(20)`/`Char(34)` here instead. change it to `font-family: "&Char(20)&"JetBrains Mono"&Char(20)&",monospace;`.
### Background Opacity CSS
you can either do it like
```html
<p style='
    position: absolute;
    text-align: center;
    background-color: transparentize(#e3e3e3,0.5);
    z-index: 1;
'>
    <i>You will be transfered to the external app <b>WFO</b></i>
</p>
<p style='
    position: absolute;
    text-align: center;
    background-color: #e3e3e3;
    opacity: 0.5;
'>
    <i>You will be transfered to the external app <b>WFO</b></i>
</p>
```
or use `background-color: rgba(0, 0, 0, 0.5);`[^css-background-opacity]

[^css-make-a-div-height-full-screen]: [CSS Make A Div Height Full Screen [THREE SIMPLE WAYS] (softauthor.com)](https://softauthor.com/css-make-a-div-height-full-screen/)
[^centering-vertically-and-horizontally-with-CSS]: [Centering vertically and horizontally with CSS (alvaromontoro.com)](https://alvaromontoro.com/blog/67995/centering-vertically-and-horizontally-with-CSS)
[^make-button-width-fit-to-the-text]: [html - Make button width fit to the text - Stack Overflow](https://stackoverflow.com/questions/27722872/make-button-width-fit-to-the-text)
[^how-to-troubleshoot-css-not-working]: [How to Troubleshoot CSS Not Working (wpforms.com)](https://wpforms.com/docs/how-to-troubleshoot-css-not-working/)
[^css-background-opacity]: [html - CSS Background Opacity - Stack Overflow](https://stackoverflow.com/questions/10422949/css-background-opacity)