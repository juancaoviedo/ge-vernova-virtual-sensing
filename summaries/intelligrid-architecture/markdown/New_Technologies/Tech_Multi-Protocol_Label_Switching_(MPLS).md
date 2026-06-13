# Multi-Protocol Label Switching (MPLS)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Multi-Protocol_Label_Switching_(MPLS).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Multi-Protocol Label Switching (MPLS)

**URL:**http://www.ietf.org/rfc/rfc3031.txt

In an Multi-protocol Label Switching (MPLS) [RFC
3031] network, incoming packets are assigned a "label" by a label
edge router (LER) and forwarded along a label switch path (LSP) where each
label switch router (LSR) makes forwarding decisions based on the contents of the
label. Label Switch Paths (LSPs) are established by network operators for
reasons such as to guarantee a certain level of performance, to route around
network congestion, or to create IP tunnels for network-based virtual private
networks (VPN). LSPs are similar to circuit-switched paths in ATM or Frame
Relay networks, except that they are not dependent on a particular Layer 2
technology. An LSP can be established that crosses multiple Layer 2 transports
such as ATM, Frame Relay or Ethernet. Thus, one of the
true promises of MPLS is the ability to create end-to-end circuits, with
specific performance characteristics, across any type of transport medium,
eliminating the need for overlay networks or Layer 2 only control mechanism.
Ongoing work includes MPLS restoration and GMPLS, an extension of MPLS to be
used for configuring paths in optical switches, TDM multiplexers, and SONET
add-drop multiplexers.

**Keywords:** Internet, Forwarding, QoS, data link layer switching, Protocol
