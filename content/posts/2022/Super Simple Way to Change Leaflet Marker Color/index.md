---
title: "Super Simple Way to Change Leaflet Marker Color"
date: 2022-08-18
lastmod: 2022-08-18
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Is there a way to randomly change marker-colors in native Leaflet? Many ways demonstrated in Leaflet changing Marker color."
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Leaflet", "Leafletjs", "Leaflet Marker Color", "JavaScript", "Javascript Map"]
toc:
  enable: false
zhtw: false
---
![](https://miro.medium.com/max/1400/0*f470wE_ChycLkfTo)

Photo by  [henry perks](https://unsplash.com/@hjkp?utm_source=medium&utm_medium=referral)  on  [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Is there a way to randomly change marker-colors in native Leaflet? Many ways demonstrated in  [Leaflet changing Marker color](https://stackoverflow.com/questions/23567203/leaflet-changing-marker-color).

Here is a super simple way without swallowing up the documentation to achieve your goal presented by  [sil](https://stackoverflow.com/users/1418014/sil).

> A cheap way to change the Leaflet marker colour is to use the CSS  `filter`  property. Give the icon an extra class and then change its colour in the stylesheet
```html
<style>  
img.huechange { filter: hue-rotate(120deg); }  
</style>  
<script>  
var marker = L.marker([y, x]).addTo(map);  
marker._icon.classList.add("huechange");  
</script>
```
And this will produce a red marker: alter the value given to  `hue-rotate`  to alter the colour. Like my example —  [臺灣清冠一號地圖 Taiwan NRICM101 Map (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/NRICM101-map/).

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)