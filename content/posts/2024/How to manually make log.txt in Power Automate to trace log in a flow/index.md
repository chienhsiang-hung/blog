---
title: "How to manually make log.txt in Power Automate to trace log in a flow"
date: 2024-05-02T09:09:00+08:00
lastmod: 2024-05-02T09:09:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
images: ["posts/2024/how-to-manually-make-log.txt-in-power-automate-to-trace-log-in-a-flow/test-logging.png"]
featuredimage: test-logging.png
tags: ["Power Automate"]
toc:
  enable: true
lightgallery: true
---
## Introduction
In the world of automation, tacing and logging are essential for diagnosing and understanding the behavior of automated workflows. Power Automate provides robust capabilities for creating flow, but sometimes you noeed to manually trace these flows for better insights. In this blog post, we'll briefly explore how to manually create a log.txt file in Power Automate to trace logs in a flow.

## Actions We Need
1. We need to first create a sample txt file in the folder.
2. and use `Get file content`
3. then follow the `Update file` to update the logs

![Test Logging.png](test-logging.png "Test Logging")
![Test Result.png](test-result.png "Test Result")
![Go Production.png](go-prod.png "Go Production")