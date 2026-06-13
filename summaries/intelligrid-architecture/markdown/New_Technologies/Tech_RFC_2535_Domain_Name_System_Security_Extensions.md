# RFC 2535 Domain Name System Security Extensions

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_2535_Domain_Name_System_Security_Extensions.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 2535 Domain Name System Security Extensions

**URL:** http://www.ietf.org/rfc/rfc2535.txt

Extensions
to the Domain Name System (DNS) are described that provide data integrity and
authentication to security aware resolvers and applications through the use of
cryptographic digital signatures. These digital signatures are included in
secured zones as resource records. Security can also be provided through
non-security aware DNS servers in some cases. The extensions provide for the
storage of authenticated public keys in the DNS. This storage of keys can
support general public key distribution services as well as DNS security. The
stored keys enable security aware resolvers to learn the authenticating key of
zones in addition to those for which they are initially configured. Keys
associated with DNS names can be retrieved to support other protocols.
Provision is made for a variety of key types and algorithms. In addition, the
security extensions provide for the optional authentication of DNS protocol
transactions and requests.

**Keywords:**
