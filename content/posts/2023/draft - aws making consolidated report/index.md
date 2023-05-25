---
title: "draft - aws making consolidated report"
date: 2023-05-25T02:00:00+08:00
lastmod: 2023-05-25T02:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
images: ["posts/2023/power-platform-and-cloud-azure-aws-handover-to-another-employee/organization-root-users.png"]
featuredimage: organization-root-users.png
tags: [""]
toc:
  enable: true
hiddenFromHomePage: true
hiddenFromSearch: true
lightgallery: true
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
## Structure
*(EXAMPLE)*

**TableandChart**
- Code
  + Python 3.9 (Architecture x86_64), HTML and CSS
    - main package - matplotlib
- Layers
  + dataVisLayer
  + AWSDataWrangler-Python39	
  + numerize

**HtmltoPDF**
- Code
  + Python 3.9 (Architecture x86_64)
    - main package - pandas, PyPDF2
    - custom-fonts
- Layers
  + wkhtmltopdf
  + pandas
  + fonts
  + PyPDF2

## How to Deploy a Lambda Function
### Regions
**First check your region.**
<!-- {{< image src="RegionsManagement.png" alt="RegionsManagement.png" caption="RegionsManagement.png" title="RegionsManagement.png">}} -->
![RegionsManagement.png](RegionsManagement.png "RegionsManagement.png")
**Find the nearest (server) region.**
![NearestRegion.png](NearestRegion.png "NearestRegion.png")
*choose Singapore for Operation (in Asia)*
### Create function
> [Lambda](https://ap-southeast-2.console.aws.amazon.com/lambda/home?region=ap-southeast-2#/) > [Functions](https://ap-southeast-2.console.aws.amazon.com/lambda/home?region=ap-southeast-2#/functions) > [Create function](#Create-function)

![Create-function.png](Create-function.png "Create-function.png")
#### Add trigger (API Gateway)
![Function-overview.png](Function-overview.png "Function-overview.png")
![Add-trigger.png](Add-trigger.png "Add-trigger.png")
