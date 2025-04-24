---
title: "Microsoft CSA"
date: 2025-04-24T04:00:00+08:00
lastmod: 2025-04-24T04:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://hsiang.eu.org/"
images: ["posts/2024/typescript-and-vue/type-warning.png"]
featuredimage: type-warning.png
tags: []
toc:
  enable: true
lightgallery: true
---
## JD
### Power Platform Consultant
#### Required Experience
- 5+ years of leading digital transformation initiatives using low-code/no-code solutions.
- 5+ years of experience working in operational organization or supporting various operational functions, ensuring efficiency and alignment with business goals.
#### Required Qualifications:
- Experience with low-code/no-code platforms (e.g., Microsoft Power Platform)
- Familiarity with integration between low-code platforms and other enterprise systems (e.g., CRM, ERP) is a plus.
- Strong understanding of business process automation and workflow optimization.
- Effective communication and stakeholder management skills.
- Technical knowledge of Power Platform extensibility into pro-code solutions such as PowerApps Framework Controls and Application Lifecycle Management.
- Familiarity with Microsoft Entra, Purview, and security products to ensure Power Platform solutions are compliant, secure, and scalable within enterprise environments.
- Experience integrating Power Platform solutions with Azure services (e.g., Azure Logic Apps, Azure API Management, Azure Functions) to build enterprise-grade solutions.
- Knowledge of security best practices within the Power Platform ecosystem

## Preparation
### Self-intro
### Questions
1. Can you describe a digital transformation initiative you led using low-code/no-code solutions?

    <b>
    In my previous company...
    
    I am currently leading the lectures design and teaching at Aiworks for Power Automate.

    In my current company, I lead a digital transformation initiative. Because the progress of the larger company to adopt...
    </b>
2. How have you ensured efficiency and alignment with business goals in your previous roles?

    <b>always rmb to check the cost (for dev and maintenance) and the benefit</b>
3. What experience do you have with integrating low-code platforms with CRM or ERP systems?
    
    <b>
    copilot studio -> power automate -> (ground truth searching) KM api (top 5)

    approval system... (writing logs back to old system, 2 ways work)
    </b>
4. How do you approach business process automation and workflow optimization?

    <b>
    identify bottlenecks and inefficiencies

    (meeting room booking system? re-build all? integrating w/ the new resources)

    (get outlook information and wrapped as api by power automate)

    (cancel meeting and cancel meeting room)
    </b>
5. Can you discuss your technical knowledge of PowerApps Framework Controls and Application Lifecycle Management?

    <b>
    (PCF) power apps component framework: I've reated custom controls to visualize complex data using charts and graphs
    
    the custom controls were built using `typescript`

    (ALM) haven't got into that...
    </b>
6. How have you ensured compliance, security, and scalability within enterprise environments using Microsoft Entra, Purview, and other security products?

    <b>Purbiews ediscovery / retention policy / auditlog to track the usage</b>
7. What experience do you have with integrating Power Platform solutions with Azure services like Azure Logic Apps, Azure API Management, and Azure Functions?

    <b>structured product quotation system (quote for the prce)</b>
8. What are some security best practices you follow within the Power Platform ecosystem?

    <b>Implementing role-based access control; using data encryption - TDE (Transparent Data Encryption)...</b>

#### Technicals
1. How do you integrate Power Apps with Dataverse to manage data effectively?

    <b>leveragin dataverse role-based access control, data validation rules and utilize dataverse data delegation</b>
2. Can you describe a scenario where you used Power Automate to automate a business process?

    <b>stock trading rules</b>
3. How do you ensure data security when using Azure SQL and Blobs for storage?
4. How have you utilized Azure Functions to enhance the capabilities of Power Platform solutions?
5. Can you explain how AI Foundry and Copilot Studio can be used to build intelligent applications?
6. How do you troubleshoot and optimize Power Automate flows?

    <b>built-in flow checker, monitor flow performance, error handling and retry polices (use flow to monitor flow)</b>
7. How do you create custom controls in Power Apps to enhance user experience?

    <b>
    creating custom controls using PCF (PowerApps Component Framework) to visualize complex data using chart and graphs.

    the custom controls were built using `typescript`.
    </b>
8. Can you explain the concept of delegation in Power Apps and how it impacts performance?

    <b>
    means offloading data processing to the data source rather than handling it within the app (device's RAM). it's crucial for performance when dealing with large datasets.

    delegation tables check:
    - https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/connections/connection-common-data-service#power-apps-delegable-functions-and-operations-for-dataverse
    - https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/connections/connection-sharepoint-online#power-apps-delegable-functions-and-operations-for-sharepoint
    - https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/connections/sql-connection-overview#power-apps-functions-and-operations-delegable-to-sql-server
    </b>
9. How do you handle non-delegable queries in Power Apps?

    <b>views in dataverse / or duplicated sharepoint in combined w/ playing with collections</b>
10. Can you describe a scenario where you used Power Apps custom controls and delegation together?

    <b>there is this app I implemented custom control that will display groups photos and groups meta data interactively. I use dataverse to handle delegation group data. this provided a rich user experience, handling large dataset smoothly, shift the workload from front end back to server side</b>
##### Guessing
