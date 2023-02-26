---
title: "[PowerApps] Display Dates in a Combo Box, Distinct not Showing all Records, Filter on Date won’t Work"
date: 2023-02-24T06:08:00+08:00
lastmod: 2023-02-24T06:08:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Display Dates in a Combo Box"
featuredimage: featured-image.png
tags: ["Powerapps", "Dataverse", "Microsoft Dataverse", "Combobox", "Distinct"]
toc:
  enable: true
---
## [Display Dates in a Combo Box](http://powerappsguide.com/blog/post/display-dates-in-a-combo-box)

Getting value but not  `“yyyy-mm-dd”`  like format for dates records in a combo box?

Change you items with  `ForAll`  or  `AddColumns`:
```
ForAll(AvailableDates,   
      {  
        DateValue:ViewingDate,   
        DateDisplay:Title & " - " & Text(ViewingDate, "dd mmm yy")  
      }  
)
```
Then it will display correctly:

![](https://miro.medium.com/max/651/0*VSbhtLWtbBLk8i2p.png)

But how to show a  `DefaultItems`?

X:  `[values]`

O:  `{column_name: value}`

## PowerApps Distinct not Showing all Records?

(2000 records limitation on each query)

workarounds:

1.  [[Canvas Apps — Dataverse] How to get distinct values from datasource ? — XRM Tricks (Power Platform & Dynamics CRM )](https://xrmtricks.com/2022/03/12/canvas-apps-dataverse-how-to-get-distinct-values-from-datasource/)

or you can:

1.  Create a view to  `Filter`  in DataVerse
2.  To use  `view`  in PowerApps:  `Filter(table, table.view)`

## Invalid Schema Expected a One-column Table PowerApps
```
IsBlank(categoryBox_1.SelectedItems.Val) || IsEmpty(categoryBox_1.SelectedItems) || mib_fld_tbl_std_Saving_Category_varchar in categoryBox_1.SelectedItems.Val
```
```
IsBlank(ProjectIDBox_1.SelectedItems.<columnName>) || IsEmpty(ProjectIDBox_1.SelectedItems.<columnName>) || mib_fld_tbl_std_Saving_Type_varchar in ProjectIDBox_1.SelectedItems.<columnName>
```
`ProjectIDBox_1.SelectedItems.<columnName>`  type in <columnName> manually instead of expecting that to be auto-generated after  `.`  by PowerApps system.

## PowerApps Filter on Date won’t Work

It works for operants  `>`  `<`  but  `=`  for DateTime data type. You can try create a new column in the DataVerse with the data using formula like  `Text(Year(<Datetime>))&Text(Month(<Datetime>), “00”)`  to convert DateTime to String.