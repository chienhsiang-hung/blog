---
title: "draft - aws making consolidated report"
date: 2023-05-23T11:00:00+08:00
lastmod: 2023-05-23T11:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
images: ["posts/2023/power-platform-and-cloud-azure-aws-handover-to-another-employee/organization-root-users.png"]
featuredimage: organization-root-users.png
tags: [""]
toc:
  enable: true
---
## Flow Outline
{{< mermaid >}}
flowchart TD
  subgraph PowerPlatform
    subgraph PowerApps
      WIT
    end
    PowerApps --> PowerAutomate
    subgraph PowerAutomate
      WAM_monthly_statement
    end
  end
  
  WAM_monthly_statement -- "POST" --> TableandChart
  WAM_monthly_statement -. "(delay 2 mins) <br>GET" .-> wampdfs

  subgraph AWS
    subgraph Lambda
      TableandChart -- "invoke RequestResponse" --> HtmltoPDF
    end
    HtmltoPDF --> wampdfs
    subgraph S3
      wampdfs
    end
  end
{{< /mermaid >}}
## Classes
TableandChart
- Code
  + Python 3.9 (Architecture x86_64), HTML and CSS
- Layers
  + dataVisLayer
  + AWSDataWrangler-Python39	
  + numerize
