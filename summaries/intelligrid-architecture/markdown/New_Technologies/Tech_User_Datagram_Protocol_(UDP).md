# User Datagram Protocol (UDP)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_User_Datagram_Protocol_(UDP).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### User Datagram Protocol (UDP)

**URL:**http://www.ietf.org/rfc/rfc793.txt

User Data Protocol (UDP) [RFC 768] is a no-frills,
bare-bones connectionless transport protocol that enables an application to
send individual messages to other applications. Delivery is not guaranteed, and
messages may not be delivered in the same order as they were sent. It is
preferable to TCP for delay-sensitive, real-time applications.

UDP is part of the TCP/IP protocol suite. UDP is
connectionless because it sends data without ever establishing a
connection and it provides very few error recovery services, offering instead a
direct way to send and receive datagrams over an IP network. It is used
primarily for broadcasting messages over a network. Applications using UDP
includes; e.g., DNS, SNMP, TFTP, RIP, DHCP, BOOTP.

**Keywords:** Internet, datagram, Transport, Protocol
