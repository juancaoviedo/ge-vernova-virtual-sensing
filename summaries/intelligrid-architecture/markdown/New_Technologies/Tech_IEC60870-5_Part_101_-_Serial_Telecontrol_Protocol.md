# IEC60870-5 Part 101 - Serial Telecontrol Protocol

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_IEC60870-5_Part_101_-_Serial_Telecontrol_Protocol.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### IEC60870-5 Part 101 - Serial Telecontrol Protocol

**URL:** http**://trianglemicroworks.com/mailman/listinfo/iec60870-5\_trianglemicroworks.com**

IEC60870-5 Part 101 was developed by IEC TC57 in WG03
as a 3-layer communications protocol standard for use by utilities for SCADA.
It was designed primarily to meet the needs of real-time exchange of data
between compute-constrained devices over media-constrained communication
channels (typically less than 1200 bps). This protocol is widely used in Europe
and other countries, but is not typically used within the United States or
Canada. In these two counties, a variation of IEC60870-5 Part 101 was
developed, called DNP.

Additional information on IEC60870-5 Part 101 can be
obtained from the IEC

IEC TC57 Working Group 3 was one of the first
organizations formed with the goal of developing a common protocol for the
utility industry. It initially focused on producing an extremely reliable data
link layer protocol for slow serial links. This data link layer was designed to
be used in either balanced point-to-point links or unbalanced multi-drop links,
with several levels of reliability which were thoroughly characterized in the
annexes of the following two specifications:

·      
60870-5-1 Transmission Frame Formats

·      
60870-5-2 Link Transmission Procedures

The next three specifications from WG3 described in
general terms the most common utility application protocol functions used by
proprietary protocols at the time. These functions included such features as
initialization, select-before-operate and direct controls, accumulator
freezing, report-by-exception, periodic reporting, remote parameter setting,
and file transfer.

·      
60870-5-3 General Structure of Application Data

·      
60870-5-4 Definition and Coding of Application Information Elements

·      
60870-5-5 Basic Application Functions

These specifications defined the protocol in general
terms only. For the details of the protocol implementation, WG3 defined several
companion standards, each designed for a different application area, and
selecting different a subset of features from the earlier five standards.

·      
60870-5-101 Telecontrol (referred to as SCADA in North America)

·      
60870-5-102 Load Profiling (energy measurement through accumulators)

·      
60870-5-103 Protection Equipment (monitoring and control of relays)

These companion standards were three-layer serial
protocols only, with no networking capabilities. With the advent of WANs in
distribution automation, WG3 developed a standard mechanism for implementing
IEC 60870-5-101 over Internet protocols:

·      
60870-5-104 Telecontrol over TCP/IP

Although the 60870-5 companion standards can technically
be used within a substation, TC57 has designated IEC 61850 (Working Groups 10,
11 and 12) as the primary standard within substations, while 60870-5 is to be
used for telecontrol (to remote sites) only.

WG3 recently released a revised edition of the original
101 companion standard and is currently investigating security solutions for
the IEC 60870-5 protocols along with Working Group 15.

**Keywords:** Protocol, Standard, Monitoring, Control, Protection, Physical layer,
Data link layer, Application layer, LAN,
WAN, Serial, High reliability, Power industry
