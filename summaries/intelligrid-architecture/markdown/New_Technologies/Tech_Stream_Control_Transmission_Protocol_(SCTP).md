# Stream Control Transmission Protocol (SCTP)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Stream_Control_Transmission_Protocol_(SCTP).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Stream Control Transmission Protocol (SCTP)

**URL:**http://www.ietf.org/rfc/rfc2960.txt

Stream Control Transmission Protocol is designed to
transport PSTN signaling messages over IP networks, but is capable of broader
applications. SCTP is a reliable transport protocol operating on top of a
connectionless packet network such as IP. It offers the following services to
its users: (1) acknowledged error-free non-duplicated transfer of user data,
(2) data fragmentation to conform to discovered path MTU size, (3) sequenced
delivery of user messages within multiple streams, (4) with an option for
order-of-arrival delivery of individual user messages, (5) optional bundling of
multiple user messages into a single SCTP packet, and most importantly (6)
support network-level fault tolerance through supporting of multi-homing at
either or both ends of an association. The design of SCTP includes appropriate
congestion avoidance behavior and resistance to flooding and masquerade
attacks.

**Keywords:**              
Internet, datagram, Transport, Protocol
