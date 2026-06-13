# Security Recommendations

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Security_Recomm2.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Major Security Recommendations

This
section discusses the major recommendations that are drawn from this appendix.

·     **Policy development is job 1!**
Several key documents are referenced that should be used/understood
when evaluating and creating security policy.  There are several
referenced throughout the appendix, however RFC 2196, RFC 2401, and EPRI Report
1008988 are major references.

·      
Decompose the security discussion into a discussion of security issues regarding a particular security domain.

·      
For any given security domain, there are more security services required
for inter-domain exchanges than intra-domain exchanges.

·      
Risk assessment methodologies should be used to determine which assets
should be secured.

·      There needs to be an established audit framework within each security
domain and this framework needs to allow the creation of an audit trail that
could span more than one security domain. ISO/IEC 10164-8 and ISO/IEC
10181-7 are recommended to be used as the basis of such a framework.

·    
There is a need to provide coordinated and secure timestamp and time
representation for the audit records to allow the creation of an appropriately
time sequenced audit trail. It is recommended that ISO/IEC 18014-1 and UTC time be used to satisfy
this need.

·      There is a need to provide guidance and usage recommendations in regards
to the management/creation of different credential types. Several different credential types (e.g. certificates,
username/password, communication addresses, etc..) are identified, and some internal recommendations
are made. Additional recommendations include that FIPS PUB
12, RFC 2527, and FIPS 186 should all be considered when managing credentials and
establishing which credentials to use.

·      Confidentiality can be provided through the use of encryption technology
and communication path selection.  There are no available technologies to
facilitate communication path selection. However, there are many documents that
are applicable to the use of encryption.
Public Key Infrastructure as defined in the X.509 series (e.g. RFC 2459, RFC
2587, RFC 3039, RFC 3161, RFC 2586, etc..) should be used. In addition, Kerberos (e.g. RFC 1510,  RFC 2400, etc…)
could be considered if PKI is not feasible due to compute-constraints,
performance-constraints, or communications constraints.
Additionally, the following documents represent strong recommendations in
regards to implementing encryption: FIPS 140-2, FIPS 197, and PKCS.

·      
Internet based transport level encryption is recommended to be provided
by TLS (RFC 2246 and IEC 62351-3).  
  
Additionally, several commonly used application protocols have had security
extensions specified.  It is recommended that the following RFCs be
considered when deploying the particular protocol:  
  
FTP:                                    
RFC 2228  
SMTP:                                
RFC 1040, RFC 1423, RFC 2045, and RFC 2505  
IMAP4:                               
RFC 2086  
SNMP:                                
RFC 1351, RFC 3411, and RFC 3414  
NTP/SNTP:                         
RFC 1305  
ISO/IEC 9506:                       IEC
62351-4  
ISO/IEC 8070-5/DNP:          
IEC 62351-5  
ISO/IEC
61850:                    
IEC 62351-6

·    Recommendations
on network and data link security technologies include the following.  
  
Dial-in:                                 RADIUS (RFC 2865)  
Direct Serial (Retrofit):
          AGA-12  
ATM:                                  
RFC 2684  
WI-FI:                                 
IEEE 802.11i (a.k.a. WPA2)

·      
RFC 2401 is recommended for the creation of 
virtual private networks (VPNs).

·      XML technologies
are recommended to be utilized for
administrative purposes (e.g. SAML, XACML, and XKMS). 
This recommendation requires that XML exchanges be done in a secure manner and
the appendix recommends that this security be implemented through the use of
several different technologies.  Some of the major technologies are:  
  
SAML Authentication Context, WS-Policy, WS-Policy Assertions, WS-Policy
Attachments, XACML Schema, and XKMS.

·      It
is also recommended, as part of the policy development/deployment,
that intrusion detection and intrusion prevention be considered.  It is
also recognized that service level agreements can also assist in this effort.
