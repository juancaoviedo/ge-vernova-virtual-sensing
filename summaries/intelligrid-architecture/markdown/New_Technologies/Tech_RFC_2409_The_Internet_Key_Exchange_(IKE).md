# RFC 2409 The Internet Key Exchange (IKE)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_2409_The_Internet_Key_Exchange_(IKE).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 2409 The Internet Key Exchange (IKE)

**URL:** http://www.ietf.org/rfc/rfc2409.txt

ISAKMP
([MSST98]) provides a framework for authentication and key exchange but does
not define them. ISAKMP is designed to be key exchange independent; that is, it
is designed to support many different key exchanges. Oakley ([Orm96]) describes
a series of key exchanges—called "modes"-- and details the services
provided by each (e.g. perfect forward secrecy for keys, identity protection,
and authentication). SKEME ([SKEME]) describes a versatile key exchange
technique that provides anonymity, repudiability, and quick key refreshment.
This document describes a protocol using part of Oakley and part of SKEME in
conjunction with ISAKMP to obtain authenticated keying material for use with
ISAKMP, and for other security associations such as AH and ESP for the IETF
IPsec DOI.
