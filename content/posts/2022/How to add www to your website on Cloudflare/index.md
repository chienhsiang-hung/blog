---
title: "How to add www to your website on Cloudflare"
date: 2022-06-19
lastmod: 2022-06-19
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "After you add your site to the Cloudflare, you mind wondering how to add www to your naked domain. Here is how:"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Cloudflare", "Domains", "DNS"]
toc:
  enable: false
zhtw: false
---
After you add your site to the Cloudflare, you mind wondering how to add www to your naked domain. Here is how:

1.  Go to your Cloudflare dashboard then click on the Navbar-> DNS.

![](https://miro.medium.com/max/594/1*vVAn_Ul6VnEA__CF7aepkA.png)

2. Then scroll down to add an A record and point IP to 192.0.2.1

![](https://miro.medium.com/max/1400/1*jCBDeMULh3FZkjbXGnWQfQ.png)

3. Go to the Rules

![](https://miro.medium.com/max/624/1*MFUPK52SMQNYMUalcKx7cw.png)

4. Deploy a page rule like this

![](https://miro.medium.com/max/1400/1*BEn4ObpIRIjSulyPS_dnLQ.png)

URL’s last character ‘*’ means forward all pages and keep the path

Thanks to DOMJH —  [Redirect www.example.com to example.com](https://community.cloudflare.com/t/redirect-www-example-com-to-example-com/78347)

and  [Redirecting www to domain apex · Cloudflare Pages docs](https://developers.cloudflare.com/pages/how-to/www-redirect/)