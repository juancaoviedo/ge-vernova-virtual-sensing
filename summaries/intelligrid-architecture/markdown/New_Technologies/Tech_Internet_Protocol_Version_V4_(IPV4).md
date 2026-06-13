# Internet Protocol Version V4 (IPV4)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Internet_Protocol_Version_V4_(IPV4).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Internet Protocol Version V4 (IPV4)

**URL:**http://www.ietf.org/rfc/rfc791.txt

IPV4 is the current version of the Internet Protocol
(IP), which is the Internet's most basic protocol and is responsible for
carrying data from a source to a destination. It is a Network layer protocol in
the TCP/IP protocol suite.

IP is a connectionless, datagram protocol that
provides two basic functions: addressing and fragmentation. Connectionless
means that the internet protocol treats each internet datagram as an
independent entity unrelated to any other internet datagram. There are no
connections or logical circuits (virtual or otherwise). IP can segment a
message into smaller packets, which are sent across the Internet (or other
network) to the destination, where the IP layer there reassembles the message.
The fragmentation of the datagram packet by IP is known as IP fragmentation.
Whenever the IP layer receives a datagram packet to send, it first finds the
local interface on which the datagram is to be sent on (routing). Then IP sends
a query to that interface to obtain its maximum transmission unit (MTU). If the
size of the datagram packet to be transmitted is greater than the MTU of the
interface, IP performs fragmentation on the packet. Fragmentation can take
place anywhere; i.e., it can be done at the host or at any intermediate router.
Techniques to discover the path MTU can be found in RFC 1191 and RFC 1981.
IPv4's current addressing consists of a 32-bits address field. IPv4 is
documented in **RFC 791**, and IP broadcasting procedures are discussed in **RFC
919**.

The Internet Protocol defines (1) the address scheme
and convention, (2) the packet format as well as the (3) control and management
functions to be supported by the compatible devices including gateways,
routers, and end-hosts.

**Keywords:** Internet, network layer, addressing.
