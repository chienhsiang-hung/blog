---
title: "TCP/IP | Backend 101"
date: 2022-11-03T02:30:00+08:00
lastmod: 2022-11-03T02:30:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: ""
resources:
- name: "featured-image"
  src: ""
tags: []
toc:
  enable: true
zhtw: false
---
## What's TCP/IP
### Internet protocol suite[^Internet_protocol_suite]
The  **Internet protocol suite,**  commonly known as  **TCP/IP,**  is a framework for organizing the set of  [communication protocols](https://en.wikipedia.org/wiki/Communication_protocol "Communication protocol")  used in the  [Internet](https://en.wikipedia.org/wiki/Internet "Internet")  and similar  [computer networks](https://en.wikipedia.org/wiki/Computer_network "Computer network")  according to functional criteria. 

![foundational-protocols](foundational-protocols.png "foundational-protocols")
The foundational protocols in the suite are
- [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol "Transmission Control Protocol")  (TCP)
- [User Datagram Protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol "User Datagram Protocol")  (UDP)
- [Internet Protocol](https://en.wikipedia.org/wiki/Internet_Protocol "Internet Protocol")  (IP)

In the development of this networking model, early versions of it were known as the  **Department of Defense**  (**DoD**)  **model**  because the research and development were funded by the  [United States Department of Defense](https://en.wikipedia.org/wiki/United_States_Department_of_Defense "United States Department of Defense")  through  [DARPA](https://en.wikipedia.org/wiki/DARPA "DARPA").

> The Internet protocol suite provides  [end-to-end data communication](https://en.wikipedia.org/wiki/End-to-end_principle "End-to-end principle")  specifying **how data should be packetized, addressed, transmitted,  [routed](https://en.wikipedia.org/wiki/Routing "Routing"), and received.**

![tcp-ip-model](tcp-ip-model.png "tcp-ip-model")
This functionality is organized into four [abstraction layers](https://en.wikipedia.org/wiki/Abstraction_layer "Abstraction layer"), which classify all related protocols according to each protocol's scope of networking.[[1]](https://en.wikipedia.org/wiki/Internet_protocol_suite#cite_note-rfc1122-1)[[2]](https://en.wikipedia.org/wiki/Internet_protocol_suite#cite_note-R9Fra-2)  An implementation of the layers for a particular application forms a  [protocol stack](https://en.wikipedia.org/wiki/Protocol_stack "Protocol stack"). From lowest to highest, the layers are
- [link layer](https://en.wikipedia.org/wiki/Link_layer "Link layer"), containing communication methods for data that remains within a single network segment (link)
- [internet layer](https://en.wikipedia.org/wiki/Internet_layer "Internet layer"), providing  [internetworking](https://en.wikipedia.org/wiki/Internetworking "Internetworking")  between independent networks
- [transport layer](https://en.wikipedia.org/wiki/Transport_layer "Transport layer"), handling host-to-host communication
- [application layer](https://en.wikipedia.org/wiki/Application_layer "Application layer"), providing process-to-process data exchange for applications

{{< youtube 2QGgEk20RXM >}}
### How They Work
- Pysical -> Data Link

  0/1 Data to Frame (Ethernet Protocol)

      head: __
      data: __
  
  in Mac Address
- Data Link -> Transport

  IP Address

      192.168.1.3
      (11000000-10101000-10000000-00000000)
  
- Transport -> Internet
  

  
  
  


[^Internet_protocol_suite]: [Internet protocol suite - Wikipedia](https://en.wikipedia.org/wiki/Internet_protocol_suite)