# IEC61850 - Substation Automation Communications

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_IEC61850_-_Substation_Automation_Communications.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### IEC61850 - Substation Automation Communications

**URL:**http://www.iec.ch/cgi-bin/procgi.pl/www/iecwww.p?wwwlang=E&wwwprog=dirwg.p&ctnum=1188

Working Groups 10 focuses on communications within
substations, as opposed to distributed Telecontrol, which was the focus of
Working Group 3, or communications between control centers, as in Working Group
7. Communications within the substation was divided into three levels: station,
process, and unit. Initially each Working Group handled a different part of the
architecture, but in later years they formed joint task forces to address
mutual issues. The initial specifications focused on a “top-down” approach,
characterizing the interactions between substation components at a requirements
level:

·      
61850-1 Introduction and Overview

·      
61850-2 Glossary

·      
61850-3 General Requirements

·      
61850-4 System and Product Management

·      
61850-5 Communications Requirements

WG 10 also have within their scope the task of
developing a standard file format for exchanging information between
proprietary configuration tools for substation devices. This standard is based
on Extensible Markup Language (XML), and draws on the data modeling concepts
found in the other parts of IEC 61850, and the capability of the IEC 61850
protocols to “self-describe” the data to be reported by a particular device.

·      
61850-6 Substation Configuration Language

At about the time when the requirements parts of the
work were approaching completion, WGs 10-12 became aware of the work that the
Electrical Power Research Institute (EPRI) and the Utility Communications Architecture
(UCA®) Forum had completed on UCA, especially on developing a standard set of
services and data models for intra-substation communications. This work was
incorporated into IEC 61850, with some significant modifications, in the
following specifications:

·      
61850-7-1 Principles and Models

·      
61850-7-2 Abstract Communications Service Interface

·      
61850-7-3 Common Data Classes (Object Models)

·      
61850-7-4 Compatible Logical Node Classes and Data Classes (Object
Models)

Most of the IEC 61850 specifications describe the
protocol in a very abstract manner, and only the last parts of the standard
describes “Specific Communication Service Mapping” onto a particular set of
protocols. The initial protocol profiles for IEC 61850 are nearly identical to
those developed for IEC 60870-6 (TASE.2) between substations, using the
Manufacturing Message Specification (MMS) and both Internet and OSI protocol
stacks. These are mainly full 7-layer profiles, but there are also high-speed
profiles used directly over Ethernet (IEEE 802.x) LANs for “process bus” and
protection tripping. The profiles are described in:

·      
61850-8 Protocol Mapping

The initial intent was that IEC 61850 would be a
superset of UCA 2.0 and that devices implementing the two protocol suites could
interoperate

Another significant contribution of IEC 61850 is a
high-speed protocol Ethernet-based protocol to be used for communications
between “smart transformers” and higher level devices, to permit several
different devices to simultaneously receive sampled waveform values from a
given transformer in real-time:

·      
61850-9 Sampled Measured Values

Parts 7.1, 7.2, 7.3, 7.4, and 9.1 of 61850 have
become International Standards with the remaining protocol pieces reaching
International Standard status in 2003to early 2004. The final work in IEC 61850
will be to develop test procedures for verifying conformance to the protocol:

·      
61850-10 Certification Test Procedures
