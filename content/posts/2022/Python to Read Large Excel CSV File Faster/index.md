---
title: "Python to Read Large Excel/CSV File Faster"
date: 2022-11-17T05:23:00+08:00
lastmod: 2022-11-17T05:23:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: ""
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Python", "Read Excel File", "Pandas", "Pandas Dataframe", "Read Csv"]
toc:
  enable: true
---
![featured-image.jpg](featured-image.jpg "Img Source: https://unsplash.com/photos/Wpnoqo2plFA")
## Read a CSV with PyArrow
In Pandas 1.4, released in January 2022, there is a new backend for CSV reading, relying on the Arrow library’s CSV parser. It’s still marked as experimental, and it doesn’t support all the features of the default parser—but it is faster.[^pandas-read-csv-fast]

<table>
  <thead>
    <tr>
      <th>CSV parser</th>
      <th style="text-align: right">Elapsed time</th>
      <th style="text-align: right">CPU time (user+sys)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Default C</td>
      <td style="text-align: right">13.2 seconds</td>
      <td style="text-align: right">13.2 seconds</td>
    </tr>
    <tr>
      <td>PyArrow</td>
      <td style="text-align: right">2.7 seconds</td>
      <td style="text-align: right">6.5 seconds</td>
    </tr>
  </tbody>
</table>

```python
import pandas as pd

pd.read_csv('Example.csv', engine='pyarrow')
```
**Notice, it's only feasible by `pd.read_csv()` not `pd.read_excel()`.**

In `pd.read_excel()`:
> `engine`: *str, default `None`*
>
> If io is not a buffer or path, this must be set to identify io. Supported engines: “xlrd”, “openpyxl”, “odf”, “pyxlsb”.[^pandas.read_excel]
### Upgrade Pandas
`pip install --upgrade pandas --user`

Noted --user is needed for windows user to handle:
```
ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied: ...
Consider using the `--user` option or check the permissions.
```
## Read Large Excel File Faster
### Parallel
Let’s imagine that you received excel files and that you have no other choice but to load them as is. You can also *use `joblib` to parallelize this*[^joblib]. Compared to our pickle code from above, we only need to update the loop function.[^read-excel-files-with-python-1000x-faster]
### Just One File
Standard `usecols`, `nrows`, `skiprows` experiment.
```python
def load_in_positions():
    '''
    @return: Positions DataFrame
    '''
    print(f'Retrieving Positions.xlsx with Pandas--{pd.__version__}...Please hold on...')

    start = time.time()
    xlsx = pd.read_excel(CFG.Positions_xlsx_path, sheet_name="Position")
    print(f'time used:\n{time.time()-start}\nxlsx:\n{xlsx}')

    start = time.time()
    xlsx = pd.read_excel(CFG.Positions_xlsx_path, sheet_name="Position", usecols=[
        'Date', 'ISIN', 'MSCI ESG Rating', 'Bloomberg ESG Disclosure Score', 'Sustainalytics ESG Risk Rating', 'Sustainalytics ESG Risk Score'
    ])
    print(f'time used:\n{time.time()-start}\nxlsx:\n{xlsx}')
```

    time used:
    40.02475333213806
    time used:
    38.12591814994812

Other great ideas to reduce time on reading data like `chunk` etc, read on [Big Data from Excel to Pandas | Python Charmers](https://pythoncharmers.com/blog/csv-xls-too-big-data-excel-to-pandas.html).

[^pandas-read-csv-fast]: [The fastest way to read a CSV in Pandas (pythonspeed.com)](https://pythonspeed.com/articles/pandas-read-csv-fast/)
[^pandas.read_excel]: [pandas.read_excel — pandas 1.5.1 documentation (pydata.org)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)
[^joblib]: [joblib · PyPI](https://pypi.org/project/joblib/)
[^read-excel-files-with-python-1000x-faster]: [Do You Read Excel Files with Python? There is a 1000x Faster Way. | by Nicolas Vandeput | Towards Data Science](https://towardsdatascience.com/read-excel-files-with-python-1000x-faster-407d07ad0ed8)