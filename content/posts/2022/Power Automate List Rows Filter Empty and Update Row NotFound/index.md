---
title: "Power Automate List Rows Filter Empty and Update Row NotFound."
date: 2022-09-06T04:00:00+08:00
lastmod: 2022-09-06T04:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Using ‘Filter Query’"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Power Automate", "Dataverse", "Odata", "Empty", "Update Table"]
toc:
  enable: false
zhtw: true
---
# Using ‘Filter Query’

The ‘List rows present in a table’ action itself supports filtering. When you ‘Show advanced options’ you’ll see a field ‘Filter Query’. Here, using an OData filter, you can define which rows will the action return. Format of the query is below.
```
<ColumnName> <operator> '<value>'

e.g. filter where column ColumnName is not equal to empty value:  
ColumnName ne ''
```
![](https://miro.medium.com/max/1400/0*LmHPidshu6gEZAsa.png)

[Skip empty row(s) when processing Excel file in Power Automate (tomriha.com)](https://tomriha.com/skip-empty-rows-when-processing-excel-file-in-power-automate/)

![](https://miro.medium.com/max/1400/1*JB0N7_FpaQuqmY4juGgc7A.png)

[Query data using the Web API (Microsoft Dataverse) — Power Apps | Microsoft Docs](https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#standard-filter-operators)

# Unable to update row in Dataverse

powerautomate update row NotFound.

![](https://miro.medium.com/max/1252/0*abw-ofsIrWXEhecL)

![](https://miro.medium.com/max/1236/0*KgnCqcf1flwzQwc4)

The output:
```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">  
<html xmlns="http://www.w3.org/1999/xhtml">  
<head>  
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>  
<title>404 - File or directory not found.</title>  
<style type="text/css">  
<!--  
body{margin:0;font-size:.7em;font-family:Verdana, Arial, Helvetica, sans-serif;background:#EEEEEE;}  
fieldset{padding:0 15px 10px 15px;}   
h1{font-size:2.4em;margin:0;color:#FFF;}  
h2{font-size:1.7em;margin:0;color:#CC0000;}   
h3{font-size:1.2em;margin:10px 0 0 0;color:#000000;}   
#header{width:96%;margin:0 0 0 0;padding:6px 2% 6px 2%;font-family:"trebuchet MS", Verdana, sans-serif;color:#FFF;  
background-color:#555555;}  
#content{margin:0 0 0 2%;position:relative;}  
.content-container{background:#FFF;width:96%;margin-top:8px;padding:10px;position:relative;}  
-->  
</style>  
</head>  
<body>  
<div id="header"><h1>Server Error</h1></div>  
<div id="content">  
 <div class="content-container"><fieldset>  
  <h2>404 - File or directory not found.</h2>  
  <h3>The resource you are looking for might have been removed, had its name changed, or is temporarily unavailable.</h3>  
 </fieldset></div>  
</div>  
</body>  
</html>
```
[saadzagh](https://powerusers.microsoft.com/t5/user/viewprofilepage/user-id/275658): The value for “Row ID=OData Id” is wrong, it should be the table identifier, like: contactid, incidentid…

[cirodom](https://powerusers.microsoft.com/t5/user/viewprofilepage/user-id/271452): the problem was the Row ID value, it should be the table identifier. Try to change that and will work

[Joshmart](https://powerusers.microsoft.com/t5/user/viewprofilepage/user-id/269771):

![](https://miro.medium.com/max/1400/0*TPc-OUvDhvjQTnzD)

[Solved: Unable to update row in Dataverse — Power Platform Community (microsoft.com)](https://powerusers.microsoft.com/t5/Building-Flows/Unable-to-update-row-in-Dataverse/td-p/961648)

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)