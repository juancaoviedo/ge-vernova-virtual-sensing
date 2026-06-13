# DNP3 Protocol over TCP/IP

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_DNP3_Protocol_over_TCP-IP.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### DNP3 Protocol over TCP/IP

**URL:**http://www.dnp.org

In 2000, the DNP Technical Committee defined a
specification for carrying DNP3 over TCP/IP and UDP/IP. Because the WAN/LAN
version is essentially the serial DNP3 encapsulated, this makes it possible to
connect serial DNP3 devices to WAN/LAN DNP3 devices using terminal servers, IP
packet radios, CDPD modems, and other networking technologies without requiring
the access devices to have knowledge of DNP3. DNP3 is often referred to as a
SCADA protocol, but was intended for use in all areas of utility communications.

The DNP Technical Committee continues to add features
to the protocol, with a mandate of maintaining backward compatibility with
existing devices. Recent additions include double-bit status inputs and
“attribute” objects that aid in self-description of the device. The committee
is working on an XML schema for description of a DNP3 implementation, and
network security features for authentication and encryption.

DNP3 Serial may use the same security technologies as
those being developed by IEC TC57 WG15 for IEC60870-5 Part 101.

DNP3 WAN/LAN may use the same security technologies
as those being developed by IEC TC57 WG15 for IEC60870-5 Part 104.

Advantages/Strengths: DNP is widely used within North
America, and increasingly in other countries.

Disadvantages/Weaknesses: DNP does not support object
models.

**Keywords:** LAN, WAN, local area network, wide area network, TCP/IP, UDP/IP,
CDPD
