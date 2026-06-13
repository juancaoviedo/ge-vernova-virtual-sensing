# RFC 2797 Certificate Management Messages over CMS

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_2797_Certificate_Management_Messages_over_CMS.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 2797 Certificate Management Messages over CMS

**URL:** http://www.ietf.org/rfc/rfc2797.txt

This
document defines a Certificate Management protocol using CMS (CMC). This
protocol addresses two immediate needs within the Internet PKI community:

1.
The need for an interface to public key certification products and services
based on [CMS] and [PKCS10], and

2.
The need in [SMIMEV3] for a certificate enrollment protocol for DSA-signed
certificates with Diffie-Hellman public keys.

A
small number of additional services are defined to supplement the core
certificate request service.

Throughout
this specification the term CMS is used to refer to both [CMS] and [PKCS7]. For
both signedData and envelopedData, CMS is a superset of the PKCS7. In general,
the use of PKCS7 in this document is aligned to the Cryptographic Message
Syntax [CMS] that provides a superset of the PKCS7 syntax. The term CMC refers
to this specification.

**Keywords:**
