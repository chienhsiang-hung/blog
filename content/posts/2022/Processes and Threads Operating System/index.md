---
title: "Processes and Threads | Operating System"
date: 2022-10-30T07:16:00+08:00
lastmod: 2022-10-30T07:16:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "When those programmes are being executed, they will consume some resources from the computer. How do we allocate the resources? Who will do this for the programs?"
resources:
- name: "featured-image"
  src: "featured-image.png"
tags: ["Process", "Threads", "Operating Systems", "Multithreading", "Os"]
categories: ["SE Interview 101"]
toc:
  enable: true
zhtw: false
---
## What's OS (Operating System)
Assume that we have a program written in Java, Python, C, etc. sort of high-level language, that a PC wouldn't be able to execute. We need a compiler to translate those languages to 0, 1 binary codes for a PC to run.

When those programmes are being executed, they will consume some resources from the computer. How do we **allocate the resources**? Who will do this for the programs?

This is when an **Operating System (OS)** comes in. 
> The OS will help in loading that executable program and allocate the memory and the resources later to be used.
## Process vs Program
A process [is a running program](https://byjus.com/gate/process-in-operating-system-notes/#:~:text=A%20process%20is%20a%20running,is%20an%20'active'%20entity.) that serves as the foundation for all computation. The procedure is not the same as computer code, although it is very similar. 

> In contrast to the program, which is often regarded as some ‘passive’ entity, a process is an ‘active’ entity.

Hardware status, RAM, CPU, and other attributes are among the attributes held by the process.
### How a Process Work
![how a process work](featured-image.png "how a process work")
When you start a programme, it's first loaded and given an address space in the main memory from your hard disk. After it's loaded in memory, it's then scheduled onto the available CPU. And the programme instruction then would be executed sequentially.
## Process vs Thread
{{< youtube OrM7nZcxXZU >}}
## Multithreading
### Why is The Threads Useful
- **Multiprocessing**
- Requires no synchronization
- Operating System prevents processes from writing to another processes address space
- Address spaces large
- **Porcesses can take up much more memory than threads** (cost is always less or equal to process)
- **Resource sharing**

![Multithreading](Multithreading.png "Multithreading")
### Related
- [What is Multithreading? - YouTube](https://www.youtube.com/watch?v=0KAGazeMZ2o)
- [(17) 周志遠作業系統 Ch4: Multithreaded Programming (A): Thread Introduction - YouTube](https://www.youtube.com/watch?v=BrfGZHZdRTw)