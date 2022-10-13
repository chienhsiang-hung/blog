---
title: "D-Link Dir 853 Access Point Mode (AP Mode) Network Subnet 路由器AP設定"
date: 2022-10-13T12:13:00+08:00
lastmod: 2022-10-13T12:16:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "先按壓 Router Reset 10秒，至192.168.0.1"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Dir 853", "Access Point", "Ap Mode", "Network Subnet", "路由器ap設定"]
toc:
  enable: true
zhtw: true
---
先按壓 Router Reset 10秒，至`192.168.0.1`

![](https://miro.medium.com/max/700/1*FFNotMaCRMgtT58Ast_fow.png)

登入後按照指令設定

Navbar點選無效

![](https://miro.medium.com/max/700/1*4UigCK9qn7t8Xlz4scoZzg.png)

直接在網址列type in:  `192.168.0.1/Network.html`

進行後續設定

![](https://miro.medium.com/max/700/1*4PCVOPDwKHEqsv1Pa62FhQ.png)

## AP 設定

例如將子網域(Network Subnet)設為`.0.2`

LAN =  `192.168.0.2`

Subnet Mask =  `255.255.255.0`

然後再重新連接 確認能透過  `192.168.0.2`  進入控制台 且能成功上網 就成功了

Resources:

[Tutorial Video](https://www.youtube.com/watch?v=tLFCZJNpKaE)