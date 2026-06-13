# Infrastructure Technologies

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Comm_Recomm.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Communications Infrastructure Technologies

This section provides an overview of the
communications infrastructure technologies recommended for use with IntelliGrid Architecture. The
complete set of recommended IntelliGrid Architecture communications infrastructure technologies
are described in detail in the Appendix D of this volume.

### Analysis of Communications Infrastructure Technologies

In the following subsections, we will analyze
some selected groups of technologies, which are critical for realizing a
scalable, extensible, resilient, high-performance, cost-effective and agile
communication infrastructure for IntelliGrid Architecture.

#### Network Layer Protocol and Address Scheme: IPV4 Vs. IPV6

The Internet Protocol version 4 (IPV4) is the
global data communications standard, dominating the currently deployed data
networks worldwide. IPV4 was designed more than twenty years ago and has
started to run into the limited address space problem due to the invention and
explosive success of the World-Wide-Web (WWW),
which was beyond the expectation of the original designers of IP.

Two major approaches have been proposed to
tackle the emerging IPV4 address shortage problem. In the first approach,
conservation of public, globally routable IPV4 addresses is achieved by
introducing Network Address Translation (NAT)
devices at the boundary between a private data network, i.e. the Intranet, of
an enterprise and the public Internet, so that multiple hosts within the
Intranet can share the same public IPV4 address when communicating to (or
through) the public Internet. The second approach is to upgrade to the next
generation of IP, namely IPV6 that has been standardized by the IETF in 1999.
IPV6 overcomes the address space limitation of IPV4 by expanding the address
space from 32 bits to 128 bits. Other significant advances in IPV6 include
better support of auto-configuration of IP hosts, better support of IP
end-point mobility as well as the reduction of processing overhead at
intermediate routers as an IP packet traverses through the network. The IPV6
standard also makes the support of IPSec mandatory in all IPV6 implementations.
In contrast, the support of IPSec in IPV4 is optional and thus has seen only
limited adoption of IPSec within current IPV4 deployments. Various transition
strategies from IPV4 to IPV6 have been proposed and are an integral part of the
design of IPV6. Transition schemes based on IPV6-in-IPV4 tunneling or IPV4/IPV6
dual-stack approaches have been defined.  

In the context of IntelliGrid Architecture, while IPV4 public
address shortage is not likely to be a major issue for the IP-based IT systems
used by power-utilities *internally*[if !supportFootnotes?[17]endif?](Anl_Comm_Recomm.htm#_ftn17), it
would become an issue during the deployment of future IntelliGrid Architecture services which may
require the introduction of a much larger number of IP-based endpoints. An
example of such is a large number of IP-based IEDs in support of widespread
large-scale deployments of ADA, WACS/WAMS and self-healing grid applications.
Another example is the massive number of IP-based consumer gateways/portals to
be located in customer premises to support Real Time Pricing applications
involving residential customers. While it is possible to address the potential
public IPV4 address shortage issue via the combined use of private IPV4
addresses and NATs, an IPV6-based solution is much more attractive in the long
run due to its ability to provide a clean end-to-end communication model to
support the deployment of innovative applications and services and computing
paradigms to be created for years to come. In contrast, the NAT-based
solution breaks the original end-to-end model of the Internet and makes the
deployment of new services and computing paradigms much more difficult. A case
in point is that while the conventional client/server computing paradigm work
reasonably well under a NAT-based
networking infrastructure, the existence of NATs has created a long list of
technical and deployment problems for new services developed under the recent
peer-to-peer computing paradigm. Similar problems can appear if a NAT-based
solution is adopted for the deployment of yet-to-be invented services involving
a massive number of IntelliGrid Architecture consumer portals. The NAT-based
approach may also unnecessarily limit the paradigms under which a loosely
coupled federation of power utilities can conduct collaborative distributed
computing under IntelliGrid Architecture framework. The automatic configuration features of
IPV6 will also facilitate the deployment and management of massive number of
new IP-based devices such as IEDs and residential consumer gateways.

On the other hand, the deployment of IPV6
will involve the financial/ technical issues and considerations that are common
for the rollout of any key protocol impacting the fundamentals of the
communication infrastructure. For instance, while it is likely that IP
end-hosts will only require software/ firmware upgrades in order to become
IPV6-capable, hardware changes (and the associated costs) would be required for
elements in the core of the network, e.g. high-speed routers. Additional
hardware, software and configuration changes would also be required in other
components of the networking infrastructure, e.g. the packet filtering rules
for firewalls and the settings of intrusion detection systems. Lastly, the
number of security vulnerabilities are likely to increase during the initial
roll-out as flaws are discovered from the initial implementations of IPV6 and
its supporting protocols and systems.

To conclude this subsection, it is noteworthy
that the U.S. Department of Defense (DOD) has recently mandated IPV6
compatibility for all assets acquired for their Global Information Grid, which
is designed to achieve the DOD's goal of network-centric warfare and operations
by 2010. A policy memorandum has been issued to outline DOD's transition to
IPV6 by 2008. The schedule is chosen because most experts estimate that
widespread commercial adoption of IPV6 will take place from 2005 to 2007.

#### Technologies for a Resilient Communications Infrastructure

The communication infrastructure of IntelliGrid Architecture
should support restoration technique(s) that offer a wide-range of services that
meet varying resiliency requirements of applications. From the end-user
standpoint, the restoration attributes of most interest are restoration time,
the failure coverage, and network capacity needed for protection and
restoration. Restoration time is the time taken to restore the end-user service
upon failure. This includes in general, failure detection, notification and
switchover of the traffic to an alternate path. Refer to Appendix D for a
review of a number of best current practices as well as and emerging solutions
for resilient services supported by various networking technologies. This
subsection summarizes the key characteristics and trade-offs across different
resilient communications technologies. 
The ideal restoration scheme would provide the smallest restoration time
with maximum failure coverage while requiring the smallest amount of
restoration capacity. However, such a scheme is not possible because of
significant tradeoffs exist between restoration time, failure coverage, and
restoration capacity.

For example, with dedicated, non-shared
restoration capacity such as a SONET/SDH
Unidirectional Path Switched Ring (UPSR), the protection capacity is not
shared. SONET/SDH
Bi-directional Line Switched Ring (BLSR) architecture allows sharing of the
protection capacity among different failures on the ring. Therefore compared to
UPSR, BLSR has better capacity utilization. Also, under no failure condition
protection capacity can be used to carry extra traffic. This provides
opportunity to service providers to generate additional revenues. However, all
this comes at the cost of more complexity in signaling as, unlike UPSR,
coordination among nodes is required. One can guarantee immediate restoration
upon detection of a failure.  Besides the
ring-based Automatic Protection Switching (APS)
scheme, SONET/SDH also
supports point-to-point 1:N[if !supportFootnotes?[18]endif?](Anl_Comm_Recomm.htm#_ftn18) as
well as 1+1[if !supportFootnotes?[19]endif?](Anl_Comm_Recomm.htm#_ftn19) APS
architectures. Like UPSR as 1+1 APS can
provide the fastest restoration time by avoiding any traffic re-route/switch
delay upon failure, but at the expense of doubling the bandwidth/traffic to be
sent across the system.

The SONET/SDH 1+1 APS
concept has also been applied in Asynchronous Transfer Mode (ATM) as well as
Multi-Protocol Label Switching (MPLS) to support two diverse paths, in the form
of ATM Virtual Circuits (VCs) or MPLS label-switched paths (LSPs), to be setup
between two peering entities.  Since data
are continuously sent over both VCs/LSPs from the sending node, the switchover
time and the service impact can be kept at a minimum at the expense of doubling
packet traffic within the network. On the other hand, the restoration can also
be done by computing and setting up an alternate path upon detection of a
failure without dedicated restoration capacity; thus requiring less restoration
capacity at the expense of slower restoration time or no guarantee that the
restoration will be successful. This approach is taken by the so-called
fast-local-re-routing scheme of MPLS currently under IETF standardization. The
basic idea of the scheme is to have the neighboring node create and use detours
to route around the failed entities such as a link or a node. Such an approach
in principle can make the recovery faster if the delay is dominated by the
communication and number of nodes traversed between the nodes.

The (sub) 50-msec restoration time of SONET/SDH has
long been the benchmark requirement for supporting resilient communications for
mission-critical applications. While it is commonly believed that
ATM/MPLS-based resilient solutions may have no problem in supporting
restoration time in the range of 100-200 msec, their ability to meet the (sub)
50-msec (or below) restoration time requirement in large-scale production
networks with general topologies remains to be proven over time. The same comment
also applies to IEEE 802.17 Resilient Packet Ring (RPR).  Lastly, there are also other layer 2
Ethernet-based resilient solutions such as the IEEE 802.1d spanning tree
protocol (STP) and the IEEE 802.1w rapid spanning tree protocol (RSTP).  RSTP can be considered as an optimization of
STP with respect to restoration time. It is believed that RSTP can
substantially reduce the worst-case recovery time of STP from 10's of seconds
or minutes to the order of several seconds. However, both of these protocols are
inherently constrained by limiting the active forwarding topology to a tree.
Such constraint often leads to inefficient utilization of network
resources.  It also makes traffic
engineering within the network more difficult.

Traditionally Utility companies have been
relying on SONET/SDH
protection for mission critical services, e.g. SCADA. This could well be
changed with the emergence of the IP/MPLS-based a cost-effective alternatives.
This is particularly true given the wide range of performance/cost trade-offs
afforded by IP/MPLS based solutions. Different IP/MPLS based solutions can
exist in the same IP network fabric which support an integrated set of IntelliGrid Architecture
services with a diverse range of QoS/survivability requirements. Examples
ranging from mission critical real-time measurement ones (which probably
require 1+1 or fast local/shared-mesh re-route types of scheme) and the less
stringent need of off-line, non-real-time data processing for which RSTP or STP
or IP route re-computation based restoration may suffice. However, for those
IntelliGrid Architecture applications/ communications which require extremely stringent,
sub-50msec, restoration protection, e.g., some part of communication paths in
an emerging WACS/WAMS system, proprietary 1+1 APS or
UPSR scheme seems to be more appropriate as the traffic re-routing delay
required by other schemes may be shown to be unacceptably long.

#### Quality-of-Service Enabling Technologies: MPLS, IntServ, DiffServ, RSVP-TE

Multi-Protocol-Label Switching (MPLS) is
poised to be the convergence technology that combines advantages of the
dominant Layer 3 (L3) IP routing protocols and connection-oriented Layer 2 (L2)
techniques including fast forwarding and traffic engineering. Although not
primarily a QoS mechanism, MPLS has become an important tool for network
service providers. It can leverage the different per-hop capabilities and the
prioritizing packet treatments that the IETF DiffServ model propose while
allowing traffic engineering of non-shortest-path routes within a network.
Packet-based MPLS also simplify the mechanics of packet processing within the
routers by replacing full or partial header classification and
longest-prefix-match lookups with simple index label lookups.

MPLS offers a powerful tool, unavailable on
conventional IP routers -- the capability to forward packets over arbitrary
non-shortest paths and emulate high-speed tunnels between non-label-switched
domains.  Such traffic engineering
capabilities can enable IntelliGrid Architecture to optimize the distribution of QoS-sensitive and
best effort traffic around different parts of IntelliGrid Architecture communications
infrastructure. Additionally, MPLS can support metering, policing, marking,
queuing and scheduling behaviors required by the IETF Differential Service
(DiffServ) standards, to offer a diverse set of quality of services for
different IntelliGrid Architecture communications and applications over a single IP/MPLS-based
network.

IETF has developed two QoS service models and
architectures for the Internet, namely the Integrated Services (IntServ) and
Differentiated Services (DiffServ) architectures. IntServ embodies the belief
that routers can and should provide differentiated queuing and scheduling for
IP traffic at the flow-level, classifying packets on IP addresses, protocol
type, and TCP/UDP
ports.  DiffServ embodies a far simpler
classification scheme based on a 6-bit Differentiate Service Code Point field
in every packet header. There are fundamental differences between these two
schemes in the granularity with which traffic can be isolated and
differentiated. While IntServ provides highly granular capabilities, the number
of flows, and associated queues and buffer pools have scared many network
operators and router designers and thus has seen (and expect to continue to
see) little deployment or vendor support. 
DiffServ is enticing with its limited number of queues, but requires
careful network provisioning and balancing acts, as well as other additional
traffic engineering tools/ protocols such as MPLS, to allow judicious sharing
of network resources amongst hundreds or thousands of demanding flows.

The third piece of supporting QoS-based IP
services is provisioning and signaling mechanisms and protocols. Although IETF
developed Resource reSerVation Protocol (RSVP) a number of years ago, it is
only just beginning to come into its own --- shedding the legacy of being
coupled tightly to IntServ and now being appreciated in other circles such as
MPLS. The most recent success of such role transition of RSVP has been the
standardization of RSVP with Traffic Engineering extensions (RSVP-TE). RSVP-TE
applies RSVP signaling on MPLS/DiffServ capable networks to setup and reserve
resources for MPLS LSPs carrying traffic with different types of QoS
requirements under the DiffServ framework.

In the context of IntelliGrid Architecture, as power utilities
are moving towards a multi-service integrated communications infrastructure to
fulfill its various communication needs in the areas of information technology
(IT), distributing computing, monitoring and control, an IP fabric equipped
with MPLS and DiffServ capabilities could well be a cost-effective mainstream
solution. This is particularly true given the wide range of performance/cost
trade-offs afforded by IP/MPLS/DiffServ based solutions.

#### Wireless Data Technologies

Wireless data refers to the mode of
transmitting data over wireless links. Wireless data applications vary from the
more common application such as Internet browsing, email, Energy Market, and
messaging, to specific business applications such as field technician support,
monitoring remote equipment, and emergency operations support.

Specific to IntelliGrid Architecture, wireless data applications
include: (i) communications with remote intelligent electronic devices (e.g.
for data acquisition and control), (ii) field technician support (e.g., for
test, repair and maintenance), and (iii) communications with customer home
portals (e.g., for real-time pricing, load balancing).

A number of different technologies support
wireless data communications. In what follows, we briefly survey some of these
technologies and provide comparisons. For more details of each technology
please refer to the Appendix D reference list.

Wireless data service providers have deployed
second generation (2G) wireless data services that involve transmitting data
over circuit switched voice at the speed of approx. 9kbps. The technologies are
TDMA (IS136), CDMA (IS95), or GSM (European TDMA system). These technologies,
although widely available, do not meet the requirements of high-speed data
applications. The subsequent 2.5 and 3rd generation (2.5G and 3G)
packet-based wireless technologies provide speeds of 300+Kbps for mobile
terminals, and 2+ Mbps for stationary terminals. Wireless LAN
technologies promise less expensive and higher BW services from 10 to 50+ Mbps.
The arguments over WLAN vs. 2.5&3G cellular data have been going on for
some time. Cellular wireless data have wider service availability, reliability
of service provided by major service providers, and potentially higher
security. WLAN has the advantage of higher bandwidth at possibly lower cost.

From the perspective of security, cellular
wireless and wireless LAN
technologies provide some form of user authentication, radio interface
encryption and end-end IPSec support. There are some differences in the
algorithms and implementation of these security features.  In the current state of the technology, 3G
cellular wireless is reported to have better security solutions than 2G
cellular and WLAN.

Trunked Mobile Radio (TMR)
technologies provide the additional capability of broadcasting, multicasting
and direct mode of communication, bypassing the network. The disadvantages of TMR
today are the lack interoperability with other wireless systems, dominance of a
few vendors with proprietary solutions, and lower bandwidth. The differences
between the two (TMR and
cellular wireless) are shrinking as broadcast, multicast and direct mode of
operations are being added to 3G cellular wireless as part of the public safety
wireless initiative, and the TMR
technologies (Project25 and TETRA) are being standardized to provide
interoperability and higher BW.

Clearly each camp emphasizes on the
advantages of their solution. The fact remains that the choice of any
technology is highly dependent on its availability within the service area and
interoperability with existing deployments.

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Table ‑2: A comparison of various Wireless Data Technologies | | | | |
| Wireless Technology | Service | Speed  (Kbps) | Availability | Notes |
| TDMA (IS136) | Circuit Switched Data | 9.6 | Wide | Data over voice channels |
| CDPD |  | 13.2 | Wide | Will be phased out |
| GSM | CS Data | 9.6 | Wide | More widely available in Europe and Asia |
| GPRS | 150 | Wide |
| EGPRS | 473 | Limited |
| CDMA | CS Data | 9.6 | Wide | Data over voice channels |
| WCDMA  (3G1X) | 307 | Limited, expected to become wide. |  |
| 3G1X-EV | 3.1 Mbps | None. Research in progress. |  |
| WCDMA (UMTS) | 340 | Limited, expected to become wide. |  |
| UMTS R5 | 10.2 Mbps | None. Research in progress. |  |
| 3G1X/DO  Rel 0 | 2.4Mbps | Limited, R0 rollout in progress in US | Low mobility, Asymmetrical BW |
| 3G1X/DO  Rel A | 3.1Mbps | None. Research in progress. |
| 802.11 | 802.11 b (WIFI) | 11 Mbps | Mostly available indoors, expected to become wide. | Shared BW, no Mobility |
| 802.11g | 20 Mbps |
| Trunked Mobile Radio | TETRA | 28.8 | Mostly used in public safety & specialized applications | Private Network, broadcast and multicast features |
| Project25 | 9.6 |

 

 

### Communication Infrastructure Integration and Federation Strategy

The wide area communications infrastructure used
within the electric power industry for interactions with field equipment
consists of a huge mixture of different technologies, protocols, and
functionalities.  The most common
categories in the communications environments, described in details in Volume 4
Appendix D include (partial list):

if !supportLists?·      
endif?Environment 2. Deterministic Inter-Site: High
speed inter-site (e.g. distance protective relaying, FSM)

if !supportLists?·      
endif?Environment 4. Inter-Field Equipment:
Inter-field devices environment (e.g. monitoring and control of IEDs on
feeders, …)

if !supportLists?·      
endif?Environment 5. Critical Operations DAC: High security
between control center and field equipment environment (e.g. monitoring and
control by SCADA of substation and DA equipment, monitoring and control of DER devices,
monitoring of security-sensitive customer meters, monitoring and control of
generation units)

if !supportLists?·      
endif?Environment 6. Non-Critical Operations DAC:
Lower security interactions among control center, substation, field equipment,
customer sites environment (e.g. monitoring non-power system equipment, less
security-sensitive substations, customer site PQ monitoring, customer metering)

if !supportLists?·      
endif?Environment 8. Inter-Control Center: Among
control centers (e.g. between utility control centers, between RTOs, between
remote subsidiary or supervisory centers)

if !supportLists?·      
endif?Environment 10. RTOs to Market Participants:
Between utility/RTO/ISO control centers and Market Participants (e.g. market
operations)

if !supportLists?·      
endif?Environment 11. Control Center to Customers:
Between customer equipment and utility control centers (e.g. customer metering,
demand response interactions, DER management)

if !supportLists?·      
endif?Environment 12. Control Center to Corporations:
Between control centers and external corporations (e.g. weather data,
regulators, auditors, vendors)

if !supportLists?·      
endif?Environment 14. Inter-Corporation: Between
corporate utility and external corporations (e.g. e-business)

if !supportLists?·      
endif?Environment 17. Inter-Customer Sites: Between
customer sites (e.g. microgrid management)

if !supportLists?·      
endif?Environment 18. Customer to ESP: Between
customers and ESPs, Aggregators, MDMAs (e.g. DER management,
customer metering, RTP, demand
response)

 

Utilities have, in the past, developed
utility-specific communications technologies to support these activities.
However, recently, new communication standards and technologies have emerged
from the communications industry that could more cost-effectively support (1)
information technology (IT) networks within an utility company, (2) control
center applications and (3) the access of operations data from the utility
corporate network to the control centers/ network.

Traditionally, the power utility communication
infrastructure typically comprises multiple physically separate networks, each
dedicated to support specific applications and functions. For example, a SONET/SDH-based network
is used to carry real-time SCADA traffic while engineers to access substation
information use dial-up modems. Further, a separate TDM-based network may exist
to support PBX-based voice communications among the substations and control
centers.

Current
conventional substation communications are impeding the electricity industry’s
march toward automation. Utilities still rely on individual wires to connect
equipment, sensors and controls within a substation. These links carry all the
communications traffic associated with data collection and dissemination,
delivery of control and protection commands and management of stored data and
programs. The use of individual lines is expensive, however, because each
device must be physically connected with the substation controllers and with
the utility control center. Further, adding new equipment under this system can
require costly interface modules.

The
mission-critical status of the utility network requires stringent reliability
and resiliency to ensure that outages are limited and quickly remedied.
Protection devices are the first line of defense. Supervisory Control and Data
Acquisition (SCADA) provides applications for real-time data acquisition and
control from remote locations and is a primary system used in the utility
industry to oversee the operations of the power system. Control center
applications help evaluate the current state and recommend pro-active solutions
for different power system contingencies.

As
information becomes increasingly vital to power system operations, utilities
want to ensure continued support for these information flows, while providing
greater insight into the state of the communications network and the computer
systems in the field, reducing latency delays, adding redundancy in its central
operations center, reducing switched path delay upon a link failure, offering
new disaster recovery options, and supporting in-service upgrades.

if !vml?![](Anl_Comm_Recomm_files/image002.gif)endif?

Figure ‑32 Migration To 61850 In The Substation
Communications Environment

 

Seeking
a common architecture to improve the reliability and operations of the network,
some utilities are now implementing new substations using IEC61850 standards
for substation automation, with a few utilities expressing interest in
upgrading existing substations. Figure 32 illustrates the ongoing changes of the communications
infrastructure within a substation. All data transactions pass through a local
area network (with switched Ethernet hubs for the protection devices requiring
deterministic rapid response environments), thus replacing the costly
individual wires that presently connect equipment, sensors and controls at
substations, and simplifying the addition of new equipment. 

Reality
is that the substation environment will be a mix of new Ethernet-enabled
Intelligent Electronic Devices (IEDs) as well as legacy equipment. The
communications between the substation and the control center are currently a
mixture of:

if !supportLists?– endif?Utility-owned
SONET/SDH
high speed wide area networks,

if !supportLists?– endif?Digital
and analog microwave systems

if !supportLists?– endif?Multiple
Address Radio Systems

if !supportLists?– endif?Leased
facilities from telecommunication providers, including leased telephone analog
lines, fractional T1 lines, and Frame Relay links

if !supportLists?– endif?Satellite
and other special communications media

 

With
this mixture of communication technologies, multi-service transport is needed.

The
existing SONET/SDH-based infrastructure enables multiple service delivery between
substations and control centers. In particular, various data/ voice services
such as ATM, Frame-Relay (FR) ,  Ethernet
as well as TDM-based voice or private data line services are overlay on the top
of  the SONET/SDH infrastructure. While this architecture
can meet the high-bandwidth and reliable communication needs of the power
utilities, it is not the most efficient and cost-effective solution due to the
rigid increments, and thus coarse bandwidth granularity, required by the SONET/SDH framing/ virtual tributes (VT)
structure. Also, bandwidth upgrades tend to be cumbersome, as the speed of all
Add/Drop Multiplexers (ADM) interfaces connecting to a ring has to
be matched. This overlay approach also requires higher capital, operations and
maintenance costs as larger number of separate communications equipments
(i.e.  the DSLAM, ATM/FR multiplexers,
Ethernet adaptors) are required. The overlay
approach also leads to additional management complexity and integration
challenges as communications equipment with separate operation support systems
needed to be managed simultaneously to support end-to-end communication
services.

To address the above issues caused by the
overlap approach, it could be cost-effective to evolve certain multi-function
wide area networks towards the emerging multi-service-capable SONET/SDH-based
solutions proposed by the telecommunications/networking community. In this
approach, new service capabilities are built into the next generation SONET/SDH ADMs for
the optimization of both circuit-switched and packet-switched services to
enable the support of multiple services over a common, integrated
infrastructure.  By supporting
packet-level multiplexing over fiber based on the ITU Generic Framing Procedure
(GFP) standards, the so-called next-generation or multiple-service SONET/SDH ADMs
reduce the SONET/SDH VT
bandwidth granularity to enable flexible and more dynamic bandwidth
provisioning capabilities. The multi-service ADMs also provide integrated LAN switching
for the converged Ethernet-over-Fiber technologies. Conventional LAN management
and security capabilities such as Virtual LAN (VLAN) can
also be effectively extended to support metropolitan and wide-area
networks.  Traffic prioritization,
policing and SLA provisioning are also supported.  Both point-to-point and point-to-multi-point
communications can be efficiently supported. For those low-priority traffic and
applications which do not demand SONET/SDH 50-mec
restoration protection, the multi-service ADMs can also substitute SONET/SDH-based
protection switching with spanning tree-based restoration schemes, i.e. 802.1d
and/or 802.1w, operating at the Ethernet layer, to conserve bandwidth along the
rings. Figure 33 summarizes the rich set of capabilities and benefits
of the integrated communication infrastructure provided by the multi-service
SONET/SDH approach.
By providing the integration at the Ethernet layer rather than the IP layer,
legacy or proprietary non-IP-based protocols can be readily handled by this
integrated communication infrastructure. It is also important to note that
Ethernet layer integration does not preclude additional service integration to be
carried out at the IP layer, e.g. using MPLS/ DiffServ,  to support multi-media IP-based services such
as Voice-over-IP and packet-based video conferencing applications.

**if !vml?![](Anl_Comm_Recomm_files/image004.gif)endif?**

Figure ‑33 Next
Generation SONET --- the Multi-service Approach and its Benefits

### Overlapping, Harmonizing and Missing Communications Infrastructure Technologies

As we have discussed in Section 3.4.1, there
are numerous overlapping technologies in various areas of communications. It is
important to note that, by overlapping, we only mean the technologies provide
similar high-level functions.  However,
most of the overlapping technologies in each area do carry implied trade-offs
in terms of implementation complexity, response time, and hardware/software
resource implications. Refer to Appendix E and the references thereof for more
detailed guidelines on selecting among alternative technological solutions for
a given set of operating environment and service requirements.

At the network layer various protocols such
as IPV4, IPV6, and other non-IP-based networking protocol/ addressing scheme,
such as IPX, or OSI/ISO
networking layer exist. Network layer overlapping technologies also including
the various intra-domain routing protocols such as OSPF, IS-IS and RIP. At the
transport layer, SCTP is poised to become a key alternative for TCP in
the support of reliable, connection-oriented transport over IP, especially in
the area of multi-homing support and fault-tolerance control applications.
Similarly, DCCP is designed to be an improvement over UDP to support
connectionless transport over IP by allowing the incorporation of TCP-friendly
congestion control mechanism amenable for real-time streaming applications.
Both SCTP and DCCP have features to address the security pitfalls of its
existing counterparts. Example, security cookies are used by SCTP to overcome
the SYN-flood vulnerabilities found during the setup of a TCP
connection.

In the area of technologies providing resilient
communications, there are also substantial overlaps.  As discussed in Section 1.3.4.1 and the
references thereof, resilient services can be provided at various layers of the
protocol stack, ranging from load-balancing/ dispatcher-based server-redundancy
solution at the application layer, to transport layer resilient via SCTP or TCP, to
network layer resilient solution based on dynamic IP routing protocols or
MPLS-LSP-based or ATM-VC-based fast restoration, to MAC-layer
solutions based on IEEE 802.1d(w) (Rapid) Spanning Tree protocols or IEEE
802.17  Resilient Packet Ring, to
physical layer SONET/SDH
self-healing rings (UPSRs and BLSRs) and linear APS 1:N
or 1+1 schemes.

The overlapping wireless data technologies
are also discussed in Section 1.3.4.1.

We have described in Section 1.3.4.2 on how a
unified communication infrastructure can be built using emerging multi-service
SONET/SDH-based
solution. It was also emphasized that alternative ways of communication service
integration are possible and should be considered in the future. In particular,
in additional to the use of multi-service SONET/SDH ADMs
to realize integration of packet and circuit-based communications at the SONET/SDH, ATM
also provides provide a proven multi-service network integration approach. The
major drawback of ATM is the cost to maintain the IP-over-ATM overlay as
end-applications are predominantly IP-based. An IP/MPLS networking
infrastructure is poised to overcome this limitation of ATM. Furthermore, with
the active standardization activities going on in the IETF Pseudo Wire
Emulation End-to-End (PW3E) Working Group, one-day, it may be possible to have
a single IP/MPLS core network to transport both IP as well as non-IP-based
services.

While IP/MPLS-based solutions have already
emerged for supporting QoS, traffic engineering as well as resilient service
requirements, the current solutions are largely limited to the support of such
services under a single administrative domain or autonomous system (AS).
Additional technological developments and standardization efforts are needed in
order to extend such capabilities across multiple ASs in a scalable, secure and
efficient manner.  Also, a more
systematic and standardized approach is needed to handle the potential
interactions between technologies providing resilient services at different
layers of the protocol stack.
