# RFC 2315 PKCS #7: Cryptographic Message Syntax Version 1.5

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_2315_PKCS_7__Cryptographic_Message_Syntax_Version_1_5.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 2315 PKCS #7: Cryptographic Message Syntax Version 1.5

**URL:** http://www.ietf.org/rfc/rfc2315.txt

This
document describes a general syntax for data that may have cryptography applied
to it, such as digital signatures and digital envelopes. The syntax admits
recursion, so that, for example, one envelope can be nested inside another, or
one party can sign some previously enveloped digital data. It also allows
arbitrary attributes, such as signing time, to be authenticated along with the
content of a message, and provides for other attributes such as
countersignatures to be associated with a signature. A degenerate case of the
syntax provides a means for disseminating certificates and
certificate-revocation lists.

**Keywords:**
