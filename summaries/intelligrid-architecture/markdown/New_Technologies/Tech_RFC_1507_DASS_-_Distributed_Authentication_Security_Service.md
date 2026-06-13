# RFC 1507 DASS - Distributed Authentication Security Service

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_1507_DASS_-_Distributed_Authentication_Security_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 1507 DASS - Distributed Authentication Security Service

**URL:** http://www.ietf.org/rfc/rfc1507.txt

DASS
supports the concept of global identity and network login. A user is assigned a
name from a global namespace and that name will be recognized by any node in
the network. (In some cases, a resource may be configured as accessible only by
a particular user acting through a particular node. That is an access control
decision, and it is supported by DASS, but the user is still known by his
global identity). From a practical point of view, this means that a user can
have a single password (or smart card) which can be used on all systems which
allow him access and access control mechanisms can conveniently give access to
a user through any computer the user happens to be logged into. Because a
single user secret is good on all systems, it should never be necessary for a
user to enter a password other than at initial login. Because cryptographic
mechanisms are used, the password should never appear on the network beyond the
initial login node.

**Keywords:**Confidentiality, Identity Establishment, Security
