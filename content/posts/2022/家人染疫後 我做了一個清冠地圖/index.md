---
title: "家人染疫後 我做了一個清冠地圖"
date: 2022-08-19
lastmod: 2022-08-19
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "臺灣清冠一號地圖 Taiwan NRICM101 Map"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["清冠一號", "清冠一號地圖", "清冠地圖", "台灣清冠一號地圖", "台灣清冠一號哪裡買"]
toc:
  enable: true
zhtw: true
---
# 臺灣清冠一號地圖 Taiwan NRICM101 Map

![](https://miro.medium.com/max/1400/1*yFTZ4hA7x87y0bfTfi4cyw.png)

> _家人同事染疫 與 網友確診搜索公費清冠一號並能視訊看診之中醫上困難_
> 
> _決定製作清冠地圖 供大家免費查閱_

[臺灣清冠一號地圖 Taiwan NRICM101 Map](https://chienhsiang-hung.github.io/NRICM101-map/)

*_初次使用因資料量龐大約需等待4~6秒載入診所資訊 ( 資料庫每20分鐘更新一次 )_

利用國家中醫藥研究所與中醫師公會全國聯合會合作建置公費清冠一號醫療資訊平台 — 公費清冠一號 (供全台民眾查詢)，供中醫視訊診療需求之COVID-19確診病患、家屬透過  [臺灣清冠一號地圖 Taiwan NRICM101 Map](https://chienhsiang-hung.github.io/NRICM101-map/)  ，查詢提供公費清冠ㄧ號之中醫醫療院所名單及當日公費清冠ㄧ號庫存量，以利民眾獲得所需醫療資訊。

如有任何使用建議歡迎  [到此提出](https://github.com/chienhsiang-hung/NRICM101-map/issues)  謝謝

# 使用API獲取清冠地圖

![](https://miro.medium.com/max/1400/0*3MYm2OxYgc9uR4Wr.png)

_(update frequency — 20min)_
```
GET https://nricm101-map.chienhsiang-hung.eu.org/api/get  
Return .json
```
[清冠地圖API](https://nricm101-map.chienhsiang-hung.eu.org/api/get)  開放給民眾免費使用

資料量大 (全台中醫資料)  [清冠地圖API](https://nricm101-map.chienhsiang-hung.eu.org/api/get)  平均讀取時間為4~6秒。已開放`'Access-Control-Allow-Origin'`  to  `'*'`  ，歡迎其他前端接取免費測試。唯因系統只有一人維護還請大家斟酌使用，不便之處敬請見諒😅

# 待新增Features

-   搜尋地址 (When Device Local Info Failed)
-   搜尋診所
-   公費圖層 (Filter)
-   TBD

# #Resources

[臺灣清冠一號地圖 Taiwan NRICM101 Map](https://chienhsiang-hung.github.io/NRICM101-map/)  搭配資料來源  [「清冠一號動態表」](https://docs.google.com/spreadsheets/d/e/2PACX-1vQjf_HNeEZKM-XJX-q5v4cfNrB3kcv4gOT8kFbV9rurfoX_H5Qv9112Pv0PgYNFSzbReyNlQkLrJib3/pubhtml)

-   [Leaflet — a JavaScript library for interactive maps](https://leafletjs.com/)
-   [OpenStreetMap](https://www.openstreetmap.org/copyright)
-   [Copied icon PNG and SVG Vector](https://uxwing.com/copied-icon/)
-   [Instruction icon PNG and SVG Vector](https://uxwing.com/instruction-icon/)
-   [Modal · Bootstrap](https://getbootstrap.com/docs/4.0/components/modal/#via-data-attributes)

網站聲明請參閱[免責聲明| 臺灣清冠一號地圖 Taiwan NRICM101 Map](https://chienhsiang-hung.github.io/NRICM101-map/immunity.html)

# 一杯咖啡支持更新

感謝有您的支持讓地圖能夠穩定持續更新。

[Chien-Hsiang Hung (buymeacoffee.com)](https://www.buymeacoffee.com/abcdefg2981)

[Buy Chien-Hsiang Hung a Coffee. ko-fi.com/chienhsianghung — Ko-fi ❤️](https://ko-fi.com/chienhsianghung)

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)