# RFC 1827 IP Encapsulating Security Payload (ESP)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_1827_IP_Encapsulating_Security_Payload_(ESP).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 1827 IP Encapsulating Security Payload (ESP)

**URL:** http://www.ietf.org/rfc/rfc1827.txt

This
document describes the IP Encapsulating Security Payload (ESP). ESP is a
mechanism for providing integrity and confidentiality to IP datagrams. In some
circumstances it can also provide authentication to IP datagrams. The mechanism
works with both IPv4 and IPv6.

ESP
is a mechanism for providing integrity and confidentiality to IP datagrams. It
may also provide authentication, depending on which algorithm and algorithm
mode are used. Non-repudiation and protection from traffic analysis are not
provided by ESP. The IP Authentication Header (AH) might provide
non-repudiation if used with certain authentication algorithms [Atk95b]. The IP
Authentication Header may be used in conjunction with ESP to provide
authentication. Users desiring integrity and authentication without confidentiality
should use the IP Authentication Header (AH) instead of ESP. This document
assumes that the reader is familiar with the related document "IP Security
Architecture", which defines the overall Internet-layer security
architecture for IPv4 and IPv6 and provides important background for this
specification [Atk95a].

**Keywords:**
