---
title: "Mock Technology Consulting Case Interview (Case Study): Architecture Strategy"
date: 2022-11-10T10:20:00+08:00
lastmod: 2022-11-11T01:56:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Architecture Strategy: Federal Finance Agency Practice Case from Deloitte and Christine Wong. Our client is a small division of a large Federal Finance Agency that is in charge of administering and enforcing economic and trade sanctions determined by US foreign policy and national security goals."
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: []
toc:
  enable: true
zhtw: false
---
![Tech Consulting](featured-image.jpg "Tech Consulting from https://unsplash.com/photos/n8Qb1ZAkK88")
## Case
*[Architecture Strategy: Federal Finance Agency Practice Case](https://docs.google.com/document/d/1-bYDsnRg4lzUpmVXavqS8jR_mGGeagFMj63du50PQOo) from [Deloitte]() and [Christine Wong](https://www.youtube.com/c/ChristineWong)[^CAREERCOACHING].*
### Architecture Strategy: Federal Finance Agency
Our client is a small division of a large Federal Finance Agency that is in charge of administering and enforcing economic and trade sanctions determined by US foreign policy and national security goals.
#### BUSINESS SITUATION
The agency’s office uses a number of software application systems to track and manage cases, applications, transactions, and other financial documents. Recently, the division has experienced increased workload due to changes in US foreign policy as well as high staff turnover. The change in US foreign policy and high staff turnover has led to a substantial backlog of unprocessed paperwork.

In addition, the organization’s business units are extremely siloed; each section of the organization has its own separate software application and database which creates redundant data in the system. The current systems used at this office are a mixture of in-house solutions and legacy systems developed by other contractors years ago. The organization wants to consolidate its systems to increase collaboration, streamline operations, and improve efficiency.
#### PROBLEM STATEMENT
An enterprise architecture plan is an overall structural strategy for all IT systems in an organization. This plan combines the business needs of key stakeholders to help an organization achieve its future goals. The officials of this agency have outlined the need for an overall structural strategy for all IT systems within their organization. Deloitte has been hired to assist with the analysis of the current systems and develop an implementation plan for a new, shared enterprise architecture solution spanning across all divisions of the organization.

*Key considerations:*

-   There are seven different internal systems being used by the organization. Each system uses the same development environment and database platform.

-   Most of the business units consist of lawyers and ex-military officers, who are experts in their field but not necessarily technology-oriented.

-   Many of the business units still work with hard-copies of cases and licenses that they need to process and hand-deliver to other business units for review.

-   High employee turnover has left remaining employees stretched very thin, including the IT department, whose time is mostly consumed providing maintenance support to employees using each of the systems.

-   Additional goals of the project include adapting to foreign languages, standardizing internal reporting and decreasing throughput time for form processing.

### Q1
Your manager has asked you to develop the new architecture plan by analyzing the current systems and interviewing stakeholders. What aspects of the current system would you want to analyze? How would you gather the information?
{{< admonition type=note title="Intuition" open=true >}}
**Architecture Plan** by
- Analyzing the current systems
- Interviewing stakeholders

+ What aspects would you focus on?
+ How to gather info?

I want to first check the current systems about 1. how much they...
{{< /admonition >}}
{{< admonition type=tip title="Tip" open=false >}}
- Analyze opportunities for alignment between the business processes
- Analyze **data issues in each database** – determine where data is being recorded twice in between different systems and similarities / differences in data models for each database
- Analyze current business processes by identifying **key use cases**
- Create a **data mapping** to see how the same information is being recorded in multiple systems
{{< /admonition >}}
### Q2
The scope of the project is potentially very large given the consolidation of software systems, data structures, and potential new development efforts. How would you prioritize the list of requirements for the new system?
{{< admonition type=note title="Intuition" open=true >}}
1. Interview
2. System examine
3. Test

Wrong in a way it should be the Priority not the Process/Procedure
{{< /admonition >}}
{{< admonition type=tip title="Tip" open=false >}}
Tell the difference btw wants and needs.

A: Rank and weight the requirements based on an objective methodology

B: Maintain a traceability matrix to **track requirements throughout implementation**

C: Have a small group of approvers from the leadership team **be responsible for approving the final list** of high priority requirements

All of the above would be good answers for how to prioritize the list of requirements for the new system.
{{< /admonition >}}
### Q3
What factors out of Deloitte’s control will determine the scope of the project?

*A good answer may include that the scope of the project is constrained by **time**, **resources**, and **budget**.*

A great answer may include some of the following:

-   Budget, new US foreign policy, and time
    
-   The agency’s availability of resources, documentation of current system and acceptance of change regarding a new system
### Q4
After your current state analysis, it has been determined that the client’s biggest pain point is the amount of time it takes to enter data into each system and that this could be improved by creating a unified data architecture to be used across all systems. What steps would you go through to implement this new database? What do each of these steps entail?

A good answer may include some of the following:

Identify requirements, design, build, testing, training and maintenance; recognize that data de-duplication is an important issue for the new system given that this pain point was mentioned in the business situation

A great answer may include some of the following:

-   Update existing software systems to pull from new database tables and use an ERD diagram/UML modeling system to display structure
    
-   Mention issues with moving data from old to new database: data conversion, data profiling/cleansing, warehousing, data standardization. Inquire about the types and quantity of data that needs to be stored as well as data dependencies in the existing databases
    
-   Test the data structure using system testing, integration testing, systems integration testing, and user acceptance testing

[^CAREERCOACHING]: [Mock Technology Consulting Case Interview: Architecture Strategy | CAREER COACHING WITH CHRISTINE - YouTube](https://www.youtube.com/watch?v=92FQs2fXJ9I&list=LL&index=2)