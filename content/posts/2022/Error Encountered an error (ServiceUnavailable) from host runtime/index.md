---
title: "Error: Encountered an error (ServiceUnavailable) from host runtime."
date: 2022-12-14T07:50:00+08:00
lastmod: 2022-12-14T07:50:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "You can explicitly set a specific host ID for your function app in the application settings by using the AzureFunctionsWebHost__hostid setting. For more information, see…"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Azure", "Deployment", "Http Trigger", "Vscode", "Runtime"]
toc:
  enable: true
---
Azure syncing triggers runtime error when deploying HTTP trigger Function app.

![](https://miro.medium.com/max/631/1*GC8hdm4vTqZWpNI2ULrhrw.png)

Let’s open up the Azure Portal to check the App.

![](https://miro.medium.com/max/700/1*xLIQrSgr0Zqo8dwX4LF8ZQ.png)

# Azure Functions Runtime Is Unreachable

Problem description  [Azure Functions Runtime Is Unreachable — Azure Lessons](https://azurelessons.com/azure-functions-runtime-is-unreachable/#Check_if_the_storage_account_Exists)

## Online solutions:

[c# — Azure Functions runtime is unreachable — Stack Overflow](https://stackoverflow.com/questions/72377617/azure-functions-runtime-is-unreachable)

[解決一個非常罕見的 Azure Functions Runtime is unreachable 問題 | The Will Will Web (miniasp.com)](https://blog.miniasp.com/post/2022/01/18/Azure-Functions-Runtime-is-unreachable-edge-case-study)

Directions:

-   Function App Configuration/Setting
-   Re-create the function app

# Troubleshoot error: “Azure Functions Runtime is unreachable”

[Troubleshoot error: Azure Functions Runtime is unreachable | Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/functions-recover-storage-account#storage-account-application-settings-were-deleted)

-   Storage account was deleted
-   Storage account application settings were deleted
-   Required application settings
-   [App settings reference for Azure Functions | Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#azurewebjobsstorage)
-   …

# Host ID considerations / Override the host ID

[Storage considerations for Azure Functions | Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations?tabs=azure-cli#override-the-host-id)

You can explicitly set a specific host ID for your function app in the application settings by using the  `AzureFunctionsWebHost__hostid`  setting. For more information, see  [AzureFunctionsWebHost__hostid](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#azurefunctionswebhost__hostid).

(GUID generator  [Free Online GUID Generator](https://guidgenerator.com/online-guid-generator.aspx)  and  [WordCounter — Count Words & Correct Writing](https://wordcounter.net/)  to fit 1–32 chrs condition)

When the collision occurs between slots, you may need to mark this setting as a slot setting. To learn how to create app settings, see  [Work with application settings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings#settings).

# AzureFunctionsWebHost__hostid

[App settings reference for Azure Functions | Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#azurefunctionswebhost__hostid)

# After a series of trying, my apps were all dying…

Thus I concluded that as an official issue and wait. Hours later it came back normal…