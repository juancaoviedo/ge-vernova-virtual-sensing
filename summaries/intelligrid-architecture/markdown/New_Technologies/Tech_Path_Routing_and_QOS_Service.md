# Path Routing & QOS

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Path_Routing_and_QOS_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Path Routing and QOS Service

This
service represents the ability of a security domain to applications with the
ability to request that a set of transactions be conveyed over a specific
communication path with specific Quality of Security (QS) being provided. Such
a service may be used in conjunction with many of the other security services.

There
are two major issues that need to be resolved:

·      
The ability to specify the actual communication path that a given
transaction will use.  
  
This type of ability is a direct contradiction to the normal dynamic routing
inherent in most networks, thus normal network infrastructures may not be able
to be used.

·      
The ability to request a Quality of Security to be guaranteed over that
path.

Technological Assessment and
Relevant Specifications

Communication Path Definition

Although
there are several IETF RFCs regarding the ability to perform this function
(e.g. RFC 1940), few if any of the operating system APIs allow the full path
specification to occur. In reality, the source routing bit can be set TRUE and
the packet will be delivered to the peer with the path hop information embedded
within it. Such a mechanism could allow the receiver to determine if a packet
was delivered over an acceptable path, and this is a useful check.

However,
the ability to actually pre-determine the path that a packet will transverse
falls upon manual configuration of static routing. It is this static routing
that can actually allow policy to dictate what route a given communication
packet will take. Typically, this is a configuration option in Firewalls or
Operating Systems. Thus it is incumbent upon the SMI function to provide the
appropriate configuration.

Quality of Security

There
are no known Quality of Security standards/specifications available to allow
packet routing based upon a requested level of security. Development of a
similar specification to RFC 2386 (Quality of Service based Routing) is
recommended.

Table 23: Relevant Specifications for the Path Routing
Service

|  |  |  |
| --- | --- | --- |
| Identification Number | Name | Comment |
| RFC 1102 | Policy routing in Internet protocols | Highly Recommended |
| RFC 1322 | A Unified Approach to Inter-Domain Routing |  |
| RFC 1940 | Source Demand Routing: Packet Format and Forwarding Specification (Version 1) | Highly Recommended |
| RFC 2386 | A Framework for QoS-based Routing in the Internet | Highly Recommended |
| RFC 2725 | Routing Policy System Security | Highly Recommended |
