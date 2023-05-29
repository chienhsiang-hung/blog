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
  + dataVisLayer (custom)
  + AWSDataWrangler-Python39	
  + numerize (custom)

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
> [Lambda](https://ap-southeast-1.console.aws.amazon.com/lambda/home?region=ap-southeast-1#/) > [Functions](https://ap-southeast-1.console.aws.amazon.com/lambda/home?region=ap-southeast-1#/functions) > [Create function](#Create-function)

![Create-function.png](Create-function.png "Create-function.png")
#### Add trigger (API Gateway)
![Function-overview.png](Function-overview.png "Function-overview.png")
![Add-trigger.png](Add-trigger.png "Add-trigger.png")
#### Layers
**2 ways to add layers**
- Add layer `AWSSDKPandas-Python310` at the Functions page *(`AWSDataWrangler-Python39` upgrades to `AWSSDKPandas-Python310`)*
![Add-AWS-layers-AWSSDKPandas-Python310.png](Add-AWS-layers-AWSSDKPandas-Python310.png "Add-AWS-layers-AWSSDKPandas-Python310.png")
> [Lambda](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/) > [Layers](#Layers)

If you can't find the ARN or you need to customize some packages inside.
- Create layer
![Create-layer.png](Create-layer.png "Create-layer.png")
- Layer configuration
![Layer-configuration.png](Layer-configuration.png "Layer-configuration.png")

***Including library dependencies in a layer:***
<table id="w366aac23c43c23b7">
  <thead>
    <tr><th class="table-header" colspan="100"><div class="title">Layer paths for each Lambda runtime</div></th></tr>
    <tr>
      <th>Runtime</th>
      <th>Path</th>
    </tr>
  </thead>
    <tbody><tr>
      <td rowspan="4">
        <p>Node.js</p>
      </td>
      <td>
        <p><code class="code">nodejs/node_modules</code></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code class="code">nodejs/node14/node_modules</code> (<code class="code">NODE_PATH</code>)</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code class="code">nodejs/node16/node_modules</code> (<code class="code">NODE_PATH</code>)</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code class="code">nodejs/node18/node_modules</code> (<code class="code">NODE_PATH</code>)</p>
      </td>
    </tr>
    <tr>
      <td rowspan="2">
        <p>Python</p>
      </td>
      <td>
        <p><code class="code">python</code></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code class="code">python/lib/python3.10/site-packages</code>(site directories)</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Java</p>
      </td>
      <td>
        <p><code class="code">java/lib</code> (<code class="code">CLASSPATH</code>)</p>
      </td>
    </tr>
    <tr>
      <td rowspan="2">
        <p>Ruby</p>
      </td>
      <td>
        <p><code class="code">ruby/gems/2.7.0</code> (<code class="code">GEM_PATH</code>)</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code class="code">ruby/lib</code> (<code class="code">RUBYLIB</code>)</p>
      </td>
    </tr>
    <tr>
      <td rowspan="2">
        <p>All runtimes</p>
      </td>
      <td>
        <p><code class="code">bin</code> (<code class="code">PATH</code>)  </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code class="code">lib</code> (<code class="code">LD_LIBRARY_PATH</code>)</p>
      </td>
    </tr>
  </tbody>
</table>

*See [Creating and sharing Lambda layers - AWS Lambda (amazon.com)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).*
##### Runtime Check
Remember to check your function runtime. Make sure the runtime of layers and the function are the same.
![Runtime-settings.png](Runtime-settings.png "Runtime-settings.png")
###### AWS Data Wrangler
And, for **AWSDataWrangler-Python39** (Python*XX* should meet your runtime version as well), the `ARN` should be `arn:aws:lambda:YOUR-REGION:336392948345:layer:AWSDataWrangler-Python39:2`. For example, **AWS Data Wrangler Lambda Layer - 2.15.0 (Python 3.9)** and region **Singapore** will be `arn:aws:lambda:ap-southeast-1:336392948345:layer:AWSDataWrangler-Python39:2`.
![AWS-Data-Wrangler-Lambda-Layer.png](AWS-Data-Wrangler-Lambda-Layer.png "AWS-Data-Wrangler-Lambda-Layer.png")
### Deploy
2 ways to manually CI/CD
#### Download and Upload
1. Actions > **Export function** > Download deployment package
![Export-function.png](Export-function.png "Export-function.png")
2. (edit your code package)
3. **Compress your files > Upload from > .zip file**
![Upload-from-zip-file.png](Upload-from-zip-file.png "Upload-from-zip-file.png")
#### Edit on the Portal
1. Save
2. Deploy
