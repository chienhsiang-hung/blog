---
title: "Address to Lat Long Free"
date: 2022-09-20T04:00:00+08:00
lastmod: 2022-09-20T04:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Find lat long coordinates"
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Lat Long", "Address", "Coordinates", "Geocode Addresses", "Latitude Longitude"]
toc:
  enable: true
zhtw: false
---
![](https://miro.medium.com/max/1400/0*YG5OpbKwiMgpdDag)

Photo by  [Robert Penaloza](https://unsplash.com/@robertography?utm_source=medium&utm_medium=referral)  on  [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

# Find lat long coordinates

[QGIS Geocoding Plugins (Free)](https://gisgeography.com/geocoders/)

the  [Python Geocoder](https://pypi.python.org/pypi/geocoder)  is another open-source library that leverages Python to retrieve lat long coordinates from Google Maps. One of its advantages is that it can be used completely separately from QGIS.

# Python Geocoder

## Simple and consistent geocoding library written in Python.

Many online providers such as Google & Bing have geocoding services,  
these providers do not include Python libraries and have different  
JSON responses between each other.

It can be very difficult sometimes to parse a particular geocoding provider  
since each one of them have their own JSON schema.

Here is a typical example of retrieving a Lat & Lng from Google using Python, things shouldn’t be this hard.
```python
>>> import requests    
>>> url = 'https://maps.googleapis.com/maps/api/geocode/json'    
>>> params = {'sensor': 'false', 'address': 'Mountain View, CA'}    
>>> r = requests.get(url, params=params)    
>>> results = r.json()['results']    
>>> location = results[0]['geometry']['location']    
>>> location['lat'], location['lng']    
(37.3860517, -122.0838511)
```
Now lets use Geocoder to do the same task
```python
>>> import geocoder    
>>> g = geocoder.google('Mountain View, CA')    
>>> g.latlng    
(37.3860517, -122.0838511)
```
# ArcGIS

The World Geocoding Service finds addresses and places in all supported countries from a single endpoint. The service can find point locations of addresses, business names, and so on. The output points can be visualized on a map, inserted as stops for a route, or loaded as input for a spatial analysis. an address, retrieving imagery metadata, or creating a route.

# Geocoding
```python
>>> **import** geocoder  
>>> g = geocoder.arcgis**(**'Redlands, CA'**)**  
>>> g.json  
...
```
This provider may return multiple results by setting the parameter maxRows to the desired number (1 by default). You can access those results as described in the page ‘[Access to geocoder results](https://geocoder.readthedocs.io/results.html)’.

# Command Line Interface
```
$ geocode 'Redlands, CA' --provider arcgis
```
# Parameters

-   location: Your search location you want geocoded.
-   maxRows: (default=1) Max number of results to fetch
-   limit:  _Deprecated_, same as maxRows
-   method: (default=geocode) Use the following:
-   geocode

# References

-   [ArcGIS Geocode API](https://developers.arcgis.com/rest/geocode/api-reference/overview-world-geocoding-service.htm)
-   [ArcGIS — geocoder 1.38.1 documentation](https://geocoder.readthedocs.io/providers/ArcGIS.html)

# Usage Example

-   [NRICM101-map/FetchLatLon.py at main · chienhsiang-hung/NRICM101-map (github.com)](https://github.com/chienhsiang-hung/NRICM101-map/blob/main/steps/FetchLatLon.py)
-   [臺灣清冠一號地圖 Taiwan NRICM101 Map (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/NRICM101-map/)
-   [chienhsiang-hung/NRICM101-map: 臺灣清冠一號地圖 Taiwan NRICM101 Map | 一個方便大家快速查詢 剩餘人數以及公費等資訊的清冠地圖 (github.com)](https://github.com/chienhsiang-hung/NRICM101-map)

A handy tool to get lat long from address, helps you to convert address to coordinates (latitude longitude) on map, also calculates the gps coordinates.

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)