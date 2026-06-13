# Transmission Control Protocol (TCP)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Transmission_Control_Protocol_(TCP).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Transmission Control Protocol (TCP)

**URL:**http://www.ietf.org/rfc/rfc793.txt

Transmission Control Protocol (TCP) [RFC 793] is a
connection-oriented, reliable transport protocol and part of the TCP/IP protocol
suite. It provides the reliability not provided by IP, by adding various
timeouts, sequence checking, and checksum features. However, it does not
provide recovery services after an error. This is partly because it was
originally designed to provide communication services between humans and computers, so that humans could always perform the recovery
effort (e.g. just hit the Reload button on your browser).

TCP performs multiplexing, demultiplexing, and error
detection (but not recovery). It operates at the Transport Layer  in the OSI model and is defined in a number of the
below listed RFCs, a host-to-host protocol, provides reliable,
connection-oriented data transmission. TCP’s congestion control mechanism
reacts to network congestion by reducing its transmission window. Various
enhancement work on TCP is discussed in the Transport Area working group of the
IETF.

**Keywords:** Internet, Reliable, Transport, Protocol
