# RFC 1826 IP Authentication Header

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_1826_IP_Authentication_Header.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 1826 IP Authentication Header

**URL:** http://www.ietf.org/rfc/rfc1826.txt

This
document describes a mechanism for providing cryptographic authentication for
IPv4 and IPv6 datagrams. An Authentication Header (AH) is normally inserted
after an IP header and before the other information being authenticated.

The
Authentication Header is a mechanism for providing strong integrity and
authentication for IP datagrams. It might also provide non-repudiation,
depending on which cryptographic algorithm is used and how keying is performed.
For example, use of an asymmetric digital signature algorithm, such as RSA,
could provide non-repudiation.

Confidentiality, and protection from traffic analysis are
not provided by the Authentication Header. Users desiring confidentiality
should consider using the IP Encapsulating Security Protocol (ESP) either in
lieu of or in conjunction with the Authentication Header [Atk95b]. This
document assumes the reader has previously read the related IP Security
Architecture document that defines the overall security architecture for IP and
provides important background information for this specification [Atk95a].

**Keywords:**
