# AGA-12 Cryptographic Protection of SCADA Communications General Recommendations.

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_AGA-12_Cryptographic_Protection_of_SCADA_Communications_Gene.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### AGA-12 Cryptographic Protection of SCADA Communications General Recommendations.

**URL:** http://www.aga.org

The
American Gas Association (AGA) represents almost 200 local utilities that
deliver natural gas to homes in the USA. These utilities are part of the
critical infrastructure and rely on SCADA networks to control the operations.
AGA, in conjunction with GTI and other industry groups, created AGA 12 to
develop cyber security standards and protocols for the industry.

AGA
12 has taken a unique approach to focus on securing the communications link
between field devices and the control servers or control center. While there
certainly is a risk of data insertion and modification in the communication
channel, it may not be the most likely or even easiest avenue of attack on a
SCADA system.

The
first Technical Report, TR-1, defines an add-on encryption module that also
could be integrated into an RTU or PLC. Oddly enough, the most recent version
includes significantly less technical detail and removed the SCADA Link
Security (SLS) protocol defined in Appendix K. If you are interested in AGA 12,
Digital Bond recommends you look at Appendix K of the March 2003 version. Note:
hit cancel when the login request appears and the document will load.

The
big hole in TR-1 is key management, which is to be addressed at a later date.
This is a significant issue given the number of encryptors that would be
deployed in a SCADA system. Until key management is addressed AGA 12-1 encryptors
can be considered a proof of concept solution at best.

The
best news on the AGA 12 front is sample implementation code exists. Andrew
Wright of Cisco's Critical Infrastructure Assurance Group (CIAG) has written
and documented the code. There are also good technical papers on the security
of the protocol available through Andrew's ScadaSafe site.

**Keywords:**Confidentiality, Authorization for Access Control, Policy,
Eavesdropping, Security
