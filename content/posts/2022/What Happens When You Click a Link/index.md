---
title: "What Happens When You Click a Link? "
date: 2022-10-30T09:16:00+08:00
lastmod: 2022-10-30T09:16:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "When those programmes are being executed, they will consume some resources from the computer. How do we allocate the resources? Who will do this for the programs?"
resources:
- name: "featured-image"
  src: ""
tags: []
categories: ["SE Interview 101"]
toc:
  enable: true
zhtw: false
---
## HTTP
### HTTP/0.9
![HTTP-0.9](HTTP-0.9.png "HTTP-0.9")
- Client send a request

  -> launch a TCP/IP connect: `telnet google.com 80`
  
  -> **one-line commend: `GET /about`**
- _CRLF_[^CRLF] to end a request
- Respond HTML in _ASCII_[^ASCII]
- Auto-shut-down every Request / Response (close TCP/IP connect)
### HTTP/1.0
![HTTP-1.0](HTTP-1.0.png "HTTP-1.0")
- Still in _ASCII_[^ASCII]
  - **Multi-line commend is allowed including `Header`**
    > Method + Header + _CRLF_[^CRLF]

  -> launch a TCP/IP connect: `telnet google.com 80`
  
  -> commend:

    ```
    GET /about HTTP/1.0
    Host: www.google.com
    ```

  -> additional _CRLF_[^CRLF]: `\n`
  ![HTTP-1.0-302-Found.png](HTTP-1.0-302-Found.png "HTTP-1.0-302-Found.png")
  ![HTTP-1.0-Location-Header](HTTP-1.0-Location-Header.png "HTTP-1.0-Location-Header")
- Response with _ASCII_[^ASCII]
  1. Status code
  2. Header
  3. Conten type
- Auto-shut-down every Request / Response (close TCP/IP connect)

[^CRLF]: The term CRLF refers to Carriage Return (ASCII 13, \r ) Line Feed (ASCII 10, \n ). They're used to note the termination of a line, however, dealt with differently in today's popular Operating Systems. [CRLF Injection | OWASP Foundation](https://owasp.org/www-community/vulnerabilities/CRLF_Injection)
[^ASCII]: ASCII, in full American Standard Code for Information Interchange, a standard data-encoding format for electronic communication between computers. ASCII assigns standard numeric values to letters, numerals, punctuation marks, and other characters used in computers. [ASCII | Definition, History, Trivia, & Facts | Britannica](https://www.britannica.com/topic/ASCII)