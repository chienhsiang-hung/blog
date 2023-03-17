---
title: "Power Automate OpenAI connector and How to Standardize the ChatGPT Response to JSON Format"
date: 2023-03-17T00:53:00+08:00
lastmod: 2023-03-17T00:53:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: ""
featuredimage: share-it-as-a-link.png
tags: []
toc:
  enable: true
---
## OpenAI Connector
[OpenAI (Independent Publisher) - Connectors | Microsoft Learn](https://learn.microsoft.com/en-us/connectors/openaiip/#gpt3-completes-your-prompt)

The OpenAI IP Connector is a tool that allows you to use GPT-3 to complete your prompts in Microsoft Learn. You can write a partial sentence or paragraph and let GPT-3 generate the rest of the text based on your style and tone. You can also adjust the parameters such as creativity, length and temperature to fine-tune the output. The OpenAI IP Connector is a great way to enhance your learning experience and explore new possibilities with GPT-3.

## Use it in Power Automate
![gpt3-completes-your-prompt-connector.png](gpt3-completes-your-prompt-connector.png "gpt3-completes-your-prompt-connector")
Search the **GPT3 Completes your prompt** Connector in your power automate flow then give it a name and Enter API Key as `Bearer YOUR_API_KEY`. When entering your API key in the Power Platform, you need to type it as: "Bearer YOUR_API_KEY" (the word "Bearer" a blank and the actual API_KEY).[^OpenAI]
[^OpenAI]: [PowerPlatformConnectors/independent-publisher-connectors/OpenAI at dev · microsoft/PowerPlatformConnectors (github.com)](https://github.com/microsoft/PowerPlatformConnectors/tree/dev/independent-publisher-connectors/OpenAI)

And you can find API Key here: [Overview - OpenAI API](https://platform.openai.com/) with the documentation i.e. Token Usage, Parameters setting etc.

## Pass Long Content
There is a 4096 token limitation in openai so you wouldn't be able to pass contents or receive the prompt longer than that. **What if you need openAI help you to summarize great contents but too long?**

Congratulations! I will show you a workaround for you in the power platform.
### Sharepoint for a Link
You can store the contents as a html etc. and put in on Sharepoint List like I did here. Then share it as a link to GPT3 for the task. This way you saved a ton of tokens but still get it reading the contents and doing the job for you.
![share-it-as-a-link.png](share-it-as-a-link.png "share-it-as-a-link")
Now another problem came up. How do we structure the response so that we can write the data back to our database? There are many ways to do this. Here I show you a simple example.

## Structure The Answer
You can either show an example or explicitly tell the machine to do what you want. In most situations, they work as same and will give you the result you want. But if we want to write it back to our database, we need them to be standardized like if I ask the GPT to summarize the link provided and extract certain information. I can do:
```
<URL>

Please read the information on this page and tell me your summary, and the related stock tickers and related industries mentioned in the following way in 2 languages - English and Traditional Chinese.
[English]
1. summary: the summary of this page
2. tickers: a list of related stock tickers in yahoo finance format i.e. [AAPL, GOOG] if there are no related stock tickers, return leave []
3. industries: a list of the related industries as above put them in [] using "," as separators if there are no related industries, leave []
[繁體中文]
1.大綱:...
2.標的股票:...
3.產業:...
```
Or you can replace the format if you want the JSON format.
```
<URL>
Please read the information on this page and tell me your summary, and the related stock tickers and related industries mentioned in the following way in 2 languages - English and Traditional Chinese.
{
    "English": {
        "Tickers": "a list of related stock tickers in yahoo finance format i.e. [AAPL, GOOG] if there are no related stock tickers, return leave []",
        "Summary": "the summary of this info",
        "Industries": "a list of the related industries as above put them in [] using ',' as separators if there are no related industries, leave []"
    },
    "繁體中文":{
        "大綱": "上面的Summary中文版",
        "產業": "上面的Industries中文版"
    }
}
```
But in this format, it will reply with the format full of space as we typed above. For better usage, we need to give the GPT a more specific guide and remove the space and`\n` etc. You can use this site to easily minify your JSON - [Best JSON Viewer and JSON Beautifier Online (codebeautify.org)](https://codebeautify.org/jsonviewer).
```
<URL>
Please read the information on this page and tell me your summary, and the related stock tickers and related industries mentioned in the following format(json) in 2 languages - English and Traditional Chinese.
{"English":{"Tickers":"a list of related stock tickers in yahoo finance format i.e. [AAPL, GOOG] if there are no related stock tickers, return []","Summary":"the summary of this info","Industries":"a list of the related industries as above put them in [] using ',' as separators if there are no related industries, return []"},"繁體中文":{"大綱":"上面的Summary中文版","產業":"上面的Industries中文版"}}
```
Last, the question is how do we read the answer in Power Automate.
## Parse JSON
That is, compose a JSON schema and use the `Parse JSON` connector that way we don't need to *handle the text response ourselves*.

(something like this if you know what I mean :grinning: `\n- {\"股票代號\":...\n\n[\"English\"]\n\"Tickers: [AAPL]\nSummary:`).

You can use this site to convert your JSON to JSON schema - [Free Online JSON to JSON Schema Converter (liquid-technologies.com[)](https://www.liquid-technologies.com/online-json-to-schema-converter) for use in the `Parse JSON` connector.

At first, I tried to *compose it by myself[^json-schema.org][^Parse-JSON-action]* and examine it through [this site](https://www.liquid-technologies.com/online-json-to-schema-converter) (it kept on showing errors even though the schema is right) but found it so inefficient in a way.
[^json-schema.org]: [Getting Started Step-By-Step | JSON Schema (json-schema.org)](https://json-schema.org/learn/getting-started-step-by-step.html)
[^Parse-JSON-action]: [How to use Parse JSON action in Power Automate (m365princess.com)](https://www.m365princess.com/blogs/2021-02-08-how-to-use-parse-json-action-in-power-automate/)

![json-schema-validator.png](json-schema-validator.png "json-schema-validator")
I think this site doesn't work so well so I strongly suggest just using the combination of the above two sites to form a schema and minification for the `prompt`.
![Parse-JSON-Schema.png](Parse-JSON-Schema.png "Parse-JSON-Schema")
And, vola! It works perfectly.
![JSON-result.png](JSON-result.png "JSON-result")