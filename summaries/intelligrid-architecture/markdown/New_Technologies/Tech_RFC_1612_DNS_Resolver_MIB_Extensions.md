# RFC 1612 DNS Resolver MIB Extensions

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_1612_DNS_Resolver_MIB_Extensions.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 1612 DNS Resolver MIB Extensions

**URL:** http://www.ietf.org/rfc/rfc1612.txt

This
memo defines a portion of the Management Information Base (MIB) for use with
network management protocols in the Internet community. In particular, it
describes a set of extensions that instrument DNS resolver functions. This memo
was produced by the DNS working group.

With
the adoption of the Internet-standard Network Management Framework [4,5,6,7], and with a large number of vendor implementations
of these standards in commercially available products, it became possible to
provide a higher level of effective network management in TCP/IP-based
internets than was previously available. With the growth in the use of these
standards, it has become possible to consider the management of other elements
of the infrastructure beyond the basic TCP/IP protocols. A key element of the
TCP/IP infrastructure is the DNS.

Up
to this point there has been no mechanism to integrate the management of the
DNS with SNMP-based managers. This memo provides the mechanisms by which
IP-based management stations can effectively manage DNS resolver software in an
integrated fashion.

We
have defined DNS MIB objects to be used in conjunction with the Internet MIB to
allow access to and control of DNS resolver software via SNMP by the Internet
community.

**Keywords:**
