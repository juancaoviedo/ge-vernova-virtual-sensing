# PROFIBUS

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_PROFIBUS.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### PROFIBUS

**URL:**http://www.profibus.org

The non-profit PROFIBUS User Organization, as a part
of the worldwide organization PROFIBUS International, promotes and maintains a
set of extremely popular specifications for local-area “bus” communications in industrial
and process automation. PROFIBUS is also frequently used in power systems
devices. The current PROFIBUS is actually PROFIBUS DP (Decentralized
Periphery), which replaces an earlier PROFIBUS FMS (Fieldbus Message
Specification). PROFIBUS FMS resembled the current IEC61850 profile, while DP
is a much more compact protocol suite.

The core of PROFIBUS DP is a data link layer that is
simultaneously token-passing (between master devices) and polled (from masters
to slaves), enabling deterministic bus access with high bandwidth utilization.
The data link layer comes in several options and operates over a variety of
physical layers. It is usually implemented in hardware. The approved physical
media include RS485, RS485-IS (Intrinsically Safe), Manchester-coded Bus,
Powered (MBP), and fiber optics, at rates from 9600bps to 12Mbps.

To aid in interoperability, the PROFIBUS User
Organization has defined several application layer profiles dedicated to
specific uses such as factory automation, process automation, and motion
control.

PROFIBUS is listed among several “field buses”
conforming to IEC 61158: “Digital Data Communication for Measurement and
Control - Fieldbus for use in Industrial Control Systems” and IEC 61784:
“Profile Sets for Continuous and Discrete Manufacturing Relative to Fieldbus
Use in Industrial Control Systems”.

Access to PROFIBUS networks and data from IP-based
Ethernet networks is achieved through PROFInet gateways, which use an
object-oriented application layer using DCOM and XML over TCP/IP.

**Keywords:** Industrial automation, LAN, WAN, Multi-drop, Serial, Physical layer,
Data link layer, Application layer, Gateway, Information model

#### ModBus
