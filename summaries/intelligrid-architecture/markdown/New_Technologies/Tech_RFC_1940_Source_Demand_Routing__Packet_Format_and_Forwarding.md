# RFC 1940 Source Demand Routing: Packet Format and Forwarding Specification (Version 1)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_1940_Source_Demand_Routing__Packet_Format_and_Forwarding.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 1940 Source Demand Routing: Packet Format and Forwarding Specification (Version 1)

**URL:** http://www.ietf.org/rfc/rfc1940.txt

The
purpose of SDRP is to support source-initiated selection of routes to
complement the route selection provided by existing routing protocols for both
inter-domain and intra-domain routes. This document refers to such
source-initiated routes as "SDRP routes". This document describes the
packet format and forwarding procedure for SDRP. It also describes procedures
for ascertaining feasibility of SDRP routes. Other components not described
here are routing information distribution and route computation. This portion
of the protocol may initially be used with manually configured routes. The same
packet format and processing will be usable with dynamic route information
distribution and computation methods under development.

The
packet forwarding protocol specified here makes minimal assumptions about the
distribution and acquisition of routing information needed to construct the
SDRP routes. These minimal assumptions are believed to be sufficient for the
existing Internet. Future components of the SDRP protocol will extend
capabilities in this area and others in a largely backward-compatible manner.

This
version of the packet forwarding protocol sends all packets with the complete
SDRP route in the SDRP header. Future versions will address route setup and
other enhancements and optimizations.

**Keywords:**
