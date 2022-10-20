---
title: "PowerApps Run failed: Connection not configured for this service."
date: 2022-10-20T07:43:00+08:00
lastmod: 2022-10-20T07:43:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "The problem: One of my Power Automate flows can’t not be added or triggered successfully in PowerApps related the problem in last the last…"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Powerapps", "Power Automate", "Connector", "Connection", "Flow"]
toc:
  enable: true
zhtw: false
---
The problem: One of my Power Automate flows can’t not be added or triggered successfully in PowerApps related the problem in last the last post —  [PowerApps Unable to Add Flow — Hung, Chien-Hsiang 洪健翔 | Blog (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/blog/posts/2022/powerapps-unable-to-add-flow/)

![](https://miro.medium.com/max/622/1*prZG8Y37J6gc95dsfolFpw.png)

By following the solution in  [Solved: connection not configured for this service — Power Platform Community (microsoft.com)](https://powerusers.microsoft.com/t5/Using-Connectors/connection-not-configured-for-this-service/td-p/891993)

We raised Microsoft ticket and issue is resolved.

1.  Navigate to  **Power Apps Admin Center**
2.  Selected the  **Environment**  you are working.
3.  Click on  **Settings**  on top bar.
4.  Go to  **User + Permissions**  >>  **Security Roles**
5.  Under the Security Roles, find the  **Basic User**  role , click on ellipses (…) >>  **Edit**
6.  Under  **Customization**  tab >> Select  **Process >>** assign  **Read**  access to the Organization

![](https://miro.medium.com/max/400/0*bKOxUzdMG5SkCrBq)

1.  Workflow with  **OneDrive connection**  works without any issue.
2.  Hope it helps someone.

## That doesn’t work.

# Solution

Similar solution to  [Power Automate Flow run failed: Connection not configured for this service (sharepains.com)](https://sharepains.com/2022/04/27/connection-not-configured-for-this-service/)  and  [PowerApps Unable to Add Flow — Hung, Chien-Hsiang 洪健翔 | Blog (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/blog/posts/2022/powerapps-unable-to-add-flow/).

Reconnect the connector, Refresh, Re-publish several times, it worked.