# Firewall Traversal

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Firewall_Traversal.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Firewall Traversal

A
major barrier to dynamic, cross-domain Grid computing today is the existence of
firewalls. As noted above, firewalls provide limited value within a dynamic
Grid environment. However, it is also the case that firewalls are unlikely to
disappear anytime soon. Thus, the OGSA security model must take them into
account and provide mechanisms for cleanly traversing them—without compromising
local control of firewall policy.

There
are several major issues with the use of firewalls:

·      
Firewalls are typically invasive and perform address translation without
providing a useable audit record.

·      
Firewalls that have the ability to perform state-based inspection are
not capable of analyzing the complex protocols that IntelliGrid Architecture is considering.

·      
Firewalls are difficult to manage and must be monitored as part of the
SMI process.

However,
firewalls are deployed in order to protect critical infrastructure
computational resources and should be deployed at inter-domain connectivity
points. With this deployment strategy, how can one facilitate firewall
transversal?

Technological Assessment and
Relevant Specifications

There
are three major types of firewalls:

·      
Transparent (see FIRE-01 and FIRE-02): These firewalls perform OSI layer
2 or 3 bridging and do not typically provide state inspection. However, they do
not obscure addressing information and tend to be the fastest type of firewall
when performance is measured in terms of packet throughput. Since these are
transparent, these types are the easiest to transverse when properly
configured.   
  
This is the only firewall type that could possible meet the 4msec performance
requirement.

·      
Non-Transparent: These firewalls typically perform the following
functions: packet filtering and proxy service (e.g. address translation).

·      
Non-Transparent with Stateful Inspection: Same capability as
non-transparent but has the additional ability to examine the contents of each
packet. This is typically the lowest performance type of firewall when
performance is measured in regards to packet throughput.

Firewall
Transversal is automatically provided when Transparent Firewalls are utilized, however the issue still remains for both versions
of non-transparent firewalls. The typical mechanism for allowing transversal
(e.g. from outside a Security Domain to inside) is via a proxy service or a set
of firewall supplied cookies. However, there are several issues about
sending/receiving such information in the clear. Therefore, encryption is
desired.

Current
firewall transversal thoughts are to create a SSL/TLS tunnel (thereby verifying
the remote node has certain access rights) and then using an internal proxy to
enforce further privilege restrictions.

Figure 1:
Example of SSL/TLS Tunnel for Firewall
Transversal[[3]](Tech_Firewall_Traversal.htm#_ftn3)

Figure
1 shows the SSL tunnel being used to a DMZ where the backend application data
is proxied on servers located within the DMZ. It would also be possible to
allow stateful and privilege proxy access directly to the back-end data
providers if needed. Either architecture is viable and will be up to the
Security Domain to decide which best meets its needs.

Whatever
the choice, the functional characteristics found in RFC 2979 should be
provided.

Table 13: References regarding Firewall Transversal

|  |  |
| --- | --- |
| FIRE-01 | Matthew Tanase, **Transparent, Bridging and In-line Firewall Devices,**October **15, 2003**  Available from: http://www.securityfocus.com/infocus/1737 |
| FIRE-02 | Transparent Cisco IOS® Firewall  Available from: http://www.cisco.com/univercd/cc/td/doc/product/software/ios123/123newft/123t/123t\_7/  gt\_trans.htm |

Table 14: Relevant Specifications regarding Firewall
Transversal

| Identification Number | Name | Comment |
| --- | --- | --- |
| RFC 1579 | Firewall-Friendly FTP |  |
| RFC 1919 | Classical versus Transparent IP Proxies | Recommended Reading |
| RFC 2008 | Implications of Various Address Allocation Policies for Internet Routing | Recommended Reading |
| RFC 2401 | Security Architecture for the Internet Protocol |  |
| RFC 2505 | http://www.armware.dk/RFC/rfc/rfc2505.htmlAnti-Spam Recommendations for SMTP MTAs |  |
| RFC 2543 | http://www.armware.dk/RFC/rfc/rfc2543.htmlSIP: Session Initiation Protocol |  |
| RFC 2547 | http://www.armware.dk/RFC/rfc/rfc2547.htmlBGP/MPLS VPNs |  |
| RFC 2764 | A Framework for IP Based Virtual Private Networks |  |
| RFC 2775 | Internet Transparency | Recommended Reading |
| RFC 2888 | Secure Remote Access with L2TP |  |
| RFC 2977 | Mobile IP Authentication, Authorization, and Accounting Requirements |  |
| RFC 2979 | Behavior of and Requirements for Internet Firewalls | Recommended |
| RFC 2993 | Architectural Implications of NAT | Recommended Reading |
