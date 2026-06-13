# RFC 2230 Key Exchange Delegation Record for the DNS

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_2230_Key_Exchange_Delegation_Record_for_the_DNS.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 2230 Key Exchange Delegation Record for the DNS

**URL:** http://www.ietf.org/rfc/rfc2230.txt

This
note describes a mechanism whereby authorization for one node to act as key
exchanger for a second node is delegated and made available via the Secure DNS.
This mechanism is intended to be used only with the Secure DNS. It can be used
with several security services. For example, a system seeking to use IP
Security [RFC-1825, RFC-1826, RFC-1827] to protect IP
packets for a given destination can use this mechanism to determine the set of
authorized remote key exchanger systems for that destination.

The
Domain Name System (DNS) is the standard way that Internet nodes locate
information about addresses, mail exchangers, and other data relating to remote
Internet nodes. [RFC-1035, RFC-1034] More recently, Eastlake and Kaufman have
defined standards-track security extensions to the DNS. [RFC-2065] These
security extensions can be used to authenticate signed DNS data records and can
also be used to store signed public keys in the DNS.

The
KX record is useful in providing an authenticatible method of delegating
authorization for one node to provide key exchange services on behalf of one or
more, possibly different, nodes. This note specifies the syntax and semantics
of the KX record, which is currently in limited deployment in certain IP-based
networks.

**Keywords:**
