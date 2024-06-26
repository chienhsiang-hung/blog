---
title: "AWS Deploy Lambda Function, API Gateway, Invoke/Call another Lambda Function, Save to S3, Public Access etc."
date: 2023-05-31T07:53:00+08:00
lastmod: 2023-05-31T07:53:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
images: ["posts/2023/aws-deploy-lambda-function-api-gateway-invoke-call-another-lambda-function-save-to-s3-public-access-etc/S3-permission-access-public.png"]
featuredimage: S3-permission-access-public.png
tags: ["AWS Lambda", "Aws S3", "Api Gateway", "Lambda Layer", "Aws Data Wrangler"]
toc:
  enable: true
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
*(ABSTRACT EXAMPLE)*

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
#### Configuration
##### Timeout
*Task timed out after 3.09 seconds...*

General configuration Timeout ~~3 sec (default)~~ set to 10 min (max).
![Timeout.png](Timeout.png "Timeout.png")
##### Existing role
And, from here, choose an **Existing role**.
![Basic-settings.png](Basic-settings.png "Basic-settings.png")
You have to create it manually for your lambda function if you want to use it to call another function.
#### Environment variables
(For HtmltoPDF function)
![Environment-variables-for-HtmltoPDF.png](Environment-variables-for-HtmltoPDF.png "Environment-variables-for-HtmltoPDF.png")
#### Roles
> [IAM](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/home) > [Roles](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/roles)
##### Create role
to create a role and add permission
![create-a-role.png](create-a-role.png "create-a-role.png")
![Select-trusted-entity.png](Select-trusted-entity.png "Select-trusted-entity.png")
add permissions (or create policy)
![Add-permissions.png](Add-permissions.png "Add-permissions.png")
![Create-policy-Specify-permissions.png](Create-policy-Specify-permissions.png "Create-policy-Specify-permissions.png")
###### Invoke Role
To invoke another lambda function in AWS.
- Permissions policies - Customer managed - `InvokeHtmltoPDF`
  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Sid": "VisualEditor0",
              "Effect": "Allow",
              "Action": [
                  "lambda:InvokeFunction",
                  "lambda:InvokeAsync"
              ],
              "Resource": "arn:aws:lambda:region:account-id:function:function-name"
          }
      ]
  }
  ```
  `Resource`: *lambda function arn[^Lambda-ARN]*, replace`region`, `account-id` and `function-name`.

  [^Lambda-ARN]: [The Lambda ARN (Amazon Resource Name) does not show up at top right when i create a function for Alexa skill set - Stack Overflow](https://stackoverflow.com/questions/38448999/the-lambda-arn-amazon-resource-name-does-not-show-up-at-top-right-when-i-creat)

- Permissions policies - AWS managed - `AWSLambdaBasicExecutionRole`
  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "logs:CreateLogGroup",
                  "logs:CreateLogStream",
                  "logs:PutLogEvents"
              ],
              "Resource": "*"
          }
      ]
  }
  ```
###### lambda to s3
lambda-s3-role
- Permissions policies - AWS managed - `AWSLambdaExecute`
  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "logs:*"
              ],
              "Resource": "arn:aws:logs:*:*:*"
          },
          {
              "Effect": "Allow",
              "Action": [
                  "s3:GetObject",
                  "s3:PutObject"
              ],
              "Resource": "arn:aws:s3:::*"
          }
      ]
  }
  ```
### Amazon S3
#### Create bucket
**Configuration**

General configuration
- Bucket name *(Bucket with the same name already exists: Bucket name must be globally unique and must not contain spaces or uppercase letters. [See rules for bucket naming](https://docs.aws.amazon.com/console/s3/bucket-naming))*

  <span hidden>~~wampdfs~~`wam-consolidated-pdfs`</span>
- AWS Region
  
  <span hidden>`Singapore`</span>

Object Ownership
- ACLs enabled
- Bucket owner preferred

Block Public Access settings for this bucket
- untick `Block all public access`
- I acknowledge that the current settings might result in this bucket and the objects within becoming public.

Bucket Versioning - `Disable`

Default encryption
- Encryption key type

  `Amazon S3 managed keys (SSE-S3)`
- Bucket Key

  `Disable`

Advanced settings
- Object Lock

  `Disable`
#### Object URL
For it to work publicly, you need to add a **Bucket policy** to make the Bucket `Publicly accessible`.
![Object-overview.png](Object-overview.png "Object-overview.png")
Go to [Amazon S3](https://s3.console.aws.amazon.com/s3/get-started?region=us-east-1) > [Buckets](https://s3.console.aws.amazon.com/s3/buckets?region=us-east-1) > YOURBUCKET > Permissions > Bucket policy
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::YOUTBUCKETNAME/*"
        }
    ]
}
```
*Replace the `Resource` with your Bucket.*

*Be careful, the objects in this bucket will all be <mark>publicly available</mark> by default.* ***So don't leak your Object URL (bucket name and file name) out.***

Once you've applied the *policy* successfully, you will see the changes made in the Permission overview sector.
![S3-permission-access-public.png](S3-permission-access-public.png "S3-permission-access-public.png")
Now you can access the object through the **Object URL**.
### Connectors
update codes' connection
#### Lambda function to Lambda function
```python
import boto3
client = boto3.client('lambda')

response  = client.invoke(
    # arn:aws:lambda:region:account-id:function:function-name
    FunctionName = 'arn:aws:lambda:REGION:ACCOUNT-ID:function:FUNCTION-NAME',
    InvocationType = 'RequestResponse',
    Payload = json.dumps({
        'example': your_var,
    })
)
# responseFromChild = json.load(response['Payload'])
```
#### Lambda function to S3
Lambda function save/upload to S3
```python
import boto3

s3 = boto3.resource('s3')
s3.meta.client.upload_file("/tmp/TEST_FILE.txt", 'YOUR_BUCKET_NAME', "NEW_FILE_NAME.txt")
```
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
