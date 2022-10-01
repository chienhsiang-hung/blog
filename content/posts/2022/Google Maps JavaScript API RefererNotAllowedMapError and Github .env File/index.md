---
title: "Google Maps JavaScript API RefererNotAllowedMapError and Github .env File"
date: 2022-08-16
lastmod: 2022-08-16
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Clone Sample won’t work at npm start"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Referernotallowedmaperror", "Google Maps", "Javascript Api", "Github Actions", "Env File"]
toc:
  enable: false
zhtw: false
---
![](https://miro.medium.com/max/1400/1*_cPilbvs66iLoCN-IAro8Q.png)

# Clone Sample won’t work at npm start

sample project:  [Place Searches | Maps JavaScript API | Google Developers](https://developers.google.com/maps/documentation/javascript/examples/place-search)
```
git clone -b sample-place-search https://github.com/googlemaps/js-samples.git  
cd js-samples  
npm i  
npm start
```
![](https://miro.medium.com/max/1400/1*NNPJUJRF_glAG_r_R3N4YA.png)

A message like this kept showing up. If you clicked in docs, it only gave you  [useless instructions](http://if%20you%20clicked%20in%20docs%2C%20it%20only%20gave%20you%20useless%20instructions%20that%20won%27t%20work%20even%20if%20you%20tried%20million%20times./)  that won’t work even if you tried million times.

![](https://miro.medium.com/max/1400/1*SpICuYXzzE5t3Vnvoph11w.png)

# How to solve it?

First, go to  **See the Maps JavaScript API and** [**Get an API Key**](https://developers.google.com/maps/documentation/javascript/get-api-key#restrict_key)**.**

![](https://miro.medium.com/max/1400/1*SZS3VnnMQF802kHz3uD7LQ.png)

Make sure you have Maps API Key and empty the others to troubleshoot.

Somehow  `npm run build`  /  `vite build`  don’t use  `.env` to update your  **API key** in  `index.html`.

![](https://miro.medium.com/max/738/1*_NhGQlapt4TnyaKbwrKxNg.png)

![](https://miro.medium.com/max/1400/1*et_LLwmRS6y29lXd-D0z8A.png)

And, don’t forget to protect you key like mine  [here](https://console.cloud.google.com/apis/credentials/key):

![](https://miro.medium.com/max/1400/1*toyjUqftICji3Um60JfXHA.png)

![](https://miro.medium.com/max/1400/1*YLFrvUP4SHeufcw19FbRtw.png)

Resources:

[Google Maps JavaScript API RefererNotAllowedMapError — Stack Overflow](https://stackoverflow.com/questions/35288250/google-maps-javascript-api-referernotallowedmaperror)

[Google Maps Javascript API Error “RefererNotAllowedMapError” — GravityKit Support, Knowledge Base, How-To & Docs](https://docs.gravitykit.com/article/626-google-maps-error-referernotallowedmaperror)

# How to use GitHub Actions secrets to hide your tokens and passwords example

What if I want to use API key in  `build`/`Production`by creating  `.env`  file.

My  [example](https://github.com/chienhsiang-hung/NRICM101-map): (add a workflow to manually  **overwrite** or  **create** one  `.env`)

![](https://miro.medium.com/max/1400/1*ow5G9boSjgG70gnMMNVqKA.png)

Set up your API key by  [Github Actions Secrets](https://github.com/chienhsiang-hung/NRICM101-map)

![](https://miro.medium.com/max/1400/1*TCjCLN3B1mhBzBXqByLNHw.png)

Resources:

[Create .env file · Actions · GitHub Marketplace](https://github.com/marketplace/actions/create-env-file)

[environment variables — How do I use an env file with GitHub Actions? — Stack Overflow](https://stackoverflow.com/questions/60176044/how-do-i-use-an-env-file-with-github-actions)

[How to use GitHub Actions secrets to hide your tokens and passwords example (theserverside.com)](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/GitHub-Actions-Secrets-Example-Token-Tutorial)

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)