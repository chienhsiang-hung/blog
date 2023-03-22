---
title: "Power Automate Update Sharepoint List Item Choice Column and Difference Between Choices and Distinct"
date: 2023-03-22T08:45:00+08:00
lastmod: 2023-03-22T08:45:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: ""
featuredimage: 
tags: []
toc:
  enable: true
zhtw: true
---
## Update Sharepoint List Item Choice Column
**Power Automate - Microsoft Forms & SharePoint choice field (multi-select) updates**

You can update the choice list item by this:
{{< youtube wX1TVWedVGA >}}

### TL;DW
Make sure you can generate the following `cell value`/`item`:
```
{
  "Value": "<iterated item>"
}
```
But like [Destroyzer](https://www.youtube.com/channel/UCoKVtS-C2ON7pP9MxXB5-NQ) mentioned:
> the items is added on my list in this way:
> 
> {"Value":"Desvio em processo"}{"Value":"Desvio em relatório"}

or it will show like `@variable('YourArrayVariable')` literally when you try to add it manually. We just can't add the arr variable to the PA connector by **Dynamic Content**. Why?

### Solution
It turned out it's the column setting in the Sharepoint List was wrong. Make sure you've selected the **Allow multiple selections** in the advanced setting of the choices column.
![column-setting-choice-AllowMultipleSelections.png](column-setting-choice-AllowMultipleSelections.png "column-setting-choice-AllowMultipleSelections")
Then you can go back to your Power Automate flow. You'll see the input box changed. Then you clicked on the icon shown below to *switch to input entire array mode*.
![switch-to-input-entire-array.png](switch-to-input-entire-array.png "switch-to-input-entire-array")
Vola! Now you can add the array variable you created before to the choice column.
![you-will-be-able-to-see-your-arr.png](you-will-be-able-to-see-your-arr.png "you-will-be-able-to-see-your-arr")