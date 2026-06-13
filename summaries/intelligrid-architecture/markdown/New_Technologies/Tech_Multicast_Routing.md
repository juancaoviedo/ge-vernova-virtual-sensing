# Multicast Routing

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Multicast_Routing.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Multicast Routing

**URL:**http://ntrg.cs.tcd.ie/undergrad/4ba2/multicast/antony/  
http://www.cisco.com/warp/public/614/17.html

Multicast is communication
between a single sender and multiple receivers on a network. Typical uses
include the updating of mobile personnel from a home office and the periodic
issuance of online newsletters. Together with anycast and unicast, multicast is
one of the packet types in the Internet Protocol Version 6 (IPv6).

An mrouter, or multicast
router, is a router program that distinguishes
between multicast and unicast packets and determines
how they should be distributed along the Multicast Internet (sometimes known as
the Multicast Backbone or MBone). Using an
appropriate algorithm, an mrouter tells a
switching device what to do with the multicast packet.

Mrouters currently make up
"islands" on the MBone separated by unicast routers. Thus, an mrouter
can disguise multicast packets so that they can cross unicast routers. This is
done by making each multicast packet look like a unicast packet; the
destination address is the next mrouter. This process is called IP tunneling.

There are two multicast
routing protocols that mrouters use to distribute multicast packets. They are
dense-mode routing and sparse-mode routing. The protocol used is determined by
available bandwidth and the distribution of
end users over the network. If the network has many end users and there is
enough bandwidth, dense-mode routing is used. However, if bandwidth is limited
and users are thinly distributed, sparse-mode routing is used.

**Keywords:** Internet, Routing, Interior Gateway Protocol, intra-domain
