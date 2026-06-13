# Fieldbus

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Fieldbus.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Fieldbus

**URL:**http://www.fieldbus.org

The non-profit Fieldbus Foundation promotes and
maintains a popular local-area “bus” communications specification for use in
industrial automation, particularly in instrumentation and control. This
specification is known as “Foundation Fieldbus”, distinguished from the generic
term “fieldbus” which may apply to several different technologies.

Foundation Fieldbus is a three-layer protocol suite
plus object model specifications, known as “function blocks” defined above the
application layer. It includes self-description in the form of “Device
Description” (DD) files that use a standard (non-XML) language specific to
Foundation Fieldbus.

The data link layer is listed among several
technologies complying IEC61158: “Digital Data Communication for Measurement
and Control - Fieldbus for use in Industrial Control Systems”. The data link
layer uses a “deterministic bus scheduler” to control access to the bus using
token passing. The application layer, the Fieldbus Message Specification (FMS)
uses a publish/subscribe model and resembles the Manufacturing Message
Specification (MMS) that is the core of IEC61850.

The standard Foundation Fieldbus physical layer is a
multi-drop 31.25Kbps, “intrinsically safe” physical layer known as H1. H1
networks may be accessed from Ethernet networks through a “Linking Device”
using a “High Speed Ethernet (HSE)” profile that includes TCP/IP, UDP/IP and SNMP, or devices may support only HSE. The HSE
specification pays special attention to redundancy in Ethernet LANs.

**Keywords:** Industrial automation, LAN, WAN, Multi-drop, Serial, Physical layer,
Data link layer, Application layer, Gateway, Information model
