# Security

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/High_Level_Concepts/IECSA_VolumeIV_AppendixA.htm

---

The Integrated Energy and Communication Systems
Architecture

Volume IV:   
Technical Analysis

Appendix A:  
Security

EPRI Project Manager

Joe Hughes

Cosponsor

Electricity Innovation Institute Consortium for Electric
Infrastructure to Support a Digital Society (CEIDS)

EPRI • 3412 Hillview Avenue, Palo Alto, California
94304 • PO Box 10412, Palo Alto, California 94303 • USA  
800.313.3774 • 650.855.2121 • askepri@epri.com • www.epri.com

DISCLAIMER OF WARRANTIES AND LIMITATION OF LIABILITIES

THIS DOCUMENT WAS PREPARED BY THE ORGANIZATION(S) NAMED
BELOW AS AN ACCOUNT OF WORK SPONSORED OR COSPONSORED BY THE ELECTRIC POWER
RESEARCH INSTITUTE, INC. (EPRI). NEITHER EPRI, ANY MEMBER OF EPRI, ANY
COSPONSOR, THE ORGANIZATION(S) BELOW, NOR ANY PERSON ACTING ON BEHALF OF ANY OF
THEM:

(A) MAKES ANY WARRANTY OR REPRESENTATION WHATSOEVER, EXPRESS
OR IMPLIED, (I) WITH RESPECT TO THE USE OF ANY INFORMATION, APPARATUS, METHOD,
PROCESS, OR SIMILAR ITEM DISCLOSED IN THIS DOCUMENT, INCLUDING MERCHANTABILITY
AND FITNESS FOR A PARTICULAR PURPOSE, OR (II) THAT SUCH USE DOES NOT INFRINGE
ON OR INTERFERE WITH PRIVATELY OWNED RIGHTS, INCLUDING ANY PARTY'S INTELLECTUAL
PROPERTY, OR (III) THAT THIS DOCUMENT IS SUITABLE TO ANY PARTICULAR USER'S
CIRCUMSTANCE; OR

(B) ASSUMES RESPONSIBILITY FOR ANY DAMAGES OR OTHER
LIABILITY WHATSOEVER (INCLUDING ANY CONSEQUENTIAL DAMAGES, EVEN IF EPRI OR ANY
EPRI REPRESENTATIVE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES)
RESULTING FROM YOUR SELECTION OR USE OF THIS DOCUMENT OR ANY INFORMATION,
APPARATUS, METHOD, PROCESS, OR SIMILAR ITEM DISCLOSED IN THIS DOCUMENT.

ORGANIZATIONS THAT PREPARED THIS DOCUMENT

General Electric Company
led by GE Global Research (Prime Contractor)

Significant
Contributions made by  
EnerNex Corporation  
Hypertek  
Lucent Technologies (Partner)  
Systems Integration Specialists Company, Inc.  
Utility Consulting International (Partner)

ORDERING INFORMATION

Requests for copies of this report should be
directed to EPRI Orders and Conferences, 1355 Willow Way, Suite 278, Concord, CA
94520. Toll-free number: 800.313.3774, press 2, or internally x5379; voice:
925.609.9169; fax: 925.609.1310.

Electric Power Research Institute and EPRI are
registered service marks of the Electric Power Research Institute, Inc. EPRI.
ELECTRIFY THE WORLD is a service mark of the Electric Power Research Institute,
Inc. All other trademarks are the property of their respective owners.

Copyright © 2002, 2003, 2004 Electric Power Research
Institute, Inc. All rights reserved.

CitationS

This document describes research sponsored by EPRI and
Electricity Innovation Institute.

The publication is a corporate document that should be cited
in the literature in the following manner:

THE INTEGRATED ENERGY AND COMMUNICATION SYSTEMS
ARCHITECTURE, EPRI, Palo Alto, CA and Electricity Innovation Institute, Palo
Alto, CA: 2003 {Product ID Number.

  

# Table of Contents

[Table of
Contents iii](IECSA_VolumeIV_AppendixA.htm#_Toc76139309)

[Appendix A –
Security. 1](IECSA_VolumeIV_AppendixA.htm#_Toc76139310)

[Executive Summary. **Error! Bookmark not defined.**](IECSA_VolumeIV_AppendixA.htm#_Toc76139311)

[Introduction. **Error! Bookmark not defined.**](IECSA_VolumeIV_AppendixA.htm#_Toc76139312)

[1     
Security and Security Domains 3](IECSA_VolumeIV_AppendixA.htm#_Toc76139313)

[2     
Common Security Services and Technologies/Standards 9](IECSA_VolumeIV_AppendixA.htm#_Toc76139314)

[2.1   
Audit Common Service. 9](IECSA_VolumeIV_AppendixA.htm#_Toc76139315)

[2.1.1   
Audit Technologies/Specifications 10](IECSA_VolumeIV_AppendixA.htm#_Toc76139316)

[2.1.1.1   Technological
Assessment 11](IECSA_VolumeIV_AppendixA.htm#_Toc76139317)

[2.2   
Authorization for Access Control 11](IECSA_VolumeIV_AppendixA.htm#_Toc76139318)

[2.2.1   
Physical 11](IECSA_VolumeIV_AppendixA.htm#_Toc76139319)

[2.2.1.1   Physical
Access Technologies/Specifications 12](IECSA_VolumeIV_AppendixA.htm#_Toc76139320)

[2.2.1.1.1   
Technological Assessment 14](IECSA_VolumeIV_AppendixA.htm#_Toc76139321)

[2.2.2   
Computational Resource. 14](IECSA_VolumeIV_AppendixA.htm#_Toc76139322)

[2.2.2.1   Operating
System and Computer Programs 15](IECSA_VolumeIV_AppendixA.htm#_Toc76139323)

[2.2.2.2   Communication
Networks 15](IECSA_VolumeIV_AppendixA.htm#_Toc76139324)

[2.2.2.3   Technological
Assessment Specifications/Standards 16](IECSA_VolumeIV_AppendixA.htm#_Toc76139325)

[2.2.2.3.1   
Technological Assessment and Recommendations 17](IECSA_VolumeIV_AppendixA.htm#_Toc76139326)

[2.2.2.3.1.1   OS
Recommendations 17](IECSA_VolumeIV_AppendixA.htm#_Toc76139327)

[2.2.2.3.1.2   Computer
Programs 17](IECSA_VolumeIV_AppendixA.htm#_Toc76139328)

[2.2.2.3.1.3   Communication
Networks and Protocols 17](IECSA_VolumeIV_AppendixA.htm#_Toc76139329)

[2.2.3   
Informational Technology Assessment/Specification.
18](IECSA_VolumeIV_AppendixA.htm#_Toc76139330)

[2.3   
Confidentiality. 18](IECSA_VolumeIV_AppendixA.htm#_Toc76139331)

[2.3.1   
Encryption. 18](IECSA_VolumeIV_AppendixA.htm#_Toc76139332)

[2.3.1.1   Technological
Assessment and Specifications 20](IECSA_VolumeIV_AppendixA.htm#_Toc76139333)

[2.3.1.1.1   
Protocol Basis 20](IECSA_VolumeIV_AppendixA.htm#_Toc76139334)

[2.3.1.1.2   
Media. 20](IECSA_VolumeIV_AppendixA.htm#_Toc76139335)

[2.3.2   
Communication Path Selection. 21](IECSA_VolumeIV_AppendixA.htm#_Toc76139336)

[2.4   
Credential Conversion. 22](IECSA_VolumeIV_AppendixA.htm#_Toc76139337)

[2.4.1   
Technological Assessment 22](IECSA_VolumeIV_AppendixA.htm#_Toc76139338)

[2.4.1.1   Certificate. 22](IECSA_VolumeIV_AppendixA.htm#_Toc76139339)

[2.5   
Credential Renewal Service. 23](IECSA_VolumeIV_AppendixA.htm#_Toc76139340)

[2.5.1   
Technological Assessment and Relevant Specifications 23](IECSA_VolumeIV_AppendixA.htm#_Toc76139341)

[2.5.1.1   Specific
Recommendations 24](IECSA_VolumeIV_AppendixA.htm#_Toc76139342)

[2.5.1.1.1   
Certificates 24](IECSA_VolumeIV_AppendixA.htm#_Toc76139343)

[2.6   
Delegation Service. 25](IECSA_VolumeIV_AppendixA.htm#_Toc76139344)

[2.6.1   
Technological Assessment and Relevant Specifications 26](IECSA_VolumeIV_AppendixA.htm#_Toc76139345)

[2.7   
Firewall Traversal 26](IECSA_VolumeIV_AppendixA.htm#_Toc76139346)

[2.7.1   
Technological Assessment and Relevant Specifications 27](IECSA_VolumeIV_AppendixA.htm#_Toc76139347)

[2.8   
Identity Establishment Service. 28](IECSA_VolumeIV_AppendixA.htm#_Toc76139348)

[2.8.1   
Identity Establishment for Physical Assets 28](IECSA_VolumeIV_AppendixA.htm#_Toc76139349)

[2.8.2   
Computational Resources 29](IECSA_VolumeIV_AppendixA.htm#_Toc76139350)

[*2.8.3*   
*Technological Assessment and Relevant Specifications* 29](IECSA_VolumeIV_AppendixA.htm#_Toc76139351)

[2.8.3.1   General
Technologies 29](IECSA_VolumeIV_AppendixA.htm#_Toc76139352)

[2.8.3.1.1   
Address Resolution. 29](IECSA_VolumeIV_AppendixA.htm#_Toc76139353)

[2.8.3.1.2   
Username/Password. 30](IECSA_VolumeIV_AppendixA.htm#_Toc76139354)

[2.8.3.1.3   
Smart Cards 30](IECSA_VolumeIV_AppendixA.htm#_Toc76139355)

[2.8.3.1.4   
Digital Certificates 31](IECSA_VolumeIV_AppendixA.htm#_Toc76139356)

[2.8.3.1.5   
Digital Signatures 32](IECSA_VolumeIV_AppendixA.htm#_Toc76139357)

[2.8.3.1.6   
Biometrics 32](IECSA_VolumeIV_AppendixA.htm#_Toc76139358)

[2.8.3.2   Specific
Technologies 33](IECSA_VolumeIV_AppendixA.htm#_Toc76139359)

[2.8.3.2.1   
Relational Databases 33](IECSA_VolumeIV_AppendixA.htm#_Toc76139360)

[2.8.3.2.2   
Web Based User Interfaces 34](IECSA_VolumeIV_AppendixA.htm#_Toc76139361)

[2.9   
Identity Mapping Service. 34](IECSA_VolumeIV_AppendixA.htm#_Toc76139362)

[2.9.1   
Technological Assessment and Relevant Specifications 34](IECSA_VolumeIV_AppendixA.htm#_Toc76139363)

[2.9.1.1   Address
Mapping. 34](IECSA_VolumeIV_AppendixA.htm#_Toc76139364)

[2.9.1.2   UserName/Password. 34](IECSA_VolumeIV_AppendixA.htm#_Toc76139365)

[2.9.1.3   Digital
Certificates 34](IECSA_VolumeIV_AppendixA.htm#_Toc76139366)

[2.10  Information
Integrity Service. 34](IECSA_VolumeIV_AppendixA.htm#_Toc76139367)

[2.11  Inter-Domain
Security. 35](IECSA_VolumeIV_AppendixA.htm#_Toc76139368)

[2.12  Non-repudiation. 35](IECSA_VolumeIV_AppendixA.htm#_Toc76139369)

[2.12.1  Technological
Assessment and Relevant Specifications 35](IECSA_VolumeIV_AppendixA.htm#_Toc76139370)

[2.13  Path
Routing and QOS service. 36](IECSA_VolumeIV_AppendixA.htm#_Toc76139371)

[2.13.1  Technological
Assessment and Relevant Specifications 36](IECSA_VolumeIV_AppendixA.htm#_Toc76139372)

[2.13.1.1  Communication
Path Definition. 36](IECSA_VolumeIV_AppendixA.htm#_Toc76139373)

[2.13.1.2  Quality
of Security. 36](IECSA_VolumeIV_AppendixA.htm#_Toc76139374)

[2.14  Policy. 37](IECSA_VolumeIV_AppendixA.htm#_Toc76139375)

[2.15  Policy
Exchange. 37](IECSA_VolumeIV_AppendixA.htm#_Toc76139376)

[2.15.1  Technology
Assessment and Relevant Specifications 37](IECSA_VolumeIV_AppendixA.htm#_Toc76139377)

[2.16  Privacy
Service. 37](IECSA_VolumeIV_AppendixA.htm#_Toc76139378)

[2.16.1  Technological
Assessment and Relevant Documents 37](IECSA_VolumeIV_AppendixA.htm#_Toc76139379)

[2.17  Profile
Service (User Profile Service) 39](IECSA_VolumeIV_AppendixA.htm#_Toc76139380)

[2.17.1  Technological
Assessment and Relevant Specifications 39](IECSA_VolumeIV_AppendixA.htm#_Toc76139381)

[2.18  Quality
of Identity Service. 39](IECSA_VolumeIV_AppendixA.htm#_Toc76139382)

[2.18.1  Technological
Assessment and Relevant Specifications 39](IECSA_VolumeIV_AppendixA.htm#_Toc76139383)

[2.19  Security
against Denial-of-Service. 41](IECSA_VolumeIV_AppendixA.htm#_Toc76139384)

[2.19.1  Technological
Assessment and Relevant Specifications 42](IECSA_VolumeIV_AppendixA.htm#_Toc76139385)

[2.20  Security
Assurance Management 42](IECSA_VolumeIV_AppendixA.htm#_Toc76139386)

[2.20.1  Technological
Assessment and Relevant Specifications 42](IECSA_VolumeIV_AppendixA.htm#_Toc76139387)

[2.21  Security
Protocol Mapping. 42](IECSA_VolumeIV_AppendixA.htm#_Toc76139388)

[2.21.1  Technological
Assessment 42](IECSA_VolumeIV_AppendixA.htm#_Toc76139389)

[2.22  Security
Service Availability Discovery Service. 43](IECSA_VolumeIV_AppendixA.htm#_Toc76139390)

[2.22.1  Technological
Assessment and Relevant Specifications 43](IECSA_VolumeIV_AppendixA.htm#_Toc76139391)

[2.23  Single
Sign on Service. 43](IECSA_VolumeIV_AppendixA.htm#_Toc76139392)

[2.24  Trust
Establishment Service. 43](IECSA_VolumeIV_AppendixA.htm#_Toc76139393)

[3     
Policy. 43](IECSA_VolumeIV_AppendixA.htm#_Toc76139394)

[3.1   
General Process 44](IECSA_VolumeIV_AppendixA.htm#_Toc76139395)

[3.1.1   
Requirements 44](IECSA_VolumeIV_AppendixA.htm#_Toc76139396)

[3.1.1.1   Risk
Assessment/Analysis 44](IECSA_VolumeIV_AppendixA.htm#_Toc76139397)

[3.1.1.2   External
Legal Directive Impacts 44](IECSA_VolumeIV_AppendixA.htm#_Toc76139398)

[3.1.1.3   Fault
Tolerance. 45](IECSA_VolumeIV_AppendixA.htm#_Toc76139399)

[3.1.2   
Implementation. 45](IECSA_VolumeIV_AppendixA.htm#_Toc76139400)

[3.1.3   
Analysis 45](IECSA_VolumeIV_AppendixA.htm#_Toc76139401)

[3.2   
PKI Infrastructure Policy and Issues 45](IECSA_VolumeIV_AppendixA.htm#_Toc76139402)

[3.2.1   
Intrusion Detection. 48](IECSA_VolumeIV_AppendixA.htm#_Toc76139403)

[3.3   
Specific Policy Issues and Recommendations per Service. 48](IECSA_VolumeIV_AppendixA.htm#_Toc76139404)

[3.3.1   
Audit Service and Non-Repudiation. 48](IECSA_VolumeIV_AppendixA.htm#_Toc76139405)

[3.3.2   
Credentials and User Accounts 48](IECSA_VolumeIV_AppendixA.htm#_Toc76139406)

[3.3.2.1   Credentials 48](IECSA_VolumeIV_AppendixA.htm#_Toc76139407)

[3.3.2.1.1   
Personal Identification. 49](IECSA_VolumeIV_AppendixA.htm#_Toc76139408)

[3.3.2.1.2   
Addresses 49](IECSA_VolumeIV_AppendixA.htm#_Toc76139409)

[3.3.2.1.2.1   Statically
Assigned Addresses 49](IECSA_VolumeIV_AppendixA.htm#_Toc76139410)

[3.3.2.1.2.2   Dynamically
Assigned Addresses 49](IECSA_VolumeIV_AppendixA.htm#_Toc76139411)

[3.3.2.1.3   
Username/Passwords 49](IECSA_VolumeIV_AppendixA.htm#_Toc76139412)

[3.3.2.1.4   
Smart Cards 51](IECSA_VolumeIV_AppendixA.htm#_Toc76139413)

[3.3.2.1.5   
Digital Certificates 51](IECSA_VolumeIV_AppendixA.htm#_Toc76139414)

[3.3.2.1.6   
Virus Protection. 51](IECSA_VolumeIV_AppendixA.htm#_Toc76139415)

[3.3.2.2   User
and Group Account Management 51](IECSA_VolumeIV_AppendixA.htm#_Toc76139416)

[3.3.2.2.1   
Setting and Verifying User Accounts Service. 52](IECSA_VolumeIV_AppendixA.htm#_Toc76139417)

[4     
Protocol Specific Recommendations 53](IECSA_VolumeIV_AppendixA.htm#_Toc76139418)

[4.1   
Network Layer Technologies 53](IECSA_VolumeIV_AppendixA.htm#_Toc76139419)

[4.1.1   
IPv4. 53](IECSA_VolumeIV_AppendixA.htm#_Toc76139420)

[4.1.2   
IPv6. 53](IECSA_VolumeIV_AppendixA.htm#_Toc76139421)

[4.1.3   
Transport Layer Technologies (TCP) 53](IECSA_VolumeIV_AppendixA.htm#_Toc76139422)

[4.1.4   
Application Layer Protocols 53](IECSA_VolumeIV_AppendixA.htm#_Toc76139423)

[4.1.4.1   IEC
60870-5/DNP. 53](IECSA_VolumeIV_AppendixA.htm#_Toc76139424)

[4.1.4.2   IEC
60870-6 TASE.2 (ICCP) 53](IECSA_VolumeIV_AppendixA.htm#_Toc76139425)

[4.1.4.3   IEC
61850. 54](IECSA_VolumeIV_AppendixA.htm#_Toc76139426)

[4.1.4.4   Modbus 54](IECSA_VolumeIV_AppendixA.htm#_Toc76139427)

[5     
Security Service vs. IntelliGrid Architecture Quality of Service. 55](IECSA_VolumeIV_AppendixA.htm#_Toc76139428)

[5.1   
Security Impact on Availability. 55](IECSA_VolumeIV_AppendixA.htm#_Toc76139429)

[5.2   
Security and its impact on performance. 55](IECSA_VolumeIV_AppendixA.htm#_Toc76139430)

[5.2.1   
Four (4) msec Performance Metric. 56](IECSA_VolumeIV_AppendixA.htm#_Toc76139431)

[5.2.2   
Ten (10) msec Performance Metric. 56](IECSA_VolumeIV_AppendixA.htm#_Toc76139432)

[5.2.3   
One (1) second Performance Metric. 56](IECSA_VolumeIV_AppendixA.htm#_Toc76139433)

[5.2.3.1   Example: 
Security Across IntelliGrid Architecture Environments 56](IECSA_VolumeIV_AppendixA.htm#_Toc76139434)

[5.2.3.2   Example
of Security Domains 58](IECSA_VolumeIV_AppendixA.htm#_Toc76139435)

[5.2.3.3   Extending
the Example: Real Time Pricing. 62](IECSA_VolumeIV_AppendixA.htm#_Toc76139436)

[6     
Summary. 63](IECSA_VolumeIV_AppendixA.htm#_Toc76139437)

[6.1   
Major recommendations 63](IECSA_VolumeIV_AppendixA.htm#_Toc76139438)

[6.2   
Major Future Work. 64](IECSA_VolumeIV_AppendixA.htm#_Toc76139439)

[7     
Reference: Security documents 65](IECSA_VolumeIV_AppendixA.htm#_Toc76139440)

[7.1   
Security Practices - Frameworks and Policy Documents 65](IECSA_VolumeIV_AppendixA.htm#_Toc76139441)

[7.1.1   
ISO/IEC Security Effective Practices Documents 65](IECSA_VolumeIV_AppendixA.htm#_Toc76139442)

[7.1.1.1   ISO/IEC
10164-8:1993 Information technology -- Open Systems Interconnection -- Systems
Management: Security audit trail function. 65](IECSA_VolumeIV_AppendixA.htm#_Toc76139443)

[7.1.1.2   ISO/IEC
18014-1:2002 Information technology -- Security techniques -- Time-stamping
services -- Part 1: Framework. 65](IECSA_VolumeIV_AppendixA.htm#_Toc76139444)

[7.1.1.3   ISO/IEC
18014-2:2002  Information technology -- Security techniques --
Time-stamping services -- Part 2: Mechanisms producing independent tokens 65](IECSA_VolumeIV_AppendixA.htm#_Toc76139445)

[7.1.1.4   ISO/IEC
18014-3:2004 Information technology -- Security techniques -- Time-stamping
services -- Part 3: Mechanisms producing linked tokens 65](IECSA_VolumeIV_AppendixA.htm#_Toc76139446)

[7.1.1.5   ISO/IEC
10181-7:1996 Information technology -- Open Systems Interconnection -- Security
frameworks for open systems: Security audit and alarms framework  65](IECSA_VolumeIV_AppendixA.htm#_Toc76139447)

[7.1.1.6   ISO
JTC1 SC37 SD 2 - Harmonized Biometric Vocabulary. 66](IECSA_VolumeIV_AppendixA.htm#_Toc76139448)

[7.1.2   
Federal Security Best Practices Documents 66](IECSA_VolumeIV_AppendixA.htm#_Toc76139449)

[7.1.2.1   CICSI
6731.01 Global Command and Control System Security Policy. 66](IECSA_VolumeIV_AppendixA.htm#_Toc76139450)

[7.1.2.2   FIPS
PUB 112 Password Usage. 67](IECSA_VolumeIV_AppendixA.htm#_Toc76139451)

[7.1.2.3   FIPS
PUB 113 Computer Data Authentication. 67](IECSA_VolumeIV_AppendixA.htm#_Toc76139452)

[7.1.3   
IETF Security Best Practices Internet Requests for Comments (RFCs) 67](IECSA_VolumeIV_AppendixA.htm#_Toc76139453)

[7.1.3.1   RFC
1102 Policy routing in Internet protocols 67](IECSA_VolumeIV_AppendixA.htm#_Toc76139454)

[7.1.3.2   RFC
1322 A Unified Approach to Inter-Domain Routing. 67](IECSA_VolumeIV_AppendixA.htm#_Toc76139455)

[7.1.3.3   RFC
1351  SNMP Administrative Model 67](IECSA_VolumeIV_AppendixA.htm#_Toc76139456)

[7.1.3.4   RFC
2008 Implications of Various Address Allocation Policies for Internet Routing  67](IECSA_VolumeIV_AppendixA.htm#_Toc76139457)

[7.1.3.5   RFC
2196 Site Security Handbook. 67](IECSA_VolumeIV_AppendixA.htm#_Toc76139458)

[7.1.3.6   RFC
2276 Architectural Principles of Uniform Resource Name Resolution  69](IECSA_VolumeIV_AppendixA.htm#_Toc76139459)

[7.1.3.7   RFC
2350 Expectations for Computer Security Incident Response. 69](IECSA_VolumeIV_AppendixA.htm#_Toc76139460)

[7.1.3.8   RFC
2386 A Framework for QoS-based Routing in the Internet 69](IECSA_VolumeIV_AppendixA.htm#_Toc76139461)

[7.1.3.9   RFC
2401 Security Architecture for the Internet Protocol 69](IECSA_VolumeIV_AppendixA.htm#_Toc76139462)

[7.1.3.10  RFC
2505 Anti-Spam Recommendations for SMTP MTAs 69](IECSA_VolumeIV_AppendixA.htm#_Toc76139463)

[7.1.3.11  RFC
2518 HTTP Extensions for Distributed Authoring -- WEBDAV.
69](IECSA_VolumeIV_AppendixA.htm#_Toc76139464)

[7.1.3.12  RFC
2527 Internet X.509 Public Key Infrastructure Certificate Policy and
Certification Practices Framework. 69](IECSA_VolumeIV_AppendixA.htm#_Toc76139465)

[7.1.3.13  RFC
2725 Routing Policy System Security. 71](IECSA_VolumeIV_AppendixA.htm#_Toc76139466)

[7.1.3.14  RFC
2775 Internet Transparency. 71](IECSA_VolumeIV_AppendixA.htm#_Toc76139467)

[7.1.3.15  RFC
2993 Architectural Implications of NAT. 71](IECSA_VolumeIV_AppendixA.htm#_Toc76139468)

[7.1.3.16  RFC
3411 An Architecture for Describing Simple Network Management Protocol (SNMP)
Management Frameworks 71](IECSA_VolumeIV_AppendixA.htm#_Toc76139469)

[7.1.4   
Other Security Best Practices Documents 71](IECSA_VolumeIV_AppendixA.htm#_Toc76139470)

[7.1.4.1   21
CFR Part 11 Guidance for Industry Part 11, Electronic Records; Electronic
Signatures - Scope and Application. 71](IECSA_VolumeIV_AppendixA.htm#_Toc76139471)

[7.1.4.2   ISA-99
Integrating Electronic Security into the Manufacturing and Control Systems
Environment 71](IECSA_VolumeIV_AppendixA.htm#_Toc76139472)

[7.1.4.3   EPRI
100898 Scoping Study on Security Processes and Impacts 71](IECSA_VolumeIV_AppendixA.htm#_Toc76139473)

[7.1.4.4   EPRI
100174 Communication Security Assessment for the United States Electric Utility
Infrastructure. 71](IECSA_VolumeIV_AppendixA.htm#_Toc76139474)

[7.1.4.5   NIST
SP 500-166 Computer Viruses and Related Threats: A Management Guide  72](IECSA_VolumeIV_AppendixA.htm#_Toc76139475)

[7.1.4.6   Radius
Protocol Security and Best Practices 72](IECSA_VolumeIV_AppendixA.htm#_Toc76139476)

[7.2   
Security Technologies 72](IECSA_VolumeIV_AppendixA.htm#_Toc76139477)

[7.2.1   
ISO/IEC Documents on Security Technologies 72](IECSA_VolumeIV_AppendixA.htm#_Toc76139478)

[7.2.1.1   IEC
62351-3 Security for Profiles including TCP/IP. 72](IECSA_VolumeIV_AppendixA.htm#_Toc76139479)

[7.2.1.2   IEC
62351-4 Security for Profiles including MMS (ISO-9506) 72](IECSA_VolumeIV_AppendixA.htm#_Toc76139480)

[7.2.1.3   IEC
62351-5 Security for IEC 60870-5 and Derivatives 72](IECSA_VolumeIV_AppendixA.htm#_Toc76139481)

[7.2.1.4   IEC
62351-6 Security for IEC 61850 Profiles 72](IECSA_VolumeIV_AppendixA.htm#_Toc76139482)

[7.2.1.5   IEC
62351-7 Objects for Network Management 72](IECSA_VolumeIV_AppendixA.htm#_Toc76139483)

[7.2.1.6   ISO/IEC
7816-1:1998 Identification cards -- Integrated circuit(s) cards with contacts
-- Part 1: Physical characteristics 72](IECSA_VolumeIV_AppendixA.htm#_Toc76139484)

[7.2.1.7   ISO/IEC
7816-3:1997 Information technology -- Identification cards -- Integrated
circuit(s) cards with contacts -- Part 3: Electronic signals and transmission
protocols 72](IECSA_VolumeIV_AppendixA.htm#_Toc76139485)

[7.2.1.8   ISO/IEC
7816-3:1997/Amd 1:2002 Electrical characteristics and class indication for
integrated circuit(s) cards operating at 5 V, 3 V and 1,8 V. 72](IECSA_VolumeIV_AppendixA.htm#_Toc76139486)

[7.2.1.9   ISO/IEC
7816-4:1995  Information technology -- Identification cards -- Integrated
circuit(s) cards with contacts -- Part 4: Inter-industry commands for
interchange  72](IECSA_VolumeIV_AppendixA.htm#_Toc76139487)

[7.2.1.10  ISO/IEC
7816-4:1995/Amd 1:1997  secure messaging on the structures of APDU
messages 73](IECSA_VolumeIV_AppendixA.htm#_Toc76139488)

[7.2.1.11  ISO/IEC
7816-5:1994  Identification cards -- Integrated circuit(s) cards with contacts
-- Part 5: Numbering system and registration procedure for application
identifiers 73](IECSA_VolumeIV_AppendixA.htm#_Toc76139489)

[7.2.1.12  ISO/IEC
7816-7:1999 Identification cards -- Integrated circuit(s) cards with contacts
-- Part 7: Interindustry commands for Structured Card
Query Language (SCQL) 73](IECSA_VolumeIV_AppendixA.htm#_Toc76139490)

[7.2.1.13  ISO/IEC
7816-8:1999   Identification cards -- Integrated circuit(s) cards
with contacts -- Part 8: Security related interindustry
commands 73](IECSA_VolumeIV_AppendixA.htm#_Toc76139491)

[7.2.1.14  ISO/IEC
7816-9:2000   Identification cards -- Integrated circuit(s) cards
with contacts -- Part 9: Additional interindustry
commands and security attributes 73](IECSA_VolumeIV_AppendixA.htm#_Toc76139492)

[7.2.1.15  ISO/IEC
7816-10:1999   Identification cards -- Integrated circuit(s) cards
with contacts -- Part 10: Electronic signals and answer to reset for
synchronous cards 73](IECSA_VolumeIV_AppendixA.htm#_Toc76139493)

[7.2.1.16  ISO/IEC
7816-11:2004 Identification cards -- Integrated circuit cards -- Part 11:
Personal verification through biometric methods 73](IECSA_VolumeIV_AppendixA.htm#_Toc76139494)

[7.2.1.17  ISO/IEC
7816-15:2004  Identification cards -- Integrated circuit cards with
contacts -- Part 15: Cryptographic information application. 74](IECSA_VolumeIV_AppendixA.htm#_Toc76139495)

[7.2.1.18  ISO
9735-9:2002   Electronic data interchange for administration,
commerce and transport (EDIFACT) -- Application level syntax rules (Syntax
version number: 4, Syntax release number: 1) -- Part 9: Security key and
certificate management message (message type- KEYMAN) 74](IECSA_VolumeIV_AppendixA.htm#_Toc76139496)

[7.2.1.19  ISO/IEC
9594-8:1998 Information technology -- Open Systems Interconnection -- The
Directory: Authentication framework. 74](IECSA_VolumeIV_AppendixA.htm#_Toc76139497)

[7.2.1.20  ISO/IEC
9594-8:2001 Information technology -- Open Systems Interconnection -- The
Directory: Public-key and attribute certificate frameworks 74](IECSA_VolumeIV_AppendixA.htm#_Toc76139498)

[7.2.1.21  ISO
9735-5:2002 Electronic data interchange for administration, commerce and
transport (EDIFACT) -- Application level syntax rules (Syntax version number:
4, Syntax release number: 1) -- Part 5: Security rules for batch EDI
(authenticity, integrity and nn-repudiation of
origin) 74](IECSA_VolumeIV_AppendixA.htm#_Toc76139499)

[7.2.1.22  ISO/IEC
10164-9:1995 Information technology -- Open Systems Interconnection -- Systems
Management: Objects and attributes for access control 74](IECSA_VolumeIV_AppendixA.htm#_Toc76139500)

[7.2.1.23  ISO/IEC
10181-1:1996 Information technology -- Open Systems Interconnection -- Security
frameworks for open systems: Overview.. 75](IECSA_VolumeIV_AppendixA.htm#_Toc76139501)

[7.2.1.24  ISO/IEC
10181-2:1996  Information technology -- Open Systems Interconnection -- Security
frameworks for open systems: Authentication framework. 75](IECSA_VolumeIV_AppendixA.htm#_Toc76139502)

[7.2.1.25  ISO/IEC
10181-3:1996 Information technology -- Open Systems Interconnection -- Security
frameworks for open systems: Access control framework. 75](IECSA_VolumeIV_AppendixA.htm#_Toc76139503)

[7.2.1.26  ISO/IEC
10181-4:1997 Information technology -- Open Systems Interconnection -- Security
frameworks for open systems: Non-repudiation framework. 76](IECSA_VolumeIV_AppendixA.htm#_Toc76139504)

[7.2.1.27  ISO
10202-1:1991 Financial transaction cards -- Security architecture of financial
transaction systems using integrated circuit cards -- Part 1: Card life cycle  76](IECSA_VolumeIV_AppendixA.htm#_Toc76139505)

[7.2.1.28  ISO
10202-7:1998 Financial transaction cards -- Security architecture of financial
transaction systems using integrated circuit cards -- Part 7: Key management 76](IECSA_VolumeIV_AppendixA.htm#_Toc76139506)

[7.2.1.29  ISO
10202-8:1998 Financial transaction cards -- Security architecture of financial
transaction systems 77](IECSA_VolumeIV_AppendixA.htm#_Toc76139507)

[7.2.1.30  ISO/IEC
TR 13335-1:1996 Information technology -- Guidelines for the management of IT
Security -- Part 1: Concepts and models for IT Security  78](IECSA_VolumeIV_AppendixA.htm#_Toc76139508)

[7.2.1.31  ISO/IEC
TR 13335-2:1997 Information technology -- Guidelines for the management of IT
Security -- Part 2: Managing and planning IT Security  78](IECSA_VolumeIV_AppendixA.htm#_Toc76139509)

[7.2.1.32  ISO/IEC
TR 13335-5 Information technology - Guidelines for the management of IT
Security - Part 5: Management guidance on network security. 78](IECSA_VolumeIV_AppendixA.htm#_Toc76139510)

[7.2.1.33  ISO/IEC
13888-1:1997 Information technology -- Security techniques -- Non-repudiation
-- Part 1: General 79](IECSA_VolumeIV_AppendixA.htm#_Toc76139511)

[7.2.1.34  ISO/IEC
13888-2:1998 Information technology -- Security techniques -- Non-repudiation
-- Part 2: Mechanisms using symmetric techniques 79](IECSA_VolumeIV_AppendixA.htm#_Toc76139512)

[7.2.1.35  ISO/IEC
13888-3:1997 Information technology -- Security techniques -- Non-repudiation
-- Part 3: Mechanisms using asymmetric techniques 79](IECSA_VolumeIV_AppendixA.htm#_Toc76139513)

[7.2.1.36  ISO/IEC
15408-1:1999 Information technology -- Security techniques -- Evaluation
criteria for IT security -- Part 1: Introduction and general mode  79](IECSA_VolumeIV_AppendixA.htm#_Toc76139514)

[7.2.1.37  ISO/IEC
15408-2:1999 Information technology -- Security techniques -- Evaluation
criteria for IT security -- Part 2: Security functional requirements 81](IECSA_VolumeIV_AppendixA.htm#_Toc76139515)

[7.2.1.38  ISO/IEC
15408-3:1999 Information technology -- Security techniques -- Evaluation
criteria for IT security -- Part 3: Security assurance requirements 81](IECSA_VolumeIV_AppendixA.htm#_Toc76139516)

[7.2.1.39  ISO/IEC
17799:2000  Information technology -- Code of practice for information
security management 81](IECSA_VolumeIV_AppendixA.htm#_Toc76139517)

[7.2.1.40  ISO
JTC1 SC37 1.37.19784.1 BioAPI - Biometric Application
Programming Interface. 81](IECSA_VolumeIV_AppendixA.htm#_Toc76139518)

[7.2.1.41  ISO
JTC1 SC37 1.37.19794 - Biometric Data Interchange Format
81](IECSA_VolumeIV_AppendixA.htm#_Toc76139519)

[7.2.1.42  ISO
JTC1 SC37 1.37.19794.3 Biometric Data Interchange Format - Part 3: Finger
Pattern Spectral Data. 81](IECSA_VolumeIV_AppendixA.htm#_Toc76139520)

[7.2.1.43  ISO
JTC1 SC37 1.37.19794.4 Biometric Data Interchange Format - Part 4: Finger Image
Data. 81](IECSA_VolumeIV_AppendixA.htm#_Toc76139521)

[7.2.1.44  ISO
JTC1 SC37 1.37.1974.5 Biometric Data Interchange Format - Part 5: Face Image
Data. 82](IECSA_VolumeIV_AppendixA.htm#_Toc76139522)

[7.2.2   
Federal Documents on Security Technologies 82](IECSA_VolumeIV_AppendixA.htm#_Toc76139523)

[7.2.2.1   FIPS
197 Federal Information Processing Standards Publication 197, Specification for
the Advanced Encryption Standard (AES) 82](IECSA_VolumeIV_AppendixA.htm#_Toc76139524)

[7.2.3   
IETF Internet Requests for Comments (RFCs) on Security Technologies 82](IECSA_VolumeIV_AppendixA.htm#_Toc76139525)

[7.2.3.1   STD
13 Domain Name System.. 82](IECSA_VolumeIV_AppendixA.htm#_Toc76139526)

[7.2.3.2   RFC
1004 Distributed-protocol authentication scheme. 82](IECSA_VolumeIV_AppendixA.htm#_Toc76139527)

[7.2.3.3   RFC
1013 X Window System Protocol, version 11: Alpha update April 1987  82](IECSA_VolumeIV_AppendixA.htm#_Toc76139528)

[7.2.3.4   RFC
1034 Domain names - concepts and facilities 82](IECSA_VolumeIV_AppendixA.htm#_Toc76139529)

[7.2.3.5   RFC
1040 Privacy enhancement for Internet electronic mail: Part I: Message encipherment and authentication. 82](IECSA_VolumeIV_AppendixA.htm#_Toc76139530)

[7.2.3.6   RFC
1423 Privacy Enhancement for Internet Electronic Mail: Part III: Algorithms,
Modes, and Identifiers 82](IECSA_VolumeIV_AppendixA.htm#_Toc76139531)

[7.2.3.7   RFC
1221 Host Access Protocol (HAP) Specification - Version 2. 83](IECSA_VolumeIV_AppendixA.htm#_Toc76139532)

[7.2.3.8   RFC
1305 Network Time Protocol (Version 3) Specification, Implementation  83](IECSA_VolumeIV_AppendixA.htm#_Toc76139533)

[7.2.3.9   RFC
1352  SNMP Security Protocols 83](IECSA_VolumeIV_AppendixA.htm#_Toc76139534)

[7.2.3.10  RFC
1507 DASS - Distributed Authentication Security Service. 83](IECSA_VolumeIV_AppendixA.htm#_Toc76139535)

[7.2.3.11  RFC
1579 Firewall-Friendly FTP. 83](IECSA_VolumeIV_AppendixA.htm#_Toc76139536)

[7.2.3.12  RFC
1591 Domain Name System Structure and Delegation. 83](IECSA_VolumeIV_AppendixA.htm#_Toc76139537)

[7.2.3.13  RFC
1608 Representing IP Information in the X.500 Directory. 84](IECSA_VolumeIV_AppendixA.htm#_Toc76139538)

[7.2.3.14  RFC
1612 DNS Resolver MIB Extensions 84](IECSA_VolumeIV_AppendixA.htm#_Toc76139539)

[7.2.3.15  RFC
1826 IP Authentication Header 84](IECSA_VolumeIV_AppendixA.htm#_Toc76139540)

[7.2.3.16  RFC
1827 IP Encapsulating Security Payload (ESP) 84](IECSA_VolumeIV_AppendixA.htm#_Toc76139541)

[7.2.3.17  RFC
1919 Classical versus Transparent IP Proxies 84](IECSA_VolumeIV_AppendixA.htm#_Toc76139542)

[7.2.3.18  RFC
1940 Source Demand Routing: Packet Format and Forwarding Specification (Version
1) 84](IECSA_VolumeIV_AppendixA.htm#_Toc76139543)

[7.2.3.19  RFC
1968 The PPP Encryption Control Protocol (ECP) 85](IECSA_VolumeIV_AppendixA.htm#_Toc76139544)

[7.2.3.20  RFC
2040 The RC5, RC5-CBC, RC5-CBC-Pad, and RC5-CTS Algorithms 86](IECSA_VolumeIV_AppendixA.htm#_Toc76139545)

[7.2.3.21  RFC
2045 Multi-Purpose Internet Mail Extensions (MIME) and Secure/MIME  86](IECSA_VolumeIV_AppendixA.htm#_Toc76139546)

[7.2.3.22  RFC
2086 IMAP4 ACL extension. 86](IECSA_VolumeIV_AppendixA.htm#_Toc76139547)

[7.2.3.23  RFC
2093 Group Key Management Protocol (GKMP) Specification. 86](IECSA_VolumeIV_AppendixA.htm#_Toc76139548)

[7.2.3.24  RFC
2228 FTP Security Extensions 86](IECSA_VolumeIV_AppendixA.htm#_Toc76139549)

[7.2.3.25  RFC
2230 Key Exchange Delegation Record for the DNS. 86](IECSA_VolumeIV_AppendixA.htm#_Toc76139550)

[7.2.3.26  RFC
2244 ACAP -- Application Configuration Access Protocol 86](IECSA_VolumeIV_AppendixA.htm#_Toc76139551)

[7.2.3.27  RFC
2246 The TLS Protocol Version 1.0. 86](IECSA_VolumeIV_AppendixA.htm#_Toc76139552)

[7.2.3.28  RFC
2313 PKCS #1: RSA Encryption Version 1.5. 88](IECSA_VolumeIV_AppendixA.htm#_Toc76139553)

[7.2.3.29  RFC
2315 PKCS #7: Cryptographic Message Syntax Version 1.5. 88](IECSA_VolumeIV_AppendixA.htm#_Toc76139554)

[7.2.3.30  RFC
2356 Sun's SKIP Firewall Traversal for Mobile IP. 88](IECSA_VolumeIV_AppendixA.htm#_Toc76139555)

[7.2.3.31  RFC
2406 IP Encapsulating Security Payload (ESP) 88](IECSA_VolumeIV_AppendixA.htm#_Toc76139556)

[7.2.3.32  RFC
2437 PKCS #1: RSA Cryptography Specifications Version 2.0. 88](IECSA_VolumeIV_AppendixA.htm#_Toc76139557)

[7.2.3.33  RFC
2440 OpenPGP Message Format 88](IECSA_VolumeIV_AppendixA.htm#_Toc76139558)

[7.2.3.34  RFC
2408 Internet Security Association and Key Management Protocol (ISAKMP) 89](IECSA_VolumeIV_AppendixA.htm#_Toc76139559)

[7.2.3.35  RFC
2409 The Internet Key Exchange (IKE) 89](IECSA_VolumeIV_AppendixA.htm#_Toc76139560)

[7.2.3.36  RFC
2459 Internet X.509 Public Key Infrastructure Certificate and CRL Profile  89](IECSA_VolumeIV_AppendixA.htm#_Toc76139561)

[7.2.3.37  RFC
2510 Internet X.509 Public Key Infrastructure Certificate Management Protocols 90](IECSA_VolumeIV_AppendixA.htm#_Toc76139562)

[7.2.3.38  RFC
2511 Internet X.509 Certificate Request Message Format 90](IECSA_VolumeIV_AppendixA.htm#_Toc76139563)

[7.2.3.39  RFC
2527 Internet X.509 Public Key Infrastructure Certificate Policy and
Certification Practices Framework. 90](IECSA_VolumeIV_AppendixA.htm#_Toc76139564)

[7.2.3.40  RFC
2535 Domain Name System Security Extensions 90](IECSA_VolumeIV_AppendixA.htm#_Toc76139565)

[7.2.3.41  RFC
2543 SIP: Session Initiation Protocol 90](IECSA_VolumeIV_AppendixA.htm#_Toc76139566)

[7.2.3.42  RFC
2547 BGP/MPLS VPNs 90](IECSA_VolumeIV_AppendixA.htm#_Toc76139567)

[7.2.3.43  RFC
2560 X.509 Internet Public Key Infrastructure Online Certificate Status
Protocol - OCSP. 90](IECSA_VolumeIV_AppendixA.htm#_Toc76139568)

[7.2.3.44  RFC
2592 Definitions of Managed Objects for the Delegation of Management Script 90](IECSA_VolumeIV_AppendixA.htm#_Toc76139569)

[7.2.3.45  RFC
2744 Generic Security Service API Version 2 : C-bindings
90](IECSA_VolumeIV_AppendixA.htm#_Toc76139570)

[7.2.3.46  RFC
2764 A Framework for IP Based Virtual Private Networks 91](IECSA_VolumeIV_AppendixA.htm#_Toc76139571)

[7.2.3.47  RFC
2753 A Framework for Policy-based Admission Control 91](IECSA_VolumeIV_AppendixA.htm#_Toc76139572)

[7.2.3.48  RFC
2797 Certificate Management Messages over CMS. 91](IECSA_VolumeIV_AppendixA.htm#_Toc76139573)

[7.2.3.49  RFC
2817 Certificate Management Messages over CMS. 91](IECSA_VolumeIV_AppendixA.htm#_Toc76139574)

[7.2.3.50  RFC
2818 HTTP over TLS. 91](IECSA_VolumeIV_AppendixA.htm#_Toc76139575)

[7.2.3.51  RFC
2820 Access Control Requirements for LDAP. 91](IECSA_VolumeIV_AppendixA.htm#_Toc76139576)

[7.2.3.52  RFC
2865 Remote Authentication Dial In User Service (RADIUS)
91](IECSA_VolumeIV_AppendixA.htm#_Toc76139577)

[7.2.3.53  RFC
2869 RADIUS Extensions 91](IECSA_VolumeIV_AppendixA.htm#_Toc76139578)

[7.2.3.54  RFC
2874 DNS Extensions to Support IPv6 Address Aggregation and Renumbering. 91](IECSA_VolumeIV_AppendixA.htm#_Toc76139579)

[7.2.3.55  RFC
2875 Diffie-Hellman Proof-of-Possession Algorithms 92](IECSA_VolumeIV_AppendixA.htm#_Toc76139580)

[7.2.3.56  RFC
2888 Secure Remote Access with L2TP. 92](IECSA_VolumeIV_AppendixA.htm#_Toc76139581)

[7.2.3.57  RFC
2898 PKCS #5: Password-Based Cryptography Specification Version 2.0  92](IECSA_VolumeIV_AppendixA.htm#_Toc76139582)

[7.2.3.58  RFC
2946 Telnet Data Encryption Option. 92](IECSA_VolumeIV_AppendixA.htm#_Toc76139583)

[7.2.3.59  RFC
2977 Mobile IP Authentication, Authorization, and Accounting Requirements 92](IECSA_VolumeIV_AppendixA.htm#_Toc76139584)

[7.2.3.60  RFC
2979 Behavior of and Requirements for Internet Firewalls
92](IECSA_VolumeIV_AppendixA.htm#_Toc76139585)

[7.2.3.61  RFC
2985 PKCS #9: Selected Object Classes and Attribute Types Version 2.0  92](IECSA_VolumeIV_AppendixA.htm#_Toc76139586)

[7.2.3.62  RFC
2986 PKCS #10: Certification Request Syntax Specification Version 1.7  92](IECSA_VolumeIV_AppendixA.htm#_Toc76139587)

[7.2.3.63  RFC
3053 IPv6 Tunnel Broker 92](IECSA_VolumeIV_AppendixA.htm#_Toc76139588)

[7.2.3.64  RFC
3268 Advanced Encryption Standard (AES) Ciphersuites
for Transport Layer Security (TLS) 94](IECSA_VolumeIV_AppendixA.htm#_Toc76139589)

[7.2.3.65  RFC
3280 Algorithms and Identifiers for the Internet X.509 Public Key
Infrastructure  Certificate and Certificate Revocation List (CRL) Profile. 94](IECSA_VolumeIV_AppendixA.htm#_Toc76139590)

[7.2.3.66  RFC
3369 Cryptographic Message Syntax (CMS) 94](IECSA_VolumeIV_AppendixA.htm#_Toc76139591)

[7.2.3.67  RFC
3370 Cryptographic Message Syntax (CMS) Algorithms 94](IECSA_VolumeIV_AppendixA.htm#_Toc76139592)

[7.2.3.68  RFC
3401 Dynamic Delegation Discovery System (DDDS) Part One: The Comprehensive
DDDS. 94](IECSA_VolumeIV_AppendixA.htm#_Toc76139593)

[7.2.3.69  RFC
3402 Dynamic Delegation Discovery System (DDDS) Part Two: The Algorithm.. 95](IECSA_VolumeIV_AppendixA.htm#_Toc76139594)

[7.2.3.70  RFC
3403 Dynamic Delegation Discovery System (DDDS) Part Three: The Domain Name
System (DNS) Database. 95](IECSA_VolumeIV_AppendixA.htm#_Toc76139595)

[7.2.3.71  RFC
3404 Dynamic Delegation Discovery System (DDDS) Part Four: The Uniform Resource
Identifiers (URI) 95](IECSA_VolumeIV_AppendixA.htm#_Toc76139596)

[7.2.3.72  RFC
3405 Dynamic Delegation Discovery System (DDDS) Part Five: URI.ARPA Assignment
Procedures 95](IECSA_VolumeIV_AppendixA.htm#_Toc76139597)

[7.2.3.73  RFC
3447 Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography
Specifications Version 2.1. 95](IECSA_VolumeIV_AppendixA.htm#_Toc76139598)

[7.2.3.74  RFC
3647 Internet X.509 Public Key Infrastructure Certificate Policy and
Certification Practices Framework. 95](IECSA_VolumeIV_AppendixA.htm#_Toc76139599)

[7.2.3.75  RFC
3761 The E.164 to Uniform Resource Identifiers (URI) Dynamic Delegation
Discovery System (DDDS) Application (ENUM) 95](IECSA_VolumeIV_AppendixA.htm#_Toc76139600)

[7.2.4   
Other Security Technology Documents 95](IECSA_VolumeIV_AppendixA.htm#_Toc76139601)

[7.2.4.1   IEEE
Documents on Security Technologies 95](IECSA_VolumeIV_AppendixA.htm#_Toc76139602)

[7.2.4.1.1   
IEEE 802.11b Web Encryption Protocol 95](IECSA_VolumeIV_AppendixA.htm#_Toc76139603)

[7.2.4.1.2   
IEEE 802.11i Security for Wireless Networks (WPA2) 96](IECSA_VolumeIV_AppendixA.htm#_Toc76139604)

[7.2.4.1.3   
IEEE Personal and Private Information (PAPI) draft standard. 96](IECSA_VolumeIV_AppendixA.htm#_Toc76139605)

[7.2.4.2   RSA
Documents on Security Technologies 96](IECSA_VolumeIV_AppendixA.htm#_Toc76139606)

[7.2.4.2.1   
RSA PKCS #8 Private-Key Information Syntax Standard. 96](IECSA_VolumeIV_AppendixA.htm#_Toc76139607)

[7.2.4.2.2   
RSA PKCS #12 Personal Information Exchange Syntax Standard, version 1.0. 96](IECSA_VolumeIV_AppendixA.htm#_Toc76139608)

[7.2.4.3   OASIS
Documents on Security Technologies 96](IECSA_VolumeIV_AppendixA.htm#_Toc76139609)

[7.2.4.3.1   
Security for Grid Services 96](IECSA_VolumeIV_AppendixA.htm#_Toc76139610)

[7.2.4.3.2   
Attribute Profiles for SAML 2.0. 96](IECSA_VolumeIV_AppendixA.htm#_Toc76139611)

[7.2.4.3.3   
SAML 2.0: Security Assertion Markup Language Version 2.0. 96](IECSA_VolumeIV_AppendixA.htm#_Toc76139612)

[7.2.4.3.4   
OASIS Security Assertion Markup Language (SAML) V2.0. 96](IECSA_VolumeIV_AppendixA.htm#_Toc76139613)

[7.2.4.3.5   
Authentication Context 96](IECSA_VolumeIV_AppendixA.htm#_Toc76139614)

[7.2.4.3.6   
Web Services Policy Framework (WS-Policy) 97](IECSA_VolumeIV_AppendixA.htm#_Toc76139615)

[7.2.4.3.7   
Web Services Policy Assertions Language (WS-PolicyAssertions) 97](IECSA_VolumeIV_AppendixA.htm#_Toc76139616)

[7.2.4.3.8   
Web Services Policy Attachment (WS-PolicyAttachment) 97](IECSA_VolumeIV_AppendixA.htm#_Toc76139617)

[7.2.4.3.9   
OASIS Extensible Access Control Markup Language (XACML) 97](IECSA_VolumeIV_AppendixA.htm#_Toc76139618)

[7.2.4.4   World
Wide Web Consortium (W3C) Documents on Security Technologies 97](IECSA_VolumeIV_AppendixA.htm#_Toc76139619)

[7.2.4.4.1   
WC3 XML Key Management Specification (XKMS 2.0) Bindings 97](IECSA_VolumeIV_AppendixA.htm#_Toc76139620)

[7.2.4.4.2   
W3C The Platform for Privacy Preferences 1.1 (P3P1.1) SpecificationW3C
Working Draft 27 April 2004. 97](IECSA_VolumeIV_AppendixA.htm#_Toc76139621)

[7.2.4.5   Miscellaneous
Security Technologies 97](IECSA_VolumeIV_AppendixA.htm#_Toc76139622)

[7.2.4.5.1   
AGA-12 Cryptographic Protection of SCADA Communications General
Recommendations. 97](IECSA_VolumeIV_AppendixA.htm#_Toc76139623)

[7.2.4.5.2   
ANSI INCITS 359-2004 Role Based Access Control (RBAC) 97](IECSA_VolumeIV_AppendixA.htm#_Toc76139624)

[7.2.4.5.3   
BCP 65 Dynamic Delegation Discovery System (DDDS) Part Five: URI.ARPA
Assignment Procedures 98](IECSA_VolumeIV_AppendixA.htm#_Toc76139625)

[7.2.4.5.4   
EPRI 1002596 ICCP TASE.2 Security Enhancements 98](IECSA_VolumeIV_AppendixA.htm#_Toc76139626)

[7.2.4.5.5   
Java Card Java Card Platform Specification v 2.2.1. 98](IECSA_VolumeIV_AppendixA.htm#_Toc76139627)

[7.2.4.5.6   
NERC Certificate Policy for the Energy Market Access and Reliability
Certificate (e MARC) Program Version 2.4. 98](IECSA_VolumeIV_AppendixA.htm#_Toc76139628)

[7.2.4.5.7   
NIST GSC-IS The NIST Interagency Report 6887 - 2003 edition (Government
Smart Card-Interoperability Specification) Version 2.1  98](IECSA_VolumeIV_AppendixA.htm#_Toc76139629)

[7.2.4.5.8   
NISTIR 6529 Common Biometric File Format (CBEFF) 98](IECSA_VolumeIV_AppendixA.htm#_Toc76139630)

[7.2.4.5.9   
Semantic Web Pervasive Computing Standard Ontology (PERVASIVE-SO) Guide
-- Describing User Profile and Preferences 98](IECSA_VolumeIV_AppendixA.htm#_Toc76139631)

[7.2.4.5.10  Smart
Card Alliance Smart Card Primer 98](IECSA_VolumeIV_AppendixA.htm#_Toc76139632)

[7.2.4.5.11  Smart
Card Alliance Privacy and Secure Identification Systems: The Role of Smart
Cards as a Privacy-Enabling Technology. 99](IECSA_VolumeIV_AppendixA.htm#_Toc76139633)

[7.2.4.5.12  Smart
Card Alliance Government Smart Card Handbook. 99](IECSA_VolumeIV_AppendixA.htm#_Toc76139634)

[7.2.4.5.13  WebDAV Access Control Extensions to WebDAV. 99](IECSA_VolumeIV_AppendixA.htm#_Toc76139635)

[7.2.4.5.14  WPA
WI-FI Protected Access 99](IECSA_VolumeIV_AppendixA.htm#_Toc76139636)

[7.2.4.5.15  WPA2
WI-FI Protected Access Version 2. 99](IECSA_VolumeIV_AppendixA.htm#_Toc76139637)

[7.2.4.5.16  TMN
PKI - Digital certificates and certificate revocation lists profiles 99](IECSA_VolumeIV_AppendixA.htm#_Toc76139638)

**Table of Figures**

[Figure 1: General Security Process 2](IECSA_VolumeIV_AppendixA.htm#_Toc76139244)

[Figure 2: Representation of Security
Domain Concept 4](IECSA_VolumeIV_AppendixA.htm#_Toc76139245)

[Figure 3: Example of SSL/TLS Tunnel
for Firewall Transversal 27](IECSA_VolumeIV_AppendixA.htm#_Toc76139246)

[Figure 4: Estimated Smart Card Storage
Costs 31](IECSA_VolumeIV_AppendixA.htm#_Toc76139247)

[Figure 5: General trend is security
vulnerabilities (extracted from EPRI Report 1008988) 45](IECSA_VolumeIV_AppendixA.htm#_Toc76139248)

[Figure 6: Simplified diagram of
Public/Private Key encryption and Digital Signature. 46](IECSA_VolumeIV_AppendixA.htm#_Toc76139249)

[Figure 7: IntelliGrid Architecture Environments 57](IECSA_VolumeIV_AppendixA.htm#_Toc76139250)

[Figure 8: Example Security Domain
Choices 58](IECSA_VolumeIV_AppendixA.htm#_Toc76139251)

[Figure 9: Web Service based Customer
Interface Example. 61](IECSA_VolumeIV_AppendixA.htm#_Toc76139252)

[Figure 10: Alternate Architecture
that could allow direct 61850 communications 62](IECSA_VolumeIV_AppendixA.htm#_Toc76139253)

  

**Table of Tables**

[Table 1: Relating Security Processes
to Functions and Services 4](IECSA_VolumeIV_AppendixA.htm#_Toc76139254)

[Table 2: Relating Security Processes
to Functions and Services 5](IECSA_VolumeIV_AppendixA.htm#_Toc76139255)

[Table 3: Primary Services and the
additional Security Services required to implement 5](IECSA_VolumeIV_AppendixA.htm#_Toc76139256)

[Table 4: Services needed for
Intra/Inter Domain Security. 6](IECSA_VolumeIV_AppendixA.htm#_Toc76139257)

[Table 5: Relevant References in
regards to Audit processes 10](IECSA_VolumeIV_AppendixA.htm#_Toc76139258)

[Table 6: Relevant
Standards/Specifications relevant to the Audit Service. 10](IECSA_VolumeIV_AppendixA.htm#_Toc76139259)

[Table 7: Typical Physical Access
Control Strategies 12](IECSA_VolumeIV_AppendixA.htm#_Toc76139260)

[Table 8: Physical Security
Strategies vs. Security Services Provided. 14](IECSA_VolumeIV_AppendixA.htm#_Toc76139261)

[Table 9: References regarding
Computational Resource Access Control
16](IECSA_VolumeIV_AppendixA.htm#_Toc76139262)

[Table 10: Relevant Computational
Resource Access Control Standards/Specifications 16](IECSA_VolumeIV_AppendixA.htm#_Toc76139263)

[Table 11: References relating to
Access Control for Informational Resources 18](IECSA_VolumeIV_AppendixA.htm#_Toc76139264)

[Table 12: Reference Relevant to
Encryption Technology. 20](IECSA_VolumeIV_AppendixA.htm#_Toc76139265)

[Table 13: Encryption Related
Specifications/Standards 20](IECSA_VolumeIV_AppendixA.htm#_Toc76139266)

[Table 14: Digital Certificate
Related Specifications/Standards 21](IECSA_VolumeIV_AppendixA.htm#_Toc76139267)

[Table 15: References and
Specifications regarding Credential Conversion. 22](IECSA_VolumeIV_AppendixA.htm#_Toc76139268)

[Table 16: Relevant Specification
regarding Credential Renewal 25](IECSA_VolumeIV_AppendixA.htm#_Toc76139269)

[Table 17: Relevant Specifications
for the Delegation Service. 26](IECSA_VolumeIV_AppendixA.htm#_Toc76139270)

[Table 18: References regarding
Firewall Transversal 28](IECSA_VolumeIV_AppendixA.htm#_Toc76139271)

[Table 19: Relevant Specifications
regarding Firewall Transversal 28](IECSA_VolumeIV_AppendixA.htm#_Toc76139272)

[Table 20: General References
Regarding Identity Establishment and Identity Infrastructure. 29](IECSA_VolumeIV_AppendixA.htm#_Toc76139273)

[Table 21: Relevant Specifications
regarding Identification Frameworks 29](IECSA_VolumeIV_AppendixA.htm#_Toc76139274)

[Table 22: Relevant Standards
Concerning Smart Cards 30](IECSA_VolumeIV_AppendixA.htm#_Toc76139275)

[Table 23: Public Key Infrastructure
(PKI) Related Specification/Standards
31](IECSA_VolumeIV_AppendixA.htm#_Toc76139276)

[Table 24: Relevant Specifications
for Digital Signatures 32](IECSA_VolumeIV_AppendixA.htm#_Toc76139277)

[Table 25: Relevant References
regarding Biometrics 33](IECSA_VolumeIV_AppendixA.htm#_Toc76139278)

[Table 26: Relevant Specification
regarding Biometrics and Smart Cards 33](IECSA_VolumeIV_AppendixA.htm#_Toc76139279)

[Table 27: Relevant Technologies for
Web Based User Interfaces 34](IECSA_VolumeIV_AppendixA.htm#_Toc76139280)

[Table 28: Relevant Specification
regarding non-repudiation. 35](IECSA_VolumeIV_AppendixA.htm#_Toc76139281)

[Table 29: Relevant Specifications
for the Path Routing Service. 36](IECSA_VolumeIV_AppendixA.htm#_Toc76139282)

[Table 30: Relevant Specification
regarding Policy Exchange. 37](IECSA_VolumeIV_AppendixA.htm#_Toc76139283)

[Table 31: References Regarding
Privacy. 37](IECSA_VolumeIV_AppendixA.htm#_Toc76139284)

[Table 32: Relevant Specification
regarding Privacy. 39](IECSA_VolumeIV_AppendixA.htm#_Toc76139285)

[Table 33: Relevant Specifications
regarding the Profile Service. 39](IECSA_VolumeIV_AppendixA.htm#_Toc76139286)

[Table 34: References Relating to
Quality of Identity. 39](IECSA_VolumeIV_AppendixA.htm#_Toc76139287)

[Table 35: Relevant Specification for
the Quality of Idenity Service. 41](IECSA_VolumeIV_AppendixA.htm#_Toc76139288)

[Table 36: Relevant Specifications
regarding Denial-of-Service. 42](IECSA_VolumeIV_AppendixA.htm#_Toc76139289)

[Table 37: Relevant Specifications
regarding Security Assurance. 42](IECSA_VolumeIV_AppendixA.htm#_Toc76139290)

[Table 38: Potentially Relevant
Specifications in regards to Security Capability Discovery. 43](IECSA_VolumeIV_AppendixA.htm#_Toc76139291)

[Table 39: Relevant Information
regarding Trust Establishment 43](IECSA_VolumeIV_AppendixA.htm#_Toc76139292)

[Table 40: References regarding
Intrusion Detection. 48](IECSA_VolumeIV_AppendixA.htm#_Toc76139293)

[Table 41: Recommended Minimum
Password size. 51](IECSA_VolumeIV_AppendixA.htm#_Toc76139294)

[Table 42: Relevant Articles
concerning User and Group Account Management 51](IECSA_VolumeIV_AppendixA.htm#_Toc76139295)

[Table 43: Summary of IntelliGrid Architecture QOS
Requirements 55](IECSA_VolumeIV_AppendixA.htm#_Toc76139296)

[Table 44: Summary of Example Communication
Technologies 59](IECSA_VolumeIV_AppendixA.htm#_Toc76139297)

[Table 45: Example Certificate and
Certificate Exchange choices 59](IECSA_VolumeIV_AppendixA.htm#_Toc76139298)

[Table 46: Example Confidentiality. 60](IECSA_VolumeIV_AppendixA.htm#_Toc76139299)

[Table 47: Suggested Roles vs.
Privileges 61](IECSA_VolumeIV_AppendixA.htm#_Toc76139300)

  

# Security Overview

## Security Concerns

Security is an issue that several industries and most
businesses are attempting to come to terms with. However, the implementation of
a robust security infrastructure often appears to be a daunting and
overwhelming task.  This can be attributed to several factors:

### There is no defined mechanism to decompose the security problem space and therefore it is perceived to be an impossible task.

Typically there are two major discussion/analysis methods
in regards to security: Enterprise based analysis and/or Technology/Threat
based analysis.  There are obvious pitfalls to both approaches.  The
instantiation of an Enterprise is continuously evolving/changing
and may encompass more than one business entity where a single set of security
policies and technologies cannot be enforced[[1]](IECSA_VolumeIV_AppendixA.htm#_ftn1). Thus any security decisions require a
large amount of coordination and tend to make the security process frustrating.

However, the security problem can be decomposed into
smaller regions of security analysis/management.  This is the “Security
Domain” concept that this appendix introduces on page 3).  This allows a
set of resources to be managed (from a security perspective) independently.

However, this raises the issue of how to provide a
security mechanism for inter-domain exchanges.  To solve this issue, the
appendix introduces several abstract security services that may be bound to
different security technologies.

The technology only based analysis approach could be
classified as flawed from the outset.  Since security is an ongoing and
evolving process, selection of security based upon today’s technology may
prevent adopting more advanced security technologies in the future.  This
appendix introduces a set of abstract security services that can be mapped to
current or future technologies, in order to resolve this analysis dilemma.

### There may be a lack of understanding in regards to the importance of a security policy and a commitment to implement that policy.

The first problem that is typically encountered is that
Enterprise policy development is overwhelming (see the previous
discussion).  However, the use of the Security Domain concept should help
mitigate this issue.  Nonetheless, the use of the Security Domain concept
means that the domains need to be identified and then the policy needs to be
developed for the domains.

The second issue is there is typically a lack of
understanding of what constitutes a security policy.  In particular, the
policy must address the entire suite of security processes, security functions,
security services, and security management.

The third issue, and typically most daunting, is how to
decide what needs to be secured within the security policy.  Some contend
that every asset needs to be secured.  However, this approach makes
security deployment/adoption costly and could prevent entities from even
attempting to deploy security.

Therefore, **all assets do not need to be secured**,
although all assets *could* be secured.  However, **all assets
should be analyzed in regards to the need of security**.

Thus the issue is raised of the type of analysis that
should be performed. This appendix recommends that a risk assessment approach to
the analysis be taken. The appendix discusses risk analysis at a high level and
then references emerging work regarding risk assessment are given instead of
embedding the intellectual content.

Therefore, Security Policies are a key security service
that should be performed in advance of any security deployment.  This is
discussed in greater detail under the Technical Analysis of Security.

### There has been no authoritative work in regards to defining abstract security services.

IntelliGrid Architecture defines several abstract security services that are
relevant to implementing inter-domain and intra-domain security.  However,
the appendix also identifies that some of the abstract services have no
deployment technologies that can be used to implement the security service. 
The appendix does attempt to define what emerging standards could be used/modified in order to allow the security service to
actually be instantiated.

In regards to abstract security service definitions, those
described in these IntelliGrid Architecture documents should be viewed as a starting point from
which future work can evolve.

### There is typically a lack of understanding in regards to the impact of security on communication requirements.  This is due in large part to the lack of communication/infrastructure requirement definition.

Other IntelliGrid Architecture documents discuss the system requirements from
a communication and user environment perspective.  The security
services/technologies recommended by IntelliGrid Architecture have be correlated and analyzed
against these IntelliGrid Architecture requirements and the power system functions.  Thus,
IntelliGrid Architecture documentation set should ease the identification of impact and aid in
the selection of the appropriate security service and technology.

## Security Processes

Protection and securing of networked communications,
intelligent equipment, and the data and information that are vital to the
operation of the future energy system is one of the key drivers behind
developing an industry-level architecture.  Cyber security faces
substantial challenges both institutional and technical.  The IntelliGrid Architecture
documents serve to provide context to this complex topic as well as providing a
pathway by which the industry can work to develop a robust portfolio of
technologies to meet the critical issues that encompass security.

Security of the energy and communications systems
addressed by IntelliGrid Architecture faces multiple challenges from the following major trends:

·       Need for
greater levels of integration with a variety of business entities

·       Increased
use of open systems based infrastructures that will  comprise the future
energy system

·       The need
for appropriate integration of existing or “legacy” systems with future systems

·       Growing
sophistication and complexity of integrated distributed computing systems

·       Growing
sophistication and threats from hostile communities

if !vml?![](IECSA_VolumeIV_AppendixA_files/image002.jpg)endif?

Security must be planned and designed into systems from
the start.  Security functions are integral to the designs of systems.
Planning for security, in advance of deployment, will provide a more complete
and cost effective solution.  Additionally, advanced planning will ensure
that security services are supportable (may be cost prohibitive to retrofit
into non-planned environments.  This means that security needs to be
addressed at all levels of the architecture.

Figure1: General Security
Process

Security is a ever evolving process and is not
static.  It takes continual work and education to help the security
processes keep up with the demands that will be placed on the systems. 
Security will continue to be a race between corporate security
policies/security infrastructure and hostile entities.  The security
processes and systems will continue to evolve in the future.  By
definition there are no communication connected systems that are 100%
secure.  There will be always be residual risks that must be taken into
account and managed. 

The normal thought process in regards to security. 
It accurately reflects that the security process is a never-ending
process.  Thus, in order to maintain security constant vigilance and monitoring
is needed as well as adaptation to changes in the overall environment. The
process depicts five (5) high level processes that are needed as part of a
robust security strategy.  Although circular in nature, there is a
definite order to the process:

**Security Assessment** – Security assessment is the
process of assessing assets for their security requirements, based on probable
risks of attack, liability related to successful attacks, and costs for
ameliorating the risks and liabilities. The recommendations stemming from the
security requirements analysis leads to the creation of security policies, the
procurement of security-related products and services, and the implementation
of security procedures.

The implication of the circular process is that a security
re-assessment is required periodically.  The re-evaluation period needs to
be prescribed for periodic review via policy. However, the policy needs to
continuously evaluate the technological and political changes that may require
immediate re-assessment.

**Security Policy** – Security policy generation is the
process of creating policies on managing, implementing, and deploying security
within a Security Domain. The recommendations produced by security assessment
are reviewed, and policies are developed to ensure that the security
recommendations are implemented and maintained over time.

**Security** **Deployment** – Security deployment is
a combination of purchasing and installing security products and services as
well as the implementation of the security policies and procedures developed
during the security policy process. As part of the deployment aspect of the
Security Policies, management procedures need to be implemented that allow
intrusion detection and audit capabilities, to name a few.

**Security** **Audit (Monitoring) –** Security audit
is the process responsible for the detection of security attacks, detection of
security breaches, and the performance assessment of the installed security
infrastructure.

However, the concept of an audit is typically applied to
post-event/incursion.  The Security Domain model, as with active security
infrastructures, requires constant monitoring.  Thus the audit process
needs to be enhanced.

**Security Training** – Continuous training on security
threats, security technologies, corporate and legal policies that impact
security, Security measures analysis is a periodic,
and best practices is needed.  It is this training in the security process
that will allow the security infrastructure to evolve.

When attempting to evaluate the security process on an
enterprise basis, as is required by IntelliGrid Architecture, it is impossible to account for all
of the business entities, politics, and technological choices that could be
chosen by the various entities that aggregate into the enterprise.  Thus
to discuss security on an enterprise level is often a daunting task that may
never come to closure.  In order to simplify the discussion, allow for
various entities to control their own resources, and to enable the discussion
to focus on the important aspects, security will be discussed in regards to
Security Domains.

# Security and Security Domains

There are many potential methods through which to
facilitate the discussion of security.  Many desire to discuss security on
an Enterprise basis.  However, there is an issue regarding the definition
and boundaries of the “Enterprise” and those boundaries are always changing.
Thus developing “Enterprise” level security constructs/policies becomes
difficult and un-productive, as they are difficult to manage.

Another method is to perform concrete analysis of
particular systems and communication technologies/topologies.  It is often
difficult to discuss a security models in concrete terms since the technology
used in deployments typically becomes the lowest common denominator that is
discussed.  Such technology based security models tend to be difficult to
scale and understand from a enterprise system perspective.  Likewise, such
concrete models are difficult to extend/scale to address systemic security.

There is another, although less used, concept.  That
is the concept discussing security in regards to atomic “security domains” that
represent security boundaries.

“The concept of a security domain that is introduced in
this paper is not new. Many computer security practitioners have been (either
explicitly or implicitly) using the ideas presented here for many years in
protecting networks.”[1]

Security Domain Definition:

“Telecommunications and Network Security domain
encompasses the structures, transmission, methods, transport formats and
security measures used to provide integrity, availability, authentication, and
confidentiality for transmission over private and public communications
networks and media.” [2]

Additionally:

“In this paper, the term Security Domain is used to
describe a network of computer systems that share a specified security level
through a common element.”[1].

if !vml?![](IECSA_VolumeIV_AppendixA_files/image004.gif)endif?

Figure 2:
Representation of Security Domain Concept[[2]](IECSA_VolumeIV_AppendixA.htm#_ftn2)

A Security Domain (SD) represents a set of resources (e.g. network, computational, and physical) that is
governed/secured and managed through a consistent set of security policies and
processes.  Thus each Security Domain is responsible for its own general
security process (e.g. Assessment, Policy, Deployment, Monitoring, and
Training). In addition to the general security process, a   Security
Domain provides a well-known set of security functions that are used to secure
transactions and information within that domain.

Security Management is defined as:  “In [network management](http://www.atis.org/tg2k/_network_management.html),
the [set](http://www.atis.org/tg2k/_set.html) of functions (a) that
protects telecommunications networks and systems from unauthorized [access](http://www.atis.org/tg2k/_access.html) by persons, acts, or
influences and (b) that includes many subfunctions,
such as creating, deleting, and controlling [security](http://www.atis.org/tg2k/_security.html) services and
mechanisms; distributing security-relevant [information](http://www.atis.org/tg2k/_information.html); reporting
security-relevant events; controlling the distribution of [cryptographic](http://www.atis.org/tg2k/_cryptographic.html) keying
material; and authorizing [subscriber](http://www.atis.org/tg2k/_subscriber.html)
access, rights, and privileges.”[9]  Based upon
this definition, it is the Security Management of an SD that is responsible for
the risk assessment, developing security policies and strategies, and
implementing those policies and strategies.  A successful SD will define
and implement the following security services:

·       Access
Control: “The prevention of unauthorized use of a resource, including the
prevention of use of a resource in an unauthorized manner.”[7]  
  
There are generally three (3) categories of Access Control that need to be
addressed within a SD: Physical; Resource; and Information.  
Trust: “In [cryptology](http://www.atis.org/tg2k/_cryptology.html)
and cryptosystems, that characteristic allowing one entity to assume that a
second entity will behave exactly as the first entity expects. Note: Trust may
apply only for some specific function. The critical role of trust in the [authentication](http://www.atis.org/tg2k/_authentication.html)
framework is to describe the relationship between an authenticating entity and
a [certification
authority](http://www.atis.org/tg2k/_certification_authority.html); an authenticating entity must be certain that it can trust the
certification authority to create only valid and reliable certificates. [After
X.509]”[9]  
  
Trust is established via Authentication.  However, there are two methods
of authentication that are prevalent in today’s electronic systems: Role Based
Authentication and Individual Authentication.  
Confidentiality: “The property that information is not made available of
disclosed to unauthorized individuals, entities, or process.” [7]  
  
There are  two (2) categories of Confidentiality that need to be addressed
within a SD: Protection from un-intentional disclosure and overall protection
of information.  
Integrity: “The principle that keeps information from being modified or
otherwise corrupted either maliciously or accidentally.”[8]  
Security Policy: “The set of rules and practices that regulate how an
organization manages, protects, and distributes sensitive equipment and
information.”[8]  
Security Management Infrastructure (SMI): “(I) System elements and activities
that support security policy by monitoring and controlling security services
and mechanisms distributing security information and reporting security
events.”[10]  
Training (as described in the general security process).

Table 1: Relating Security Processes to Functions and
Services

| **General Security Process Name** | **Secu****rity Function Name** |
| --- | --- |
| Assessment | Policy  SMI |
| Deployment | Trust  Access Control  Confidentiality  Integrity  Policy  SMI |
| Monitoring | SMI  Policy |
| Policy | Policy |
| Training | Policy  Training |

Table 1 shows that the Policy security function is a
function that is required in ALL aspects of the security process. 
Additionally, the table also shows that an appropriate Security Management
Infrastructure needs to be deployed in order to monitor and perform
re-assessment of the security system within a Security Domain.

In order to actually implement the security functions,
within a Security Domain, several security services have been identified. 
Table 2 shows the relationships of the Functions to the Security Services that
would be used to actually implement the security function.

Table 2: Relating Security Processes to Functions and
Services

| **Function Name** | **Service Name** |
| --- | --- |
| Access Control | Authorization for Access Control  - All Trust related Services |
| Confidentiality | Confidentiality  Path Routing and QOS  Firewall Transversal |
| Integrity | Information Integrity  Profile  Protocol Mapping |
| Policy | Policy |
| Security Management Infrastructure (SMI) | Audit  User and Group Mngt.  Security Assurance  Non-Repudiation  Security Assurance  Policy  -- Management of all services |
| Trust | Identity Establishment  Identity Mapping  Quality of Identity  Credential Conversion  Credential Renewal  Delegation  Privacy  Single Sign-on  Trust Establishment |

Further, it is notable that there are inter-relationships
between the services themselves. As an example, Table 3 indicates that in order
to provide the Identity Mapping Service the Credential Conversion service is
needed.

Table 3: Primary Services and the additional Security
Services required to implement

| **Service** | **Requ****ired Services** |
| --- | --- |
| Audit | Policy  Security Assurance |
| Authorization for Access Control | Identity Establishment  Information Integrity  Setting and Verifying User   Trust Establishment  Non-Repudiation  Quality of Identity |
| Confidentiality | Identity Establishment  Authorization for Access Control.  Privacy  Trust Establishment  Path Routing and QOS |
| Delegation | Identity Mapping |
| Identity Establishment | Credential Renewal  Information Integrity  Policy  User and Group Mangement  Audit  Policy |
| Identity Mapping | Identity Establishment  Credential Conversion  Non-Repudiation  Quality of Identity |
| Information Integrity |  |
| Inter-Domain Security | Identity Mapping  Security Protocol Mapping  Security Against Denial of Service  Trust Establishment  Security Service Availability  Path Routing and QOS |
| Non-Repudiation | Audit  Security Assurance |
| Policy |  |
| Profile | Audit  Identity Mapping |

The combination of Table 1 through Table 3 should allow
users to determine what security services need to be implemented in order to
achieve a specific Security Process.  However, there are different services
required for inter-domain and intra-domain exchanges. These services are shown
in Table 4.

Table 4: Services needed for Intra/Inter Domain Security

| **Security Service** | **Intra-Domain** | **Inter-Domain** | **Comments** |
| --- | --- | --- | --- |
| Audit | m | m |  |
| Authorization for Access Control | m | m |  |
| Confidentiality | o | m |  |
| Credential Conversion | o | m |  |
| Credential Renewal | m | m |  |
| Delegation | o | m |  |
| Firewall Transversal | o | m |  |
| Identity Establishment | m | m |  |
| Identity Mapping | o | m |  |
| Information Integrity | m | m |  |
| Inter-Domain Security | Not Applicable | m |  |
| Non-Repudiation | m | m |  |
| Path Routing and QOS | o | o |  |
| Policy | m | m |  |
| Privacy | o | o |  |
| Profile | m | m |  |
| Quality of Identity | See comment | m | In order to provide this service for inter-domain, it must be available for intra-domain applications to make use of. |
| Security Against Denial of Service | o | m |  |
| Security Assurance | m | m |  |
| Security Protocol Mapping | o | m |  |
| Security Service Availability Discovery | m | m |  |
| Setting and Verifying User Authorization | m | m |  |
| Single Sign-On | m | Not Applicable |  |
| Trust Establishment | m | m |  |
| User and Group Management | m | m |  |

  

 

# Common Security Services and Technologies/Standards

This section discusses the common security services and the particular technologies/standards that
could be useful in actually implementing the common service.

## Audit Common Service

An audit service is responsible for producing records
known as audit records which contain audit record
fields, which track security relevant events. The resulting audit records may
be reduced and examined in order to address several key aspects of security
within a security domain:

·      
Audit records and audit trails can be used to determine if a
pre-scripted security policy is being enforced.

·      
Auditing and subsequently reduction tooling are used by the security
administrators within a Security Domain to determine the Security Domain’s
adherence to the stated access control and authentication policies.

·      
Audit records that support the recording of usage data, secure storage
of that data, analysis of that data allows Security Domains to detect fraud and
intrusion detection.

 A robust auditing mechanism enables a
Non-repudiation service through the creation of an audit trail.

Key definitions:

**audit: 1.** To conduct an
independent review and examination of [system](http://www.atis.org/tg2k/_system.html) records and activities
in order to test the adequacy and effectiveness of [data security](http://www.atis.org/tg2k/_data_security.html) and [data integrity](http://www.atis.org/tg2k/_data_integrity.html)
procedures, to ensure compliance with established policy and operational
procedures, and to recommend any necessary changes. **2.** Independent
review and examination of records and activities to assess the adequacy of
system controls, to ensure compliance with established policies and operational
procedures, and to recommend necessary changes in controls, policies, or
procedures. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99]

**audit record field:** A [field](http://www.atis.org/tg2k/_field.html) containing [information](http://www.atis.org/tg2k/_information.html) regarding all
entities in a transaction, and indicators of the types of processing performed
by those entities. [After X9.17/95]

**audit trail: 1.** A record
of both completed and attempted accesses and [service](http://www.atis.org/tg2k/_service.html). **2.** [Data](http://www.atis.org/tg2k/_data.html) in the form of a logical
path linking a [sequence](http://www.atis.org/tg2k/_sequence.html)
of events, used to trace the transactions that have affected the contents of a
record. **3.** [In [INFOSEC](http://www.atis.org/tg2k/_infosec.html),
a] chronological record of [system](http://www.atis.org/tg2k/_system.html)
activities to enable the reconstruction and examination of the sequence of
events and/or changes in an event. Note: [Audit](http://www.atis.org/tg2k/_audit.html) trail may apply to [information](http://www.atis.org/tg2k/_information.html) in an [information system](http://www.atis.org/tg2k/_information_system.html)
(IS), to [message](http://www.atis.org/tg2k/_message.html) [routing](http://www.atis.org/tg2k/_routing.html) in a [communications
system](http://www.atis.org/tg2k/_communications_system.html), or to the [transfer](http://www.atis.org/tg2k/_transfer.html)
of [COMSEC material](http://www.atis.org/tg2k/_comsec_material.html).
[INFOSEC-99]

There are several well-understood audit issues that must
be taken into account when implementing the audit trail. The audit trails need
to be analyzed to determine vulnerabilities, establish accountability, assess damage and recover the system. Manual analysis of audit
trails though cumbersome is often resorted to because of the difficulty to
construct queries to extract complex information from the audit logs. There are
many tools that help in browsing the audits. The major obstacle in developing
effective audit analysis tools is the copious amounts of data that logging
mechanisms generate.

There are three significant issues in creating an audit
trail from various electronic audit sources:

·       A coherent
and well-defined service to query an audit provider for audit records.  
  
There needs to be mechanism through which queries for Audit records can be
issued.  Although multiple protocols could carry such a request, such a deployment
strategy would require profile-mapping capabilities.  While to date, there
is no security specific standards for such a service a general purpose log
query service could be used.

·       A common
and self-describing format for the audit records that can account for
specializations.  
  
The capability to query for audit records allows the start of the information
transfer.  However, in order to re-construct an Audit Trail from multiple
audit record sources, there needs to be a common Audit Record format.  The
format should be self-describing with standardized contents, but allow for
additional information to be conveyed.  Some of the standardized fields
might be:  
  
<AuditRecord>, <RecordType>,<AuthBy>, <SubjectUid>,<TimeStamp>[[3]](IECSA_VolumeIV_AppendixA.htm#_ftn3) , etc…  However, there is no
internationally recognized specification for such. 
What is important here is that the record structure be self describing so
that a general purpose log query service could present log data intelligently.

·       A well-defined
mechanism to detect tampering with the transferred audit records.  
  
One of the major purposes for audits/audit trails/audit records is provide an
authoritative mechanism to perform non-repudiation.  One of the key issues
with providing non-repudiation in an authoritative manner is to prove that the
audit trail/record has not been tampered with.   
  
Although there is no recognized standard for such purposes, there is a
recognized approach to the problem.  This is to digitally sign the audit
record or to provide a non-repeating serial number for the record.  The
actual mechanics of the digital signature and how to convey the signature would
be issues for the common audit record format specification.

·       The ability
to correlate audit records from multiple audit sources.  
  
It is conceivable that different Security Domains would be in different time
zones.  In order to create an inter-domain audit trail, it is necessary to
be able to correlate the times of the various audit records.    
  
Thus all audit records should have a timestamp whose reference time is UTC.
However, the timestamp itself may not have the accuracy to differentiate
between several audit records that occur within the same timestamp
period.  Thus, it is also a requirement that a audit record serial number
be provided within each audit record.  The combination of the timestamp
and serial number would need to be unique.  
  
Problems with correlation can also occur if the timestamp accuracies of the
audit records are not the same.  Thus IntelliGrid Architecture should specify an appropriate
accuracy and time synchronization skew that is allowable.

·       Determination
of where to place auditing capability.  
  
Many security infrastructures/policies have difficulty identifying the types of
applications that need an audit trail.  The use of the definition of IntelliGrid Architecture security services allows the following base recommendations to be made.  
  
Audit records should be generated whenever/wherever the following security
services are invoked: Authorization for Access Control; Credential Conversion;
Credential Renewal; Delegation; Firewall Transversal; Identity Establishment;
Identity Mapping; Profile; Security Protocol Mapping; Setting and Verifying
User Authorization; Single Sign-On; Trust Establishment; User and Group Management.

·       Determination
of the minimum-maximum audit record time availability.  There is a need to
determine/specify through policy a minimum amount of time that an audit record
must be maintained within the audit trail system.  In IntelliGrid Architecture
environment, this time would need to be specified so that non-repudiation for
an appropriate period of time can be provided.

·       The issues
of privacy and legal relevance needs to be addressed.  
  
There are issues regarding the privacy of emails and text messages. 
However, during the 9/11 terrorism hearings, email evidence was allowed to be
submitted.  However, in the Kobe Bryant trial, the subpoena for text
messages (e.g. via cell phone) is being fought on the basis of privacy.    
  
Until recently, there have been no publicly available authoritative documents
describing best practices in this area.  However, the Federal Government
(AUDT-01) and the American Bar Association (AUDT-02) have published some
initial work that should be reviewed to determine if the recommendations are
viable within a given security domain.

### Audit Technologies/Specifications

Table 6 represents a set of specifications and/or standards that are relevant to the understanding of the issues
regarding the audit service. Those specifications marked as Recommended or
Recommended Reading should be considered as materials that should be considered
prior to actually implementing the audit service.

Table 5: Relevant References in regards to Audit processes

|  |  |
| --- | --- |
| AUDT-01 | US Department of Justice:LEGAL CONSIDERATIONS IN DESIGNING AND IMPLEMENTING ELECTRONIC PROCESSES: A GUIDE FOR FEDERAL AGENCIES  Available from: http://www.cybercrime.gov/eprocess.htm |
| AUDT-02 | Joint Administrative Office/Department of Justice Working Group on Electronic Technology in the Criminal Justice System: Working Group Report.  Available from: http://www.abanet.org/lpm/lpt/docs/ao-doj\_committee\_electronic\_technology\_wg\_report.pdf |

Table 6: Relevant Standards/Specifications relevant to the
Audit Service

| **Identification Num****ber** | **Name** | **Comment** |
| --- | --- | --- |
| [ISO/IEC 10164-8:1993](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=18165&ICS1=35&ICS2=100&ICS3=70) | Information technology -- Open Systems Interconnection -- Systems Management: Security audit trail function | Recommended |
| [ISO/IEC 10181-7:1996](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=18200&ICS1=35&ICS2=100&ICS3=1) | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Security audit and alarms framework |  |
| [ISO/IEC 18014-1:2002](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=34386&ICS1=35&ICS2=40&ICS3=) | Information technology -- Security techniques -- Time-stamping services -- Part 1: Framework | Recommended Reading |
| [ISO/IEC 18014-2:2002](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=34387&ICS1=35&ICS2=40&ICS3=) | Information technology -- Security techniques -- Time-stamping services -- Part 2: Mechanisms producing independent tokens |  |
| [ISO/IEC 18014-3:2004](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=34388&ICS1=35&ICS2=40&ICS3=) | Information technology -- Security techniques -- Time-stamping services -- Part 3: Mechanisms producing linked tokens |  |
| 21 CFR Part 11 | Guidance for Industry Part 11, Electronic Records; Electronic Signatures – Scope and Application | Recommended Reading |

###### Technological Assessment

An inspection of Table 6 shows that there are no
technology specific specifications/standards that
address the issues/problems previously discussed in this section.

## Authorization for Access Control

The authorization for Access Control is concerned with resolving a policy based access control decision based
upon appropriate Identity Establishment. The service consumes as input a
credential/identity token which embodies the identity of a service requestor
and/or for the resource that the service requestor requests. Based upon the
credentials and trust factors and policy, the resource will determine if
authenticating the peer is to be performed.  Once authenticated, the peers
may process each other’s requests based upon appropriate policy enforcement (e.g.
privilege or role based access).

It is expected that IntelliGrid Architecture environment will provide
access control functions, and it is appropriate to further expose an abstract
authorization service depending on the granularity of the access control policy
that is being enforced. Allow for controlling access to IntelliGrid Architecture services and
resources will be based on authorization policies (i.e., who can access a
service, under what conditions) attached to each service. Also allow for
service requestors to specify invocation policies (i.e. who does the client
trust to provide the requested service). Authorization should accommodate
various access control models and implementation.

It is a design objective that IntelliGrid Architecture services be
supportive of the functions and services defined within OSGA.

Key definitions:

**authenticate: 1.** To
establish, usually by challenge and response, that a [transmission](http://www.atis.org/tg2k/_transmission.html) attempt is
authorized and valid. **2.** [To] verify the identity of a [user](http://www.atis.org/tg2k/_user.html), user device, or other
entity, or the [integrity](http://www.atis.org/tg2k/_integrity.html)
of [data](http://www.atis.org/tg2k/_data.html) stored, transmitted,
or otherwise exposed to unauthorized modification in an [information system](http://www.atis.org/tg2k/_information_system.html)
(IS), or establish the validity of a transmission. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99] **3.** A
challenge given by voice or electrical means to attest to the authenticity of a
[message](http://www.atis.org/tg2k/_message.html) or transmission.
[JP1]

**authentication: 1.** [Any] [Security](http://www.atis.org/tg2k/_security.html) measure designed to
establish the validity of a [transmission](http://www.atis.org/tg2k/_transmission.html), [message](http://www.atis.org/tg2k/_message.html), or [originator](http://www.atis.org/tg2k/_originator.html), or a means of
verifying an individual's [authorization](http://www.atis.org/tg2k/_authorization.html)
to receive specific categories of [information](http://www.atis.org/tg2k/_information.html). [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99] [After JP 1-02] **2.**
A security measure designed to protect a [communications
system](http://www.atis.org/tg2k/_communications_system.html) against [acceptance](http://www.atis.org/tg2k/_acceptance.html)
of a fraudulent transmission or simulation by establishing the validity of a
transmission, message, or originator. [JP 1-02] **3.** Evidence by proper [signature](http://www.atis.org/tg2k/_signature.html) or seal that a document
is genuine and official. [JP 1-02]

**access control: 1.** A [service feature](http://www.atis.org/tg2k/_service_feature.html) or
technique used to permit or deny use of the components of a communication [system](http://www.atis.org/tg2k/_system.html). **2.** A technique
used to define or restrict the rights of individuals or [application](http://www.atis.org/tg2k/_application.html) programs to
obtain [data](http://www.atis.org/tg2k/_data.html) from, or place
data onto, a [storage](http://www.atis.org/tg2k/_storage.html)
device. **3.** The definition or restriction of the rights of individuals or
application programs to obtain data from, or place data into, a storage device.
**4.** [Limiting](http://www.atis.org/tg2k/_limiting.html) [access](http://www.atis.org/tg2k/_access.html) to [information system](http://www.atis.org/tg2k/_information_system.html)
resources only to authorized users, programs, processes, or other systems. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99] **5.** That
function performed by the [resource controller](http://www.atis.org/tg2k/_resource_controller.html)
that allocates system resources to satisfy [user](http://www.atis.org/tg2k/_user.html) [requests](http://www.atis.org/tg2k/_requests.html).

Authentication for Access Control relies upon several basic
factors being achieved:

·       That the identity
of the entity/person is established.  
  
The Identity Establishment Service performs this function.

* That there is an acceptable level of Trust
  established that the entity is who they claim to be.  
    
  The Trust Establishment and Quality of Identity services are involved in
  providing this functionality.
* That there is a policy and management process that
  has been used to determine which entity has the privileges to access
  certain assets, resources, or information.  
    
  The Policy and SMI related services provide this functionality.
* That
  there is a mechanism to enforce the mandates of the policy and management
  process.   
    
  The Authorization for Access Control service is responsible for providing
  this functionality.

There are generally three (3) categories of Access Control
that need to be addressed within a SD: Physical Assets; Computational
Resources; and Information.

### Physical

The basic premise of physical
access control is intended to allow authorized individuals
to be able to enter the areas for which they have clearance to enter and to
make it difficult for un-authorized individuals to enter.  Based on the
Security Domain definition, physical access control is not an inter-domain
issue. However, there are some desirable aspects to any physical access control
system:

·       The system
should be capable of providing an audit trail of who actually entered a
specific area.

·       The system
should be capable of detecting intrusion attempts of an un-authorized
individual to enter an area.

·       There are
issues in regards to the quickness/speed of enunciating intrusion or intrusion
attempts.  The speed at which this enunciation can occur is a key metric
in regards to the ability of a SMI to respond to the intrusion.

·       The system
should be robust enough that intrusions can be proven in an authoritative
manner so that legal prosecution has a probability of success.

·       Properly
implemented, a physical access control system can provide on-site personnel
listings/locations in the event of an emergency event.

·       The choice
of access control mechanisms should allow for multi-factor authentication and
ease of management in the event that revocation of access privileges is
required (e.g. User and Group Management issues). In order to accomplish this
service function, there must be a security token that is used to enable a final
access mechanism (e.g. a lock).

·       A
policy/strategy needs to address assets that are not capable of being
physically secured.  For these types of resources, informational and resource
security measures will need to be enhanced.  Examples of such an assets
are wireless networks and wireless technologies.

·       A residual
risk analysis and recovery plan needs to be developed, as part of the Policy
service, to address resources for which no type of adequate security can be
provided.  An example of such physical resources are transmission lines
and telephone lines.

In order to provide physical access control, there needs to
have a physical barrier that separates critical or controlled areas from
un-controlled areas.  These barriers would typically be fences, walls, or
doors that have locks or security guards so that proper access privileges can
be determined.

#### Physical Access Technologies/Specifications

There are no relevant specifications regardingPhysical Authorization for Access Control. However,
there are typical strategies that are worthy of some discussion (see Table 7).

Table 7: Typical Physical Access Control Strategies

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Security Strategy** | **Authentication Factor** | | | **Biometric** | **Comments** |
| **Single** | **Two** | **Three** |
| Security Guard Only |  |  |  |  | Needs to be augmented in order to provide audit capability, at a minimum. |
| Key/Lock | X |  |  |  | Adequate token that can be properly managed but can easily be duplicated that would facilitate un-authorized access. |
| Combination Lock | X |  |  |  | Typically adequate, but can be stolen through observation. |
| Sign-in sheet |  |  |  |  | Should not be used solely.  At a minimum, verification of the person’s identity signing-in must be facilitated. |
| Sign-in sheet with Photo-ID | X |  |  | X | Requires a security guard. |
| Sign-in sheet with confirmed clearance to enter. | X |  |  | X | Typically used for guest entry.  In order to be biometric, the confirming party must visually recognize and clear the entity requesting entry. |
| Video Surveillance |  |  |  |  | Should be used as audit/security for major/sensitive entrances. Provides a good mechanism for legal prosecution for remote sites. |
| Photo-ID with no sign-in sheet |  |  |  | X | Should not be used since no audit trail is possible. |
| Smart Card | X |  |  |  | It is assumed that SMART Cards would be used in conjunction with computerized locks so that a computerized audit trail can be generated.  However, it is typical that only ½ of the audit trail is generated since the cards are typically not required to exit the room. |
| Smart Card with Photo ID Card | X |  |  | X | if !vml?endif?Has the benefit of the Smart Card, but can also double as a Personal ID.  This is a recommended strategy. |
| Smart ID Card  used to enable Combination Lock |  | X |  |  | This is the best mechanism for restricting access to sensitive areas.  if !vml?endif? |
| Biometric Combination Lock |  | X |  | X | if !vml?endif?This is the best mechanism for restricting access to sensitive areas. |

Another method of analyzing the same strategies would be:

Table 8: Physical Security Strategies vs. Security Services
Provided

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Security Strategy** | **Security Service Provided** | | | **Comment** |
| **Identity** | **Trust** | **Access  Control** |
| Security Guard Only | ? |  |  | It is questionable that a security guard only strategy could provide adequate identification establishment. |
| Key/Lock |  | x | x | Provides a mechanism to establish a relative level of Trust (due to the person having the key) and provides appropriate access control. |
| Combination Lock |  | x | x | Provides a mechanism to establish a relative level of Trust (due to the person having the combination) and provides appropriate access control. |
| Sign-in sheet |  |  |  | Without actual identity establishment, no security can be provided. |
| Sign-in sheet with Photo-ID | x |  |  |  |
| Sign-in sheet with confirmed clearance to enter. | ? | x |  | Only provides Identity Establishment if a photo-ID is used in conjunction with the sign-in sheet. |
| Video Surveillance |  |  |  | Provides audit and repudiation capability only. |
| Photo-ID with no sign-in sheet | x |  |  |  |
| Smart Card |  | x | x | A Smart-Card only does not provide Identity Establishment.  Identity Establishment is a required function/service for Access Control. Therefore, the use of Smart-Cards only should not be considered. |
| Smart Card with Photo ID Card | x | x | x | This is a recommended strategy for non-critical area access. |
| Smart ID Card  used to enable Combination Lock | x | x | x | This is one of the recommended deployment strategies for critical areas. |
| Biometric Combination Lock | x | x | x | This is one of the recommended deployment strategies for critical areas. |

##### Technological Assessment

The suggested technology to be used to provide Access
Control to critical areas is the use of multi-factor access control.  It
is further suggested that SMART-CARD[[4]](IECSA_VolumeIV_AppendixA.htm#_ftn4)s that double as personal identification
cards be utilized to enable combination locks.  Furthermore, it is also
recommended that such technologydeployment be used in
conjunction with an electronic audit mechanism. 

It is recommended
that biometric identification mechanism be used when applicable. For specific
biometric recommendations, see page 32.

### Computational Resource

The
basic premise of computational access control is intended to allow authorized
individuals to be able to access programs for which they have clearance to make use of. Based on the Security Domain definition,
computational access control is both an inter-domain and intra-domain issue.
However, the enforcement of computation access control is purely an
intra-domain issue.  For inter-domain access control the Identity Mapping
service (and its required sub-functions) actually provides the mapping from an external
identity to an identity recognized and managed intra-domain.

·       The system
should be capable of providing an audit trail of who accessed a given
computational resource.

·       The system
should be capable of detecting intrusion attempts of an un-authorized
individual to a computational resource.

·       There are
issues in regards to the quickness/speed of enunciating intrusion or intrusion
attempts.  The speed at which this enunciation can occur is a key metric
in regards to the ability of a SMI to respond to the intrusion.

·       The system
should be robust enough that intrusions can be proven in an authoritative
manner so that legal prosecution has a probability of success.

·       The choice
of access control mechanisms should allow for multi-factor authentication and
ease of management in the event that revocation of access privileges is
required (e.g. User and Group Management issues). In order to accomplish this
service function, there must be a security token that is used to enable a final
access mechanism (e.g. a lock).

·       A
policy/strategy needs to address assets that are not capable of being
secured.  For those types of resources, the level of trust should be
considered low.

 

The aforementioned
issues need to be addressed for a variety of computational resources: 
Operating Systems (OSs); programs within a OS that
has access control; programs within an environment where there is no OS access
control required to access the program (e.g. an RTU); and wireless networks.

 

#### Operating System and Computer Programs

Operating System
(OS) access control requires Identity Establishment (see the identity
establishment service).  The access control service, forOSs, determines which programs/computational
resources the Identified User/Program has privileges to execute/access.

The major issues
regarding this access are:

·      
To provide an appropriate policy and SMI so that such access is granular
enough to provide enough audit capability.

·      
Managing the configuration in a distributed environment.

·      
The level of trust that can be associated with the OS to perform its
tasks in a secure manner (see ACC-01).  Several issues are mitigated if a
“Trusted/Secure” OS is used.  However, the use of such OSs
in IntelliGrid Architecture environment is not viable in a majority of the cases, therefore
this section will address non-Trusted OS issues.

For all OSs, the issue of access control relates to properly
managed Access Control Lists that are typically OS specific.  However,
care needs to be taken to ensure that if Role Based Access is used, that an
audit mechanism is provided in order to reference back to the actual
individual/entity that has accessed the OS. Additionally, the information in
ACC-02 should be considered when developing the OS access framework in a
distributed environment.

**Computer
Programs**

In the cases where
an OS does not provide Access Control to the programmatic level, programs
themselves need to provide this capability. This is particularly true for
electronic protocol processes that bypass OS authentication on the destination
of the communication path.  In such a situation, it is incumbent upon the
destination program/process to apply the appropriate security mechanisms. 

In IntelliGrid Architecture there
will be computational and communication technologies integrated of various
capabilities.   These various capabilities (e.g.
process/memory/storage capacity or bandwidth limitations) require that
different technological solutions be available.  However the functional
objectives remain consistent: provide a manageable environment and to provide
enough granularity to provide a capability for non-repudiation.

#### Communication Networks

There are several
types of communication networks that need to be addressed:

·      
Inter-Domain networks where the physical network are exposed.  
  
The major issue with these types of physical
networks is that both domains do not manage the network segments that provide
the inter-domain interfaces.  These segments are typically provided by a
third party and therefore constitutes a third Security Domain. Thus it is
important that appropriate access control be provided at the security domain
interface points.

·      
Intra-Domain networks where the physical network is within a Security
Domain.  
  
For intra-domain networks, some Security Domains may desire to control the
computers/computer users that actually have access to the network.  Once a
resource is within a Security Domain, there is no reliable mechanism to prevent
physical access to the network.  Thus it becomes incumbent upon the SMI to
detect that a non-authorized access to the network has been attempted or been
successful.  Additionally, it may be possible to make it more difficult
for a non-authorized resource to make use of the network through proper
management of the network addresses so that no address is assigned to the
intruding resource.

·       Wireless
LAN/WAN Networks whose transmissions can be easily monitored and spoofed.  
  
This type of network represents a intra-domain network that REQUIRES management
in regards to who can actually make use of the network.  The issue can be
easily demonstrated by looking at the prevalence of WI-FI.  
  
In the WI-FI case, hot-spots (e.g. Starbucks, airports) could not recoup their
investment without a challenge response mechanism to ensure that only
authorized (e.g. paid subscription entities) are actually assigned an address
that facilitates real communications.   
  
Such mechanisms may prevent off-segment communications, but will not prevent
denial-of-service attacks (see ACC-03).  Thus such systems need to be
augmented beyond challenge-response.

·      
Dial-up Networks: There is a well-documented history in regards to the
vulnerabilities associated with dial-up networks.  These types of networks
are inherently susceptible to denial-of-service attacks and have poor identity
establishment/access control at a physical/network level.  This is
especially true for equipment that is deployed in the Transmission and
Distribution environment.

Table 9: References
regarding Computational Resource Access Control

|  |  |
| --- | --- |
| ACC-01 | Stephen Radford – Trusted Operating Systems and Their Evolving Non-Trusted Counterparts , January 23, 2003.SANSInstitute |
| ACC-02 | **Fine-Grain Authorization for Resource Management in the Grid Environment**. K. Keahey, V. Welch. Proceedings of Grid2002 Workshop,  2002. |
| ACC-03 | AA-2004.02 -- Denial of Service Vulnerability in IEEE 802.11 Wireless Devices (AusCERT) |
| ACC-04 | RADIUS Protocol Security and Best Practices, Published: January 1, 2002, By Joseph Davies, Microsoft Corporation  Available from:  <http://www.microsoft.com/technet/itsolutions/network/security/radiusec.mspx> |
|  |  |

 

#### Technological Assessment Specifications/Standards

Table 10 represents
a set of specifications and/or standards that are relevant to the understanding
of the issues regarding access control for computational
resources. Those specifications marked as Recommended or Recommended
Reading should be considered as materials that should be considered prior to
actually implementing the access control service.

Table 10: Relevant
Computational Resource Access Control Standards/Specifications

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| ANSI INCITS 359-2004 | Role Based Access Control | Recommended |
| RFC 2244 | ACAP -- Application Configuration Access Protocol | Recommended |
| RFC 1013 | X Window System Protocol, version 11: Alpha update April 1987 |  |
| RFC 2086 | IMAP4 ACL extension |  |
| RFC 2820 | Access Control Requirements for LDAP | Recommended for Directory Services |
| RFC 1305 | Network Time Protocol (Version 3) Specification, Implementation | Recommended for NTP |
| RFC 2753 | A Framework for Policy-based Admission Control |  |
| RFC 2744 | Generic Security Service API Version 2 : C-bindings |  |
| RFC 2356 | Sun's SKIP Firewall Traversal for Mobile IP |  |
| RFC 1004 | Distributed-protocol authentication scheme |  |
| RFC 2865 | Remote Authentication Dial In User Service (RADIUS) | Recommended for Dial-up Lines |
| RFC 2869 | RADIUS Extensions |  |
| RFC 1221 | Host Access Protocol (HAP) Specification - Version 2 |  |
| ISO/IEC 10164-9:1995 | Information technology -- Open Systems Interconnection -- Systems Management: Objects and attributes for access control |  |
| ISO/IEC 10181-3:1996 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Access control framework | Recommended |
| WebDAV | Access Control Extensions to WebDAV |  |
| Microsoft | Remote Access Service (RAS) |  |
| OASIS | Extensible Access Control Markup Language (XACML)  Available from:  http://xml.coverpages.org/xacml-schema-policy-v15.pdf | Recommended when used in conjunction with other XML based technologies. |
| IBM | XML Access Control (XACL) | Proprietary but has been implemented as part of IBM’s security framework. |
| CJCSI 6731.01 | Global Command and Control System Security Policy,  Chairman of the Join Chiefs of Staff Instruction, December 31, 1998 |  |
| FIPS PUB 112 | Password Usage |  |
| FIPS PUB 113 | Computer Data Authentication |  |

 

##### Technological Assessment and Recommendations

###### OS Recommendations

It is recommended
that Trusted OSs be used whenever possible.
Additionally, ANSI INCITS 359-2004 us suggested as an implementation
strategy for Role Based Access.

###### Computer Programs

It is recommended
that the appropriate access control list mechanisms be used in regards to the
applications where such technologies have been noted in Table 10.  Thus, make use of:

·      
RFC 1013 for X Windows applications.

·      
RFC 2086 for IMAP based applications.

·      
RFC 2045 for SNTP.

·      
RFC 2228 for FTP.

·      
RFC 2820 for LDAP.

·      
RFC 1305 in regards to NTP. It is recommended that the security
extension be implemented and used.

·      
RFC 3414, RFC 3411, and RFC 1351 for SNMP.  It is also recommended
that SNMPv3 be utilized when possible.    
  
There is an issue regarding the lack of definition of standardized security
related Management Information Base (MIB) objects.  IEC TC57 WG15 has
undertaken the task to define security MIB objects that could facilitate
intrusion detection.  It is recommended that the recommendations of IEC
62351-7 (Objects for Network Management) be reviewed carefully.

·      
RFC 2817 and RFC 2818 (HTTPS) for HTTP.

Otherwise, it is
suggested to follow the general policies/procedures set forth in ISO/IEC
10181-3:1996 and make use of any application specific access control strategies
set forth.

 

###### Communication Networks and Protocols

In general it is
recommended that all computational resources, when possible, be assigned
dynamic addresses that allow off-segment communications. 
There is no single technology that can accomplish this, but a challenge
response mechanism is suggested as part of the implementation strategy.

 

For those resources
that require fixed addresses (e.g. servers of data), it is suggested that
network based access control lists be implement in order to prevent
un-authorized off-segment communication.

 

There is a
substantial amount of work occurring within IEC TC57 WG15 to secure several of
the communication protocols that are intended to be used by IntelliGrid Architecture.  It is
suggested that these be adopted and deployed as rapidly as is feasible.

 

Wireless networks
are extremely susceptible to denial-of-service attacks.  In order to
mitigate this issue, AES encryption on wireless links is suggested.

 

Dial-up access
control should be implemented through the use of RAIDUS (RFC 2865 and RFC 2869)
when this is feasible.  Such access should be deployed so that there is an
additional access control list (e.g. a Firewall or router based ACL) that
provides additional security.  Thus, when possible, it is suggested that
NO direct dial-up access be given to a computer or a computer process.

 

However, this is not
feasible in the Transmission and Distribution systems deployed within IntelliGrid Architecture
environment (e.g. RTUs and field devices).  For this class of resource, or
resources with similar constraints, it is suggested that the devices be
implemented in such a manner that denial-of-service is mitigated:

 

·       Dial-up
connections should be constructed such there is an inactivity time-out to
prevent a connect/hold the port open denial of service attack.

·       Once the
port is connected, there should be a time-out on the connection that requires
valid communication protocol/application level information flow.

 

It is not suggested to implement a dial-back
strategy since these become difficult to manage and maintain and does not allow
the type of environment that IntelliGrid Architecture is attempting to promote.

 

### Informational Technology Assessment/Specification

Information access
control is extremely similar to a combination of OS and program access. 
However, it is up to each individual program to provide
the appropriate level of access control. 

ACC-04 represents
a very simple summary of the granularity required in access control for most PICOMs:  Control over Reading; Control over
Changing;  and Control over Storing.  Additionally, for Object
Oriented access, there may need to be an ability to prevent an entity from
discovering that an Object Exists (optional).

 

Table 11:
References relating to Access Control for Informational Resources

|  |  |
| --- | --- |
| ACC-04 | Access Control on the Semantic Web (wc3.org)  Available from: http://www.w3.org/2002/03/semweb/access-control |

 

## Confidentiality

Protect the
confidentiality of the underlying communication (transport) mechanism, and the
confidentiality of the messages or documents that flow over the transport mechanism in a OGSA compliant infrastructure. The
confidentiality requirement includes point–to–point transport as well as
store-and-forward mechanisms.

Key definitions:

**confidentiality:
1.** Of classified or sensitive [data](http://www.atis.org/tg2k/_data.html),
the degree to which the data have not been compromised; i.e., have not been
made available or disclosed to unauthorized individuals, processes, or other
entities. [After 2382-pt.8] **2.** [Assurance](http://www.atis.org/tg2k/_assurance.html)
that [information](http://www.atis.org/tg2k/_information.html) is not
disclosed to unauthorized persons, processes, or devices. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99]
**3.** A property by which information relating to an entity or party is not
made available or disclosed to unauthorized individuals, entities, or
processes. [T1.Rpt22-1993]

 

There are two main
mechanism to provide confidentiality for electronically transmitted information:
encryption or transmission over a secure infrastructure.

### Encryption

It is important to
realize that there is no 100% effective mechanism to protect electronically
transmitted information for an indefinite length of time.  Initially, when
the Data Encryption Standard (DES) was specified, it
was thought that 56-bit encryption protection could protect information for
20-30 years.  However, with the increase in computational capability, and
the decrease in cost for that capability, in 1999 DES was cracked in under 22
hours (see CONF-02) . Based upon Moore’s Law, today DES could be cracked in
approximately 41 minutes considering.    
To respond to the new reality, NIST and several standards organizations (in
particular IEEE) developed a more advanced and secure encryption standard known
as the Advanced Encryption Standard (AES).

“In
comparison, DES keys are 56 bits long, which means that there are approximately
7.2 x 1016 possible DES keys. Thus, there are on the order of 10 (21) times
more AES 128-bit keys than DES 56-bit keys. Assuming that one could build a
machine that could recover a DES key in a second (i.e. try 255 keys per
second), then it would take that machine approximately 149 thousand-billion
(149 trillion) years to crack a 128-bit AES key. To put this into perspective,
the Universe is believed to be less than 20 billion years old. NIST believes
that AES will remain secure beyond the next twenty years. AES implementations
will also be exportable, and AES implementations in proprietary systems will
just need a one-time review prior to export” [CONF-01]

The above claim is
similar to the claims made by DES when it was first introduced.  Whereas
DES and Triple-DES (3DES) have had almost twenty years of deployment prior to
replacement due to “crackability”, the advent of
Quantum Computers (see CONF-03) may not allow the modern encryption algorithms
the same.  If Quantum Computers were available today, using Grover’s
Algorithm (see CONF-04) it could be extrapolated that even 512 bit DES could be
cracked in approximately 1 second.  AES is more complex and is less prone
to Grover’s Algorithm, however the NIST statement (CONF-01) will definitely not
be true in the near-term future.

The advent of
Quantum Computers raises the issue of how to make encryption effective. 
Even without the advent of Quantum technology, the following recommendations
are valid:

·      
Choose a modern encryption algorithm for the purposes of encryption.  
  
There are many factors that enter into an appropriate algorithmic choice. 
The factors that need to be considered are the additional CPU processing that
the use of encryption will require and the bandwidth/transmission performance
characteristics desired.  
  
At the NERC Data Exchange Working Group meeting in April 2004, the following
results were presented for Secure IEC-60870-6 TASE.2 (ICCP).  
  
The additional CPU performance requirements, for the use of TLS and AES 256,
represented an increase from 1% to 1.35% for encryption and 1% to 1.41% for
decryption (percentages based upon total CPU being 100%).  It was also
found that AES 256 was more CPU efficient than either DES or 3DES.  
  
It was found that the bandwidth overhead increased by the size of certificates
exchanged, but only increased 1% in regards to normal ICCP traffic once the initial
connection and symmetric keys were established.

·      
When using encryption, make sure that the technology used to “negotiate”
encryption can negotiate multiple encryption algorithms.

·      
If possible, make sure that the negotiation can be upgraded to newer
encryption algorithms as new, more robust algorithms, become available.

·      
Make use of technologies where the encryption keys can dynamically be
re-negotiated without interrupting the communication information flow.

 

Table 12: Reference
Relevant to Encryption Technology

|  |  |
| --- | --- |
| CONF-01 | **NIST Announces New Government Aes Encryption Standard - Technology Information**  Available from: <http://articles.findarticles.com/p/articles/mi_m0BNO/is_2000_Nov/ai_66297312> |
| CONF-02 | Jason Meserve , DES code cracked in record time, Network World, 01/20/99  Available from:  <http://www.nwfusion.com/news/1999/0120cracked.html> |
| CONF-03 | Aaron Ricadela, Quantum’s Next Leap, Information Week, May 10, 2004 |
| CONF-04 | Matias Castro ,What Use is My Quantum Computer Now I Have it?    Available From:  http://www.doc.ic.ac.uk/~nd/surprise\_97/journal/vol2/mjc5/ |

 

#### Technological Assessment and Specifications

There are several
different mechanisms through which to develop assessments regarding
encryption.  For the purposes of this section, applicability
to specific communication media will be used.

In general, it is
suggested to make use of X.509 certificates to provide public/private key
encryption exchanges when possible.  Such a choice will ease integration
with other certificate technologies (e.g. management) that are being
recommended as part of other security services.

When X.509
certificate use is not appropriate, it is suggested that RFC 2898 (PKCS#5) be
utilized.  This allows encryption to be established based upon
username/passwords.

##### Protocol Basis

In general, it is
recommended to use the appropriately specified encryption standard associated
with the protocol (e.g. HTTPS for HTTP).  There are further recommendation for TCP/IP:

**TCP/IP
Transmissions**

It is recommended
that TLS with AES (RFC 3268) or PPP Encryption Control Protocol (RFC 1968)
be used to provide encryption.  These represent the most modern and secure
mechanism.

##### Media

**Serial**

If the path of the
serial link does not provide enough confidentiality nor the protocol in use over
the link, and confidentiality is still desired then the following is recommended:

·      
If the peers can be upgraded to support encryption, then this should be
the preferred approach.

·      
For legacy systems, that are not upgradeable, it is suggested that
external hardware be applied.  Further it is recommended that AGA-12 be
evaluated for this purpose.

**Ethernet,
SONET, FDDI, etc.**

It is recommended
to make use of VPN technology when possible.

**WI-FI and
Wireless Technologies**

The Web Encryption
Protocol (WEP) specified in IEEE 802.11b has been proven to be vulnerable and
to not provide adequate protection.  New versions of WI-FI and wireless
technologies are coming equipped with AES encryption.  It is the AES
encryption that is recommended.  Further it is recommended that
WPA2/80211.i be adopted in order to achieve the implementation of this
recommendation.

It is further
recommended that any legacy (e.g. WEP based) WI-FI equipment be replaced or
upgraded, as the vulnerabilities are well known and not manageable.

 

Table 13:
Encryption Related Specifications/Standards

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| RFC 3370 | Cryptographic Message Syntax (CMS) Algorithms |  |
| RFC 3447 | Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.1 |  |
| RFC 2898 | PKCS #5: Password-Based Cryptography Specification Version 2.0 | Recommended when certificate exchange is not appropriate. |
| RFC 1968 | The PPP Encryption Control Protocol (ECP) |  |
| RFC 2246 | The TLS Protocol Version 1.0 |  |
| RFC 2409 | The Internet Key Exchange (IKE) | Used for VPNs |
| RFC 1040 | Privacy enhancement for Internet electronic mail: Part I: Message encipherment and authentication |  |
| RFC 2946 | Telnet Data Encryption Option |  |
| RFC 2440 | OpenPGP Message Format |  |
| RFC 1423 | Privacy Enhancement for Internet Electronic Mail: Part III: Algorithms, Modes, and Identifiers |  |
| RFC 2408 | Internet Security Association and Key Management Protocol (ISAKMP) | Used for VPNs |
| RFC 2510 | Internet X.509 Public Key Infrastructure Certificate Management Protocols |  |
| RFC 3268 | Advanced Encryption Standard (AES) Ciphersuites for Transport Layer Security (TLS) |  |
| RFC 2093 | Group Key Management Protocol (GKMP) Specification |  |
| RFC 2459 | Internet X.509 Public Key Infrastructure Certificate and CRL Profile |  |
| RFC 2040 | The RC5, RC5-CBC, RC5-CBC-Pad, and RC5-CTS Algorithms |  |
| FIPS 197 | Federal Information Processing Standards Publication 197, November 26, 2001, Specification for the Advanced Encryption Standard (AES)  Available from: http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf | Recommended |
| RSA PKCS #12 | Personal Information Exchange Syntax Standard, version 1.0. |  |
| RSA PKCS #8 | Private-Key Information Syntax Standard |  |
| IEEE 802.11b | Web Encryption Protocol |  |
| AGA-12 | Cryptographic Protection of SCADA Communications General Recommendations. |  |
| WPA | WI-FI Protected Access |  |
| IEEE 802.11i | Security for Wireless Networks |  |
| WPA2 | WI-FI Protected Access Version 2 |  |

 

Table 14: Digital
Certificate Related Specifications/Standards

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| RFC 2510 | Internet X.509 Public Key Infrastructure Certificate Management      Protocols.C. Adams, S. Farrell. March 1999. |  |
| RFC 2511 | Internet X.509 Certificate Request Message Format. M. Myers, C.      Adams, D. Solo, D. Kemp. March 1999. |  |
| RFC 2527 | Internet X.509 Public Key Infrastructure Certificate Policy and      Certification Practices Framework. S. Chokhani, W. Ford. March 1999. |  |
| RFC 2560 | X.509 Internet Public Key Infrastructure Online Certificate  Status Protocol - OCSP. M. Myers, R. Ankney, A. Malpani, S. Galperin,      C. Adams. June 1999. |  |

 

### Communication Path Selection

 

There is a
mechanism of mitigating the need to encryption.  This is to evaluate or
provide a communication path that inherently provides enough protection (see the Path Routing and QOS service for further
information).

## Credential Conversion

The credential
conversion service provides credential conversion between one type of
credential to another type or form of credential. This may include such tasks as reconciling group membership, privileges,
attributes and assertions associated with entities (service requestors and
service providers). For example, the credential conversion service may convert
a Kerberos credential to a form which is which is required by the authorization
service. The policy driven credential conversion service facilitates the
interoperability of differing credential types, which may be consumed by
services. It is expected that the credential conversion service would use the
identity mapping service.

Key definitions:

**credential:
1.** In [cryptography](http://www.atis.org/tg2k/_cryptography.html), a subset of [access](http://www.atis.org/tg2k/_access.html)
permissions (developed with the use of media-independent [data](http://www.atis.org/tg2k/_data.html))
attesting to, or establishing, the identity of an entity, such as a birth certificate,
driver's license, mother's maiden name, social security number, fingerprint,
voice print, or other [biometric](http://www.atis.org/tg2k/_biometric.html) parameter(s).
[After X9.69] **2.** [In [security](http://www.atis.org/tg2k/_security.html)],
[information](http://www.atis.org/tg2k/_information.html), passed from
one entity to another, used to establish the sending entity's access rights. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99]

 

Credential
conversion is also a required service for Single-Sign on and the Identity
Mapping security services.  Besides performing the actual mappings, there
is an inherent requirement that such a service provide an audit mechanism so
that it is possible to determine the original identity/credential that was
converted.  This is a necessary requirement in order to provide a robust
audit mechanism in a multi-domain environment.

### Technological Assessment

The prevalent work
is being sponsored by the Organization for the Advancement of Structured
Information Standards (OASIS).  This is work in progress but is the first industry/standards based consortium that is
attempting to solve the problem.  However, the current work involves
certificate usage and does not directly address the issue of username/password
conversion nor the audit trail issues.

 

Except for the
general recommendations found in the Identity Establishment service, only
certificates require further recommendations in regards to credential
conversion.

 

#### Certificate

 

Furthermore, there
has been little thought in enhancing the SAML specification to standardize a
chain or properties that would allow the Quality of Identity service to be facilitated. 

 

It is suggested that
SAML and the OASIS work be adopted as the foundation for the Credential
Delegation service. However, further work and IntelliGrid Architecture enhancements may be
required.

 

Table 15:
References and Specifications regarding Credential Conversion

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| OASIS Security Technical Committee | Security for Grid Services  Available from:  http://www.globus.org/Security/GSI3/GT3-Security-HPDC.pdf |  |
| OASIS Security Technical Committee | Attribute Profiles for SAML 2.0  Available from:  http://www.oasis-open.org/committees/download.php/6344/sstc-hughes-mishra-baseline-attributes-03.pdf | Incomplete, but is on the correct track. |
| OASIS Security Technical Committee | SAML 2.0: Security Assertion Markup Language Version 2.0  Available from:  http://www.oasis-open.org/committees/download.php/2290/oasis-sstc-saml-1.0.zip | Recommended |
| OASIS Security Technical Committee | Bindings for OASIS Security Assertion Markup Language (SAML) V2.0  Available from:  http://www.oasis-open.org/committees/download.php/6773/sstc-saml-bindings-2.0-draft-11-diff.pdf | Draft that specifies how to bind SAML over various protocols. Highly recommended. |
| OASIS Security Technical Committee | Authentication Context  Available from:  http://www.oasis-open.org/committees/download.php/6539/sstc-saml-authn-context-2.0-draft-04a-diff.pdf | Draft that is needed to establish identity within a SAML environment. |
|  |  |  |

 

## Credential Renewal Service

In many scenarios,
a job initiated by a user may take longer than the life span of the user’s
initially delegated credential. In those cases, the user needs the ability to be notified prior to expiration of the
credentials, or the ability to refresh those credentials such that the job can
be completed.

It is worthy to
note that the Credential Renewal service provides some of the capability of
User and Group Management service.  However, it does not include how to
revoke or initially allocate the credentials.  However, in general it is a
Security Domain and IntelliGrid Architecture issue in regards to the period of time required for
credential renewal.

Performing a more
in-depth analysis of the credential renewal process, the general issues are:

·      
Determining when the credentials need to be renewed.  This is
typically a Security Domain’s policy issue.

·      
Determining a mechanism to detect a credential that needs to be renewed.

·      
Provide a mechanism for credential renewal.

 

OASIS specifies
several different types of credentials that need to be considered for
renewal.  Each has different aspects to renewal.  The IntelliGrid Architecture relevant
types are:

·      
Internet Protocol based credentials are
related solely to address resolution as the credential.  Address spoofing
is a prevalent threat in IntelliGrid Architecture environment and therefore the use of this
credential mechanism is not suggested.  
  
In order to renew an addressed based credential, address-to-name resolution is
required as well as appropriate security on such resolution requests.

·      
InternetProtocolPassword makes use of
username/password as well as address resolution to establish credentials.  
  
This credential methodology has the same issues with address credential renewal
as well as verifying that the password is viable or in need of renewal.

·      
Password makes use of a username/password combination in the clear.  
  
Username/Password management is a major issue that needs to be resolved.

·      
PasswordProtectedTransport makes use of an
encrypted transport to transmit a username/password combination (e.g. HTTPS
conveying a username/password).

·      
SmartCard renewal is strictly a policy and SMI
issue.  The policy must address when a SmartCard
must be renewed and the mechanism for performing a renewal.

·      
SmartCardPKI renewal adds the issue of digital
certificate renewal to the need to renew a particular Smart Card.  Since
most digital certificates have an expiration date, it is the certificate date
that should take precedence in the renewal process (e.g. policy may be able to
ignore the renewal of the card itself).  However, this is not the case if
the SmartCardPKI solution is being used as a Personal
Identification card that requires visual inspection for physical access.

·      
SoftwarePKI uses digital certificates and
therefore certificate renewal is the major issue.

·      
TimesyncToken is a hardware token that is used
to generate a unique token as a credential.

·      
Visual Person Identification Card used with visual inspection to provide
physical access control.  
  
Any credential type that can be used to obtain physical access based upon
visual inspection need to be replaced or modified in a timely manner.  The
periodicity of the change is dependent upon the Security Domain’s policies.

 

### Technological Assessment and Relevant Specifications

There are certain
general recommendations that can be made:

·      
When using address resolution and TCP/IP, make use of the Domain Name Service and a authenticated Directory server. 
Dynamic address assignment should be the preferred mechanism with the resulting
address being placed in the authenticated directory server.

·      
Visual Credentials should be replaced/modified on a time period based
upon the Security Domain’s policy.  It may be less expensive to adopt a
modification, as opposed to a replace strategy (e.g. the same model as
automobile license tabs versus license plates).

·      
Smart Cards should include a renewal date as part of the information
that is contained on the card.  This field should encrypt and digitally
signed so that tampering can be detected.  As the Smart Card is used,
advanced notification of the need for renewal needs to be given to the holder.

·      
Certificate based technologies: X.509 certificates are the recommended
certificate type.  Certificates should be accessible via PKCS#10
interfaces.  The date of certificate lifetime expiration should be used as
the renewal date. As the certificate is used, advanced notification of the need
for renewal needs to be given to the holder.

·      
Biometric based technologies need to have renewal dates based upon the
Security Domain’s policy.

#### Specific Recommendations

##### Certificates

It is recommended
that RFC 2797 or RFC 2560 (OCSP) to determine if the certificate needs to be
renewed. If neither of these is possible, then itbecomes a local SecurityDomain/implementation
issue.

Certificate renewal should be performed via RFC 2797 when
possible.

Table 16: Relevant
Specification regarding Credential Renewal

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| ISO 9735-9:2002 | Electronic data interchange for administration, commerce and transport (EDIFACT) -- Application level syntax rules (Syntax version number: 4, Syntax release number: 1) -- Part 9: Security key and certificate management message (message type- KEYMAN) |  |
| NERC | Certificate Policy for the Energy Market Access and Reliability Certificate (e‑MARC) Program Version 2.4  Available from:  ftp://www.nerc.com/pub/sys/all\_updl/cip/pkitf/e-MARC-PKI\_draft\_version\_V2-4b\_March\_2003-rev1.doc |  |
| OASIS Security Technical Committee | Authentication Context  Available from:  http://www.oasis-open.org/committees/download.php/6539/sstc-saml-authn-context-2.0-draft-04a-diff.pdf |  |
| RFC 2459 | Internet X.509 Public Key Infrastructure Certificate and CRL Profile |  |
| RFC 2511 | Internet X.509 Certificate Request Message Format |  |
| RFC 2560 | X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP |  |
| RFC 2797 | Certificate Management Messages over CMS |  |
| RFC 2875 | Diffie-Hellman Proof-of-Possession Algorithms |  |
| RFC 2986 | PKCS #10: Certification Request Syntax Specification Version 1.7 |  |
| RFC 3280 | Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure  Certificate and Certificate Revocation List (CRL) Profile |  |
| RFC 3369 | Cryptographic Message Syntax (CMS) |  |
| RFC 3647 | Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework |  |
| RFC 1591 | Domain Name System Structure and Delegation |  |
| RFC 1608 | Representing IP Information in the X.500 Directory | Recommended |
| RFC 1612 | DNS Resolver MIB Extensions | Recommended |
| RFC 2230 | Key Exchange Delegation Record for the DNS |  |
| RFC 2276 | Architectural Principles of Uniform Resource Name Resolution |  |
| RFC 2535 | Domain Name System Security Extensions | Recommended |
| RFC 2592 | Definitions of Managed Objects for the Delegation of Management Script |  |
| RFC 2874 | DNS Extensions to Support IPv6 Address Aggregation and Renumbering |  |
| ISO 10202-1:1991 | Financial transaction cards -- Security architecture of financial transaction systems using integrated circuit cards -- Part 1: Card life cycle | Recommended Reading |
| ISO 10202-7:1998 | Financial transaction cards -- Security architecture of financial transaction systems using integrated circuit cards -- Part 7: Key management |  |

 

## Delegation Service

Provide facilities
to allow for delegation of access rights from requestors to services, as well
as to allow for delegation policies to be specified. When dealing with delegation of authority from an entity to another,
care should be taken so that the authority transferred through delegation is
scoped only to the task(s) intended to be performed and within a limited
lifetime to minimize the misuse of delegated authority.

Based upon the
aforementioned definition, delegation involves Credential Conversion and
Authorization for Access Control services. There are two primary types of
delegation that need to be addressed:

·      
Delegation of Addresses:  This type of delegation could occur due
to proxies, firewalls or gateways.  The main requirements of such
delegation are to be able to provide an audit mechanism that allows repudiation
to the original address.   
  
A good example of why this is needed is the email SPAM problem that we face
today.  It is difficult with address and email account spoofing to
determine the actual sender of the original SPAM message.

·      
Access Privilege Delegation would typically result in the transformation
of one entity’s privileges to some type of Role Based set of privileges. 
Once the ability to audit the delegation is of primary importance.

 

### Technological Assessment and Relevant Specifications

It is recommended
that either RBAC or SAML be considered as appropriate.

 

Table 17: Relevant
Specifications for the Delegation Service

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| BCP 65 | Dynamic Delegation Discovery System (DDDS) Part Five: URI.ARPA Assignment Procedures |  |
| RFC 1034 | Domain names - concepts and facilities |  |
| RFC 1507 | DASS - Distributed Authentication Security Service |  |
| RFC 1591 | Domain Name System Structure and Delegation |  |
| RFC 1608 | Representing IP Information in the X.500 Directory |  |
| RFC 1612 | DNS Resolver MIB Extensions |  |
| RFC 2230 | Key Exchange Delegation Record for the DNS |  |
| RFC 2276 | Architectural Principles of Uniform Resource Name Resolution |  |
| RFC 2535 | Domain Name System Security Extensions |  |
| RFC 2592 | Definitions of Managed Objects for the Delegation of Management Script |  |
| RFC 2874 | DNS Extensions to Support IPv6 Address Aggregation and Renumbering |  |
| RFC 3401 | Dynamic Delegation Discovery System (DDDS) Part One: The Comprehensive DDDS |  |
| RFC 3402 | Dynamic Delegation Discovery System (DDDS) Part Two: The Algorithm |  |
| RFC 3403 | Dynamic Delegation Discovery System (DDDS) Part Three: The Domain Name System (DNS) Database |  |
| RFC 3404 | Dynamic Delegation Discovery System (DDDS) Part Four: The Uniform Resource Identifiers (URI) |  |
| RFC 3405 | Dynamic Delegation Discovery System (DDDS) Part Five: URI.ARPA Assignment Procedures |  |
| RFC 3761 | The E.164 to Uniform Resource Identifiers (URI) Dynamic Delegation Discovery System (DDDS) Application (ENUM) |  |
| STD 13 | Domain Name System | Recommended |
| ANSI INCITS 359-2004 | Role Based Access Control (RBAC) | Recommended |
| OASIS Security Technical Committee | SAML 2.0: Security Assertion Markup Language Version 2.0 | Recommended |

 

## Firewall Traversal

A major barrier to
dynamic, cross-domain Grid computing today is the existence of firewalls. As
noted above, firewalls provide limited value within a dynamic Grid environment. However, it is also the case that firewalls
are unlikely to disappear anytime soon. Thus, the OGSA security model must take
them into account and provide mechanisms for cleanly traversing them—without
compromising local control of firewall policy.

There are several
major issues with the use of firewalls:

·      
Firewalls are typically invasive and perform address translation without
providing a useable audit record.

·      
Firewalls that have the ability to perform state-based inspection are
not capable of analyzing the complex protocols that IntelliGrid Architecture is considering.

·      
Firewalls are difficult to manage and must be monitored as part of the
SMI process.

However, firewalls
are deployed in order to protect critical infrastructure computational
resources and should be deployed at inter-domain connectivity points. 

Within the context
of IntelliGrid Architecture environment, there are several different functions that a firewall
could provide.  It is a policy/deployment issue in regards to which ones
are provided.

·      
Media Isolation: Provides physical isolation from the extranet to the intranet
of the security domain.  This typically means that two physical media
interfaces are required.  It is worthy to note that bridges and most
routers have two physical interfaces and therefore could be used to provide the
media isolation in a deployment scenario.  
  
It is recommended that media isolation be provided for all firewalls.

·      
Address Translation: It is often difficult to protect an intranet if the
addresses of that intranet are the same as and accessible of the
extranet.  It is worthy to note that some routers have this capability.  
  
It is recommended that each firewall transversal include address translation if
access control is not implemented.

·      
Protocol/Port Restriction:  One of the main purposes of a firewall
is to restrict what type of communications can occur in-bound/out-bound through
the firewall.  Typically, domain firewalls should be configured to allow
only the communication traffic set by policy.  This is typically done via
port restriction or some other means.  
  
It is recommended that all firewalls deployed have the capability to restrict
incoming protocol traffic.  It is a policy issue if restriction of
outgoing traffic is needed.

·      
Audit:  Although many firewalls do not provide adequate audit
capability, this is a mandatory function.  It is recommended that all
address pair (e.g. extranet/intranet pair establishment) be logged into an
audit record.  Additionally, if the protocol/port identification can be
provided in the record, as well as identity, this would also be recommended.

·      
Identity Establishment:  This function allows a firewall to
establish the identity of an external entity in order to establish trust.

·      
Access Control:  The ability to make use of the established
identity in order to restrict access to intranet resources.

·      
Confidentiality:  The ability for a firewall to encrypt
inter-domain information (typically done via establishment of a VPN).

·      
State based inspection: The firewall has a knowledge of the protocol and
therefore makes use of the identity established and Access Control to determine
which protocol packets to forward to the intranet.

### Technological Assessment and Relevant Specifications

There are three
major types of firewalls:

·      
Transparent (see FIRE-01 and FIRE-02): These firewalls perform OSI layer
2 or 3bridging and do not typically provide state
inspection.  However, they do not obscure addressing information and
tend to be the fastest type of firewall when performance is measured in terms
of packet throughput.  Since these are transparent, these types are the
easiest to transverse when properly configured.    
  
This is the only firewall type that could possible meet the 4msec performance
requirement.

·      
Non-Transparent: These firewalls typically perform the following
functions:  packet filtering and proxy service (e.g. address translation).

·      
Non-Transparent with Stateful Inspection: Same
capability as non-transparent but has the additional ability to examine the
contents of each packet.  This is typically the lowest performance type of
firewall when performance is measured in regards to packet throughput.

Firewall
Transversal is automatically provided when Transparent Firewalls are utilized,
however the issue still remains for both versions of non-transparent firewalls.
The typical mechanism for allowing transversal (e.g. from outside a Security
Domain to inside) is via a proxy service or a set of firewall supplied cookies.
However, there are several issues about sending/receiving such information in
the clear. Therefore, encryption is desired.

Current firewall
transversal thoughts are to create a SSL/TLS tunnel (thereby verifying the
remote node has certain access rights) and then using a internal proxy to
enforce further privilege restrictions.

if !vml?![](IECSA_VolumeIV_AppendixA_files/image011.jpg)endif?

Figure 3: Example
of SSL/TLS Tunnel for Firewall Transversal[[5]](IECSA_VolumeIV_AppendixA.htm#_ftn5)

Figure 3 shows the
SSL tunnel being used to a DMZ where the backend application data is proxied on servers located within the DMZ.  It would
also be possible to allow stateful and privilege proxy access directly
to the back-end data providers if needed.  Either
architecture is viable and will be up to the Security Domain to decide
which best meets its needs.

 

Whatever the
choice, the functional characteristics found in RFC 2979 should be provided.

Table 18:
References regarding Firewall Transversal

|  |  |
| --- | --- |
| FIRE-01 | Matthew Tanase, **Transparent,** Bridging and In-line Firewall Devices,October 15, 2003  Available from:  <http://www.securityfocus.com/infocus/1737> |
| FIRE-02 | Transparent Cisco IOS Firewall  Available from: http://www.cisco.com/univercd/cc/td/doc/product/software/ios123/123newft/123t/123t\_7/  gt\_trans.htm |

 

Table 19: Relevant
Specifications regarding Firewall Transversal

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| RFC 1579 | Firewall-Friendly FTP |  |
| RFC 1919 | Classical versus Transparent IP Proxies | Recommended Reading |
| RFC 2008 | Implications of Various Address Allocation Policies for InternetRouting | Recommended Reading |
| RFC 2401 | Security Architecture for the Internet Protocol |  |
| RFC 2505 | Anti-Spam Recommendations for SMTP MTAs |  |
| RFC 2543 | SIP: Session Initiation Protocol |  |
| RFC 2547 | BGP/MPLS VPNs |  |
| RFC 2764 | A Framework for IP Based Virtual Private Networks |  |
| RFC 2775 | Internet Transparency | Recommended Reading |
| RFC 2888 | Secure Remote Access with L2TP |  |
| RFC 2977 | Mobile IP Authentication, Authorization, and Accounting Requirements |  |
| RFC 2979 | Behavior of and Requirements for Internet Firewalls | Recommended |
| RFC 2993 | Architectural Implications of NAT | Recommended Reading |

 

## Identity Establishment Service

An identity establishment
(e.g. identity authentication) service is concerned with verifying proof of an
asserted identity. The implementation of the service must allow for 
multiple identity authentication mechanisms (e.g. identity tokens) to be utilized. Additionally, the service needs to
provide a mechanism to allow the information from various identity
tokens/identity authentication mechanisms to be electronically conveyed.

The requirement
that the Identity Establishment service be agnostic in regards to technology
can be easily demonstrated.  One Security Domain may make use of a User
ID/password combination as a identity token. Another Security Domain may
require the use of Kerberos based identity tokens.  It is the Security
Management Infrastructure (SMI) and the Security Domain’s security policies
that will determine the actual identity token(s) used and the mechanism(s)
through which they are conveyed.

Key defintitions:

**identity
authentication:** The performance of tests to enable a [data processing](http://www.atis.org/tg2k/_data_processing.html) [system](http://www.atis.org/tg2k/_system.html)
to recognize entities. Note: An example of identity [authentication](http://www.atis.org/tg2k/_authentication.html) is the checking of a [password](http://www.atis.org/tg2k/_password.html)
or [identity token](http://www.atis.org/tg2k/_identity_token.html). [2382-pt.8]

**identity
token: 1.** A device, such as a metal [key](http://www.atis.org/tg2k/_key.html)
or [smart card](http://www.atis.org/tg2k/_smart_card.html), used for [identity authentication](http://www.atis.org/tg2k/_identity_authentication.html).
[After 2382-pt.8] **2.** [A] Smart card, metal key, or other physical object
used to [authenticate](http://www.atis.org/tg2k/_authenticate.html) identity. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99]

**identity
validation:** Tests enabling an [information system](http://www.atis.org/tg2k/_information_system.html)
to [authenticate](http://www.atis.org/tg2k/_authenticate.html) users or
resources. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99]

 

### Identity Establishment for Physical Assets

Physical access control
should be based upon multi-factor Identity Establishment.  The use of
multi-factor authentication, using the appropriate technologies can provide a
significant security advantage above and beyond simple identity
cards.  Additionally, the selectionand creation of physical access
control policies and procedures would needs to include the capability to manage
and revoke access privileges easily.  This would typically indicate the
need for some type of token/id that can be managed/changed.  However, if
only the picture matching the holder of the identity card determines access,
there is a high probability that such access control mechanisms can be
falsified.  Thus, to improve access security there should be another
security factor used in order to authorize access.

 

This “other-factor”
should be “something the individual knows” (e.g. username/password) or
combination code.  However, typically username/passwords or combination
codes can be compromised through observation or garbage diving. 
Therefore, it would be recommended that some type of electronic mechanism, with
verification/challenge be implemented.  The most widely deployed example
of this would be the use of a Smart-ID card (e.g. a card that electronically
authorizes the holder to enter a combination and that explicitly bound to the
identity of the holder) and a combination lock.  Only the proper Smart-ID
badge authorization allows the combination to be entered into the lock which
then enable access.  The side benefit of the use of such technology is
that an audit trail of access can be created electronically. 
Additionally, management issues (especially revocation of access privileges)
are eased since the Smart-ID card can be revoked thereby disallowing access.

 

Should a Security
Domain decide to perform electronic auditing of physical access (recommended),
then appropriate audit trail time-stamping techniques need to be utilized (see
the audit service section).

### Computational Resources

Identity
establishment, for computational resources, is directly related to the types of
credentials that are in use within a Security Domain.  The definition of
the credentials that IntelliGrid Architecture may be using may be found in the Credential Renewal
section (see page 23).  The credential types
used to establish identity are: addresses and address resolution,
username/passwords, smart cards, digital certificates, and biometric
identifications.

The issue with
computational resource identification establishment is that of architecting a
solution that creates a framework for authentication. Table 20 and Table 21
list relevant references and specifications that may aid in the construction of
such a framework within a security domain.

 

Table 20: General
References Regarding Identity Establishment and Identity Infrastructure

 

**A National-Scale Authentication
Infrastructure**. R. Butler, D. Engert, I.
Foster, C. Kesselman, S. Tuecke,
J. Volmer, V. Welch. *IEEE Computer*, 33(12):60-66, 2000.

 

**An Online Credential Repository for the Grid: MyProxy**. J.
Novotny, S. Tuecke, V. Welch. *Proceedings of the Tenth International Symposium on
High Performance Distributed Computing (HPDC-10)*, IEEE Press,
August 2001.

 

**A Community Authorization Service
for Group Collaboration**. L. Pearlman, V. Welch, I. Foster, C. Kesselman, S. Tuecke. *Proceedings of the IEEE 3rd International Workshop
on Policies for Distributed Systems and Networks*, 2002.

 

**X.509 Proxy Certificates for
Dynamic Delegation**. V. Welch, I. Foster, C. Kesselman,
O. Mulmo, L. Pearlman, S. Tuecke,
J. Gawor, S. Meder, F. Siebenlist. *3rd
Annual PKI R&D Workshop*, 2004.

 

**Introduction to Public Key
Technology and the Federal PKI Infrastructure,** **February 26, 2001****, NIST.**

**Available from:
http://www.cccure.org/Documents/PKI/NIST\_pkidraft.pdf**

 

Table 21: Relevant Specifications
regarding Identification Frameworks

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| ISO/IEC 10181-2:1996 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Authentication framework | Recommended |
| ISO/IEC 10181-4:1997 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Non-repudiation framework | Recommended |
| ISO/IEC 10181-1:1996 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Overview | Recommended |
| ISO 10202-8:1998 | Financial transaction cards -- Security architecture of financial transaction systems | Recommended Reading |

 

### *Technological Assessment and Relevant Specifications*

The following
section discusses issues and potential general resolution to the issues
regarding the use of any particular identification mechanism. In general,
two-factor authentication is desired.

#### General Technologies

##### Address Resolution

The most prevalent issue in using address
resolution as an identification mechanism is address spoofing.  This
attack is easy to generate and is well documented.  Therefore, such a identification
mechanism should not be used on its own.  It must
be augmented with anotherfactor to actually
establish the identity.

Address resolution
is a worthwhile qualifier for actions/information exchanges that are only
supposed to occur between certain peers.  However, this is not a
reasonable mechanism for inter-domain exchanges since neither domain controls
the other domain’s address allocation/changes.

##### Username/Password

This is a typical
mechanism employed by Web based interfaces (especially for customers
interfacing for retrieval of billing information).  However, the use of
cookies or password caches (e.g. the prompt to remember the username password)
represents an issue that should be addressed by the
addition of a challenge/response mechanism.

The challenge
response should be user selectable/definable so that they can remember the
response when prompted.

##### Smart Cards

The references
given previously in this section give a large amount of guidance in the
selection of SMART-CARDS that can be used in the implementation of physical or
cyber access control.  The smart card industry embraces ISO 7816 as one of
the prevalent smart card specification and this is
the recommended base specification for smart cards.

However, ISO 7816
does not specify a programmatic interface to such cards that is portable. 
Therefore, it is recommended that the Java Card Platform Specification be used
in conjunction with ISO 7816 technology.

The remaining issue
is how much storage to deploy on the smart cards.  The Gartner Group
published the information found in Figure 4.  At this juncture there is no
recommendation in regards to the amount of storage to deploy.

Table 22: Relevant
Standards Concerning Smart Cards

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| ISO/IEC 7816-1:1998 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 1: Physical characteristics |  |
| ISO/IEC 7816-10:1999 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 10: Electronic signals and answer to reset for synchronous cards |  |
| ISO/IEC 7816-11:2004 | Identification cards -- Integrated circuit cards -- Part 11: Personal verfication through biometric methods |  |
| ISO/IEC 7816-15:2004 | Identification cards -- Integrated circuit cards with contacts -- Part 15: Cryptographic information application |  |
| ISO/IEC 7816-3:1997 | Information technology -- Identification cards -- Integrated circuit(s) cards with contacts -- Part 3: Electronic signals and transmission protocols |  |
| ISO/IEC 7816-3:1997/Amd 1:2002 | Electrical characteristics and class indication for integrated circuit(s) cards operating at 5 V, 3 V and 1,8 V |  |
| ISO/IEC 7816-4:1995 | Information technology -- Identification cards -- Integrated circuit(s) cards with contacts -- Part 4: Interindustry commands for interchange |  |
| ISO/IEC 7816-4:1995/Amd 1:1997 | secure messaging on the structures of APDU messages |  |
| ISO/IEC 7816-5:1994 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 5: Numbering system and registration procedure for application identifiers | Highly recommended reading as part of the management (e.g. User/Group Management service) |
| ISO/IEC 7816-7:1999 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 7: Interindustry commands for Structured Card Query Language (SCQL) (available in English only) |  |
| ISO/IEC 7816-8:1999 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 8: Security related interindustry commands |  |
| ISO/IEC 7816-9:2000 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 9: Additional interindustry commands and security attributes |  |
| Java Card | Java Code Smart Card API | Can make use of ISO 7816 Based  smart cards. Referenced by Global Platform and ETSI. |
| Java Card | Java Card Platform Specification v 2.2.1    Available from:  http://java.sun.com/products/javacard/specs.html |  |
| NIST GSC-IS | The NIST Interagency Report 6887 - 2003 edition (Government Smart Card-Interoperability Specification) Version 2.1  Available from:  http://csrc.nist.gov/publications/nistir/nistir-6887.pdf | Recommended Reading. Specifies the use of ISO 7816 GSM based implementations. |
| Smart Card Alliance | Smart Card Primer    Available from: http://www.smartcardalliance.org | Recommended Reading |
| Smart Card Alliance | Privacy and Secure Identification Systems: The Role of Smart Cards as a Privacy-Enabling Technology ­     Available from: http://www.smartcardalliance.org | Recommended Reading |
| Smart Card Alliance | Government Smart Card Handbook    Available from: http://www.smartcardalliance.org | Recommended Reading. Specifies the use of ISO 7816 based implementations. |

 

if !vml?![](IECSA_VolumeIV_AppendixA_files/image013.jpg)endif?

Figure 4: Estimated
Smart Card Storage Costs

##### Digital Certificates

The industry
accepted digital certificate is an X.509 certificate.  This is the
certificate format that should be used by IntelliGrid Architecture when applicable.  There
are some issues in identifying a certificate:

·      
There is an issue in regards to how to uniquely identify a
certificate.  There are many fields that could be used, however only the certificate Thumbprint is truly unique.  All other
fields could be non-unique.  Therefore, it is the thumbprint that should be
used to identify and match certificates.

·      
Enunciation of lifetime expiration (see Credential Renewal service).

·       Policy
issues in regards to use will need to be addressed.  The NERC e-Marc
certificate policy discusses many of these issues. It is recommended that the
e-Marc policy be used as a basis for certificate usage.    
  
It is worthwhile to note that the NERC policy does not allow the same
certificate to be duplicated.  Should a security domain adopt this as a
policy, the number of certificates required (e.g. in the case of redundancy)
will be higher.

·      
A policy in regards to how applications should react in the case that an
in use certificate is revoked.  
  
Revocation is basically caused when the integrity of a certificate has been compromised
(e.g. the private certificate may have been stolen).  Since none of the
revocation protocols give a indication that could be used to determine if the
certificate was compromised prior to use, the safe option is to terminate use
of the certificate upon revocation.  This may cause information exchange
to be terminated if fail-over procedures are not made part of the policy.

 

Table 23: Public
Key Infrastructure (PKI) Related Specification/Standards

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| RFC 2898 | PKCS #5: Password-Based Cryptography Specification Version 2.0.     B. Kaliski. September 2000. |  |
| RFC 2985 | PKCS #9: Selected Object Classes and Attribute Types Version 2.0.      M. Nystrom, B. Kaliski. November 2000. |  |
| RFC 2986 | PKCS #10: Certification Request Syntax Specification Version 1.7.     M. Nystrom, B. Kaliski. November 2000. |  |
| RFC 3280 | Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile |  |
| ISO/IEC 9594-8:1998 | Information technology -- Open Systems Interconnection -- The Directory: Authentication framework | Definition of X.509 Certificate is found here. |
| ISO/IEC 9594-8:2001 | Information technology -- Open Systems Interconnection -- The Directory: Public-key and attribute certificate frameworks |  |
| X.521 | PKI - Digital certificates and certificate revocation lists profiles |  |
| NERC | Certificate Policy for the Energy Market Access and Reliability Certificate (e‑MARC) Program Version 2.4  Available from:  ftp://www.nerc.com/pub/sys/all\_updl/cip/pkitf/e-MARC-PKI\_draft\_version\_V2-4b\_March\_2003-rev1.doc |  |

##### Digital Signatures

Typically
considered a subset of Digital Certificates, as certificates are required in
order to digitally sign, these have their own benefit for identification
purposes.  In instances where bandwidth or packet size is a limiting
factor, a digital signature can be used in place of a certificate.

In IEC 61850, for
GOOSE, this signature, in conjunction with address
resolution would provide two-factor authentication if properly
implemented.  However, this raises the issue that:

·      
Digital signatures should not repeat often in order to prevent spoofing.

There
are several different interpretations in regards to what a digital signature
is.   
  
It is recommended that RFC 2313 be used as the definitive definition for a
digital signature algorithm:  
  
“For digital signatures, the content to be signed   is first reduced
to a message digest with a  message-digest algorithm (such as MD5), and
then an octet string containing the message digest is encrypted with the RSA
private key of the signer of the content. The content and the encrypted message
digest are represented together according to the syntax in PKCS #7 to yield a
digital signature.”  
  
However, it is recommended that RFC 2437 be the actual Cryptography
specification used[[6]](IECSA_VolumeIV_AppendixA.htm#_ftn6)

 

Table 24: Relevant
Specifications for Digital Signatures

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| RFC 2313 | <http://www.armware.dk/RFC/rfc/rfc2313.html>PKCS #1: RSA Encryption Version 1.5 |  |
| RFC 2315 | PKCS #7: Cryptographic Message Syntax Version 1.5 |  |
| RFC 2437 | PKCS #1: RSA Cryptography Specifications Version 2.0 |  |

 

##### Biometrics

There is a large
body of biometric work occurring.  The standards development is largely
being performed in ISO JTC1 SC37.  The total scope of work can be obtained
from [www.jtc1.org](http://www.jtc1.org/). 
However, some of the major work items have been included in Table 25. The major
focus of ISO JTC1 SC37 is focused on the biometric aspects of fingerprints
and facial images.  However, from a practical perspective fingerprint
biometrics represents a much lower cost alternative than facial and therefore
would be recommended for IntelliGrid Architecture deployment.

It is also
suggested that the biometric data be encoded on a smart-card so that two-factor
authentication is achievable using the appropriate NISTIR 6529
specified/registered format.

The use of
biometric based authentication mechanisms is becoming acceptable due to the
cost of the technology becoming lower.  There are four biometric
technologies that have been or are being used:

·      
Voice:  Although this is a type of biometric identification, it has
proven to be weak since recording and replay of the key identification
phrase(s) could allow such an authentication system to be spoofed[[7]](IECSA_VolumeIV_AppendixA.htm#_ftn7).

·      
Fingerprint: There are now electronic mice and locks that are relatively
low cost that can make use of fingerprints as a biometric.  However, there
are multiple competing standards for the metrics that determine what
information needs to be stored (e.g. to represent a fingerprint).  It is
recommended that this technology be used due to its
cost/benefit ratio.

·      
Facial: Facial biometrics could prove to be the biometric technology of
the future.  However, current technology yields has proven to produce
false positives (e.g. identify one individual as being another). The technology
previously needed for facial scanning was difficult, but the technology is
migrating to WebCam like cameras that will lower the
cost of such biometrics. Based upon this trend, the federal government
announced its intent to produce passports with facial biometric information[[8]](IECSA_VolumeIV_AppendixA.htm#_ftn8).  
  
It is recommended that facial biometrics be considered once the federal system
is proven.

·      
Retinal/Iris pattern mathing: This biometric
is one of the most difficult to spoof, but also one of the most costly to
deploy.  The cost/benefit ratio is questionable within IntelliGrid Architecture
environment.

·      
Hand Geometry: This biometric is one of the most
difficult to spoof, but also one of the most costly to deploy.  The
cost/benefit ratio is questionable within IntelliGrid Architecture environment.

Biometric exchange
formats have now been coordinated under one governing umbrella, the
International Biometric Industry Association (IBIA, www.ibia.org).

Table 25: Relevant
References regarding Biometrics

|  |  |
| --- | --- |
| Global Analytic Information Technology Services | **Fingerprint Recognition**  **Available from:** <http://www.gaits.com/biometrics_fingerprint.asp> |
|  | **Ralph Gross, Quo Vadis Face Recognition? The current state of the art in Face Recognition**    **Available from:** <http://dagwood.vsam.ri.cmu.edu/FaceRecognition/> |
|  | **Philip E. Agre, Your Face is Not a Bar Code: Arguments Against Automatic Face Recognition in Public Places.** |
| ISO JTC1 SC37 | **SD 2 – Harmonized Biometric Vocabulary** |
| ISO JTC1 SC37 | **1.37.19784.1 BioAPI – Biometric Application Programming Interface** |
| ISO JTC1 SC37 | **1.37.19794 – Biometric Data Interchange Format** |
| ISO JTC1 SC37 | **1.37.1974.3 Biometric Data Interchange Format – Part 3: Finger Pattern Spectral Data** |
| ISO JTC1 SC37 | **1.37.1974.4 Biometric Data Interchange Format – Part 4: Finger Image Data** |
| ISO JTC1 SC37 | **1.37.1974.5 Biometric Data Interchange Format – Part 5: Face Image Data** |
| NISTIR 6529 | **Common Biometric Exchange File Format (CBEFF)**    **Available from: http://www.nist.gov/cbeff** |

 

Table 26: Relevant
Specification regarding Biometrics and Smart Cards

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| ISO/IEC 7816-11:2004 | Identification cards -- Integrated circuit cards -- Part 11: Personal verification through biometric methods | Recommended Reading |

 

#### Specific Technologies

##### Relational Databases

The use of
relational databases merits discussion in regards to identity
establishment.  The first issue that needs to be resolved is the
definition of what is a relational database.  For the purposes of this
document, relational databases shall be constrained to any database that
conforms to ANSI X3.135-1989 (SQL’89), ANSI X3.135-1992
(SQL’92), or ANSI X3-135-199x (SQL3- still under
development).

“The
basic security model of SQL consists of three entities: objects, actions, and
users. Objects are defined in the database schema. In SQL'89, the objects are
tables, views, columns of tables, and columns of views. In SQL'92, the objects
also include domains and assertions. In SQL3, objects will include user defined
constructs….

A
privilege is an authorization to a user of an action on an object. A privilege
is a 5-tuple:

(grantor,
grantee, object, action, grantable)….

….some
of these implementations, the user name and password make up the user
identification string in the SQL connect command and this string is passed in
plain text across the network. From a security point of view, that this string
is passed in plain text is not good practice.”[[9]](IECSA_VolumeIV_AppendixA.htm#_ftn9)

 

Obviously, the use
of plaintext being transmitted across a network IS NOT ACCEPTABLE. 
Therefore, it is recommended that encryption, preferably provided via TLS, be
used.

##### Web Based User Interfaces

There are many
current devices (e.g. the GE UR Relay and others) that embed Web servers that
provide a monitoring and configuration setting
interface.  These definitely need to be secured via some identification
mechanism.  Currently username/passwords are used without
challenge/response. 

It would be
recommended that these interfaces implement a
challenge/response mechanism or be converted to make use of SOAP Web
Services with the appropriate Digital Signature SOAP security (Certificate
based).  It is also recommended that the digital signature be used in
conjunction with encryption provided by TLS.

Table 27: Relevant
Technologies for Web Based User Interfaces

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| W3C | SOAP Security Extensions: Digital Signature | Recommended |

 

## Identity Mapping Service

The identity
mapping service provides the capability of transforming an identity which
exists in one identity domain into a identity within another identity domain.
It is worthwhile to note that there may be multiple
identity domains within a single Security Domain.  There is an additional
attribute to identity mapping, the mapping may result in
either a mapping of a individual into another set of credentials that represent
the individual (but for a different resource) or in a mapping to a role/group
based identity for the resource.

 As an
example, consider an identity in the form of an X.500 Distinguished Name (DN),
which is carried within a X.509v3 digital certificate. The combination of the
subject DN, issuer DN and certificate serial number may be considered to carry
the subject’s or service requestor’s identity. The scope of the identity domain
in this example is considered to be the set of certificates that are issued by
the certificate authority. Assuming that the certificate is used to convey the
service requestor’s identity the identity mapping service via policy may map
the service requestor’s identity to a identity which has meaning (for instance)
to the hosting environment’s local platform registry. The identity mapping
service is not concerned with the authentication of the service requestor;
rather it is strictly a policy driven name mapping service.

The Identity
Mapping can occur due to Credential Conversion or local/programmatic
reasons.  The major issues with Identity Mapping are very similar to the
issues in Credential Conversion:

·      
There needs to be an audit mechanism inserted into the mapping process
so that the originator of the transaction can be identified if needed.

 

### Technological Assessment and Relevant Specifications

Relevant
specifications and references may be drawn from the Identity Establishment,
Credential Conversion, and Firewall Transversal services.  In order to be
concise, they will not be repeated in this section.  This section will
only contain additional recommendation above and beyond the other service
recommendations.

 

#### Address Mapping

It is recommended that Network Address
Translation be used as part of the non-Transparent Firewall deployment. 
However, in the use of NAT or most non-Transparent firewalls, there is an issue
of providing a proxy for multiple “protected addresses” into the public address
space.  It is recommended that firewalls be evaluated for their capability
to proxy and map multiple addresses as it may save
deployment and management cost.

 

#### UserName/Password

Although there are
no relevant standards/specifications pertaining to this issue, the most natural
mapping service is through the use of single sign-on (SSO).  However, this
does not truly represent the true Identity Mapping (although it is credential
mapping).

#### Digital Certificates

See the discussion
in the Credential Conversion service discussion.

## Information Integrity Service

Ensure that unauthorized
changes made to messages or documents may be detected by the recipient. The use
of message or document level integrity checking is determined by policy, which
is tied to the offered quality of the service (QoS).

Key definitions:

**integrity:** [In [INFOSEC](http://www.atis.org/tg2k/_infosec.html),
the] quality of an[information
system](http://www.atis.org/tg2k/_information_system.html) (IS) reflecting the
logical correctness and [reliability](http://www.atis.org/tg2k/_reliability.html) of
the [operating
system](http://www.atis.org/tg2k/_operating_system.html); the logical
completeness of the [hardware](http://www.atis.org/tg2k/_hardware.html) and [software](http://www.atis.org/tg2k/_software.html)
implementing the [protection](http://www.atis.org/tg2k/_protection.html)
mechanisms; and the consistency of the [data](http://www.atis.org/tg2k/_data.html)
structures and occurrence of the stored data. Note that, in a formal [security](http://www.atis.org/tg2k/_security.html) [mode](http://www.atis.org/tg2k/_mode.html),
integrity is interpreted more narrowly to mean protection against unauthorized
modification or destruction of information. [INFOSEC-99]

The first thought, when it comes to
Integrity, is that it is the same issue as Confidentiality.  However, the
Confidentiality Service provides protection from information disclosure not the
detection of information modification.  It is the protection from
information modification that the Integrity Service represents.

In order to provide message integrity a
algorithm that generates a result similar to a CRC needs to executed and
imbedded in the message.  However, this alone will not guarantee integrity
as a man-in-the-middle attack could change the message, recalculate the CRC,
and then forward the message. 

In order to prevent man-in-the-middle
attacks, a digital signature is typically used on the CRC like result and both
are embedded in the message.  It is this digital signature “seal” that
actually prevents the attack.  Such signatures are typically referred to
as Message Authentication Codes (MACs) and it is
recommended that the Integrity Service be implemented through the use of such
techniques.

## Inter-Domain Security

This service represents the capability to
provide additional security services, as needed, in order to facilitate
inter-domain information exchanges.   These additional security
services may not typically be required for intra-domain exchanges

The additional security services that must be
provided for Inter-Domain security are:

·       Confidentiality

·      
Credential Conversion

·       Delegation

·       Firewall Transversal

·       Identity Mapping

·       Security against Denial of
Service

Additionally, a much more robust audit
mechanism should be instituted at the inter-domain boundaries.

 

## Non-repudiation

This service represents the ability of a
security domain to provide proof that a given exchange action has
occurred.  This ability is used to resolve disputes with other entities
that claim that the action did not occur, thus non-repudiation.  In order
to provide this service, a strong audit service must be present within the security
domain.

Keydefinition:

**re****pudiation:**
In cryptosystems, the denial by one of the entities involved in a communication
of having participated in all or part of the communication.

 

In order to provide this service, strong
audit capabilities need to be in place for Identity Establishment, Access
Control, Credential Conversion, and Identity Mapping.  Without an
appropriate level of audit capability on these other services, non-repudiation
will not be able to be performed.

Non-repudiation is typically a manual process
of retrieving the relevant audit records, analyzing those records, creating a
report that summarizes those records and the conclusion.  Thus, strong
policies and procedures must be put in place to accomplish non-repudiation as
well.

 

### Technological Assessment and Relevant Specifications

Table 28 shows the relevant specifications
regarding non-repudiation.  In order to provide the non-repudiation
service, it is suggested that a non-repudiation framework similar to what is
specified in ISO/IEC 10181-4 be created.  It is further recommended that
SAML be used and the non-repudiation capabilities of
SAML be integrated into the created framework.

 

Table 28: Relevant Specification regarding
non-repudiation

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| ISO 9735-5:2002 | Electronic data interchange for administration, commerce and transport (EDIFACT) -- Application level syntax rules (Syntax version number: 4, Syntax release number: 1) -- Part 5: Security rules for batch EDI (authenticity, integrity and non-repudiation of origin) |  |
| ISO/IEC 10181-4:1997 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Non-repudiation framework | Recommended |
| ISO/IEC 13888-1:1997 | Information technology -- Security techniques -- Non-repudiation -- Part 1: General | Recommended Reading |
| ISO/IEC 13888-2:1998 | Information technology -- Security techniques -- Non-repudiation -- Part 2: Mechanisms using symmetric techniques |  |
| ISO/IEC 13888-3:1997 | Information technology -- Security techniques -- Non-repudiation -- Part 3: Mechanisms using asymmetric techniques |  |
| ISO/IEC TR 13335-5 | Information technology - Guidelines for the management of IT Security - Part 5: Management guidance on network security |  |
| WC3 | XML Key Management Specification (XKMS 2.0) Bindings |  |
| OASIS Security Technical Committee | Bindings for OASIS Security Assertion Markup Language (SAML) V2.0  Available from:  http://www.oasis-open.org/committees/download.php/6773/sstc-saml-bindings-2.0-draft-11-diff.pdf | Draft that specifies how to bind SAML over various protocols. Highly recommended. |

 

## Path Routing and QOS service

This service represents the ability of a
security domain to applications with the ability to request that a set of
transactions be conveyed over a specific communication path with specific
Quality of Security (QS) being provided.  Such a service may be used in
conjunction with many of the other security services.

There are two major issues
that need to be resolved:

·       The ability to specify the
actual communication path that a given transaction will use.  
  
This type of ability is a direct contradiction to the normal dynamic routing inherent
in most networks, thus normal network infrastructures may not be able to be
used.

·       The ability
to request a Quality of Security to be guaranteed over that path.

### Technological Assessment and Relevant Specifications

#### Communication Path Definition

Although there are several IETF RFCs
regarding the ability to perform this function (e.g. RFC 1940), few if any of
the operating system APIs allow the full path specification to occur.  In
reality, the source routing bit can be set TRUE and the packet will be
delivered to the peerwith the path hop information
embedded within it.Such a mechanism could
allow the receiver to determine if a packet was delivered over an
acceptable path, and this is a useful check.

However, the ability to actually pre-determine
the path that a packet will transverse falls upon manual configuration of
static routing.  It is the this static routing that can actually allow
policy to dictate what route a given communication packet will take. 
Typically, this is a configuration option in Firewalls or Operating
Systems.  Thus it is incumbent upon the SMI function to provide the
appropriate configuration.

#### Quality of Security

There are no known Quality of Security
standards/specifications available to allow packet routing based upon a
requested level of security.  Development of a similar specification to
RFC 2386 (Quality of Service based Routing) is recommended.

 

Table 29: Relevant Specifications for the
Path Routing Service

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| RFC 1102 | Policy routing in Internet protocols | Highly Recommended |
| RFC 1322 | A Unified Approach to Inter-Domain Routing |  |
| RFC 1940 | Source Demand Routing: Packet Format and Forwarding Specification (Version 1) | Highly Recommended |
| RFC 2386 | A Framework for QoS-based Routingin the Internet | Highly Recommended |
| RFC 2725 | Routing Policy System Security | Highly Recommended |

 

## Policy

The policy service and policy
processes/guidance can be found in Section **Policy** starting on page 43.

 

## Policy Exchange

Allow service requestors and providers to
exchange dynamically security (among other) policy information to establish a
negotiated security context between them. Such policy information can contain
authentication requirements, supported functionality,
constraints, privacy rules etc.

Typically, there has been no defined
framework or policy exchange mechanism available
that is technology neutral and therefore such exchanges have not occurred or
have been performed manually.  There are several issues that have
prevented the development of such a framework:

·       Agreement in regards to what
constitutes security policy varies.  Therefore, such an exchange mechanism
would need to provide basic attribute definitions and also allow for a large
amount of customization.

·       There has not been a single
secure and ubiquitous technology available over which to perform such an
exchange.

 

### Technology Assessment and Relevant Specifications

When analyzing how to exchange policies in IntelliGrid Architecture environment, the problem of having a ubiquitous technology has not been
solved.  There still does not appear to be a solution that can solve
policy exchange issues in the Transmission & Distribution environment
(especially serially connected devices), spanning to
databases, to web technology.  However, thereis emerging
specifications in how to perform such exchanges when web services/SOAP
infrastructures are available. 

For policy exchanges via SOAP, it is
recommended that the WS-Policy, WS-PolicyAssertions,
and WS-PolicyAttachment specifications form the basis
of such exchanges.  It is also recommended that customizations be kept to
a minimum in order to maximize interoperability and interworkability.

Table 30: Relevant Specification regarding Policy
Exchange

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| OASIS | Web Services Policy Framework (WS-Policy)  Available from:  http://xml.coverpages.org/ws-policyV11.pdf | Recommended |
| OASIS | Web Services Policy Assertions Language (WS-PolicyAssertions)  Available from:   http://xml.coverpages.org/ws-policyassertionsV11.pdf | Recommended |
| OASIS | Web Services Policy Attachment (WS-PolicyAttachment)  Available from:  http://xml.coverpages.org/ws-policyattachmentV11.pdf | Recommended |

## Privacy Service

The privacy service is primarily concerned
with the policy driven classification of personally identifiable information
(PII). Service providers and service requestors may store personally
identifiable information using the Privacy Service. Such a service can be used
to articulate and enforce a Security Domain’s privacy policy. Allow both a
service requester and a service provider to define
and enforce privacy policies, for instance taking into account things like
personally identifiable information (PII), purpose of invocation, etc. (Privacy
policies may be treated as an aspect of authorization policy addressing privacy
semantics such as information usage rather than plain information access.).

Many may consider privacy equivalent to
confidentiality/encryption, however this is not true.  In reality, privacy
is an issue regarding the PII after a secure transfer of that information
occurs.  The issue relevant, mostly to web technology, is how to determine
in advanced if the privacy offered by a web site is sufficient.

### Technological Assessment and Relevant Documents

A review of relevant information reveals that
there are many well know legal/legislative aspects to privacy and disclosure of
that information.  However, there is little relevant work in regards to
being able to determine and enforce the level of privacy electronically. 
The sole exception, that has maturity, is the P3P
specification from W3C.  References PRIV-01 and PRIV-02 are
recommended reading to allow the SMI/policy services to determine if P3P can be
used/monitored within the Security Domain.

Other work in this are is highly recommended.

Table 31: References Regarding Privacy

|  |  |
| --- | --- |
| PRIV-01 | Web consortium backs P3P privacy standard  Available from: http://www.cnn.com/2002/TECH/internet/04/18/p3p.privacy.idg/ |
| PRIV-02 | Web Privacy Standard: It's a Start  Available from: http://www.pcworld.com/news/article/0,aid,94544,00.asp |

 

Table 32: Relevant Specification regarding
Privacy

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| W3C | The Platform for Privacy Preferences 1.1 (P3P1.1) Specification  W3C Working Draft 27 April 2004 | Highly Recommended |
| Oblix | Guide to Regulatory Compliance and Privacy | Recommended |

## Profile Service (User Profile Service)

The profile service is concerned with
managing service requestor’s preferences and data
which my not be directly consumed by the authorization service.
This may be service requestor specific personalization data, which for example
can be used to tailor or customize the service requestor’s experience (if
incorporated into anapplication which interfaces with
end-users.) It is expected that primarily this data will be used by
applications that interface with a person. 

### Technological Assessment and Relevant Specifications

Research and experience indicates the web
user profiles are the trend.  To experience this, use any of the
commercial web portals (e.g. yahoo, msn, etc…).  These all offer the
ability to personalize the information displayed and the actual display
format.  However, it is doubtful that any of the current portaltechnologies make use of the Semantic Web specification.

It is recommended, when possible, that the
Semantic Web specification be utilized when possible.  If such an
implementation is not feasible or costly, it is recommended to implement based
upon some local means.

 

Table 33: Relevant Specifications regarding
the Profile Service

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| Semantic Web | Pervasive Computing Standard Ontology (PERVASIVE-SO) Guide -- Describing User Profile and Preferences    Available from: http://pervasive.semanticweb.org/doc/2004-01-ont-guide/part1/ | Highly Recommended |
| IEEE | IEEE Personal and Private Information (PAPI) draft standard |  |

## Quality of Identity Service

This service allows an entity to determine
the trust level associate with the identity being conveyed.  This is of
particular interest where the source Identity, of the original transaction, has
been mapped several times.

This service represents a specific capability
that could be viewed as a subset of the Identity Service.  However,technical evaluations of existing solutions indicate
that no solutions provide this ability and therefore are worthy of being
defined independently so that the service requirement is not lost.

This is a service that is not widely
recognized, although QID-01 makes a strong case for its need.  The basic
issue raised by QID-01 is that of the ability to trust an identity being
established if the identity has been mapped or its credentials converted
several times.  At a minimum, without a mechanism for originator
determination, there is a relevant issue.  However, originator
determination could be provided by and adequate audit mechanism, but this does
not assist the receptor of a transaction.  Thus there is a need to provide
a mechanism to allow the receptor to determine a level of trust based upon the
number of mappings that have occurred along the transaction path.

Table 34: References Relating to Quality of
Identity

|  |  |
| --- | --- |
| QID-01 | Audun Josang, An Algebra for Assessing Trust in Certification Chains, Telnor R&D  email: audun.josang@fou.telenor.no |

### Technological Assessment and Relevant Specifications

There are two aspects in regards to Quality
of Identity, the ability to determine the number of times that an identity has
been transformed, which is a superset of the number
of times that credentials have been converted.

There are no relevant specifications/solutions
that can be applied to the generalized identity mapping
issue, as many of these mappings are local issues. 

However, in the particular case of digital
certificate conversion, the SAML specification yields a possible solution.
However, the solution would require that attribute definitions and attribute
chaining be added to SAML’s use within IntelliGrid Architecture
environment.

There are no such solutions for
username/password and it may be worthwhile to develop such a specification
based upon the SAML principles.

For address based credentials, source routing
offers a potential solution (see Path Routing and QS service).

  

Table 35: Relevant Specification for the
Quality of Idenity Service

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| OASIS Security Technical Committee | Attribute Profiles for SAML 2.0  Available from:  http://www.oasis-open.org/committees/download.php/6344/sstc-hughes-mishra-baseline-attributes-03.pdf | Incomplete, but is on the correct track. |
| OASIS Security Technical Committee | SAML 2.0: Security Assertion Markup Language Version 2.0 | Recommended |
| OASIS Security Technical Committee | Bindings for OASIS Security Assertion Markup Language (SAML) V2.0  Available from:  http://www.oasis-open.org/committees/download.php/6773/sstc-saml-bindings-2.0-draft-11-diff.pdf | Draft that specifies how to bind SAML over various protocols. Highly recommended. |
| OASIS Security Technical Committee | Authentication Context  Available from:  http://www.oasis-open.org/committees/download.php/6539/sstc-saml-authn-context-2.0-draft-04a-diff.pdf | Draft that is needed to establish identity within a SAML environment. |

## Security against Denial-of-Service

This service is for assisting in preventing a
denial of service.  This is not a service that can be invoked
programmatically, rather it is a service that must be designed into the
capabilities of a Security Domain or the implementations deployed within the
domain.

Key definitions:

**denial of service: 1.** The prevention
of authorized[access](http://www.atis.org/tg2k/_access.html) to resources or the delaying of [time](http://www.atis.org/tg2k/_time.html)-critical [operations](http://www.atis.org/tg2k/_operations.html). [2382-pt.8] **2.** The result of any
action or series of actions that prevents any part of an [information system](http://www.atis.org/tg2k/_information_system.html) (IS) from functioning. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99]

The
overall issue is to understand what can allow denial-of-service and then to
take steps to mitigate the causes.  There are several general categories
of denial-of-service attacks that need to be well understood:

·      
Resource exhaustion: Resource exhaustion is a denial-of-service attack
that causes required resources to be un-available for the intended use when a
valid transaction needs to be processed. The recent SYN FLOOD attacks represents
a well known denial-of-service attack.  
  
Resources that can be exhausted are virtual connections, memory, serial ports,
TCP ports, etc.  However these could be generalized into two categories:
connectivity resources and computational resources. 

·      
Buffer overflow: This type of attack causes a memory overrun to occur
within a computational resource.  The end result is typically the
computational process terminates or becomes unstable.  In reality, this
attack exploits poorly implemented programs that actually allow for the overrun
to occur without being properly trapped.  Recent examples of this type of
attack are the PING OF DEATH and some attacks on SNMP.

·      
Protocol oversights: In some protocols, not all state transitions may be
defined.  Exploitation of such oversights could allow a denial of service
attack to cause a protocol deadlock situation.  
  
As an example, from STD 62 (SNMP):

“Denial
of Service

A
Security Model need not attempt to address the broad range of attacks by which
service on behalf of authorized users is denied.  Indeed, such
denial-of-service attacks are in many cases indistinguishable from the type of
network failures with which any viable management protocol must cope as a
matter of course.”

Basically
is a statement that no DOS countermeasures need to be taken within the
specification.  This is typical of most standards.

·      
Improper Coding Practice:  Both the Buffer Overflow and Protocol
Oversight threats are sub-categories of the improper coding practice
category.  However, this category includes improper use of semaphores,
threads, etc.  that could be utilized to decrease performance/resource
available to the point that a valid transaction could not be processed in a
timely manner.

### Technological Assessment and Relevant Specifications

In
order to provide a denial-of-service attack protection, inter-domain connection
points need to be well-designed and monitored.

For
connectivity resources, it is recommended that timeouts be implemented that are
based upon valid traffic being transmitted/received through the connection
point.  Additionally,it is recommended that
through policy or coding practice that a peer remote be limited to the
number of connectivity resources that it is allowed to consume.

For
protocol oversights, it is recommended that prior to implementation the
protocol(s) are analyzed for vulnerabilities and that these be addressed during
the implementation phase. It is recommended that appropriate coding methodology
be employed to prevent CPU resource exhaustion as well as protocol oversight
vulnerabilities.

It is
also recommended that as part of the policy/SMI of a security domain that
implementations are tested for vulnerabilities with tools that are publicly
available.

Table
36: Relevant Specifications regarding Denial-of-Service

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| ISO/IEC 17799:2000 | Information technology -- Code of practice for information security management |  |
| ISO/IEC TR 13335-1:1996 | Information technology -- Guidelines for the management of IT Security -- Part 1: Concepts and models for IT Security |  |
| ISO/IEC TR 13335-2:1997 | Information technology -- Guidelines for the management of IT Security -- Part 2: Managing and planning IT Security |  |

 

## Security Assurance Management

Explicitly
recognize the need for manageability of security functionality within IntelliGrid Architecture
security model. For example, identity management, policy management, key management,
and so forth. The need for security management also includes higher-level
requirements such as anti-virus protection, intrusion detection and protection,
which are requirements in their own rights but are
typically provided as part of security management.

 

### Technological Assessment and Relevant Specifications

Security
assurance is part of a Security Domain’s policy and SMI.  It is
recommended that ISO/IEC 15408-3:1999
be the guideline for determine and assessing such a policy.

Table
37: Relevant Specifications regarding Security Assurance

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| RFC 2401 | Security Architecture for the Internet Protocol |  |
| RFC 2196 | Site Security Handbook |  |
| RFC 2350 | Expectations for Computer Security Incident Response |  |
| ISO/IEC 15408-1:1999 | Information technology -- Security techniques -- Evaluation criteria for IT security-- Part 1: Introduction and general mode |  |
| ISO/IEC 15408-2:1999 | Information technology -- Security techniques -- Evaluation criteria for IT security -- Part 2: Security functional requirements |  |
| ISO/IEC 15408-3:1999 | Information technology -- Security techniques -- Evaluation criteria for IT security -- Part 3: Security assurance requirements | Highly Recommended |

 

## Security Protocol Mapping

Security
protocol mapping services, enabling distributed security protocols to be
transparently mapped onto native platform security services for participation by
platform resource managers not implemented to support the distributed security
authentication and access control mechanism.

### Technological Assessment

To
date there has been no definition of abstract security
services and their parameters.   
The security work found in this appendix actually defines a set of services,
but further modeling is required in fully specify the parameters that are
conveyed within those services.

The
issue involving the ability to map to different communication technologies will be mitigated if a full abstract model
of IntelliGrid Architecture security services can be developed.

## Security Service Availability Discovery Service

A
Security Domain must provide a mechanism for an entity to discover what other
security services are available for its use.

Within
the IntelliGrid Architecture, such a service would be required for Inter-Domain usage
where a-priori knowledge is not available.  It would also be a mandatory
service if Quality of Security routing became a reality.

### Technological Assessment and Relevant Specifications

Although
there is no immediately usable technology to accomplish this service, it is
recommended that the WS-Policy series be extended to provide this
capability.  It should be fairly straightforward to model security service
availability as policy (e.g. the Policy Attachment may need to be
extended).  At a minimum, the information required
to be conveyed needs to be determined in advance of attempting to adopt
WS-Policy.

Since
the discovery service is needed inter-domain, it is reasonable to attempt to
make use of Web Services at the domain interconnect points to provide this
capability.

Table
38: Potentially Relevant Specifications in regards to Security Capability
Discovery

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| OASIS | Web Services Policy Framework (WS-Policy)  Available from:  http://xml.coverpages.org/ws-policyV11.pdf |  |
| OASIS | Web Services Policy Assertions Language (WS-PolicyAssertions)  Available from:   http://xml.coverpages.org/ws-policyassertionsV11.pdf |  |
| OASIS | Web Services Policy Attachment (WS-PolicyAttachment)  Available from:  http://xml.coverpages.org/ws-policyattachmentV11.pdf |  |

 

## Single Sign on Service

Relieve
an entity having successfully completed the act of authentication once from the
need to participate in re-authentications upon subsequent accesses to
OGSA-managed resources for some reasonable period of time. This must take into
account that a request may span security domains and hence should factor in
federation between identitydomains and mapping of
identities. This requirement is important from two perspectives: a) It places a
secondary requirement on an OGSA-compliant implementation to be able to
delegate an entity’s rights, subject to policy (e.g., lifespan of credentials,
restrictions placed by the entity) b) If the credential material is delegated
to intermediaries, it may be augmented to indicate the identity of the
intermediaries, subject to policy.

This
service is a local combination of  the Credential Conversion and Identity
Mapping services.

## Trust Establishment Service

This
service represents the ability of one resource to determine if its peer can be
trusted.  In order to establish trust, well known identities and security
policies must be used.  Additionally, if inter-domain trust establishment
requires an analysis of the security policies and procedures of the peer
security domain.

Key
definitions:

**trust:** In [cryptology](http://www.atis.org/tg2k/_cryptology.html) and
cryptosystems, that characteristic allowing one entity to assume that a second
entity will behave exactly as the first entity expects. Note: Trust may apply
only for some specific function. The critical role of trust in the [authentication](http://www.atis.org/tg2k/_authentication.html)
framework is to describe the relationship between an authenticating entity and
a [certification
authority](http://www.atis.org/tg2k/_certification_authority.html); an
authenticating entity must be certain that it can trust the certification
authority to create only valid and reliable certificates. [After X.509]

Trust establishment is implemented through
the Identity Establishment and Quality of Identity Services.

 

Table 39: Relevant Information regarding
Trust Establishment

|  |  |
| --- | --- |
| DOD | DOD 5200.28-STD  Trusted Computer System Evaluation Criteria |
| DOD | DOD 5200.28-STD 1991 Trusted Database Management System Interpretation of the Trusted Computer System Evaluation Criteria |

# Security Policy Issues

The Security Domain’s policy service is concerned
with the management of policies. The aggregation of the
policies contained within and managed by the policy service comprises a
Security Domain’s policy set. This service is also responsible for the
enforcement of the domain’s policy for intra-domain and inter-domain exchanges.
The policy service may be thought of as another
primitive service, which is used by the authorization, audit, identity mapping
and other services as needed.

## General Process

The policy service is a process through which
a Security Domain determines its risks vs. costs in order to protect critical
assets.  The policy development must encompass:

 

* A **Requirements** analysis process
  which is used to determine the critical assets that need protection,
  security needs of the Security Domain, technological choices for implementation, security management and monitoring
  requirements, audit capability, and non-repudiation capability.
* The **Implementation** process that
  monitors and tests the policies as they are implemented.  If there are
  problems detected during implementation, the policy should be revised and
  requirements should be revisited.
* The **Monitoring** process is
  responsible for the detection of security attacks, detection of security
  breeches, and the performance of the installed security infrastructure.
  This process is critical to the overall effectiveness of security.
* The **Analysis** process is
  responsible for determining when the deployed security measures need to be
  re-evaluated.  This re-evaluation may be required due to environment,
  legal, or internally developed metrics.

There is a relevant body of work that can be
found in EPRI Report 1008988, Scoping Study on Security Processes and
Impacts.  The following is a summarization of that work.

### Requirements

A policy must determine what assets need to
be protected, determine what attacks need to be mitigated, how to mitigate the
attacks including technology and procedural, and how to detect attempted
attacks.

·       Asset
Protection:  In order to determine which assets need to be protected, all
aspects of the “value” of an asset needs to be determined.This means that legal, community good will, asset value, and cascade
effects (if an attack did compromise a particular asset) need to be taken into
account.  Since it is not possible to secure every asset in the
infrastructure, it is recommended that the high risk or high-value assets be
protected first.

·       Determining
what Attacks to Mitigate: The requirements process must determine what is the
cost/benefit/probability of a successful attack and what form such an attack
might take.  The higher the probability of success indicates the higher
need for mitigation.

·       Mitigation
Strategies:  The security services, discussed in this report, provide
suggestions in regards to how to mitigate many of the threats.  It is up
to each security domain (SMI) to determine the best method to mitigate the
attack and then write the appropriate policies to reflect that intent.

·       Attack
Detection: Since there is no absolute security, detection of an attempted
attack is an important objective of any security policy.  For each asset
being secured, a mechanism for detecting attempted/successful attacks needs to
be part of the policy and it MUST be implemented and monitored on a constant
basis.

As part of the requirement process, 
ISO/IEC 15408 (e.g. the standardized version of the NIST Common Criteria) 
should be used as a basis for the technological requirements assessment and
determining threats and mitigation strategies.

The requirements phase of policy development
must also take into account risk assessment.

#### Risk Assessment/Analysis

“The classical definition of Risk Analysis is
one that describes it as a process to ensure that the security controls for a
system are fully commensurate with its risks.”[[10]](IECSA_VolumeIV_AppendixA.htm#_ftn10)

Translated, this means that the amount of
security deployed should be related to the overall asset value (including
collateral assets that could be effected[[11]](IECSA_VolumeIV_AppendixA.htm#_ftn11)). 
Thus, risk analysis provides a mechanism to determine which assets should be
protected immediately (based upon relative worth) and not
require that all Security Domain assets be secured.

Some of the other documented benefits of
performing risk assessment are:

·       Provides a
means to cost justify security investments.

·      
Breaks down business boundaries and build business relationships.  
  
Business management would be responsible to determine the security risk level
that would be tolerable for a particular asset.  IT/Security staff would
need to work with the management team to determine the cost/solution. 
Based upon both factors, a cost/security ratio could be developed and used as a
metric. 

·       Risk Analysis
allows security to be analyzed from a business needs perspective and not just
from a technological solution basis.

·       The team
risk analysis activity raises the security awareness to a greater number of
personnel.

·       Provides a
mechanism to evaluate security in a “consistent” manner.

·       Facilitates
communication between different business entities.

#### External Legal Directive Impacts

The policy developed for a particular domain
must take into account binding legal and industry directives as well as
industry best practices.  In regards to the maintenance of security
policy, the impact of binding directives needs to be evaluated/re-evaluated
when directives or best practices are issued from an authoritative andbinding source.

Example:
A state entity issues a binding directive to supply a given class of
security service for certain financial exchanges.  This directive would
need to be evaluated by the SMI against existing policy and security
services/technologies for the domain. If the directive could not be met with
the existing security domain policy/infrastructure, the domain’s policy should
be revised in order to accommodate the directive.

#### Fault Tolerance

Security issues can impact the fault tolerant
aspect of systems.  There are two(2) prevalent issues that need to be
considered in determining a fault tolerance policy:

·       System
Availability (see page 55).

·       Denial of
Service created by successful security attacks.

Policies and system designs must accommodate
these issues.

### Implementation

As
the selected assets are secured, tests should be executed to make sure
that the created policies and deployed technologies actually perform as
desired.  If not, new policies reflecting new requirements need to be
generated.  Therefore, test procedures need to be considered as part of
the policy development cycle.

As an example, the policies andprocedures for physical access should be tested on an
un-announced basis.  This should be written into the policy as well as the
maximum re-test interval allowed.  Additionally, the expected results of
such tests should be documented.  If the expected results are not
obtained, an analysis of the causes for not achieving the expected results
needs to occur.  If the analysis indicates that the policy is in error,
then the policy needs to be revised.

### Analysis

Policies and procedures need to be written to
state how often re-analysis of the existing policies and security
infrastructure needs to occur (given no successful attack or repeated attempted
attacks being detected).  The policy for re-analysis needs to recognize
that shifts in the world political environment (just think of before 9/11
versus now) and technology advances all need to be
taken into account.

if !vml?![](IECSA_VolumeIV_AppendixA_files/image015.gif)endif?

Figure 5: General trend is security
vulnerabilities (extracted from EPRI Report 1008988)

Figure 5 shows the probability of a
successful attack.  It depicts a high probability prior to security
measures being implemented.  At the time the security measures are
implemented, this represents the “lowest” probability of successful attack if
the security process has worked properly.  However, the figure accurately
reflects that over time the probability of successful
attack increases.  Thus it is important to understand and specify the
periodicity of security re-evaluation in order to keep the probability of
successful attack at an acceptable level.

Thus the aforementioned represent the general
types of problems that must be faced when developing an overall Security Domain
security policy.  However, there are technology specific policies that
also need to be addressed.

Note: ISA-99, Integrating Electronic Security
into the Manufacturing and Control Systems Environment is a document worth
reading.  It discusses, in more detail, the aspects of policy development.

 

## PKI Infrastructure Policy and Issues

Note: This section is intended as a simple
discussion of the issues regarding PKI.  There are more authoritative
documents available from NIST or NERC.

The purpose of the Public Key Infrastructure
is to allow the establishment of Trust through the binding of encryption keys
(typically “public” keys) and identities. In order to understand how PKI works,
it is first important to that PKI to understand the three prevalent types of encryption: symmetric, asymmetric, and
public/private.

·       Symmetric
encryption refers to the fact that both peers have the knowledge and use the
same encryption key.  Since both peers have and use the same key,
symmetric encryption does not lend itself to unambiguous bindings (e.g. one key
to a particular application/entity), thus symmetric encryption should not be
used as the Trust establishment binding (e.g. should not be used within a PKI
environment).

·       Asymmetric
encryption refers to the fact that each entity has its own key.  Unlike
symmetric encryption, asymmetric keys can allow for unambiguous identity
establishment.  However, since cooperating peers would need to have
knowledge of the other peer’s key, it is often difficult to protect the
identifying key.  Although asymmetric keys could facilitate a PKI
environment, the use of such keys for identity binding is not recommended since
the keys must be disseminated/configured on multiple peers and therefore a
prone to being compromised.

·       Public/Private
key encryption works on the basis that the use of the public key allows the
decryption of information encrypted with the private key.  Conversely,
information encrypted with the public key can only be decrypted with the
private key. It represents a specialization of asymmetric encryption.

if !vml?![](IECSA_VolumeIV_AppendixA_files/image017.gif)endif?The
use of public/private key encryption can be used for two purposes: encryption
and digital signatures.

if !vml?![](IECSA_VolumeIV_AppendixA_files/image019.gif)endif?

 

Figure 6: Simplified diagram of
Public/Private Key encryption and Digital Signature

Figure 6 shows in order to Node A to encrypt
data to be sent to Node B, the use of Node B’s public key is required.  It
also shows that only the holder of Node B’s private key can decrypt the
information (neglecting encryption attacks).  Likewise, the Digital
Signature exchange shows that Node A’s signature is decoded by Node B through
the use of Node A’s public key.  Thus for both encryption and digital
signatures, only public keys need to be exchanged and therefore
it becomes easier to control and protect the private keys.  Thus
public/private key based PKI systems should be the preferred approach.

 

Obviously, it is critical to have a robust
PKI infrastructure:

 

·       Create the appropriate
bindings between public/private keys and identification.  
  
The typical mechanism for the bindings is through a digital X.509 certificate.
A public certificate that includes the public key is created, and an equivalent
is created as the “private certificate” that contains both the private and
public keys.  It is the creation of these two “certificates” that are
typically the responsibility of a Certificate Authority (CA).  
  
The protection of the public certificate/key is not that important, but the
protection of the private key/certificate is. It is the responsibility of the
CA to provide adequate protection during the generation process and to protect
this information even if the certificate has been sent to the actual user.  
  
Since the CA is the “root” source of the certificate, it is important that the
CA also provide Certificate Revocation List (CRL) ability so that compromised
or stolen certificates can be revoked.

·       The user of
a “private certificate” must provide security mechanism to protect the private
information.    
  
The actual mechanism for Security Domain/user archiving is a local issue, but
great care needs to be taken during the policy establishment to be able to
quickly and properly detect if there has been un-authorized access to the
Security Domain private certificates.  The policy must include the
appropriate mechanism/procedures for reporting the compromised certificate and
revoking its use locally.

 

·       Even though
the public certificates do not have the same criticality, the Security Domain
policy should address the procedures for releasing the public certificate for
use.

·       A mechanism
for tracking the lifetime expiration date in advance to actual expiration needs
to be addressed.

 

·       Policies/procedures
for replacement and renewal of older certificates (prior to expiration) or
revoked certificates needs to be developed.

 

Of particular concern in IntelliGrid Architecture, and the
utility industry, is how to provide an appropriate revocation capability for a
Security Domain.  There are several design criteria for such an
infrastructure:

·       The
infrastructure must be able to accommodate revocations of certificates that
have been issued from more than one CA.  
  
There is no central CA for the utility industry, or the world, and it does not
appear that there is movement towards such an entity.  Even NERC, in its
e-Marc program, intends to allow certificates from multiple (although
“certified”) CAs to be used.  If a insecure CA
is selected, problems can occur as is demonstrated in the following example

Example: (from
<http://www.iona.com/support/docs/e2a/asp/5.0/corba/ssl/html/OpenSSL2.html>)

if !vml?![](IECSA_VolumeIV_AppendixA_files/image021.jpg)endif?

 

·       Many of the
certificate using computational resources will not be allowed direct access to
the Internet that would be required in order to query the CRL of a particular
CA.  
  
Additionally, CRLs can be large and can consume
bandwidth and be computationally intensive.

·       An ability
to determine if a particular Certificate has been revoked.  
  
The X.509 Internet Public Key Infrastructure Online Certificate Status Protocol
– OCSP (RFC 2560) allows such a capability.  It is worthwhile to note that
OCSP is a request/response-oriented protocol (e.g. the certificate user must
request to check if a certificate has been revoked).

However, the fact that OCSP is
request/response means that there is an issue of timeliness in revocation
information.  However such a protocol/procedure does not exist
today.  In a future time, it could be envisioned that a central Security
Domain revocation server (not a CRL server) could be created with the following
attributes:

·       Allows
certificate users to register that certificates are in the user certificate
cache.

·       The
Revocation Server would query the CAs CRL servers and
process the revocation list(s).

·       Based upon
the CRL processing, the Revocation Server would notify the certificate user
that the particular certificate has been revoked.

·       Optionally,
such a Revocation Server could alert Security Domain management that a
certificate of a particular user is about to expire so that corrective action
could be taken.

·       Optionally,
such a Revocation Server could respond to OCSP requests so that newly configured
certificates could be validated as still being valid.

It is believed that work on such an entity is
needed to allow more timely delivery of revocation information and to allow
automation of such tasks.

### Intrusion Detection

Any developed policy must include the ability
to detect and attempt to prevent intrusion. There are no authoritative
technologies that are available today.  There are two issues that need to
be resolved:  How to detect that an intrusion has occurred and how to
report/coordinate the fact that there has been an intrusion.

Intrusion detection is a local issue and may
vary based upon the communication media/technology/protocol that is being
employed.  There are two types of intrusions to be considered: passive
(e.g. eavesdropping) and active where the intruder is actively attempting to
access a particular computational resource.

Passive
intrusion is difficult if not impossible to detect.  Thus intrusion
prevention becomes a key issue to prevent this type of intrusion.  Passive
intrusion (e.g. eavesdropping by a network analyzer) can be prevented through
the use of encryption and monitoring/controlling network access (e.g. managed
switches).  In a radio environment, intrusion can’t be prevented, but
eavesdropping can be prevented through the use of encryption that prevents a
real security issue of information disclosure.

The active intruder can be detected through
means that are local to the resource.  However there needs to be a
framework in which the detection can be coordinated, verified, and
reported.  There are no relevant standards in regards to intrusion
detection frameworks. However, the closest is the Communication in the Common
Intrusion Detection Framework (CDIF).    

The following are key attributes of an
integrated intrusion detection technology/framework that should be considered:

·       A detection
framework must be able to communicate over the wire in a standardized manner.

·       A intrusion
detection technology must be able to securely contact the proper peer components.  
  
There must be a mechanism to locate peer components in a secure manner.  
  
There must be a mechanism for verifying each partner’s authenticity and access
privileges.

·       Additionally,
an intrusion detection technology should integrate with the audit
framework/technology.

|  |  |
| --- | --- |
| INT-01 | CDIF Working Group - Communication in the Common Intrusion Detection  Framework v 0.7  Available from:  <http://gost.isi.edu/cidf/drafts/communication.txt> |
| INT -02 | Protocol Anomaly Detection for Network-based Intrusion Detection  Available from: <http://www.sans.org/rr/papers/30/349.pdf> |
| INT-03 | Designing and Implementing a Family of Intrusion Detection Systems  Available from:  http://www.cs.ucsb.edu/~vigna/pub/  2003\_vigna\_valeur\_kemmerer\_esec03.pdf |

Table 40: References regarding Intrusion
Detection

The common thread throughout the references, and
others, is that to perform network based intrusion detection, intrusion
detection component/agents must be able to interact and exchange information
creating a distributed intrusion detection system.

## Specific Policy Issues and Recommendations per Service

Some security services merit specific policy
recommendations that were not expressed within the security service section
explicitly.

### Audit Service and Non-Repudiation

The major policy issues that effect non-repudiation
is the time-frame for which a valid audit trail can be generated.  It is recommended that audit information be
archived and available for no less than a three (3) month period of time.

### Credentials and User Accounts

#### Credentials

There are some general issues for credentials
that apply to many of the credential types that have been discussed.

·       How many
credentials of a given type will a user be allocated?  
  
Ingeneral, it is recommended to allocate a single physical credential of
each type (e.g. Smart Card, Personal ID card, Token Generator).This recommendation even applies to Digital
certificates.  Such a policy will minimize the effort required for
management, renewal, and revocation (if needed).

·       Upon
revocation, a policy/mechanism needs to be developed to detect and enunciate if
that credential,even a network address, hasbeen used after revocation.  The policy must
address the expected detection timeframe allowed and the type of response
expected from SMI.    
  
Note: Typically, the smaller the detection window the higher the cost to
implement.

·       The period
at which credentials need to be renewed/modified.

·       The
determination of an appropriate non-use time that causes an investigation and
potential revocation of the credential if the credential has not been used
within that non-use time period.

·       Determine a
policy for revoking the credentials.

##### Personal Identification

The design and management of Personal Identification
cards will impact the ability to enforce physical access control.

It is recommended that such ID cards require
a photograph of the person and also have an area where an easy modification can
be made. 

As a minimum, it is suggested that these
modifications occur on a monthly basis and be a multi-colored/foil label with a
valid through date printed on it.

##### Addresses

In order to provide an infrastructure for
monitor and revocation of addresses, it is important to address the two (2)
main address types: statically and dynamically assigned.

###### Statically Assigned Addresses

For
statically address assigned computation resources:

·       The policy
should require that the physical (e.g. Media Access Control address or
equivalent) be recorded.  The policy must also allow for tracking changes
in that address.

·       That the
communication segment has an Access Control List (ACL) that prevents off
segment communication if the address is revoked.  
  
It is recommended that this policy be enforcedthroughthe
deployment of SNMP manageable switches. So that an address can be associated
with a switch port, and upon revocation the port is disabled.

·       The
policy/implementationshould allow for continuousmonitoring/detection
of addresses that should not be present and that have not been used for a
policy specified period of time.  
  
The policy/implementation infrastructure must provide the technology to detect
usage and determine periods of inactivity.

·       A
policy/procedure is needed that allows renewal/reactivation of the address if
the address has been revoked incorrectly.

·       A
policy/procedure is needed that allows re-assignment of a previously assigned
addressed.

###### Dynamically Assigned Addresses

For dynamically addressed computation
resources:

 

·       The policy
should prohibit dynamically assigned addresses from being used as single-factor
identification credentials.  The probability of incorrect identity
establishment is high; therefore it should not be allowed.

·       The policy
should not allow off-segment communication unless a challenge-response is
performed.

·       The
policy/procedures/SMI must be able to provide an audit record/trail regarding
the address assigned to the challenge/response so that actual identification of
the user can occur.

·       The
challenge-response should be on an individual basis (e.g.
no group assigned passwords).

##### Username/Passwords

There are a couple of recommendations in
regards to the use of usernames/passwords:

·       In general,
a particular user should be allowed one and only one password for a given
computational resource.

·       The size of
the password, and its required characters/format needs to be specified and
enforced.  
  
The first question that needs to be answered is the character set.  It is
recommended that upper, lower, punctuation, and numeric characters be allowed.
This increases the possible permutations of passwords dramatically:  
  
Example assumes ASNI Character Set:  
  
Number upper case
characters:                    
24  
Number of lowercase characters:                 
24  
Number of numeric
characters:                    
10  
Number of punctuation characters[[12]](IECSA_VolumeIV_AppendixA.htm#_ftn12):             
30  
  
Based upon a four(4) character password, then number of possible permutations
is shown to be:  
  
Permutations if upper case
only:                              
331,776  
Permutations if upper and lower case
:                     
5,308,416  
Permutations if upper, lower, numeric case
:            
11,316,496  
Permutations if  using all characters:                        
59,969,536  
  
It should be noted that some computational resources may not be able to accept
punctuation characters within passwords, but it is strongly recommended to
include upper, lower, and numeric characters within the
password character set.

The policy
needs to determine the minimum size of a password in order to provide adequate
protection.    
  
Unfortunately, many existing policies assume that password size is the
criteria, however protection comes from the number of possible permutations. 
It is suggested that the minimum number of password permutations be
approximately 1 trillion for any computational resource.  
  
This means, based upon allowed characters, the minimum password size is :

Table 41: Recommended Minimum Password size

|  |  |
| --- | --- |
| **Character Set Allowed** | **Recommended Password Size** |
| Upper Case Characters Only | 9 |
| Upper/lower case characters only | 8 |
| Upper/lower/numeric characters | 7 |
| All characters | 6 |

It is further recommended that seven(7) characters
be the absolute minimum.

·       The policy
needs to require at least one numeric character, if numeric characters are
allowed.  Additionally, the policy should not allow numeric characters as
the last character of the password.  Such a policy will eliminate the
natural tendency to append a number to a base password when revision of the
password is required.

·       The policy needs to address the period of time that requires
password changing.

##### Smart Cards

Smart cards can be used to contain personal
identification information (e.g. username/passwords), digital certificates,
biometric information, and other types of information.  Therefore, the
credential types they contain typically address the credential aspects of a
smart card. 

The major policy issue, specifically related
to smart cards, is the development of policies/procedures relating to the
serialization of the smart cards.

##### Digital Certificates

There is a major issue regarding digital
certificates, and that is the handling of revocation. Certificate Authorities (CAs) typically maintain Certificate Revocation Lists (CRLs) that are updated on a twenty-four
(24) hour interval.  A certificate that has been placed on a CRL is no
longer trustworthy and therefore should not be useable.

Policies and procedures should be developed
to:

·       Specify a
periodicity to check the CAs CRLs
and how to disseminate this information within the security domain.  
  
The NERC DEWG has expressed a major concern in this area and further policy
study in order to develop a specific recommendation
is warranted.

##### Virus Protection

The developed policy should address virus and
worm protection.   It is suggested that the following NIST guide be
used as part of the policy development.

NIST, NIST SP 500-166, August 1989, Computer
Viruses and Related Threats: A Management Guide, Springfield, Springfield, VA:
NTIS.

#### User and Group Account Management

This service allows the ability to define, assign,
organize, control and maintain mapping for user and group identifiers within
the security domain.  There is no authoritative technology that is
applicable to providing this service and therefore must be rigorously addressed
via policy.

However, there are
several relevant articles that may prove of assistance.

Table 42: Relevant Articles concerning User
and Group Account Management

|  |  |
| --- | --- |
| Oblix | Best Practices in Extranet Portals and Identity Management |
| Oblix | Mastering Supply Chain Partnerships: Achieving Core Business Objectives through Effective Identity Management  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | Lowering eBusiness Administrative Costs with Effective Group Management  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | An Overview of Federated Identity Architecture  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | Creating a Secure and Unified eBusiness Infrastructure  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | An Overview of Federated Identity Architecture  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | Creating a Secure and Unified eBusiness Infrastructure  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Computerworld | Five rules for top-notch user management and provisioning  Available from:  http://www.computerworld.com/securitytopics/security  /story/0,10801,90407,00.html?f=x10 |

If thoroughly reviewed, the articles clearly
indicate that the basic premise of User and Group Management has its
foundations in Identity management (e.g. Identity Establishment and Mapping
services).  Thus, the technological recommendations from those security
services needs to be part of the User and Group Management service. 
Additionally, the following are key recommendations from the literature:

·       Deprecation
or changing of all default accounts is needed.  
  
This would mean that for Operating Systems, that the default user accounts
should be removed or a least have the credentials changed (e.g.
passwords).  This should include ALL user accounts, including remote diagnostic
accounts.

·       Accounts
that are not frequently used should be de-activated.  
  
One of the most prevalent issues is determining the usage of a particular user
account.  The Security Domain’s policy should specify a period of
inactivity that causes user accounts to become inactive (e.g. no longer valid
but available to be renewed/re-activated).

·       Group
Accounts should be granular enough to provide appropriate access privilege
restriction.  
  
At a general level, the following privileges need to be addressed:  
  
Remote Login: Does the User belong to a group that has the privilege to make
use of the computational resource remotely.   
  
Execute: Does the User belong to a group that has the privilege to execute a
particular program/application.   
  
Access: Does the User belong to a group that has the privilege to access the
information contained in a computational resource (e.g. file, database,
etc…).  There is a need for further granularity based upon the particular
instance of file/resource.  
  
Modification: Does the User belong to a group that has the privilege to modify
the information contained in a computational resource.  Similar
granularity to Access is typically needed.  
  
View: Does the User belong to a group that is allowed to view the existence of a
particular resource (e.g. the ability to have a directory with particular files
appearing in the directory response).  
  
Within the IntelliGrid Architecture, there are two additional privileges that need to
be considered.  These are privileges that typically relate to interactions
with field devices and not business level computational resources, although
they may be needed in some cases (e.g. User Management): Configuration and
Control Privileges.  
  
Configuration: Does the user belong to a group that has the privilege to change
the configuration of a computational resource.  There may be further
granularity required based upon the types of configuration supported by the
computational resource (e.g. users, protective schemes, control settings,
initial values, setting groups, etc.).  
  
Control: Does the user belong to a group that has the privilege to change
/control real-time process aspects of a computational resource.  Further
granularity may need to be provided based upon the class of controllable
resources available on a computational resource.

·       Within a
Security Domain, there needs to be centralized management and storage of the
user/account information, typically in a directory like environment.

·       Single
Sign-On is a typical objective of intra-domain management.

This service can be subdivided into a policy
part and an actual security service: Setting and Verifying User Accounts. 

##### Setting and Verifying User Accounts Service

This service is for assigning and validating
authority given to a user or a group of users in accessing/utilizing specific
enterprise resources. 

There is no authoritative technology to
evaluate for this service.  However, from an abstract security service
level such a service needs to exist.  The service needs to provide the
functionality of:

·       Lifecycle
management of user and group account.  This includes the ability to
create, renew, deprecate, modify, and delete users and groups.

·       Credential
Management is required so that passwords, certificates, etc. can be replaced/renewed/deprecated as required.

# Protocol Specific Recommendations

The previous sections have dealt with
security from a generalized service perspective or from a “physical” network
topology perspective.  However, it is useful to discuss specific security
recommendations for particular protocols that may be prevalent in the IntelliGrid Architecture.

## Network Layer Technologies

There are two prevalent routing network
layers that can be envisioned within IntelliGrid Architecture environment: Internet Protocol
Version 4 (IPv4) and Internet Protocol Version 6 (IPv6). There four(4) basic
security functions that could be provided within the network layer: 
Confidentiality, packet level authentication, integrity,
and address protection.  Each of the prevalent network protocols will
be discussed.

### IPv4

IPv4 (RFC 791) is the currently most widely
deployed version the Internet Protocol.  IPv4 is relatively simple and has
NO Security provisions within the protocol itself.  However, VPN
technologies,  IPSEC (RFC 1826 and RFC 1827)
and ESP (RFC 2406) provide the additional security services needed at the
network layer.

Confidentiality is provided via RFC 1827 and
RFC 2406.

Packet level authentication is provided via
RFC 1826.

Integrity is provided by RFC 1826.

Address protection is provided by RFC 1827
and RFC 2406.

### IPv6

IPv6 (RFC 2460 ) is not interoperable with
IPv4, however it was designed to expand the number of available Internet Addresses from 232 to 2128
(e.g. 4 bytes versus 16 bytes of addressing). Besides the increase in address
space, security extensions were added: Authentication and Encapsulation
Security Payload.  Thus incorporating several of the key security
provisions of RFC 1826 and RFC 2406 into the IPv6 protocol.

Thus Confidentiality, packet authentication,
and integrity can all be provided through the use of the appropriate fields of
IPv6.  However, IPv6 does not protect network addressing information since
the IP Address information occurs before the
security extensions in the IPv6 packet.  Thus if source/destination
address protection is still desired, VPN or tunnel extensions still need to be
used.

Tunneling can occur via the current VPN
technologies (RFC 1826 and RFC 1827 support tunneling of both IPv4 and IPv6) or
RFC 3053 (IPv6 Tunnel Broker) could be utilized.

“The growth of IPv6 networks started mainly
using the transport facilities offered by the current Internet.  This led
to the development of several techniques to manage IPv6 over IPv4
tunnels.    At present most of the 6bone network is built using
manually configured tunnels over the Internet.  The main drawback of this
approach is the overwhelming management load for network administrators, who
have to perform extensive manual configuration for each tunnel.”[[13]](IECSA_VolumeIV_AppendixA.htm#_ftn13)

Thus the selection of technology is dependent
upon the inter-domain connectivity that is being provided.  The current
Internet is a “4bone” network and thus VPN technology would need to be
deployed.  However, if a “6bone” network were in use, then RFC 3053 would
be the preferred approach.

Current deployment technologies would lend
itself to IPv6 use for Inter-domain exchanges and not intra-domain.  Most
intra-domain addressing is still IPv4.

### Transport Layer Technologies (TCP)

The Transmission Control Protocol (RFC 793)
can be used over IPv4 or IPv6 (slight modifications required to interface properly with IPv6).  However, thereare no
security provisions within RFC 793 itself.  Thus Transport Layer Security
(TLS)[[14]](IECSA_VolumeIV_AppendixA.htm#_ftn14) is
recommended to provide transport level authentication, integrity, and
confidentiality. 

There is ongoing work in IEC TC57 WG15 to
specify implementation guidelines for TLS, and these should be implemented as
appropriate.

If transport port number protection is
desired, then a network layer security mechanism must be used.

### Application Layer Protocols

#### IEC 60870-5/DNP

IEC TC57 WG15 currently has a work item to
address security for 870-5 and DNP.  The current strategy appears to be
headed towards the use of TLS, as specified by WG15, with authentication
objects added to the protocol.

The recommendations from
IEC 62351-5 (Security for IEC 60870-5 and derivatives) should be followed.

#### IEC 60870-6 TASE.2 (ICCP)

EPRI sponsored several initiatives to develop
security recommendations for TASE.2.  These recommendations have been the
basis of new work items for IEC TC57 WG15.  It is these developing
standards that should be used.

The recommendations from IEC 62351-3 (Security for profiles
including TCP) and IEC 62351-4 (Security for profiles including MMS) should
be followed.

There is a potential need to provide
intrusion detection capability for IEC 60870-6 TASE.2 implementation. 
There is an issue regarding the lack of definition of standardized security
related Management Information Base (MIB) objects.  IEC TC57WG15 has undertaken thetask to define security MIB
objects that could facilitate intrusion detection.  It is recommended that
the recommendations of IEC 62351-7 (Objects for Network Management) be reviewed
carefully.

#### IEC 61850

IEC 61850 has several different communication
profiles.  However, one directly aligns with TASE.2 and it has been
recommended in IEC TC57 WG15 that this profile and TASE.2 implement security in
a similar manner.

The Virtual Lan
(VLAN) high speed profiles used for GOOSE, GSSE, IEC 61850-9-1, and IEC
61850-9-2, have performance requirements (e.g. 4 msecs
or less) that prohibit the use of full encryption.  Current thoughts
within IEC TC57 WG15 are to use a CRC based Message Authentication Code/Seal to
provide integrity.  Authentication would be provided via an address-based
credential.  Confidentiality would need to be provided
through appropriate communication path selection. It is expected that the
MAC mechanism will be addressed in IEC 62351-6 (Security for IEC 61850
profiles).

It is also expected IEC 62351-6 will
reference IEC 62351-3 (Security for profiles including TCP) and IEC 62351-4
(Security for profiles including MMS) in regards to the IEC 61850 MMS based
profile.

There is a potential need to provide
intrusion detection capability for IEC 61850 implementation.  There is an
issue regarding the lack of definition of standardized security related
Management Information Base (MIB) objects.  IEC TC57 WG15 has undertaken
the task to define security MIB objects that could facilitate intrusion
detection.  It is recommended that the recommendations of IEC 62351-7
(Objects for Network Management) be reviewed carefully.

#### Modbus

This is a defacto
standard protocol that is in wide deployment.  It can be used in a serial
or network based deployment (TCP based).  There are no provisions in the
basic Modbus protocol for security, nor are any authentication extensions known
to be in development.  However, it is recommended that the Modbus/TCP implementations
be augmented with TLS in a manner similar to the recommendations specified by
IEC TC57 WG15 for TC57 protocols.

# Security Service vs. IntelliGrid Architecture Quality of Service

The use of security services/technologies may
have an impact on the level of quality of service that can be achieved. 
IntelliGrid Architecture has defined several QOS requirements that need
to be analyzed in regards to achieving the QOS when security is applied.

Table 43: Summary of IntelliGrid Architecture QOS Requirements

|  |  |
| --- | --- |
| QOS-1 | Provide ultra high speed messaging (short latency) of less than 4 milliseconds |
| QOS-2 | Provide very high speed messaging of less than 10 milliseconds |
| QOS-3 | Provide high speed messaging of less than 1 second       Provide medium speed messaging on the order of 10 seconds |
| QOS-4 | Support contractual timeliness (data must be available at a specific time or within a specific window of time) |
| QOS-5 | Support ultra high availability of information flows of 99.9999+ (~1/2 second) |
| QOS-6 | Support extremely high availability of information flows of 99.999+ (~5 minutes) |
| QOS-7 | Support very high availability of information flows of 99.99+ (~1 hour) |
| QOS-8 | Support high availability of information flows of 99.9+ (~9 hours) |
| QOS-9 | Support medium availability of information flows of 99.0+ (~3.5 days) |
| QOS-10 | Support high precision of data (< 0.5 variance) |
| QOS-11 | Support time synchronization of data for age and time-skew information |
| QOS-12 | Support high frequency of data exchanges |

 

An analysis of Table 43 shows that IntelliGrid Architecture
QOS requirements.  There are two general categories that are impacted
through the application of security services: performance and
availability. 

## Security Impact on Availability

The definition of availability is:

“**availability: 1.** The degree to which
a [system](http://www.atis.org/tg2k/_system.html),
subsystem, or equipment is operable and in a committable state at the start of
a mission, when the mission is called for at an unknown, i.e., a random, [time](http://www.atis.org/tg2k/_time.html).
Note 1: The conditions determining operability and commitability
must be specified. Note 2: Expressed mathematically, availability is 1 minus the
[unavailability](http://www.atis.org/tg2k/_unavailability.html). **2.**
The ratio of (a) the total time a [functional unit](http://www.atis.org/tg2k/_functional_unit.html) is capable of being used during a given
interval to (b) the length of the interval. Note 1: An example of availability
is 100/168 if the unit is capable of being used for 100 hours in a week. Note
2: Typical availability objectives are specified in decimal fractions, such as
0.9998. **3.** Timely, reliable [access](http://www.atis.org/tg2k/_access.html) to [data](http://www.atis.org/tg2k/_data.html) and [information](http://www.atis.org/tg2k/_information.html) services for authorized users.” [From ANSI
T1.525-2001]

Based
upon the definition, the following security services have an impact on
availability:

·      
Policy:  The developed policy for credential renewal and revocation
will have an impact on availability.  If an in-use credential is
revoked/deprecated incorrectly, then information exchange will not be able to
be achieved, thus impacting availability.  Thus, policy development must
be particularly careful in only revoking the credentials for appropriate
reasons.   
  
 However, the actual revocation, based upon stolen or compromised
credentials will have an impact on availability.  Thus the time required
to renew, create, or deploy new credentials needs to be factored into the
availability calculation. For further discussion see credential renewal.

·      
Credential Renewal: In situations where credentials are compromised, if
QOS-5 is to be achieved, backup credentials need to be deployed so that
automatic switchover away from the compromised credentials is the only
mechanism to achieve close to this availability.   Even with such an
approach, achieving QOS-5 may be questionable, however such an approach would
guarantee QOS-6.  
  
Other mechanism could be employed for QOS-7 through QOS-9.

·      
Security for Denial of Service: Proper deployment of this service will
have a positive impact on availability.

## Security and its Impact on Performance

For
the purposes of this section, the performance QOS requirements (e.g. 
QOS-1 through QOS-4) shall be defined as the information exchange performance
metric (e.g. the amount of time in which that it is desired to exchange
information).  Furthermore, one needs to carefully define when the metric
measurement is started and finished.  Borrowing from IEC 61850, these
types of performance metrics are defined to start when an application
determines that information needs to be sent and is finished when that
information is received by the peer application.  Based upon this set of
definitions, anysecurity service that increases CPU utilization,
bandwidth, and delivery latencies will have an impact on the ability to achieve
the performance requirements.

Most
of the security services do not impact performance, however Confidentiality
(e.g. encryption), Information Integrity, Identity Establishment, and Path
Routing and QOS service all have a direct impact on performance.  Indirect
performance impact can be caused through the use of Credential Conversion,
Identity Mapping, and Firewall Transversal.  The following sections
discuss what security services or options of which services could be utilized
and still achieve the QOS requirements.  These services will be analyzed
in regards to providing the following security functions: Confidentiality,
Integrity, and Trust.

### Four (4) msec Performance Metric

The
Confidentiality security function requires the use of the Confidentiality
security service.  However, the use of full encryption of the information
being exchanged will probably be to CPU intensive to meet the performance
metric.  Thus, the confidentiality function would need to be provided
through the communication path selection capability of the confidentiality
service.  However, care with the path selection must also be taken. 

The
use of routers or slower store/forward types of devices (e.g. Firewalls and
others) would have a potentially severe impact on the transmission
latency.  Thus it is recommended that no routers
or firewalls be used within the selected communication path.  This would
typically indicate that single physical local area network would be the
recommended solution.  However, a limited number of bridges could be used
(based upon the bridge performance) to create a logical network segment and
still achieve the performance metric.

The
Integrity function directly relates to the Integrity service.  At this
performance metric level, integrity would need to be implemented through the
use of low CPU utilization algorithms and low bandwidth consumption
solutions.  The combination of signed CRCs,
similar the TLS’s Message Authentication Code (MAC)
algorithm, would be recommended. 

The
ability to establish trust is a more difficult issue.  The use of digital
certificates would be preferred.  However, most certificate use would have
a significant impact on bandwidth, could be prohibitive based upon allowed
protocol data unit size (e.g. MAC/VLAN level messaging is restricted to a
maximum of 1542 bytes and certificates are typically larger). Thus, the
recommended identification mechanism would be through the use of address
identification.  However, if such a mechanism is used, then the Integrity
protection must extend to the source and destination addresses as well.

### Ten (10) msec Performance Metric

The
Confidentiality security function requires the use of the Confidentiality
security service.  However, the use of full encryption, with high volumes
of transactions, of the information being exchanged will probably be to CPU
intensive to meet the performance metric.  Thus, the confidentiality
function would need to be provided through the communication path selection
capability of the confidentiality service.  However, care with the path
selection must also be taken.  Unlike the 4msec metric, this metric can
tolerate a limited usage of routers and firewalls along the communication path.

 The
Integrity function directly relates to the Integrity
service.  At this performance metric level, integrity would need to be
implemented through the use of low CPU utilization algorithms and low bandwidth
consumption solutions.  The combination of signed CRCs,
similar the TLS’s Message Authentication Code (MAC)
algorithm, would be recommended. 

With
the advent of routers being allowed in the communication path, there is now an
ability to perform network/transport level segmentation/reassembly.  This
means that if the communication path has enough bandwidth, digital certificates
could be used.  However, if segmentation/reassembly is not available or if
the bandwidth is not sufficient, address based identification would be
recommended.

### One (1) second Performance Metric

There
would appear to be no special considerations at this performance metric
level.  The only issue that needs to be properly investigated is the
communication path bandwidth to make sure that there is enough bandwidth to
allow the performance metric at the anticipated volume level.

#### Example:  Security Across IntelliGrid Architecture Environments

IntelliGrid Architecture
has defined several different Environments, as shown in the figure below.

if !vml?![](IECSA_VolumeIV_AppendixA_files/image023.jpg)endif?

Figure
7: IntelliGrid Architecture Environments

 

The
use of the environmental construct allows information exchange discussions in regards to particular types of
application/business exchanges.  However, security constructs need to be
applied to the environmental model. It could be convenient to discuss security
in regards to a collaboration of integrated security functions that cross all
environments, but the definition of such a collaborative
environment is difficult and often fails, in reality, since multiple
business entities are involved.  The difficultly could exist even within a
single environment.

To
solve the issue of security granularity, boundaries, and security management
responsibility, the model of Security Domains has been
introduced in previous sections of this appendix.  Based upon the
Security Domain construct, each IntelliGrid Architecture Environment could encompass one or
multiple security domains; but the important security issue is whether the
security services are required for information crossing multiple security
domains (inter-domain) or are strictly for information within one security
domain (intra-domain).

Since
there is not a one-to-one relationship between Environments and Security
Domains, an example may be useful to illustrate how to use the recommendations
set forth in this document.  For the purposes of this example, Environment
18, the Customer to Energy Service Provider Environment will be used.

Based
upon the Environment’s definition[[15]](IECSA_VolumeIV_AppendixA.htm#_ftn15)

if !vml?![](IECSA_VolumeIV_AppendixA_files/image025.gif)endif?if !vml?![](IECSA_VolumeIV_AppendixA_files/image025.gif)endif?if !vml?![](IECSA_VolumeIV_AppendixA_files/image025.gif)endif?“This environment encompasses communications
between end customers and the utility, aggregator, or Energy Service Provider
(ESP) to which they are connected.  This environment includes the
requirements for what is traditionally known as Automatic Meter Reading (AMR).

**Typical
applications:** Customer metering, management of distributed energy resources
on customer sites, real-time pricing and demand response.”

The
“demand response” application of this Environment will be used in the example
as it provides a relevant example of the required coordination between more
that one security domain.  However, “demand response” can be implemented
in two different manners:

The
ESP provides information requesting energy consumption
curtailment and the customer takes action based upon the supplied information.

The
ESP acts on behalf of the customer and actually takes the curtailment action
(e.g. controls customer owned assets).  This is the mechanism that will be
investigated in the example.

There
are several steps involved with applying the security concepts put forth in
this appendix to this example.  The following sections will attempt to
describe each step.

#### Example of Security Domains

if !vml?![](IECSA_VolumeIV_AppendixA_files/image027.gif)endif?Upon initial inspection, a simplistic
Security Domain model of the example would lend itself to a three (3) security
domain model.   The three potential domains
could be:

ESP:
The Energy Service Provider is its own security domain.  It has its own
security policy and security management.  The ESP would need to be able to
communicate with the Meter (e.g. for meter reading) and to the building’s
Gateway for demand management.

Meter:
This includes the metering, AMR system, and communication infrastructure. 
It represents the system that allows the ESP or other entities to access the
readings of the meter.

Gateway:  This represents a boundary for communication
from external systems to systems within the customer premises.

 

if !vml?![](IECSA_VolumeIV_AppendixA_files/image029.gif)endif?if !vml?![](IECSA_VolumeIV_AppendixA_files/image031.gif)endif?

Figure
8: Example Security Domain Choices

However,
Figure 8 clearly depicts that there are more security domains than the
simplistic model conveys.  The more developed model adds the following
domains:

Safety
and Physical Security:  Most buildings and other customer premises will
have a separately managed domain that is involved with safety and physical
security (e.g. fire, physical intrusion, etc.).  Some ESP’s may offer to
monitor the information provided by this domain as a tertiary service (e.g.
Home Security Services), but for the purposes of the example, this information
will be exchanged with the entity that is responsible for
maintaining and configuring the safety devices.  Therefore, by definition,
the Safety domain includes the management entity that is external to the
customer premises.   
  
However, the information
from the safety domain may be accessed by entities within the building
(excluded from the example).

Lighting
and HVAC Domains: This domain covers lighting, HVAC, and other building and
campus environmental systems.

DER: 
This domain includes the controls of any Distributed Energy Resources (DERs)
within the customer premises, of which Combined Heat and Power (CHP)
distributed energy would be prevalent in most industrial facilities.  It
is the CHP resource that is justified as being its own security domain and this
will be used in the example. The inclusion of DER also causes the inclusion of
another IntelliGrid Architecture Environment.

For
the purposes of the example, there are two interesting exchanges: ESP to/from
the Gateway and the Lighting/HVAC security domains, and ESP to/from the DER
security domain.

For
this example, in both scenarios, it is assumed that the ESP to Gateway
communication will be via the Internet.  It is also assumed that the
Gateway to either of the other domains will be via TCP/IP and Ethernet. 
However, it would be typical that the internal communication infrastructure for
Lighting/HVAC domains and the DER/CHP security domains would be different.

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Communication** | **ESP to Gateway  (Inter-domain)** | **Gateway to Customer Premises Security Domains  (Inter-domain)** | **Customer Premises Network  (Intra-Domain)** |
| ESP to Lighting/HVAC | Internet, Web Services | TCP/IP and Ethernet, IEC 61850 | BACnet  LonWorks |
| ESP to DER | Internet, Web Services | TCP/IP and Ethernet, IEC 61850 | Modbus/TCP |

Table
44: Summary of Example Communication Technologies

For each
of the identified security domains, full security policies and Security
Management Infrastructures (SMI) needs to be developed.  The first issue
that needs to be decided is which security services to implement for
Intra-domain communications and then selecting the types of credentials that
will be used for intra-domain and inter-domain identification purposes.

**Step
1: Establish Identity Establishment Policies**

It is
recommended, in previous section of this appendix, that each security domain establish
its own identity establishment policies and procedures.  The basic issue
to be resolved is whose credentials are acceptable for identity
establishment.  There are two options for inter-domain exchanges:

The
target security domain (e.g. the one to whichthe
connection/request is being issued) issues the appropriate credential(s) to the
entity that it will allow to connect.  
  
In the case of certificate-based credentials, this allows the security domain
to issue time-limited certificates that expire naturally and therefore would be
a good mechanism to provide temporary access.  
  
There are two sets of credentials that need to be issued by the security domain
if this process is used: one to identify the external domain entity and the
other that identifies the security domain entity (e.g. gateway).  This is
needed since identity establishment is required by both entities.

The
target security domain accepts the external entity’s credential (e.g. the
domain does not issue the credential) but does supply the credential to
establish identity of the security domain.

It is
recommended that, when possible, the security domain issue both credentials.
However, security domain boundaries must be able to handle either method.

Besides
the management of the credentials, the credential type needs to be identified
for use by the security domains.  This is often based upon the
communication infrastructure that the security domain supports.

For
the example, the following could be the selected inter-domain credentials and
how to exchange the certificates:

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Inter-Domain Exchange** | **Communication Method** | **Credential to use** | **Exchanged by** |
| ESP to Gateway | Internet, Web Services | X.509 Certificate | W3C - SOAP Security Extensions |
| Gateway to Customer Premises Network | TCP/IP, IEC 61850 | X.509 Certificate | IEC 62351-4 (ACSE Authentication) |

Table
45: Example Certificate and Certificate Exchange choices

**Step
2: Establish Confidentiality Policies**

Once the
appropriate selections have been made on a policy basis, the next policy issue
is if confidentiality needs to be provided and if so how it should be provided.

 

| **Inter-Domain Exchange** | **Communication Method** | **Confidentiality Needed** | **Provided by** |
| --- | --- | --- | --- |
| ESP to Gateway | Internet, Web Services | Yes | Secure HTTP (HTTPS) |
| Gateway to Customer Premises Network | TCP/IP, IEC 61850 | Questionable | IEC 62351-3 and IEC 62351-4 |

Table
46: Example Confidentiality

Once the
confidentiality decision has been made, the tokens/credentials required to
establish and maintain confidentiality need to be decided upon.  In the
case of this example, both HTTPS and IEC 62351-3 (e.g. TLS) make use of X.509
certificates and therefore could be managed in a
similar fashion to the identity establishment credentials.

Note: 
If the tokens/credentials required to establish confidentiality are determined
to be different than the identity establishment credentials, it may be
advisable for the policy to attempt to align the credentials in order to
minimize maintenance issues.  In some cases, this alignment may not be
possible, and thus the SMI will become more complicated.

**Step
3: Establish Message Integrity Policies**

Message
integrity is the next policy issue.  In the
IEC 62351-3 specification, the TLS Message Authentication Code (MAC) use is
mandatory.  It is recommended that the policy decision for HTTPS also
mandate the use of the TLS MAC capability.

**Step
4: Establish Firewall Transversal Policies**

The
next policy issue is that of Firewall Transversal.  Should the
inter-domain boundary be protected by a firewall and what is the mechanism for
allowing transversal of the firewall if implemented?  In this example,
each domain boundary (e.g. the building gateway and the Customer Premises
Network protocol conversion gateways) offers a potential to implement a
firewall.  The policy must decide what functions the firewall is to
provide (see page 26 for the function definitions).  For the example, the
following decisions could be made:

 

| **Firewall Function** | **ESP to Building** | **Building to  Customer Premises Network** | **Comment** |
| --- | --- | --- | --- |
| Media Isolation | Yes | Yes |  |
| Address Translation | Yes | Yes | Building to Customer Premises Network Naturally requires this since the addressing structure of the intra-net is different. |
| Protocol/Port Restriction | Yes | Yes |  |
| Audit | Yes | Yes |  |
| Identity Establishment | No | No | The use of HTTPS (for end-to-end confidentiality) becomes problematic for identity establishment at a firewall boundary.    The use of IEC 62351-3 (TLS) makes identity establishment problematic. |
| Access Control | No | No | Could be done by the building firewall based upon address. |
| Confidentiality | No | No | Since the policy desire is to have confidentiality provided from the ESP to the Customer Premises Network gateway, confidentiality is being provided by another mechanism (e.g. HTTPS and IEC 62351-3). |
| State based Inspection | No | No | With encryption encapsulating the actual protocol that could be analyzed, state based inspection is not possible. |

**Step
5: Establish Role-Based Access Control Policies**

One
of the next policy issues that need to be address is that of roles versus
access control once identity is established.  It would be recommended that
Role Based Access Control be the preferred mechanism.  It is further
recommended that the following privileges be considered: Read, write,
configure, execute, control, and view.  Based upon these privileges, the
following Roles could be defined.

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Role** | **Assigned Privileges** | | | | | |
| **Read** | **Write** | **Configure** | **Execute** | **Control** | **View** |
| Monitor | x |  |  |  |  | x |
| Maintenance | x | x | x | x |  | x |
| Control | x | x |  |  | x | x |
| Super | x | x | x | x | x | x |

Table
47: Suggested Roles vs. Privileges

**Step
6: Determine Audit Policies and Information**

It is
important to realize that the audit policies and the information available in
the audit records constitute the information that can actually provide
repudiation/non-repudiation capability of particular transactions.  In
this example, the types of information that needs to be placed in the audit
records vary by security domain.

In
general, the audit records should contain the information as recommended in the
Audit Service section of the appendix (see page 9).  There is a need to be
special attention given to the audit capabilities associated with the different
access control privileges.   However, the recommendations are the
audit section is non-specific in regards to the issue of writes, configuration,
and control privileges (these privileges may vary
based upon policy).

It is
extremely important that any interaction where that can cause a potential
change in the process behavior, that the information regarding that transaction
be placed within an audit record.  Such a policy/audit record combination
would allow audit trails to be created that could provide a non-repudiation
function for control actions or configuration changes that cause damage or mis-operation.

With
such a policy, the direct control of the DER resource or HVAC system could be
audited and allow thereby allowing secure and auditable exchanges that would
truly facilitate demand load functionality and potentially real time pricing
based control of the system.

**Step
7: Select Deployment Architecture and Equipment**

Once
all of the associated policy issues with inter-domain information exchanges
have been documented, it is now an issue of selecting a deployment architecture
and equipment that meet those requirements.

if !vml?![](IECSA_VolumeIV_AppendixA_files/image033.gif)endif?

Figure
9: Web Service based Customer Interface Example

It is
worthwhile to note that there could be alternate choices that could better
facilitate communication and diagnostics.  The use of web services as the
gateway to the building is only truly required for the load demand commands
from the ESP (this is the typical mechanism used).  Alternate
architectures could allow direct access through the use of IEC 61850 and or
Modbus/TCP.  However, since Modbus/TCP does not currently have the
capability to utilize TLS or true authentication, the latter is not recommended
until/unless TLS and authentication capabilities are added to Modbus/TCP. 
The following shows an alternate architecture.

if !vml?![](IECSA_VolumeIV_AppendixA_files/image035.gif)endif?

Figure
10: Alternate Architecture that could allow direct 61850 communications

In
general, implementation of security requires that thepolicy
be established first, deployment architecture second, deployment equipment
third (not addressed in this example), development of security test
strategies/monitoring, re-evaluation, and then deployment.

One
such issue, raised in the alternate architecture, is the issue of
confidentiality for both the BACnet and Modbus gateways. Table 46 (Example
Confidentiality) has the need for Confidentiality marked “Questionable”. 
However, the alternate architecture clearly allows communication from the
Internet, through the firewall, to be exchanged directly with either the DER or
Lighting/HVAC security domains.  Without the confidentiality and integrity
services being mandated/available for such exchanges security will be
compromised.  Thus for the alternate architecture, the policy would need
to specify:

 

| **Inter-Domain Exchange** | **Communication Method** | **Confidentiality Needed** | **Provided by** |
| --- | --- | --- | --- |
| ESP to Gateway | Internet, Web Services | Yes | Secure HTTP (HTTPS) |
| Gateway to Customer Premises Network | TCP/IP, IEC 61850 | Yes | IEC 62351-3 and IEC 62351-4 |

Since
IEC 62351-3 specifies the use of the TLS MAC, the integrity service is implemented
via default.

The SMI’s, in the example, would be required to retrieve and
analyze the audit records on an interval set by the policy.  Additionally,
the ability to have a firewall alert upon non-authorized access attempts could
prove useful.

#### Extending the Example: Real Time Pricing

There
are two scenarios through which demand load control (e.g. discussed in the
previous example) can be extended to incorporate real time pricing (RTP). 
The RTP scenario involves an agent issuing the pricing signal (e.g. a pricing
agent) and a load management agent (including DER dispatch) that understands
how to manage load/generation based upon the price signal.

The
location of the agents could be:

Co-located
in the ESP security domain.  
  
In this particular scenario, the ESP would issue the load control commands and
has already been accommodated in the example.

Distributed
locations of agents.  
  
The pricing agent is located externally to the set of security domains that are
contained within the building/campus. There are two logical locations for the
pricing agent: the ESP, some government/state regulatory entity, or both. For
the purpose of the extended example, the example will assume that the pricing
agent is located within the ESP’s security domain and
the load management agentis located within the building/campus security
domain infrastructure.  
  
This deployment strategy allows two potential methods to deliver the pricing
signal:  the ESP sends the pricing information to the load management
agent or the load management agent polls for pricing information.  
  
If the ESP sends the pricing information to the load management agent and uses
the same Web Service exchange approach (typical), then the security domains
previously discussed already cover this case.  
  
If the load management agent is required to poll for the data (not typical),
then the ESP must take appropriate measures at its security domain
boundary.  This case will not be discussed as the policies and
technologies that would be used are similar to those already discussed.

# Summary

The
appendix introduces the concept of the security process, discusses the process
in terms of security domains, and defines abstract security services for
security utilization inter and intra domain. 

Technological
investigations are found within each abstract security service section. 
These investigations allow the appendix to determine if the service can be
instantiated given the state of today’s set of available specifications. 
From these investigations, there is a set of recommended technologies that
should be considered for deployment.  Additionally, key missing
technologies have been identified.

Although
the detail recommendations can be found in the individual abstract service
sections of the appendix, it is worthwhile to summarize and aggregate the
recommendation and missing technologies.

## Major Recommendations

This
section discusses the major recommendations that are drawn from this appendix.

·      
Decompose the security discussion into a discussion of security issues regarding a particular security domain.

·      
For any given security domain, there are more security services required
for inter-domain exchanges than intra-domain exchanges.

·      
Policy development is job 1!    
  
The appendix reference several key documents that should be used/understood
when evaluating and creating security policy.  There are several
referenced throughout the appendix, however RFC 2196, RFC 2401, and EPRI Report
1008988 are major references.

·      
Risk assessment methodologies should be used to determine which assets
should be secured.

·      
There needs to be an established audit framework within each security
domain and this framework needs to allow the creation of an audit trail that
could span more than one security domain.  
  
The appendix recommends that ISO/IEC 10164-8 and ISO/IEC
10181-7 be used as the basis of such a framework.

·      
There is a need to provide coordinated and secure timestamp and time
representation for the audit records to allow the creation of an appropriately
time sequenced audit trail.  
  
This appendix recommends that ISO/IEC 18014-1 and UTC time be used to satisfy
this need.

·      
There is a need to provide guidance and usage recommendations in regards
to the management/creation of different credential types.  
  
The appendix identifies several different credential types (e.g. certificates,
username/password, communication addresses, etc..) .  The appendix has
made some internal recommendations and additionally recommends that FIPS PUB
12, RFC 2527, and FIPS 186 all be considered when managing credentials and
establishing which credentials to use.

·      
Confidentiality can be provided through the use of encryption technology
and communication path selection.  There are no available technologies to
facilitate communication path selection. However, there are many documents that
are applicable to the use of encryption.  
  
The appendix recommends that:  
  
Public Key Infrastructure as defined in the X.509 series (e.g. RFC 2459, RFC
2587, RFC 3039, RFC 3161, RFC 2586, etc..) be used.    
  
That Kerberos (e.g. RFC 1510,  RFC 2400, etc…) be considered.  
  
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
ISO/IEC 9506:           IEC
62351-4  
ISO/IEC 8070-5/DNP:          
IEC 62351-5  
ISO/IEC
61850:                    
IEC 62351-6

·      
The appendix makes recommendations regarding network and data link security technologies.  
  
Dial-in:                      
RADIUS (RFC 2865)  
Direct Serial (Retrofit):
          AGA-12  
ATM:                                  
RFC 2684  
WI-FI:                                 
IEEE 802.11i (a.k.a. WPA2)

·      
In order to create a virtual private network, the appendix recommends
RFC 2401.

·      
The appendix also recommends that XML technologies be utilized for
administrative purposes (e.g. SAML, XACML, and XKMS).    
  
This recommendation requires that XML exchanges be done in a secure manner and
the appendix recommends that this security be implemented through the use of
several different technologies.  Some of the major technologies are:  
  
SAML Authentication Context, WS-Policy, WS-Policy Assertions, WS-Policy
Attachments, XACML Schema, and XKMS.

·      
The appendix recommends, as part of the policy development/deployment,
that intrusion detection and intrusion prevention be considered.  It is
also recognized that service level agreements can also assist in this effort.

 

All the
actual details on each document can be found starting on page 65.

## Major Future Work

During
the development of the appendix and security services, it became clear that the
full implementation of the concepts set forth is not possible given the
technological state today.  The following is a list of major work items
that should be targeted to be started in the near future.

·      
There is no standardized and extensible audit record format that can be
used easily to create audit trails for information supplied by multiple audit
framework components/security domains.  
  
The appendix recommends that some type of XML format be standardized and that
this activity be considered for future work.

·      
There is no usable mechanism to manage certificate/credential revocation
within a security domain.  
  
The appendix recommends that future standardization work be targeted at the
creation of a Revocation Server/protocol combination that meets the criteria
set forth within the appendix.

·      
There is no mechanism available for communicating entities to specify a
particular communication path or dynamic path
selection based on Security being used in a similar manner to Quality of
Service.  
  
The appendix recommends that the standardization of such ability be targeted as
future work.

·      
The industry is inundated with different security related activities,
coordination of these activities would make sure that redundant and conflicting
work is not performed.

# Reference: Security documents

## Security Practices - Frameworks and Policy Documents

### ISO/IEC Security Effective Practices Documents

#### ISO/IEC 10164-8:1993 Information technology -- Open Systems Interconnection -- Systems Management: Security audit trail function

**URL:** http://www.iso.ch

Establishes user requirements for the service
definition needed to support the security audit trail reporting function,
defines the service provided by the security audit trail reporting function,
specifies the protocol that is necessary in order to provide the service,
defines the relationship between the service and management notifications,
defines relationships with other systems management functions, specifies
conformance requirements.

Security,
Audit, Non-Repudiation

#### ISO/IEC 18014-1:2002 Information technology -- Security techniques -- Time-stamping services -- Part 1: Framework

**URL:** http://www.iso.ch

ISO/IEC
18014-1:2002:

1.
identifies the objective of a time-stamping authority;

2.
describes a general model
on which time-stamping services are based;

3. defines time-stamping services;

4. defines the basic protocols of time-stamping;

5. specifies the protocols between the
involved entities.

Audit, Non-Repudiation, Security

#### ISO/IEC 18014-2:2002  Information technology -- Security techniques -- Time-stamping services -- Part 2: Mechanisms producing independent tokens

**URL:** http://www.iso.ch

ISO/IEC
18014-2:2002 describes time-stamping services producing independent tokens. It
describes a general model for time-stamping services of this type and the basic
components used to construct a time-stamping service of this type, it defines
the data structures and protocols used to interact with a time-stamping service
of this type, and it describes specific instances
of such time-stamping services.

The usage of independent tokens presumes a
high trust on the time-stamping authority (TSA).

Three
independent mechanisms are currently covered:

Time-stamps
using digital signatures

In
this mechanism the TSA has an asymmetric key pair, and uses the private key to
digitally sign the time-stamp token. Signature verification will use the public
key. This mechanism may require the use of a PKI (Public Key Infrastructure).

Time-stamps using message authentication codes

In this mechanism the TSA uses a secret key
to digitally bind the time association. The time-stamp token is
authenticated using a Message Authentication Code (MAC). When using this
mechanism, the TSA is needed to carry out the verification.

Time-stamps
using archiving

In
this mechanism the TSA returns a time-stamp token that only has reference
information to bind the time-stamp to the message Imprint in the time-stamp
token. The TSA archives locally enough information to verify that the
time-stamp is correct.

#### ISO/IEC 18014-3:2004 Information technology -- Security techniques -- Time-stamping services -- Part 3: Mechanisms producing linked tokens

**URL:** [http://www.iso.ch](http://www.iso.ch/)

The
documents describe the timestamp request protocol and the timestamp
verification protocol for timestamp based credentials/token generators. 

#### ISO/IEC 10181-7:1996 Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Security audit and alarms framework

**URL:** <http://www.iso.ch/>

Provides
guidance to the creation of a robust audit and alarming framework that is
critical for intrusion detection.

Audit,
Non-Repudiation, Security

#### ISO JTC1 SC37 SD 2 - Harmonized Biometric Vocabulary

**URL:**  

Provides
a dictionary of vocabulary that should be used as the standardized vocabulary
when discussing biometrics.

### Federal Security Best Practices Documents

#### CICSI 6731.01 Global Command and Control System Security Policy

**URL:** http://www.dtic.mil/cjcs\_directives/cdata/unlimit/6722\_02.pdf

Provides a framework and policy directives
that allow security to assist in operational assurance.

  

#### FIPS PUB 112 Password Usage

**URL:** <http://www.itl.nist.gov/fipspubs/fip112.htm>  
             
http://csrc.nist.gov/publications/fips/fips112/fip112-2.pdf

The document specifies basic security
criteria for two different uses of passwords in an ADP system, (I) personal
identity authentication and (2) data access authorization. It establishes the
basic criteria for the design, implementation and use of a password system in
those systems where passwords are used. It identifies fundamental ADP
management functions pertaining to passwords and specifies some user
actions required to satisfy these functions. In addition, it specifies several
technical features which may be implemented in an ADP system in order to support a password system. An implementation schedule
is established for compliance with the Standard. Numerous guidelines are
provided in the Appendices for managers and users seeking to comply with the
Standard.

Identity
Establishment, Policy, Authorization for Access Control,
Credential Renewal, Security

#### FIPS PUB 113 Computer Data Authentication

**URL:** http://
<http://www.itl.nist.gov/fipspubs/fip113.htm>  
             
http://www.dice.ucl.ac.be/crypto/standards/ **fips**/**fips113**/fip**113**.pdf

This
publication specifies a standard to be used by Federal organizations which
require that the integrity of computer data be cryptographically authenticated.
In addition, it may be used by any organization whenever cryptographic
authentication is desired. Cryptographic authentication of data during transmission
between electronic components or while in storage is necessary to maintain the
integrity of the information represented by the data. The standard specifies a
cryptographic authentication algorithm for use in ADP systems and networks. The
authentication algorithm makes use of the Data Encryption Standard (DES)
cryptographic algorithm as defined in Federal Information Processing Standard
46 (FIPS PUB 46).

Information
Integrity, Confidentiality, Privacy, Authorization for
Access Control, Setting and Verifying User Authorization, Encryption, Spoof,
Security

### IETF Security Best Practices Internet Requests for Comments (RFCs)

#### RFC 1102 Policy routing in Internet protocols

**URL:** http://www.ietf.org/rfc/rfc1102.txt

An
integral component of the Internet protocols is the routing function, which
determines the series of networks and gateways a packet will traverse in
passing from the source to the destination. Although there have been a number
of routing protocols used in the Internet, they share the idea that one route
should be selected out  of all available routes based on minimizing some
measure of the route, such as delay.  Recently, it has become important to
select routes in order to restrict the use of network resources to certain
classes of customers.  These considerations, which are usually described
as resource policies, are poorly enforced by the existing technology in the
Internet.  This document proposes an approach to integrating policy
controls into the Internet.

Policy,
Security

#### RFC 1322 A Unified Approach to Inter-Domain Routing

**URL:** http://www.ietf.org/rfc/rfc1322.txt

The document’s focus is on scalability to very large networks and
functionality, as well as scalability, to support routing in an environment of
heterogeneous services, requirements, and route selection criteria.

Policy,
Security

#### RFC 1351  SNMP Administrative Model

**URL:** http://www.ietf.org/rfc/rfc1351.txt

This
memo presents an elaboration of the SNMP administrative model   
set forth in [1]. It describes how the elaborated administrative model is
applied to realize effective network management in a variety of configurations
and environments. The model described here entails the use of distinct
identities for  peers that exchange SNMP messages. Thus, it represents a
departure from the community-based administrative model set forth in [1]. By
unambiguously identifying the source and intended recipient of each SNMP
message, this new strategy improves upon the historical community scheme both by supporting a more convenient access control   
model and allowing for effective use of asymmetric (public key) security
protocols in the future.

Policy,
Security

#### RFC 2008 Implications of Various Address Allocation Policies for Internet Routing

**URL:** http://www.ietf.org/rfc/rfc2008.txt

IP unicast address allocation and management
are essentialoperational functions for the Public Internet. The
exact policies for IP unicast address allocation and
management continue to be the  subject of many discussions. Such
discussions cannot be pursued in a vacuum - the participants must understand
the technical issues and implications associated with various address
allocation and management policies. 

The
purpose of this document is to articulate certain relevant  fundamental
technical issues that must be considered in formulating unicast
address allocation and management policies for the Public Internet, and to
provide recommendations with respect to these policies.

#### RFC 2196 Site Security Handbook

**URL:** http:// [www.ietf.org/rfc/rfc2196.txt](http://www.ietf.org/rfc/rfc2196.txt)

This
handbook is a guide to developing computer security policies
and  procedures for sites that have systems on the Internet.  The
purpose of this handbook is to provide practical guidance to
administrators  trying to secure their information and services.  The
subjects covered include policy content and formation, a broad range of
technical system and network security topics, and security incident response.

Policy,
Security

  

#### RFC 2276 Architectural Principles of Uniform Resource Name Resolution

**URL:** http:// [www.ietf.org/rfc/rfc2276.txt](http://www.ietf.org/rfc/rfc2196.txt)

This
document addresses the issues of the discovery of URN (Uniform Resource Name) resolver services that in turn will directly translate URNs into URLs (Uniform Resource Locators) and URCs (Uniform Resource Characteristics).  The document
falls into three major parts, the assumptions underlying the work,
the guidelines in order to be a viable Resolver
Discovery Service or RDS, and a framework for designing RDSs. 
The guidelines fall into three principle areas:  evolvability,
usability, and security and privacy.  An RDS that is compliant with the
framework will not necessarily be compliant with the guidelines. 
Compliance with the guidelines will need to be validated separately.

#### RFC 2350 Expectations for Computer Security Incident Response

**URL:** http:// [www.ietf.org/rfc/rfc2350.txt](http://www.ietf.org/rfc/rfc2196.txt)if !supportNestedAnchors?endif?

The purpose of this document is to express the general Internet community's expectations of Computer Security Incident
Response Teams (CSIRTs). It is not
possible to define a set of requirements that would be appropriate for all
teams, but it is possible and helpful to list and describe the general set of
topics and issues which are of concern and interest to constituent communities.

CSIRT constituents have a legitimate
need and right to fully understand the policies and procedures of 'their' Computer
Security Incident Response Team.  One way to support this understanding is
to supply detailed information which users may consider, in the form of a
formal template completed by the CSIRT.  An outline of such a template and
a filled in example are provided.

#### RFC 2386 A Framework for QoS-based Routing in the Internet

**URL:** http:// [www.ietf.org/rfc/rfc2386.txt](http://www.ietf.org/rfc/rfc2196.txt)

QoS-based
routing has been recognized as a missing piece in the evolution of QoS-based
service offerings in the Internet. This document describes some of the
QoS-based routing issues and requirements, and proposes a framework for
QoS-based routing in the Internet. This framework is based on extending the
current Internet routing model of intra and interdomain
routing to support QoS.

#### RFC 2401 Security Architecture for the Internet Protocol

**URL:** http:/[//www.ietf.org/rfc/rfc2401.txt](http://www.ietf.org/rfc/rfc2401.txt)

This
memo specifies the base architecture for IPsec compliant systems.  The
goal of the architecture is to provide various security services for traffic at
the IP layer, in both the IPv4 and IPv6 environments.  This document
describes the goals of such systems, their components and how they fit together with each other and into the IP environment.  It also describes
the security services offered by the IPsec protocols, and how these services
can be employed in the IP environment.  This document does not address all
aspects of IPsec architecture.

 Policy,
Security, Encryption, Path Routing and QOS,  Confidentiality, Encryption,
Security

#### RFC 2505 Anti-Spam Recommendations for SMTP MTAs

**URL:** http:/[//www.ietf.org/rfc/rfc2505.txt](http://www.ietf.org/rfc/rfc2401.txt)

This
memo gives a number of implementation recommendations for SMTP,
[1], MTAs (Mail Transfer Agents, e.g. sendmail, [8]) to make
them more capable of reducing the impact of spam(\*).  The intent is that
these recommendations will help clean up the spam situation, if applied on
enough SMTP MTAs on the Internet, and that they
should be used as guidelines for the various MTA vendors. We are fully aware
that this is not the final solution, but if these  recommendations were
included, and used, on all Internet SMTP MTAs, things
would improve considerably and give time to design a more long term solution.
The Future Work section suggests some ideas that may be part of such a long
term solution. It might, though, very well be   the case that the
ultimate solution is social, political, or legal, rather than technical in
nature.

#### RFC 2518 HTTP Extensions for Distributed Authoring -- WEBDAV

**URL:** http:/[//www.ietf.org/rfc/rfc2518.txt](http://www.ietf.org/rfc/rfc2401.txt)

This
document describes an extension to the HTTP/1.1 protocol that  allows
clients to perform remote web content authoring operations. This extension
provides a coherent set of methods, headers, request entity body formats, and
response entity body formats that provide operations for:

Properties:
The ability to create, remove, and query information about Web pages, such as
their authors, creation dates, etc. Also, the ability to link pages of any
media type to related pages.

Collections:
The ability to create sets of documents and to retrieve a hierarchical
membership listing (like a directory listing in a file system).

Locking:
The ability to keep more than one person from working on a document at the same
time. This prevents the "lost update problem," in which modifications
are lost as first one author then another writes changes without
merging the other author's changes.

Namespace Operations: The ability to
instruct the server to copy and move Web resources.

Requirements
and rationale for these operations are described in a companion document,
"Requirements for a Distributed Authoring and Versioning Protocol for the
World Wide Web" [[RFC2291](http://www.armware.dk/RFC/rfc/rfc2291.html)].

#### RFC 2527 Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework

**URL:** http://www.ietf.org/rfc/rfc2527.txt

The
purpose of this document is to establish a clear relationship between
certificate policies and CPSs, and to present a
framework to assist the writers of certificate policies or CPSs
with their tasks. In particular, the framework identifies the elements that may
need to be considered in formulating a certificate policy or a CPS.  The
purpose is not to define particular certificate policies or CPSs,
per se.

Policy,
Identity Establishment, Identity Mapping, Credential Renewal, Spoof, Security

  

#### RFC 2725 Routing Policy System Security

**URL:** http://www.ietf.org/rfc/rfc2725.txt

The
RIPE database specifications and RPSL language define languages used as the
basis for representing information in a routing policy system.  A
repository for routing policy system information is known as a routing
registry.  A routing registry provides a means of exchanging
information needed to address many issues of importance to the operation of the
Internet.  The implementation and deployment of a routing policy
system must maintain some degree of integrity to be of any operational
use.  This document addresses the need to assure integrity of the data by
providing an authentication and authorization model.

#### RFC 2775 Internet Transparency

**URL:** http://www.ietf.org/rfc/rfc2775.txt

This
document describes the current state of the Internet from the architectural
viewpoint, concentrating on issues of end-to-end connectivity and transparency.
It concludes with a summary of some major architectural alternatives
facing the Internet network layer.

#### RFC 2993 Architectural Implications of NAT

**URL:** http://www.ietf.org/rfc/rfc2993.txt

In
light of the growing interest in, and deployment of network address translation
(NAT) RFC-1631, this paper will discuss some of the architectural implications
and guidelines for implementations. It is assumed the reader is familiar with
the address translation concepts presented in RFC-1631.

#### RFC 3411 An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks

**URL:** http://www.ietf.org/rfc/rfc3411.txt

This
document describes an architecture for describing Simple Network Management
Protocol (SNMP) Management Frameworks.  The architecture
is designed to be modular to allow the evolution of the SNMP protocol
standards over time.  The major portions of the architecture are an SNMP
engine containing a Message Processing Subsystem, a Security Subsystem and an
Access Control Subsystem, and possibly multiple SNMP applications which provide
specific functional processing of management data.  This document obsoletes
RFC 2571.

### Other Security Best Practices Documents

#### 21 CFR Part 11 Guidance for Industry Part 11, Electronic Records; Electronic Signatures - Scope and Application

**URL:** http://www.fda.org

The 
rule provides criteria under which FDA will consider   
electronic records to be equivalent to paper records, and electronic   
signatures equivalent to traditional handwritten signatures.
Part 11   
(21 CFR part 11) applies to any paper records required by statute or   
agency regulations and supersedes any existing paper record   
requirements by providing that electronic records may be used in lieu   
of paper records. Electronic signatures which meet the requirements of   
the rule will be considered to be equivalent to full handwritten   
signatures, initials, and other general signings required by agency   
regulations.

#### ISA-99 Integrating Electronic Security into the Manufacturing and Control Systems Environment

**URL:** http://www.isa.org

Is a
work, in progress, that is attempting to standardized/document issues that allow risk-assessment to be factored into the development of security policies.

#### EPRI 100898 Scoping Study on Security Processes and Impacts

**URL:** http://www.epri.com/OrderableitemDesc.asp?product\_id=1008988

“The
primary objective of this Scoping Study is the assessment of the financial and
societal costs of implementing security measures. Financial costs include the
costs for developing security policies and implementing security countermeasure
technologies. Societal costs include the impact of security policies and
technologies on the efficiency of personnel and systems.  
  
A second objective of this Scoping Study is twofold: (a) to assess whether or
not the Internet can provide adequate security for the different utility
control center functions, including power operations and market operations; and (b) to
identify viable alternatives to the Internet for this purpose. This assessment
would include determining what alternative communication means are possible and
what the impact would be to move functions using the Internet to using these
alternative communications methods. As a part of this assessment,
the communication security needs of different functions would be
addressed, along with possible alternative communications methods, such as
privately owned media, private access to media owned by telecommunications
providers, and secure access to more public media. The assessment methodology
does not directly analyze the use of alternative media, but discusses the
mechanisms for analysis. Specific recommendations may be developed as part of
future work.”

#### EPRI 100174 Communication Security Assessment for the United States Electric Utility Infrastructure

**URL:** http://www.epri.com

Provides
an overview of the state of the US power utility infrastructure.

#### NIST SP 500-166 Computer Viruses and Related Threats: A Management Guide

**URL:** http://www.csrc.nist.gov/publications/nistpubs/

Describes
policies and procedures for management, detection, and elimination of viruses.

#### Radius Protocol Security and Best Practices

**URL:** http://www.microsoft.com/windows2000/techinfo/administration/radius.asp

Remote
Authentication Dial-In User Service (RADIUS) is commonly used to provide
centralized authentication, authorization, and accounting for dial-up, virtual
private network, and, more recently, wireless network access. This article provides
an overview of RADIUS and the Extensible Authentication Protocol (EAP) and
describes how to minimize or resolve various security issues of the RADIUS
protocol using implementation and deployment best practices.

## Security Technologies

### ISO/IEC Documents on Security Technologies

#### IEC 62351-3 Security for Profiles including TCP/IP

A
developing standard that specifies how to use Transport Layer Security in order
to secure IEC TC57 protocols and their derivatives.

#### IEC 62351-4 Security for Profiles including MMS (ISO-9506)

IEC
62351-4 is a  developing standard that specifies how to secure the
ISO-9506 (MMS) protocol.  It references IEC 62351-3 and
adds application level authentication ability. It has applicability in
securing IEC 60870-6 TASE.2 (ICCP) and IEC 61850.

#### IEC 62351-5 Security for IEC 60870-5 and Derivatives

IEC
62351-5 is a developing standard that specifies how to secure the IEC 60870-5
and its derivatives (e.g. DNP) protocols.  It references IEC 62351-3 and
adds application level authentication ability.

#### IEC 62351-6 Security for IEC 61850 Profiles

IEC
62351-6 is a developing standard that specifies how to secure all the
communication profiles specified within IEC 61850.  It references IEC 62351-5 and adds additional security
extensions to provide security for Generic
Object Oriented Substation Event (GOOSE), Generic Substation Status
Event (GSSE), and Sampled Measured Values (SMV) profiles.

#### IEC 62351-7 Objects for Network Management

IEC 62351-7 is a developing standard that is focused to
develop standardized Network Management object definitions that facilitate
intrusion detection, security infrastructure management, and audit
capabilities.

#### ISO/IEC 7816-1:1998 Identification cards -- Integrated circuit(s) cards with contacts -- Part 1: Physical characteristics

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=29257&ICS1=35&ICS2=240&ICS3=15

This
Standard specifies the physical characteristics of integrated circuit(s) cards
with contacts. It applies to identification cards
of the ID-1 card type which may include embossing and/or a magnetic
stripe

 

#### ISO/IEC 7816-3:1997 Information technology -- Identification cards -- Integrated circuit(s) cards with contacts -- Part 3: Electronic signals and transmission protocols

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=14735&ICS1=35&ICS2=240&ICS3=15

This
part of lSO/IEC 7816 specifies
the power and signal structures, and information exchange between an
integrated circuit(s) card and an interface device such as a terminal. It also
covers signal rates, voltage levels, current values, parity convention,
operating procedure, transmission mechanisms and communication
with the card. It does not cover information and instruction content, such as identification
of issuers and users, services and limits, security features, journaling and
instruction definitions.

#### ISO/IEC 7816-3:1997/Amd 1:2002 Electrical characteristics and class indication for integrated circuit(s) cards operating at 5 V, 3 V and 1,8 V

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=34974&ICS1=35&ICS2=240&ICS3=15

Update to the original ISO/IEC 7816-3:
1997.  Adds signal levels of 5, 3, and 1.8 V.

#### ISO/IEC 7816-4:1995  Information technology -- Identification cards -- Integrated circuit(s) cards with contacts -- Part 4: Inter-industry commands for interchange

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=14738&ICS1=35&ICS2=240&ICS3=15

This
part of ISO/IEC 7816 specifies

- the
content of the messages, commands and responses, transmitted by the interface
device to the card and conversely,  
- the structure and content of the historical bytes sent by the card during the
answer to reset,  
- the structure of files and data, as seen at the interface when processing
inter-industry commands for interchange.  
- access methods to files and data in the card,  
- a security architecture defining access rights to files and data in the card,  
- methods for secure messaging,  
- access methods to the algorithms processed by the card. It does not describe
these algorithms.

It
does not cover the internal implementation within the card and/or the outside world.

It allows further standardization of
additional inter-industry commands and security architectures.

#### ISO/IEC 7816-4:1995/Amd 1:1997  secure messaging on the structures of APDU messages

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=28731&ICS1=35&ICS2=240&ICS3=15

Adds
security and management commands to the original 7816-4.

#### ISO/IEC 7816-5:1994  Identification cards -- Integrated circuit(s) cards with contacts -- Part 5: Numbering system and registration procedure for application identifiers

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=19980&ICS1=35&ICS2=240&ICS3=15

This
standard specifies a numbering system for application identifiers and a
registration procedure for application provider identifiers.

#### ISO/IEC 7816-7:1999 Identification cards -- Integrated circuit(s) cards with contacts -- Part 7: Interindustry commands for Structured Card Query Language (SCQL)

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=28869&ICS1=35&ICS2=240&ICS3=15

This
standard specifies: the concept of a SCQL database (SCQL =
Structured Card Query Language based on SQL, see MS ISO 9075); and the
related inter industry enhanced commands. These commands allow access to
information store on smartcards.

#### ISO/IEC 7816-8:1999   Identification cards -- Integrated circuit(s) cards with contacts -- Part 8: Security related interindustry commands

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=30194&ICS1=35&ICS2=240&ICS3=15

This
part of ISO/IEC 7816 specifies:

- 
security protocols for use in cards;  
-  secure messaging extensions;  
-  the mapping of the security mechanisms on to the card(s) security
functions/services, including  
             
 a description of the in-card security mechanisms;  
-  data elements for security support;  
-  the use of algorithms implemented on the card though the algorithms
themselves are not   
             
described in detail;  
-  the use of certificates;  
-  security related commands.

#### ISO/IEC 7816-9:2000   Identification cards -- Integrated circuit(s) cards with contacts -- Part 9: Additional interindustry commands and security attributes

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=31035&ICS1=35&ICS2=240&ICS3=15

This standard specifies: a description and
coding of the life cycle of cards and related objects; a description and coding
of security attributes of card related objects; functions and syntax of
additional inter industry commands; data elements associated with these
commands; and a mechanism for initiating card-originated messages. This part of
ISO 7816 does not cover the internal implementation within the card and/or the
outside world.

#### ISO/IEC 7816-10:1999   Identification cards -- Integrated circuit(s) cards with contacts -- Part 10: Electronic signals and answer to reset for synchronous cards

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=30558&ICS1=35&ICS2=240&ICS3=15

This
part of ISO/IEC 7816 specifies the power, signal
structures, and the structure for the answer to reset between an integrated
circuit(s) card with synchronous transmission and an interface device
such as a terminal. The specifications in ISO/IEC 7816-3 apply where
appropriate, unless otherwise stated here. It also covers signal rates,
operating conditions, and communication with the integrated circuit(s) card.

This
part of ISO/IEC 7816 specifies two types of synchronous cards: type 1 and type
2.

#### ISO/IEC 7816-11:2004 Identification cards -- Integrated circuit cards -- Part 11: Personal verification through biometric methods

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=31419&ICS1=35&ICS2=240&ICS3=15

Defines basic fields used by biometric data
(e.g. security, additional biometric information, and the biometric
data). 

#### ISO/IEC 7816-15:2004  Identification cards -- Integrated circuit cards with contacts -- Part 15: Cryptographic information application

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=35168&ICS1=35&ICS2=240&ICS3=15

From [http://www.csa-intl.org](http://www.csa-intl.org/):

ISO/IEC
7816-15:2004 specifies a card application. This application contains
information on cryptographic functionality. Further, ISO/IEC 7816-15:2004
defines a common syntax (in ASN.1) and format for the cryptographic information
and mechanisms to share this information whenever appropriate.

ISO/IEC
7816-15:2004 supports the following capabilities:

    \* storage of multiple
instances of cryptographic information in a card;

    \* use of the cryptographic
information;

   
\* retrieval of the cryptographic information;

   
\* cross-referencing of the cryptographic information with DOs
defined in ISO/IEC 7816 when appropriate;

   
\* different authentication mechanisms; and

   
\* multiple cryptographic algorithms.

#### ISO 9735-9:2002   Electronic data interchange for administration, commerce and transport (EDIFACT) -- Application level syntax rules (Syntax version number: 4, Syntax release number: 1) -- Part 9: Security key and certificate management message (message type- KEYMAN)

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=35040&ICS1=35&ICS2=240&ICS3=60

This
part of ISO 9735 for batch EDIFACT security defines the security key and
certificate management message KEYMAN.

#### ISO/IEC 9594-8:1998 Information technology -- Open Systems Interconnection -- The Directory: Authentication framework

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=32210&ICS1=35&ICS2=100&ICS3=70

This
standard defines a framework for public-key certificates. That framework
includes specification of data objects used to represent the certificates
themselves as well as revocation notices for issued certificates that should no
longer be trusted.

#### ISO/IEC 9594-8:2001 Information technology -- Open Systems Interconnection -- The Directory: Public-key and attribute certificate frameworks

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=34551&ICS1=35&ICS2=100&ICS3=70

Defines additional attributes for ISO/IEC
9594-8.

#### ISO 9735-5:2002 Electronic data interchange for administration, commerce and transport (EDIFACT) -- Application level syntax rules (Syntax version number: 4, Syntax release number: 1) -- Part 5: Security rules for batch EDI (authenticity, integrity and non-repudiation of origin)

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=35036&ICS1=35&ICS2=240&ICS3=60

This
part of ISO 9735 specifies syntax rules for EDIFACT security. It provides a
method to address message/package level, group level and interchange level
security for authenticity, integrity and non-repudiation of origin, in
accordance with established security mechanisms.

#### ISO/IEC 10164-9:1995 Information technology -- Open Systems Interconnection -- Systems Management: Objects and attributes for access control

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=18166&ICS1=35&ICS2=100&ICS3=70

Describes
an Access Control Security Model and the management information necessary for creating and administering access control associated with
OSI System Managements. Security policy adoped for
any instance of use is not specified and is left as an implementation choise. This Specification is of generic application and is
applicable to the security management of many types of application. It
is expected to be adoped for TMN use. Identical text
is published as ITU-T Recommendation X.741.

  

#### ISO/IEC 10181-1:1996 Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Overview

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=24404&ICS1=35&ICS2=100&ICS3=1

From
http://www.csa-intl.org:

The security frameworks address the
application of security services in an Open Systems environment, where the term
Open Systems is taken to include areas such as Database, Distributed
Applications, ODP and OSI. The security frameworks are concerned with defining
the means of providing protection for systems and objects within systems, and
with the interactions between systems. The security frameworks are not
concerned with the methodology for constructing systems or mechanisms.

The
security frameworks address both data elements and sequences of operations (but
not protocol elements) which are used to obtain specific security services.
These security services may apply to the communicating entities of systems as
well as to data exchanged between systems, and to data
managed by systems.

The security frameworks provide the basis for
further standardization, providing consistent terminology and
definitions of generic abstract service interfaces for specific security
requirements. They also categorize the mechanisms that can be used to achieve
those requirements.

One
security service frequently depends on other security services, making it
difficult to isolate one part of security from the others. The security
frameworks address particular security services, describe the range of
mechanisms that can be used to provide the security services, and identify
interdependencies between the services and the mechanisms. The description of
these mechanisms may involve a reliance on a different security service, and it
is in this way that the security frameworks describe the reliance of one
security service on another.

This
part of the security frameworks:

-
describes the organization of the security frameworks;  
- defines security concepts which are required in more than one part of the
security frameworks;  
- describes the inter-relationship of the services and mechanisms identified in
other parts of the   
             
frameworks.

#### ISO/IEC 10181-2:1996  Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Authentication framework

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=18198&ICS1=35&ICS2=100&ICS3=1

From
http://www.csa-intl.org:

This
series of Recommendations / International Standards on Security Frameworks for
Open Systems addresses the application of security services in an Open Systems
environment, where the term "Open Systems" is taken to include areas
such as Database, Distributed Applications, Open Distributed Processing and
OSI. The Security Frameworks are concerned with defining the means of providing
protection for systems and objects within systems, and with the interactions
between systems. The Security Frameworks are not concerned with the methodology
for constructing systems or mechanisms.

The
Security Frameworks address both data elements and sequences of operations (but
not protocol elements) which are used to obtain specific
security services. These security services may apply to the communicating
entities of systems as well as to data exchanged between systems, and to
data managed by systems.

This
Recommendation / International Standard:

-
defines the basic concepts for authentication;  
- identifies the possible classes of authentication mechanisms;  
- defines the services for these classes of authentication mechanism;  
- identifies functional requirements for protocols to support these classes of authentication  
             
mechanism; and  
- identifies general management requirements for authentication.

A
number of different types of standards can use this framework including:

(1)
standards that incorporate the concept of authentication;  
(2) standards that provide an authentication service;  
(3) standards that use an authentication service;  
(4) standards that specify the means to provide authentication within an open
system   
             
architecture; and  
(5) standards that specify authentication mechanisms.

#### ISO/IEC 10181-3:1996 Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Access control framework

**URL:** http://www.iso.ch/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=18199&ICS1=35&ICS2=100&ICS3=1

From
http://www.csa-intl.org:

The
Security Frameworks are intended to address the application of security
services in an Open Systems environment, where the term Open Systems is taken
to include areas such as Database, Distributed Applications, ODP and OSI. The
Security Frameworks are concerned with defining the means of providing
protection for systems and objects within systems, and with the interactions
between systems. The Security Frameworks are not concerned with the methodology
for constructing systems or mechanisms.

The
Security Frameworks address both data elements and sequences of operations (but
not protocol elements) that are used to obtain specific security services.
These security services may apply to the communicating entities of systems as well as to data exchanged between systems, and
to data managed by systems.

In the case of Access Control, accesses may
either be to a system (i.e. to an entity that is the communicating part
of a system) or within a system. The information items that need to be
presented to obtain the access, as well as the sequence of operations to
request the access and for notification of the results of the access, are
considered to be within the scope of the Security Frameworks. However, any
information items and operations that are dependent solely on a particular
application and that are strictly concerned with local access within a system
are considered to be outside the scope of the Security Frameworks.

Many
applications have requirements for security to protect against threats to
resources, including information, resulting from the interconnection of Open
Systems. Some commonly known threats, together with the security services and
mechanisms that can be used to protect against them, in an OSI environment, are
described in CCITT Rec. X.800 / ISO 7498-2.

The
process of determining which uses of resources within an Open System
environment are permitted and, where appropriate, preventing unauthorized
access is called access control. This Recommendation / International Standard
defines a general framework for the provision of access control services.

This
Security Framework:

(a)
defines the basic concepts for access control;  
(b) demonstrates the manner in which the basic concepts of access control can
be specialized to   
             
support some commonly recognized access control services and mechanisms;  
(c) defines these services and corresponding access control mechanisms;  
(d) identifies functional requirements for protocols to support these access
control services and   
             
mechanisms;  
(e) identifies management requirements to support these access control services
and   
             
mechanisms;  
(f) addresses the interaction of access control services and mechanisms with
other security services and mechanisms.

As
with other security services, access control can be provided only within the
context of a defined security policy for a particular application. The
definition of access control policies is outside the scope of this
Recommendation / International Standard, however, some characteristics of
access control policies are discussed.

It is
not a matter for this Recommendation / International Standard to specify
details of the protocol exchanges which may need to be performed in order to
provide access control services.

This
Recommendation / International Standard does not specify particular mechanisms
to support these access control services nor the details of security management
services and protocols.

A
number of different types of standard can use this framework including:

(a)
standards that incorporate the concept of access control;  
(b) standards that specify abstract services that include access control;  
(c) standards that specify uses of an access control service;  
(d) standards that specify the means of providing access control within an Open
System   
             
environment; and  
(e) standards that specify access control mechanisms.

#### ISO/IEC 10181-4:1997 Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Non-repudiation framework

**URL:** [http://www.iso.ch](http://www.iso.ch/)

From [http://www.csa-intl.org](http://www.csa-intl.org/):

This
Recommendation / International Standard addresses the application of security
services in an Open Systems environment, where the term "Open
Systems" is taken to include areas such as Database, Distributed
Applications, Open Distributed Processing and OSI. The Security Frameworks are
concerned with defining the means of providing protection for systems and
objects within systems, and with the interactions between systems. The Security
Frameworks are not concerned with the methodology for constructing systems or
mechanisms.

The
Security Frameworks address both data elements and sequences of operations (but
not protocol elements) which are used to obtain specific security services.
These security services may apply to the communicating entities of systems
as well as to data exchanged between systems, and to data managed by systems.

This Recommendation / International
Standard:

-
defines the basic concepts of Non-repudiation;  
- defines general Non-repudiation services;  
- identifies possible mechanisms to provide the Non-repudiation services;  
- identifies general management requirements for Non-repudiation services and
mechanisms.

As
with other security services, Non-repudiation can only be provided within the
context of a defined security policy for a particular application. The
definitions of security policies are outside the scope of this Recommendation /
International Standard.

The
scope of this Recommendation / International Standard does not include
specification of details of the protocol exchanges which need to be performed
in order to achieve Non-repudiation.

This
Recommendation / International Standard does not describe in detail the
particular mechanisms that can be used to support the Non-repudiation services
nor does it give details of the supporting security management services and
protocols.

#### ISO 10202-1:1991 Financial transaction cards -- Security architecture of financial transaction systems using integrated circuit cards -- Part 1: Card life cycle

**URL:** [http://www.iso.ch](http://www.iso.ch/)

Specifies
the principles for the protection of the Integrated Circuits from their
manufacture and issue, through use to their termination. Annex A forms an
integral part of this standard. Annexes B and C are for information only.

#### ISO 10202-7:1998 Financial transaction cards -- Security architecture of financial transaction systems using integrated circuit cards -- Part 7: Key management

**URL:** [http://www.iso.ch](http://www.iso.ch/)

Specifies
policies, procedures, and algorithms for performing key management for
financial transaction cards.

#### ISO 10202-8:1998 Financial transaction cards -- Security architecture of financial transaction systems

**URL:** [http://www.iso.ch](http://www.iso.ch/)

Specifies
an architecture for security financial transaction
systems when using transaction cards.

  

#### ISO/IEC TR 13335-1:1996 Information technology -- Guidelines for the management of IT Security -- Part 1: Concepts and models for IT Security

**URL:** [http://www.iso.ch](http://www.iso.ch/)

Presents
the basic management concepts and models which are essential for an
introduction into the management of IT security. These concepts and models are
further discussed and developed in the remaining parts
to provide more detailed guidance.

#### ISO/IEC TR 13335-2:1997 Information technology -- Guidelines for the management of IT Security -- Part 2: Managing and planning IT Security

**URL:** [http://www.iso.ch](http://www.iso.ch/)

**URL:** http://www.csa-intl.org/onlinestore/GetCatalogItemDetails.asp?mat=2414358&Parent=2586

From [http://www.csa-intl.org](http://www.csa-intl.org/):

The guidelines in this part of ISO/IEC
TR 13335 address subjects essential to the management of IT security, and the
relationship between those subjects. These guidelines are useful for the identification and the management of all aspects of IT
security.

Familiarity with the concepts and models
introduced in Part 1 is essential for a complete understanding of this
part.

#### ISO/IEC TR 13335-5 Information technology - Guidelines for the management of IT Security - Part 5: Management guidance on network security

**URL:** [http://www.iso.ch](http://www.iso.ch/)

**URL:** http://www.csa-intl.org/onlinestore/GetCatalogItemDetails.asp?mat=2416204&Parent=3548

 From [http://www.csa-intl.org](http://www.csa-intl.org/):

ISO/IEC TR 13335-5 provides guidance
with respect to networks and communications to those responsible for the
management of IT security. This guidance supports the identification and
analysis of the communications related factors that should be taken into
account to establish network security requirements.

This
part of ISO/IEC TR 13335 builds upon Part 4 of this Technical Report by
providing an introduction on how to identify appropriate safeguard areas with
respect to security associated with connections to communications networks. It
is not within the scope of this TR to provide advice on the detailed design and
implementation aspects of the technical safeguard
areas. That advice will be dealt with in future ISO documents.

  

#### ISO/IEC 13888-1:1997 Information technology -- Security techniques -- Non-repudiation -- Part 1: General

**URL:** [http://www.iso.ch](http://www.iso.ch/)

**URL:** [http://www.csa-intl.org/onlinestore/GetCatalogDrillDown.asp?Parent=2628](http://www.csa-intl.org/)

From [http://www.csa-intl.org](http://www.csa-intl.org/):

Non-repudiation
mechanisms provide protocols for the exchange of non-repudiation tokens
specific to each non-repudiation service. Non-repudiation tokens consist of
Secure Envelopes and/or digital signatures and, optionally, of additional data.
Non-repudiation tokens may be stored as non-repudiation information that may be
used subsequently by disputing parties or by an adjudicator to arbitrate in
disputes.

Depending
on the non-repudiation policy in effect for a specific application, and the
legal environment within which the application operates, additional information
may be required to complete the non-repudiation information, e.g.,

- evidence including a trusted time stamp
provided by a Time Stamping Authority,  
- evidence provided by a notary which provides assurance about data
created or the action or   
             
event performed by one or more entities.

Non-repudiation
can only be provided within the context of a clearly defined security policy
for a particular application and its legal environment. Non-repudiation
policies are described in ISO/IEC 10181-4.

This
part of ISO/IEC 13888 serves as a general model for subsequent parts specifying
non-repudiation mechanisms using cryptographic techniques. ISO/IEC 13888
provides non-repudiation mechanisms for the following phases of
non-repudiation:

-
evidence generation,  
- evidence transfer, storage and retrieval, and  
- evidence verification.

Dispute
arbitration is outside the scope of ISO/IEC 13888.

#### ISO/IEC 13888-2:1998 Information technology -- Security techniques -- Non-repudiation -- Part 2: Mechanisms using symmetric techniques

**URL:** [http://www.iso.ch](http://www.iso.ch/)

 This
standard provides the same service as ISO/IEC 13888-3, but through the use of
symmetric encryption techniques.

#### ISO/IEC 13888-3:1997 Information technology -- Security techniques -- Non-repudiation -- Part 3: Mechanisms using asymmetric techniques

**URL:** http://www.iso.ch

**URL:** http://www.csa-intl.org/onlinestore/GetCatalogDrillDown.asp?Parent=2627

From [http://www.csa-intl.org](http://www.csa-intl.org/):

The
goal of the Non-repudiation Service is to generate, collect, maintain, make
available and validate evidence concerning a claimed event or action in order
to resolve disputes about the occurrence or non occurrence of the event or
action. This part of ISO/IEC 13888 specifies mechanisms for the provision of
some specific, communication related non-repudiation Services using asymmetric techniques.

Non-repudiation mechanisms are specified to
establish the following non-repudiation services:

- non-repudiation of origin,  
- non-repudiation of delivery,  
- non-repudiation of submission,  
- non-repudiation of transport.

Non-repudiation
mechanisms involve the exchange of non-repudiation tokens
specific for each non-repudiation Service. Non-repudiation tokens consist of
digital signatures and additional data. Non-repudiation tokens shall be
stored as non-repudiation information that may be used subsequently in case of
disputes.

Depending
on the non-repudiation policy in effect for a specific application, and the
legal environment within which the application operates, additional information
may be required to complete the non-repudiation information, e.g.,

-
evidence including a trusted time stamp provided by a Time Stamping Authority,  
- evidence provided by a notary which provides assurance about the action or
event performed by   
             
one or more entities.

Non-repudiation
can only be provided within the context of a clearly defined security policy
for a particular application and its legal environment. Non-repudiation
policies are described in the multipart Standard of Security Frameworks for open
systems - Part 4: Non-repudiation Framework, ISO/IEC 10181-4.

#### ISO/IEC 15408-1:1999 Information technology -- Security techniques -- Evaluation criteria for IT security -- Part 1: Introduction and general mode

**URL:** [http://www.iso.ch](http://www.iso.ch/)

**URL:** http://www.csa-intl.org/onlinestore/GetCatalogItemDetails.asp?mat=2414891&Parent=3052

From [http://www.csa-intl.org](http://www.csa-intl.org/):

This
multipart standard ISO/IEC 15408 defines criteria, which for historical and
continuity purposes are referred to herein as the Common Criteria (CC), to be
used as the basis for evaluation of security properties of IT products and
systems. By establishing such a common criteria base, the results of an IT
security evaluation will be meaningful to a wider audience.

The
CC will permit comparability between the results of independent security
evaluations. It does so by providing a common set of requirements for the
security functions of IT products and systems and for assurance measures
applied to them during a security
evaluation. The evaluation process establishes a level of confidence that the
security functions of such products and systems and the assurance measures
applied to them meet these requirements. The evaluation results may help
consumers to determine whether the IT product or system is secure enough for
their intended application and whether the security risks implicit in its use
are tolerable.

The
CC is useful as a guide for the development of products or systems with IT
security functions and for the procurement of commercial products and systems
with such functions. During evaluation, such an IT product or system is known
as a Target of Evaluation (TOE). Such TOEs include,
for example, operating systems, computer networks, distributed systems, and
applications.

The
CC addresses protection of information from unauthorised
disclosure, modification, or loss of use. The categories of protection relating
to these three types of failure of security are commonly called
confidentiality, integrity, and availability, respectively. The CC may also be
applicable to aspects of IT security outside of these three. The CC
concentrates on threats to that information arising from human activities,
whether malicious or otherwise, but may be applicable to some nonhuman threats
as well. In addition, the CC may be applied in other areas of IT, but makes no
claim of competence outside the strict domain of IT security.

The
CC is applicable to IT security measures implemented in hardware, firmware or
software. Where particular aspects of evaluation are intended only to apply to
certain methods of implementation, this will be indicated within the relevant
criteria statements.

Certain
topics, because they involve specialised techniques
or because they are somewhat peripheral to IT security, are considered to be
outside the scope of the CC. Some of these are identified below.

a)
The CC does not contain security evaluation criteria pertaining to
administrative security measures not related directly to the IT security
measures. However, it is recognised that a
significant part of the security of a TOE can often be achieved through
administrative measures such as organisational,
personnel, physical, and procedural controls. Administrative security measures
in the operating environment of ISO/IEC 15408-1:1999(E) © ISO/IEC the TOE are
treated as secure usage assumptions where these have an impact on the ability
of the IT security measures to counter the identified threats.

b)
The evaluation of technical physical aspects of IT security such as
electromagnetic emanation control is not specifically covered, although many of
the concepts addressed will be applicable to that area. In particular, the CC
addresses some aspects of physical protection of the TOE.

c)
The CC addresses neither the evaluation methodology nor the administrative and
legal framework under which the criteria may be applied by evaluation
authorities. However, it is expected that the CC will be used for evaluation
purposes in the context of such a framework and such a methodology.

d)
The procedures for use of evaluation results in product or system accreditation
are outside the scope of the CC. Product or system accreditation is the
administrative process whereby authority is granted for the operation of an IT
product or system in its full operational environment. Evaluation focuses on
the IT security parts of the product or system and those parts of the
operational environment that may directly affect the secure use of IT elements.
The results of the evaluation process are consequently a valuable input to the
accreditation process. However, as other techniques are more appropriate for
the assessments of non-IT related product or system security properties and
their relationship to the IT security parts, accreditors
should make separate provision for those aspects.

e)
The subject of criteria for the assessment of the inherent qualities of
cryptographic algorithms is not covered in the CC. Should independent
assessment of mathematical properties of cryptography embedded in a TOE be
required, the evaluation scheme under which the CC is applied must make
provision for such assessments.

  

#### ISO/IEC 15408-2:1999 Information technology -- Security techniques -- Evaluation criteria for IT security -- Part 2: Security functional requirements

**URL:** [http://www.iso.ch](http://www.iso.ch/)

**URL:** http://www.csa-intl.org/onlinestore/GetCatalogItemDetails.asp?mat=2414892&Parent=3053

From [http://www.csa-intl.org](http://www.csa-intl.org/):

Security
functional components, as defined in this part of ISO/IEC 15408, are the basis
for the TOE IT security functional requirements expressed in a Protection
Profile (PP) or a Security Target (ST). These requirements describe the desired
security behaviour expected of a Target of Evaluation
(TOE) and are intended to meet the security objectives as stated in a PP or an
ST. These requirements describe security properties that users can detect by
direct interaction with the TOE (i.e. inputs, outputs) or by the TOE#s response to stimulus.

Security
functional components express security requirements intended to counter threats in the assumed operating environment of the TOE
and/or cover any identified organisational security
policies and assumptions.

The audience for this part of ISO/IEC
15408 includes consumers, developers, and evaluators of secure IT systems and
products. ISO/IEC 15408-1 clause 3 provides additional information on the
target audience of ISO/IEC 15408, and on the use of the standard by the groups
that comprise the target audience. These groups may use this part of ISO/IEC
15408 as follows:

-
Consumers who use ISO/IEC 15408-2 when selecting components to express
functional requirements to satisfy the security objectives expressed in a PP or
ST. ISO/IEC 15408-1 sub clause 4.3 provides more detailed information on the
relationship between security objectives and security requirements.

-
Developers, who respond to actual or perceived consumer security requirements
in constructing a TOE, may find a standardised method
to understand those requirements in this part of ISO/IEC 15408. They can also
use the contents of this part of ISO/IEC 15408 as a basis for further defining
the TOE security functions and mechanisms that comply with those requirements.

-
Evaluators, who use the functional requirements defined in this part of ISO/IEC
15408 in verifying that the TOE functional requirements expressed in the PP or
ST satisfy the IT security objectives and that all dependencies are accounted
for and shown to be satisfied. Evaluators also should use this part of ISO/IEC
15408 to assist in determining whether a given TOE satisfies stated
requirements.

#### ISO/IEC 15408-3:1999 Information technology -- Security techniques -- Evaluation criteria for IT security -- Part 3: Security assurance requirements

**URL:** [http://www.iso.ch](http://www.iso.ch/)

<http://www.csa-intl.org/onlinestore/GetCatalogItemDetails.asp?mat=2414893&Parent=3054>

From [http://www.csa-intl.org](http://www.csa-intl.org/):

This
part of ISO/IEC 15408 defines the assurance requirements of the standard. It
includes the evaluation assurance levels (EALs) that
define a scale for measuring assurance, the individual assurance components
from which the assurance levels are composed, and the criteria for evaluation
of PPs and STs.

#### ISO/IEC 17799:2000  Information technology -- Code of practice for information security management

**URL:** [http://www.iso.ch](http://www.iso.ch/)

**URL:** /iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=33441&ICS1=35&ICS2=40&ICS3=

From NIST <http://csrc.nist.gov/publications/secpubs/otherpubs/reviso-faq.pdf>:

ISO/IEC
17799 is a code of practice. As such it offers guidelines and voluntary
directions for information security management.  It is meant to provide a
high level, general description of areas currently considered important when
initiating, implementing or maintaining information security in an
organization.

#### ISO JTC1 SC37 1.37.19784.1 BioAPI - Biometric Application Programming Interface

**URL:** http://www.jtc1.org

**URL:** http://www.bioapi.org/BIOAPI1.1.pdf

This
emerging standard on a programming interface that provides the general
capability to query and exchange biometric
information.   It is based upon the work of the BioAPI
consortia and the source document can be obtained from their website.

#### ISO JTC1 SC37 1.37.19794 - Biometric Data Interchange Format

**URL:** http://www.jtc1.org

The
standardization of the content, meaning and representation of biometric data
formats which are specific to a particular biometric technology. To ensure a
common look and feel for Biometric Data Structure standards, with notation and
transfer formats that provide platform independence and separation of transfer
syntax from content definition

#### ISO JTC1 SC37 1.37.19794.3 Biometric Data Interchange Format - Part 3: Finger Pattern Spectral Data

**URL:** http://www.jtc1.org

A
specification that further refines ISO JTC1 SC37 1.37.19794 and
standardizes formats for finger spectral data (e.g. blood/heat patterns)
for biometric identification use.

#### ISO JTC1 SC37 1.37.19794.4 Biometric Data Interchange Format - Part 4: Finger Image Data

**URL:** http://www.jtc1.org

A
specification that further refines ISO JTC1 SC37 1.37.19794 and standardizes
formats for finger print image (also known as Fingerscanning) for biometric identification use.   
  
The definition of Fingerscanning
(supplied by SearchSecurity.com) is:

Fingerscanning is a [biometric](http://searchsecurity.techtarget.com/sDefinition/0,,sid14_gci211666,00.html) process, because it involves the automated
capture, analysis, and comparison of a specific characteristic of the human
body. There are several different ways in which an instrument can bring out the
details in the pattern of raised areas (called [ridge](http://searchsecurity.techtarget.com/sDefinition/0,,sid14_gci957123,00.html)s)
and branches (called [bifurcation](http://searchsecurity.techtarget.com/sDefinition/0,,sid14_gci957106,00.html)s) in
a human finger image. The most common methods are
optical, thermal, and tactile. They work using visible light analysis, heat-emission
analysis, and pressure analysis, respectively.

#### ISO JTC1 SC37 1.37.1974.5 Biometric Data Interchange Format - Part 5: Face Image Data

**URL:** http://www.jtc1.org

 A specification that further refines
ISO JTC1 SC37 1.37.19794 and standardizes formats for facial images for
biometric identification use.

### Federal Documents on Security Technologies

#### FIPS 197 Federal Information Processing Standards Publication 197, Specification for the Advanced Encryption Standard (AES)

**URL:** http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf

The standard is based on the Rijndael encryption formula and has been in the works since
1997 when the National Institute of Standards and Technology (NIST) began a
contest to determine the best encryption algorithm. The new standard is
compulsory and binding on Federal agencies for the protection of sensitive,
unclassified information. This new robust encryption standard replaces the aging
DES standard, which was developed in the 1970s.

### IETF Internet Requests for Comments (RFCs) on Security Technologies

#### STD 13 Domain Name System

**URL:** http://www.ietf.org/
RFC/std/std13.html

This
RFC is an introduction to the Domain Name System (DNS), and omits many
details which can be found in a companion RFC, "Domain Names -
Implementation and Specification" [RFC-1035]. 
That RFC assumes that the reader is familiar with
the concepts discussed in this memo.

A
subset of DNS functions and data types constitute an official protocol. 
The official protocol includes standard queries and their responses and most of
the Internet class data formats (e.g., host addresses).

However, the domain system is intentionally
extensible.  Researchers are continuously proposing, implementing and
experimenting with new data types, query types, classes, functions, etc. 
Thus while the components of the official protocol are expected to stay
essentially unchanged and operate as a production service, experimental behavior
should always be expected in extensions beyond
the official protocol.

Policy, Identity Establishment, Profile

#### RFC 1004 Distributed-protocol authentication scheme

**URL:** http://www.ietf.org/rfc/rfc1004.txt

The purpose of this RFC is to focus
discussion on authentication problems in the Internet and possible methods of
solution.  The proposed solutions this document are not intended as
standards for the Internet at this time.  Rather, it is hoped that a
general consensus will emerge as to the appropriate solution to authentication
problems, leading eventually to the adoption of   standards.

#### RFC 1013 X Window System Protocol, version 11: Alpha update April 1987

**URL:** http://www.ietf.org/rfc/rfc1013.txt

This RFC is distributed to the Internet
community for information only.  It does not establish an Internet
standard.  The X window system has been widely reviewed and tested. 
The internet community is encouraged to experiment with it.

#### RFC 1034 Domain names - concepts and facilities

**URL:** http://www.ietf.org/rfc/rfc1034.txt

This RFC introduces domain style names, their
use for Internet mail and host address support, and the
protocols and servers used to implement domain name facilities.

#### RFC 1040 Privacy enhancement for Internet electronic mail: Part I: Message encipherment and authentication

**URL:** http://www.ietf.org/rfc/rfc1040.txt

This RFC defines message encipherment
and authentication procedures, as the initial phase of an effort to provide
privacy enhancement services for electronic mail transfer in the
Internet.  Detailed key management mechanisms to support these procedures will be defined in a subsequent RFC.  As a
goal of this initial phase, it is intended that the procedures defined
here be compatible with a wide range of key management approaches, including
both conventional (symmetric) and public-key (asymmetric) approaches for
encryption of data encrypting keys.  Use of conventional cryptography for message text encryption and/or integrity check
computation is anticipated.

Privacy enhancement services
(confidentiality, authentication, and message integrity assurance) are offered
through the use of end-to-end cryptography between originator and recipient User Agent processes, with no special processing requirements
imposed on the Message Transfer System at endpoints or at intermediate
relay sites.  This approach allows privacy enhancement facilities to be
incorporated on a site-by-site or user-by-user basis without impact on other
Internet entities.  Interoperability among heterogeneous components and
mail transport facilities is supported.

#### RFC 1423 Privacy Enhancement for Internet Electronic Mail: Part III: Algorithms, Modes, and Identifiers

**URL:** http://www.ietf.org/rfc/rfc1423.txt

This document provides definitions, formats,
references, and citations for cryptographic algorithms, usage modes, and
associated identifiers and parameters used in support of Privacy Enhanced Mail
(PEM) in the Internet community.  It is intended to become one member of
the set of related PEM RFCs.  This document is organized into four primary
sections, dealing with message encryption algorithms, message integrity check
algorithms, symmetric key management algorithms, and asymmetric key management
algorithms (including both asymmetric encryption and asymmetric signature
algorithms).

Some parts of this material are cited by
other documents and it is anticipated that some of the material herein may be
changed, added, or replaced without affecting the citing documents. 
Therefore, algorithm-specific material has been placed into this separate document.

Use
of other algorithms and/or modes will require case-by-case study to
determine applicability and constraints.  The use of additional algorithms
may be documented first in Prototype or Experimental RFCs.  As experience
is gained, these protocols may be considered for incorporation into the
standard.  Additional algorithms and modes approved for use in PEM in this
context will be specified in successors to this document.

#### RFC 1221 Host Access Protocol (HAP) Specification - Version 2

**URL:** http://www.ietf.org/rfc/rfc1221.txt

The Host Access Protocol (HAP) is a network
layer protocol (as is X.25).  ("Network layer" here means ISO
layer 3 lower, the protocol layer below the DoD Internet Protocol (IP) layer
[3] and above any link layer protocol.)  HAP defines the different types
of host-to-network control messages and host-to-host data messages that may be
exchanged over the access link connecting a host and the network packet switch
node.  The protocol establishes formats for these messages, and describes
procedures for determining when each type of message should be transmitted and
what it means when one is received.

#### RFC 1305 Network Time Protocol (Version 3) Specification, Implementation

**URL:** http://www.ietf.org/rfc/rfc1305.txt

This document describes Version 3 of the
Network Time Protocol (NTP). It supersedes Version 2 of the protocol described
in RFC-1119 dated September 1989. However, it neither changes the
protocol in any significant way nor obsoletes previous versions or
existing implementations. The main motivation for the new version is to refine
the analysis and implementation models for new applications at much higher
network speeds to the gigabit-per-second regime and to provide for the enhanced
stability, accuracy and precision required at such speeds. In particular, the
sources of time and frequency errors have been rigorously examined and error
bounds established in order to improve performance, provide a model for
correctness assertions and indicate timekeeping quality to the user. The
revision also incorporates two new optional features, (1) an algorithm to
combine the offsets of a number of peer time servers in order to
enhance accuracy and (2) improved local-clock algorithms which allow the
poll intervals on all synchronization paths to be substantially increased in
order to reduce network overhead. It also adds recommendations in regards to
security.

  Authorization for Access Control,
Policy, Spoof, Security

#### RFC 1352  SNMP Security Protocols

**URL:** http://www.ietf.org/rfc/rfc1352.txt

The Simple Network Management Protocol (SNMP)
specification [1]  allows for the protection of network management
operations by a  variety of security protocols.  The SNMP administrative
model described in [2] provides a framework for securing SNMP network 
management. In the context of that framework, this memo defines protocols to
support the following three security services:

     o data integrity,

     o data origin authentication,
and

     o data
confidentiality.

 Confidentiality, Integrity, Identity
Establishment, Policy, Spoof, Security

#### RFC 1507 DASS - Distributed Authentication Security Service

**URL:** http://www.ietf.org/rfc/rfc1507.txt

DASS supports the concept of global identity
and network login.  A  user is assigned a name from a global
namespace and that name will be recognized by any node in the network. 
(In some cases, a resource may be configured as accessible only by a particular
user acting through a particular node.  That
is an access control decision, and it is supported by DASS, but the user is
still known by his global identity).  From a practical point of view, this
means that a user  can have a single password (or smart card) which can be
used on all  systems which allow him access and access control mechanisms
can conveniently give access to a user through any computer the user happens to
be logged into.  Because a single user secret is good on  all
systems, it should never be necessary for a user to enter a password other than
at initial login.  Because cryptographic mechanisms are used, the password should never appear on the network  beyond the initial
login node.

Confidentiality, Identity Establishment,
Security

#### RFC 1579 Firewall-Friendly FTP

**URL:** http://www.ietf.org/rfc/rfc1579.txt

This document describes a suggested change to
the behavior of FTP client programs.  No protocol modifications are
required, though we outline some that might be useful.

The FTP protocol uses a secondary TCP
connection for actual transmission of files.  By default, this connection
is set up by an active open from the FTP server to the FTP client. 
However, this scheme does not work well with packet filter-based firewalls, which
in general cannot permit incoming calls to random port numbers.  If, on
the other hand, clients use the PASV command, the data channel will be an
outgoing call through the firewall.  Such calls are more easily handled,
and present fewer problems.

 Policy, Firewall Transversall

#### RFC 1591 Domain Name System Structure and Delegation

**URL:** http://www.ietf.org/rfc/rfc1591.txt

This memo provides some information on the
structure of the names in  the Domain Name System (DNS), specifically the top-level domain names; and on the administration of
domains.  The Internet Assigned  Numbers Authority (IANA) is the
overall authority for the IP Addresses, the Domain Names, and many other
parameters, used in the  Internet.  The day-to-day responsibility for
the assignment of IP Addresses, Autonomous System Numbers, and most top and
second level Domain Names are handled by the Internet Registry (IR) and
regional registries.

 Policy

#### RFC 1608 Representing IP Information in the X.500 Directory

**URL:** http://www.ietf.org/rfc/rfc1608.txt

This document describes the objects necessary
to include information about IP networks and IP numbers in the X.500 Directory.
It extends the work "Charting networks in the X.500 Directory" [1]
where a general framework is presented for representing
networks in the Directory by applying it to IP networks.  This
application of the Directory is intended to support the work of IP network
assigning authorities, NICs, as well as other
applications looking for a mapping of IP numbers to data of related networks.
Furthermore, Autonomous Systems and related routing policy information can be
represented in the Directory along with their relationship to networks and
organizations.

#### RFC 1612 DNS Resolver MIB Extensions

**URL:** http://www.ietf.org/rfc/rfc1612.txt

This memo defines a portion of the Management
Information Base (MIB) for use with network management protocols in the
Internet community.  In particular, it describes a set
of extensions which instrument DNS resolver
functions.  This memo was produced by the DNS working group.  

With the adoption of the Internet-standard
Network Management Framework [4,5,6,7], and with a large number of vendor
implementations of these standards in commercially available products, it
became possible to provide a higher level of effective network management in
TCP/IP-based internets than was previously available.  With the growth in
the use of these standards, it has   become possible to consider the
management of other elements of the infrastructure beyond the basic TCP/IP
protocols.  A key element of the TCP/IP infrastructure is the DNS.

Up to this point there has been no mechanism
to integrate the management of the DNS with SNMP-based
managers.  This memo provides the mechanisms by which IP-based
management stations can effectively manage DNS resolver
software in an integrated fashion.

We have defined DNS MIB objects to be used in
conjunction with the Internet MIB to allow access to and control of DNS resolver software via SNMP by the Internet community.

#### RFC 1826 IP Authentication Header

**URL:** http://www.ietf.org/rfc/rfc1826.txt

This document describes a mechanism for
providing cryptographic authentication for IPv4 and IPv6 datagrams.  An
Authentication Header (AH) is normally inserted after an IP header and before
the other information being authenticated.

The Authentication Header is a mechanism for
providing strong integrity and authentication for IP datagrams.  It might
also provide non-repudiation, depending on which cryptographic algorithm is
used and how keying is performed.  For example, use of an asymmetric
digital signature algorithm, such as RSA, could provide non-repudiation.

Confidentiality, and protection from traffic
analysis are not provided by the Authentication Header.  Users desiring
confidentiality should consider using the IP Encapsulating Security Protocol
(ESP) either in lieu of or in conjunction with the Authentication Header
[Atk95b].  This document assumes the reader has previously read the
related IP Security Architecture document which defines
the overall security architecture for IP and provides important background
information for this specification [Atk95a].

#### RFC 1827 IP Encapsulating Security Payload (ESP)

**URL:** http://www.ietf.org/rfc/rfc1827.txt

This document describes the IP Encapsulating
Security Payload (ESP).  ESP is a mechanism for providing integrity and
confidentiality to IP datagrams.  In some circumstances it can also
provide authentication to IP datagrams.  The mechanism works with both
IPv4 and IPv6.

ESP is a mechanism for providing integrity
and confidentiality to IP datagrams.  It may also provide authentication,
depending on which algorithm and algorithm mode are used.  Non-repudiation
and protection from traffic analysis are not provided by ESP.  The IP
Authentication Header (AH) might provide non-repudiation if used with certain
authentication algorithms [Atk95b].  The IP Authentication Header may be
used in conjunction with ESP to provide authentication.  Users desiring
integrity and authentication without confidentiality should use the IP
Authentication Header (AH) instead of ESP.  This document assumes that the
reader is familiar with the related document
"IP Security Architecture", which defines the overall
Internet-layer security architecture for IPv4 and IPv6 and provides important
background for this specification [Atk95a].

#### RFC 1919 Classical versus Transparent IP Proxies

**URL:** http://www.ietf.org/rfc/rfc1919.txt

Many modern IP security systems (also called
"firewalls" in the trade) make use of proxy technology to achieve
access control.  This document explains "classical" and
"transparent" proxy techniques and attempts to provide rules to help
determine when each proxy system may be used without causing problems.

#### RFC 1940 Source Demand Routing: Packet Format and Forwarding Specification (Version 1)

**URL:** http://www.ietf.org/rfc/rfc1940.txt

The purpose of SDRP is to support
source-initiated selection of routes to complement the route selection provided
by existing routing protocols for both inter-domain and intra-domain routes.
This document refers to such source-initiated routes as "SDRP
routes".  This document describes the packet format and forwarding
procedure for SDRP.  It also describes procedures for ascertaining feasibility
of SDRP routes.  Other components not described here are
routing   information distribution and route
computation.  This portion of the protocol may initially be used
with manually configured routes. The same packet format and processing will be
usable with dynamic route information distribution and computation methods
under development.

The packet forwarding protocol specified here
makes minimal assumptions about the distribution and acquisition of routing
information needed to construct the SDRP
routes.  These minimal   assumptions are believed to be
sufficient for the existing Internet.  Future components of the SDRP
protocol will extend capabilities in this area and others in a largely
backward-compatible manner.

This version of the packet forwarding
protocol sends all packets with the complete SDRP route in the SDRP header.
Future versions will address route setup and other enhancements and
optimizations.

#### RFC 1968 The PPP Encryption Control Protocol (ECP)

**URL:** http://www.ietf.org/rfc/rfc1968.txt

The Point-to-Point Protocol (PPP) [1]
provides a standard method for transporting multi-protocol datagrams over
point-to-point links.  PPP also defines an extensible Link Control
Protocol.

This document defines a method for
negotiating data encryption over PPP links.

  

#### RFC 2040 The RC5, RC5-CBC, RC5-CBC-Pad, and RC5-CTS Algorithms

**URL:** http://www.ietf.org/rfc/rfc2040.txt

This document defines four ciphers with
enough detail to ensure interoperability between different
implementations.  The first cipher is the raw RC5 block cipher.  The
RC5 cipher takes a fixed size input block and produces a fixed sized output
block using a transformation that depends on a key.  The second cipher,
RC5-CBC, is the Cipher Block Chaining (CBC) mode for RC5.  It can process
messages whose length is a multiple of the RC5 block size.  The third
cipher, RC5-CBC-Pad, handles plaintext of any length, though the ciphertext will be longer than the plaintext by at most the
size of a single RC5 block.  The RC5-CTS cipher is the Cipher Text
Stealing mode of RC5,   which handles plaintext of any length and the
ciphertext length matches the plaintext length.

The RC5 cipher was invented by Professor
Ronald L. Rivest of the Massachusetts Institute of
Technology in 1994.  It is a very fast and
simple algorithm that is parameterized by the block size, the number of
rounds, and key length.  These parameters can be adjusted to meet
different goals for security, performance, and exportability.

RSA Data Security Incorporated has filed a patent
application on the RC5 cipher and for trademark protection for RC5, RC5-CBC,
RC5-CBC-Pad, RC5-CTS and assorted variations.

#### RFC 2045 Multi-Purpose Internet Mail Extensions (MIME) and Secure/MIME

**URL:** <http://www.ietf.org/rfc/rfc2045.txt>

Multipurpose Internet Mail Extensions (MIME)
[[RFC2045](ftp://ftp.rfc-editor.org/in-notes/rfc2045.txt)-[RFC2049](ftp://ftp.rfc-editor.org/in-notes/rfc2049.txt)]
extends the format of Internet mail to allow non-US ASCI textual messages,
non-textual messages, multi-part message bodies, and non-US ASCI information in
the headers. The Secure/MIME (S/MIME) working group is developing
specifications, e.g., [[RFC 2311](http://www.ietf.org/rfc/rfc2311.txt)], to
send and receive secure MIME data, providing the following cryptographic
security services for electronic messaging applications: authentication,
message integrity and non-repudiation of origin (using digital signatures) and
privacy and data security (using encryption).

 Security, Mail, Internet, protocol,
application layer

#### RFC 2086 IMAP4 ACL extension

**URL:** http://www.ietf.org/rfc/rfc2086.txt

Provides
Access Control List (ACL) ability to IMAP applications.

 Authorization for Access Control,
Setting and Verifying User Accounts, Policy, Un-authorized access, Security

#### RFC 2093 Group Key Management Protocol (GKMP) Specification

**URL:** http://www.ietf.org/rfc/rfc2093.txt

This specification proposes a protocol to
create grouped symmetric keys and distribute them amongst communicating peers.
This protocol has the following advantages: 1) virtually invisible to operator,
2) no central key distribution site is needed, 3) only group members have the
key, 4) sender or receiver oriented operation, 5) can make use of multicast
communications protocols.

#### RFC 2228 FTP Security Extensions

**URL:** http://www.ietf.org/rfc/rfc2228.txt

This document defines extensions to the FTP
specification [STD 9](http://www.armware.dk/RFC/std/std9.html), [RFC 959](http://www.armware.dk/RFC/rfc/rfc959.html)if !supportNestedAnchors?endif?, "FILE TRANSFER PROTOCOL
(FTP)" (October 1985).  These extensions provide strong
authentication, integrity, and confidentiality on both  the control and
data channels with the introduction of new optional    commands,
replies, and file transfer encodings.

Encryption,
Authorization for Access Control, Confidentiality, Security

#### RFC 2230 Key Exchange Delegation Record for the DNS

**URL:** http://www.ietf.org/rfc/rfc2230.txt

This note describes a mechanism whereby authorisation for one node to act as key exchanger for a
second node is delegated and made available via the Secure DNS.  This
mechanism is intended to be used only with the Secure DNS.  It can be used
with several security services.  For example, a system seeking to use IP Security [RFC-1825, RFC-1826, RFC-1827] to protect
IP packets for a given destination can use this mechanism to determine the set
of authorised   remote key exchanger
systems for that destination.

The Domain Name System (DNS) is the standard
way that Internet nodes locate information about addresses, mail exchangers,
and other data relating to remote Internet nodes. [RFC-1035, RFC-1034] More
recently, Eastlake and Kaufman have defined standards-track
security   extensions to the DNS. [RFC-2065] These security
extensions can be used to authenticate signed DNS data records and can also be used to store signed public keys in the DNS.

The KX record is useful in providing an authenticatible method of delegating authorisation
for one node to provide key exchange services on behalf of one or more,
possibly different, nodes.  This   note specifies the syntax and
semantics of the KX record, which is currently in limited deployment in certain
IP-based networks.

#### RFC 2244 ACAP -- Application Configuration Access Protocol

**URL:** http://www.ietf.org/rfc/rfc2244.txt

The Application Configuration Access Protocol
(ACAP) is designed to support remote storage and access of program option,
configuration and preference information.  The data store model is
designed to allow a client relatively simple access to interesting data, to
allow new information to be easily added without server re-configuration, and
to promote the use of both standardized data and custom or proprietary
data.  Key features include "inheritance" which can be used to
manage default values for configuration settings and access control lists which
allow interesting personal information to be shared and group information to be
restricted.

#### RFC 2246 The TLS Protocol Version 1.0

**URL:** http://www.ietf.org/rfc/rfc2246.txt

This document specifies Version 1.0 of the
Transport Layer Security (TLS) protocol. The TLS protocol provides
communications privacy over the Internet. The protocol allows
client/server applications to communicate in a way that is designed to
prevent eavesdropping, tampering, or message forgery.

  

#### RFC 2313 PKCS #1: RSA Encryption Version 1.5

**URL:** http://www.ietf.org/rfc/rfc2313.txt

This document describes a method for
encrypting data using the RSA public-key cryptosystem. Its intended use is in
the construction of digital signatures and digital envelopes, as described in
PKCS #7:

·       
For digital signatures, the content to be signed is first reduced to a
message digest with
a            
message-digest algorithm (such as MD5), and then an octet string containing the
message digest is encrypted with the RSA private key of the signer of the
content. The content and the encrypted message digest are represented together
according to the syntax in PKCS #7 to yield a digital signature. This
application is compatible with Privacy-Enhanced Mail (PEM) methods.

·       
For digital envelopes, the content to be enveloped is first encrypted
under a content-encryption key with a content-encryption algorithm (such as
DES), and then the content-encryption key is encrypted with the RSA public keys of the recipients of the content. The
encrypted content and the encrypted content-encryption key are represented
together according to the syntax in PKCS #7 to yield a digital envelope. This
application is also compatible with PEM methods.

The document also describes a syntax for RSA
public keys and private keys. The public-key syntax would be used in
certificates; the private-key syntax would be used typically in PKCS #8
private-key information. The public-key syntax is identical to that in both
X.509 and Privacy-Enhanced Mail.  Thus X.509/PEM RSA keys can be used in
this document.

The document also defines three signature
algorithms for use in signing X.509/PEM certificates and certificate-revocation
lists, PKCS #6 extended certificates, and other objects employing digital
signatures such as X.401 message tokens.

Details on message-digest and
content-encryption algorithms are outside the scope of this document, as are
details on sources of the pseudorandom bits required by certain methods in this
document.

#### RFC 2315 PKCS #7: Cryptographic Message Syntax Version 1.5

**URL:** http://www.ietf.org/rfc/rfc2315.txt

This document describes a general syntax for
data that may have cryptography applied to it, such as digital signatures and
digital envelopes. The syntax admits recursion, so that, for example,
one   envelope can be nested inside another, or one party can sign
some previously enveloped digital data.  It also allows arbitrary
attributes, such as signing time, to be authenticated along with
the   content of a message, and provides for other attributes such as
countersignatures to be associated with a signature. A degenerate case of the
syntax provides a means for disseminating certificates and
certificate-revocation lists.

#### RFC 2356 Sun's SKIP Firewall Traversal for Mobile IP

**URL:** http://www.ietf.org/rfc/rfc2356.txt

The Mobile IP specification establishes the
mechanisms that enable a mobile host to maintain and use the same IP address as
it changes its point of attachment to the network. Mobility
implies higher security risks than static operation, because the traffic
may at times take unforeseen network paths with unknown or unpredictable
security characteristics. The Mobile IP specification makes no provisions for
securing data traffic.  The mechanisms described in this
document   allow a mobile node out on a public sector of the internet
to negotiate access past a SKIP firewall, and construct a secure channel into
its home network.

In addition to securing traffic, our
mechanisms allow a mobile node to roam into regions that (1) impose ingress
filtering, and (2) use a different address space.

#### RFC 2406 IP Encapsulating Security Payload (ESP)

**URL:** http://www.ietf.org/rfc/rfc2406.txt

The Encapsulating Security
Payload (ESP) header is designed to provide a mix of security services
in IPv4 and IPv6.  ESP may be applied alone, in combination with the IP Authentication
Header (AH) [KA97b], or in a nested fashion, e.g., through the use of tunnel
mode (see "Security Architecture for the Internet Protocol" [KA97a],
hereafter referred to as the Security Architecture document).  Security
services can be provided between a pair of communicating hosts, between a pair
of communicating security gateways, or between a security gateway and a
host.  For more details on how to use ESP and AH in various network
environments, see the Security Architecture document [KA97a].

#### RFC 2437 PKCS #1: RSA Cryptography Specifications Version 2.0

**URL:** http://www.ietf.org/rfc/rfc2437.txt

This document provides recommendations for
the implementation of public-key cryptography   based on the RSA
algorithm [18], covering the following aspects:

     
-cryptographic primitives

      -encryption
schemes

      -signature
schemes with appendix

      -ASN.1 syntax
for representing keys and for identifying the schemes

The recommendations are intended for general
application within computer and communications systems, and as such include a
fair amount of flexibility. It is expected that application
standards   based on these specifications may include additional
constraints. The recommendations are intended to be compatible with draft
standards currently being developed by the ANSI X9F1 [1] and IEEE P1363 working
groups [14].  This document supersedes PKCS #1 version 1.5
[20].   Editor's note. It is expected that subsequent versions of
PKCS #1 may cover other aspects of the RSA algorithm
such as key size, key generation, key validation, and signature schemes
with message recovery.

#### RFC 2440 OpenPGP Message Format

**URL:** http://www.ietf.org/rfc/rfc2440.txt

This document is maintained in order to
publish all necessary information needed to develop interoperable applications
based on the OpenPGP format. It is not a step-by-step
cookbook for writing an application. It describes only the format and methods
needed to read, check, generate, and write conforming packets crossing any
network.  It does not deal with storage and implementation
questions.  It does, however, discuss implementation issues necessary to
avoid security flaws.  Open-PGP software uses a combination of strong
public-key and symmetric cryptography to provide security services for electronic
communications and data storage.  These services include confidentiality,
key management, authentication, and digital signatures. This document specifies
the message formats used in OpenPGP.

#### RFC 2408 Internet Security Association and Key Management Protocol (ISAKMP)

**URL:** http://www.ietf.org/rfc/rfc2408.txt

This memo
describes a protocol utilizing security concepts necessary for
establishing Security Associations (SA) and cryptographic keys in an Internet
environment.  A Security Association protocol that negotiates,
establishes, modifies and deletes Security Associations and their attributes is
required for an evolving Internet, where there will be numerous security
mechanisms and several options for each security mechanism.  The key management
protocol must be robust   in order to handle public key generation
for the Internet community at large and private key requirements for those
private networks with that requirement.  The Internet Security Association
and Key Management Protocol (ISAKMP) defines the procedures for authenticating
a communicating peer, creation and management of Security Associations, key
generation techniques, and threat mitigation (e.g.  denial of service and replay attacks).  All of these are necessary
to establish and maintain secure communications (via IP Security Service
or any other security protocol) in an Internet environment.

#### RFC 2409 The Internet Key Exchange (IKE)

**URL:** http://www.ietf.org/rfc/rfc2409.txt

ISAKMP ([MSST98]) provides a framework for
authentication and key exchange but does not define them.  ISAKMP is
designed to be key exchange independant; that is, it
is designed to support many different key exchanges.  Oakley ([Orm96])
describes a series of key exchanges—called "modes"-- and details the
services provided by each (e.g. perfect forward secrecy for keys, identity
protection, and authentication).  SKEME ([SKEME]) describes a versatile
key exchange technique which provides anonymity, repudiability,
and quick key refreshment.  This document describes a protocol using part
of Oakley and part of SKEME in conjunction with ISAKMP to obtain authenticated
keying material for use with ISAKMP, and for other security
associations   such as AH and ESP for the IETF IPsec DOI.

#### RFC 2459 Internet X.509 Public Key Infrastructure Certificate and CRL Profile

**URL:** http://www.ietf.org/rfc/rfc2459.txt

This memo profiles
the X.509 v3 certificate and X.509 v2 CRL for use in the Internet. 
An overview of the approach and model are provided as an introduction. 
The X.509 v3 certificate format is described in detail, with additional
information regarding the format and semantics of Internet name forms (e.g., IP
addresses).  Standard certificate extensions are described and one new
Internet-specific extension is defined.  A required set of certificate
extensions is specified.  The X.509 v2 CRL format is described and a
required extension set is defined as well.  An algorithm for X.509
certificate path validation is described. Supplemental information is provided  
describing the format of public keys and digital signatures in X.509
certificates for common Internet public key encryption algorithms (i.e., RSA,
DSA, and Diffie-Hellman).  ASN.1 modules and
examples are provided in the appendices.

  

#### RFC 2510 Internet X.509 Public Key Infrastructure Certificate Management Protocols

**URL:** http://www.ietf.org/rfc/rfc2510.txt

This document describes the Internet X.509
Public Key Infrastructure (PKI) Certificate Management Protocols. Protocol
messages are defined for all relevant aspects of certificate creation and
management.  Note that "certificate" in this document refers to
an X.509v3   Certificate as defined in [COR95, X509-AM].

#### RFC 2511 Internet X.509 Certificate Request Message Format

**URL:** http://www.ietf.org/rfc/rfc2511.txt

This document describes the Certificate
Request Message Format (CRMF).  This syntax is used to convey a request
for a certificate to a Certification Authority (CA) (possibly via a
Registration Authority (RA)) for the purposes of X.509 certificate production. 
The request will typically include a public key and associated registration
information.

#### RFC 2527 Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework

**URL:** http://www.ietf.org/rfc/rfc2527.txt

This document
presents a framework to assist the writers of certificate policies or
certification practice statements for certification authorities and public key
infrastructures.  In particular, the framework provides a comprehensive
list of topics that potentially (at the writer's discretion) need to be covered
in a certificate policy definition or a certification practice statement.

#### RFC 2535 Domain Name System Security Extensions

**URL:** http://www.ietf.org/rfc/rfc2535.txt

Extensions to the Domain Name System (DNS)
are described that provide data integrity and authentication to security aware resolvers and applications through the use of cryptographic
digital signatures.  These digital signatures are included in secured
zones as resource records.  Security can also be provided through
non-security aware DNS servers in some cases.  The extensions
provide for the storage of authenticated public keys in the DNS.  This
storage of keys can support general public key distribution services as
well as DNS security.  The stored keys   enable security aware resolvers to learn the authenticating key of zones in
addition to those for which they are initially configured.  Keys
associated with DNS names can be retrieved to support other protocols. 
Provision is made for a variety of key types and algorithms.  In addition,
the security extensions provide for the optional authentication of DNS
protocol transactions and requests.

#### RFC 2543 SIP: Session Initiation Protocol

**URL:** http://www.ietf.org/rfc/rfc2543.txt

The Session Initiation Protocol (SIP) is an
application-layer control (signaling) protocol for creating, modifying and
terminating sessions with one or more participants. These sessions include
Internet multimedia conferences, Internet telephone calls and multimedia distribution.
Members in a session can communicate via multicast or via a mesh of unicast relations, or a combination of these.  SIP
invitations used to create sessions carry session descriptions which allow
participants to agree on a set of compatible media types.  SIP supports
user mobility by proxying and redirecting requests to
the user's current location. Users can register their current  
location.  SIP is not tied to any particular conference control protocol.
SIP is designed to be independent of the lower-layer transport protocol and can
be extended with additional capabilities.

#### RFC 2547 BGP/MPLS VPNs

**URL:** http://www.ietf.org/rfc/rfc2547.txt

This
document describes a method by which a Service Provider with an IP
backbone may provide VPNs (Virtual Private Networks) for its customers. 
MPLS (Multiprotocol Label Switching) is used for
forwarding packets over the backbone, and BGP (Border Gateway Protocol) is used
for distributing routes over the backbone.  The primary goal of this
method is to support the outsourcing of IP backbone services for enterprise
networks. It does so in a manner which is simple for the enterprise, while
still scalable and flexible for the Service Provider, and while allowing the
Service Provider to add value. These techniques can also be used to provide a
VPN which itself provides IP service to customers.

#### RFC 2560 X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP

**URL:** http://www.ietf.org/rfc/rfc2560.txt

This document specifies a protocol useful in
determining the current status of a digital certificate without
requiring CRLs. Additional mechanisms addressing PKIX
operational requirements are specified in separate documents.  An overview
of the protocol is provided in section 2. Functional   requirements
are specified in section 4. Details of the protocol are in section 5. We cover
security issues with the protocol in section 6. Appendix A defines OCSP over
HTTP, appendix B accumulates ASN.1 syntactic elements and appendix C specifies
the mime types for the  messages.

#### RFC 2592 Definitions of Managed Objects for the Delegation of Management Script

**URL:** http://www.ietf.org/rfc/rfc2592.txt

This memo defines a portion of the Management
Information Base (MIB) for use with network management protocols in the
Internet community.  In particular, it describes a set of
managed objects that allow the delegation of management scripts to distributed
managers.

#### RFC 2744 Generic Security Service API Version 2 : C-bindings

**URL:** http://www.ietf.org/rfc/rfc2744.txt

This document specifies C language bindings
for Version 2, Update 1 of the Generic Security Service Application Program
Interface (GSS-API), which is described at a language-independent conceptual
level in RFC-2743 [GSSAPI].  It obsoletes RFC-1509, making specific
incremental changes in response to implementation experience and liaison
requests.  It is intended, therefore, that this memo or a successor
version thereof will become the basis for subsequent progression of the GSS-API
specification on the standards track.  The Generic
Security Service Application Programming Interface provides security
services to its callers, and is intended for  implementation atop a
variety of underlying cryptographic mechanisms.  Typically, GSS-API
callers will be application protocols into which security enhancements are
integrated through invocation of services provided by the GSS-API. The GSS-API allows a caller application to   authenticate
a principal identity associated with a peer application, to delegate rights to
a peer, and to apply security services such as confidentiality and integrity on
a per-message basis.

#### RFC 2764 A Framework for IP Based Virtual Private Networks

**URL:** http://www.ietf.org/rfc/rfc2764.txt

This document describes a framework for
Virtual Private Networks (VPNs) running across IP backbones.  It discusses
the various different types of VPNs, their respective requirements, and
proposes specific mechanisms that could be used to implement each type of VPN
using existing or proposed specifications.  The objective of this document
is to serve as a framework for related protocol development in order to develop
the full set of specifications required for widespread deployment of
interoperable VPN solutions.

#### RFC 2753 A Framework for Policy-based Admission Control

**URL:** http://www.ietf.org/rfc/rfc2753.txt

This document is concerned with specifying a
framework for providing policy-based control over admission control decisions.
In particular, it focuses on policy-based control over admission control using
RSVP as an example of the QoS signaling mechanism. Even though the focus of the work is on RSVP-based admission control, the document
outlines a framework that can provide policy-based admission control in other
QoS contexts. We argue that policy-based control must be applicable to
different kinds and qualities of services offered in the same network and our
goal is to consider such extensions whenever possible.

#### RFC 2797 Certificate Management Messages over CMS

**URL:** http://www.ietf.org/rfc/rfc2797.txt

This document defines a Certificate
Management protocol using CMS (CMC).  This protocol addresses two
immediate needs within the Internet PKI community:

1. 
The need for an interface to public key certification products and
services based on
[CMS]             
and [PKCS10], and

2.  The need in [SMIMEV3] for a
certificate enrollment protocol for DSA-signed certificates with   Diffie-Hellman public keys.

A small number of additional services are
defined to supplement the core certificate request service.

Throughout this specification the term CMS is
used to refer to both [CMS] and [PKCS7].  For both signedData
and envelopedData, CMS is a superset of the PKCS7. In
general, the use of PKCS7 in this document is aligned to the Cryptographic
Message Syntax [CMS] that provides a   superset of the PKCS7 syntax.
The term CMC refers to this specification.

#### RFC 2817 Certificate Management Messages over CMS

**URL:** http://www.ietf.org/rfc/rfc2817.txt

This document explains how to use the Upgrade
mechanism in HTTP/1.1 to initiate Transport Layer Security (TLS) over an
existing TCP connection. This allows unsecured and secured HTTP traffic to
share the same well known port (in this case, http: at 80 rather than https: at
443). It also enables "virtual hosting", so a single HTTP + TLS
server can disambiguate traffic intended for several hostnames at a single IP
address.

#### RFC 2818 HTTP over TLS

**URL:** http://www.ietf.org/rfc/rfc2818.txt

  This document describes how to use TLS
to secure HTTP connections over the Internet. Current practice is to layer HTTP
over SSL (the predecessor to TLS), distinguishing secured traffic from insecure
traffic by the use of a different server port. This document documents that
practice using TLS. A companion document describes a    method
for using HTTP/TLS over the same port as normal HTTP [[RFC2817](http://www.armware.dk/RFC/rfc/rfc2817.html)].

#### RFC 2820 Access Control Requirements for LDAP

**URL:** http://www.ietf.org/rfc/rfc2820.txt

This document describes the fundamental
requirements of an access control list (ACL) model for the Lightweight
Directory Application Protocol (LDAP) directory service.  It is intended
to be a gathering place for access control requirements needed to provide
authorized access to and interoperability between directories.

#### RFC 2865 Remote Authentication Dial In User Service (RADIUS)

**URL:** http://www.ietf.org/rfc/rfc2865.txt

This document describes a protocol for
carrying authentication, authorization, and configuration information between a
Network Access Server which desires to authenticate its links and a shared
Authentication Server.

#### RFC 2869 RADIUS Extensions

**URL:** http://www.ietf.org/rfc/rfc2869.txt

This document describes additional attributes
for carrying authentication, authorization and accounting information between a
Network Access Server (NAS) and a shared Accounting Server using the Remote Authentication Dial In User Service (RADIUS)
protocol described in RFC 2865 [1] and RFC 2866 [2].

#### RFC 2874 DNS Extensions to Support IPv6 Address Aggregation and Renumbering

**URL:** http://www.ietf.org/rfc/rfc2874.txt

This document defines changes to the Domain
Name System to support renumberable and aggregatable IPv6 addressing.  The changes include a
new resource record type to store an IPv6 address in a
manner which expedites network renumbering and updated definitions of
existing   query types that return Internet addresses as part of
additional section processing.

For lookups keyed on IPv6 addresses (often
called reverse lookups), this document defines a new zone structure which
allows a zone to be used without modification for parallel copies of
an address space (as for a multihomed provider or
site) and across network renumbering events.

#### RFC 2875 Diffie-Hellman Proof-of-Possession Algorithms

**URL:** http://www.ietf.org/rfc/rfc2875.txt

This document describes two methods for
producing an integrity check value from a Diffie-Hellman
key pair.  This behavior is needed for such operations as
creating the signature of a PKCS #10 certification request.  These
algorithms are designed to provide a proof-of-  possession rather than
general purpose signing.

#### RFC 2888 Secure Remote Access with L2TP

**URL:** http://www.ietf.org/rfc/rfc2888.txt

L2TP protocol is a virtual extension of PPP
across IP network infrastructure. L2TP makes possible for an access
concentrator (LAC) to be near remote clients, while allowing PPP termination
server (LNS) to be located in enterprise premises. L2TP allows an enterprise to
retain control of RADIUS data base, which is used to control Authentication,
Authorization and Accountability (AAA) of dial-in users. The objective of this
document is to extend security   characteristics of IPsec to remote
access users, as they dial-in through the Internet. This is
accomplished without creating new protocols and using the existing practices of
Remote Access and IPsec. Specifically, the document proposes three new RADIUS
parameters for use by the LNS node, acting as Secure Remote Access Server
(SRAS) to mandate network level security between remote clients and the
enterprise. The document also discusses limitations of the approach.

#### RFC 2898 PKCS #5: Password-Based Cryptography Specification Version 2.0

**URL:** http://www.ietf.org/rfc/rfc2898.txt

This memo represents a republication of PKCS
#5 v2.0 from RSA Laboratories' Public-Key Cryptography Standards (PKCS) series,
and change control is retained within the PKCS process.  The body of this
document, except for the security considerations section, is taken directly
from that specification.  This document provides recommendations for the
implementation of   password-based cryptography, covering key
derivation functions, encryption schemes, message-authentication schemes, and
ASN.1 syntax identifying the techniques.

The recommendations are intended for general
application within computer and communications systems, and as such include a
fair amount of flexibility. They are particularly intended for the  
protection of sensitive information such as private keys, as in PKCS #8 [25].
It is expected that application standards and implementation profiles based on
these specifications may include additional
constraints.

Other
cryptographic techniques based on passwords, such as password-based key
entity authentication and key establishment protocols [4][5][26] are outside
the scope of this document.  Guidelines for the selection of passwords are
also outside the scope.

#### RFC 2946 Telnet Data Encryption Option

**URL:** http://www.ietf.org/rfc/rfc2946.txt

This document describes a the telnet
encryption option as a generic method of providing data confidentiality
services for the telnet data stream.  While this document summarizes
currently utilized encryption types and codes, it does not define a specific
encryption algorithm.  Separate documents are to be published defining
implementations of this option for each encryption algorithm.

#### RFC 2977 Mobile IP Authentication, Authorization, and Accounting Requirements

**URL:** http://www.ietf.org/rfc/rfc2977.txt

The Mobile IP and Authentication,
Authorization, Accounting (AAA) working groups are currently looking at
defining the requirements for Authentication, Authorization, and
Accounting.  This document contains the requirements which would have to
be supported by a AAA service to aid in providing Mobile IP services.

#### RFC 2979 Behavior of and Requirements for Internet Firewalls

**URL:** http://www.ietf.org/rfc/rfc2979.txt

This
memo defines behavioral characteristics of and interoperability
requirements for Internet firewalls.  While most of these things may seem
obvious, current firewall behavior is often either unspecified or
underspecified and this lack of specificity often causes problems in
practice.  This requirement is intended to be a necessary first step in
making the behavior of firewalls more consistent across implementations and in
line with accepted IP protocol practices.

#### RFC 2985 PKCS #9: Selected Object Classes and Attribute Types Version 2.0

**URL:** http://www.ietf.org/rfc/rfc2985.txt

This memo represents a republication of PKCS
#9 v2.0 from RSA Laboratories' Public-Key Cryptography Standards (PKCS) series,
and change control is retained within the PKCS process.  The body of this
document, except for the security considerations section, is taken directly
from that specification.

This memo provides
a selection of object classes and attribute types for use in conjunction
with public-key cryptography and Lightweight Directory Access Protocol (LDAP)
accessible directories.  It also includes ASN.1 syntax for all constructs.

#### RFC 2986 PKCS #10: Certification Request Syntax Specification Version 1.7

**URL:** http://www.ietf.org/rfc/rfc2986.txt

This memo represents a republication of PKCS
#10 v1.7 from RSA Laboratories' Public-Key Cryptography Standards (PKCS)
series, and change control is retained within the PKCS process.  The body
of this document, except for the security considerations section, is
taken directly from the PKCS #9 v2.0 or the PKCS #10 v1.7 document.

#### RFC 3053 IPv6 Tunnel Broker

**URL:** http://www.ietf.org/rfc/rfc3053.txt

The IPv6 global Internet as of today uses a
lot of tunnels over the existing IPv4 infrastructure.  Those tunnels are
difficult to configure and maintain in a large scale environment.  The
6bone has   proven that large sites and Internet Service Providers
(ISPs) can do it, but this process is too complex for the isolated end user who
already has an IPv4 connection and would like to enter the IPv6 world. 
The motivation for the development of the tunnel broker model is to help early IPv6 adopters to hook up to an existing IPv6 network
(e.g., the 6bone) and to get stable, permanent IPv6 addresses and DNS
names.  The concept of the tunnel broker was first presented
at   Orlando's IETF in December 1998.  Two implementations were
demonstrated during the Grenoble IPng
& NGtrans interim meeting in February 1999.

  

#### RFC 3268 Advanced Encryption Standard (AES) Ciphersuites for Transport Layer Security (TLS)

**URL:** http://www.ietf.org/rfc/rfc3268.txt

This document proposes several new ciphersuites.  At present, the symmetric ciphers
supported by Transport Layer Security (TLS) are RC2, RC4, International Data
Encryption Algorithm (IDEA), Data Encryption Standard (DES), and triple
DES.  The protocol would be enhanced by the addition of Advanced
Encryption Standard (AES) ciphersuites.

#### RFC 3280 Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure  Certificate and Certificate Revocation List (CRL) Profile

**URL:** http://www.ietf.org/rfc/rfc3280.txt

This memo profiles the X.509 v3 certificate
and X.509 v2 Certificate Revocation List (CRL) for use in the Internet. 
An overview of this approach and model are provided as an introduction. 
The X.509 v3 certificate format is described in detail, with additional
information regarding the format and semantics of Internet name forms.  Standard certificate extensions are described and
two   Internet-specific extensions are defined.  A set of
required certificate extensions is specified.  The X.509 v2 CRL format is
described in detail, and required extensions are defined.  An algorithm
for X.509 certification path validation is described.  An ASN.1 module and
examples are provided in the appendices.

#### RFC 3369 Cryptographic Message Syntax (CMS)

**URL:** http://www.ietf.org/rfc/rfc3369.txt

This document describes the
Cryptographic Message Syntax (CMS).  This syntax is used to digitally
sign, digest, authenticate, or encrypt arbitrary message content.

#### RFC 3370 Cryptographic Message Syntax (CMS) Algorithms

**URL:** http://www.ietf.org/rfc/rfc3370.txt

This document describes the conventions for
using several cryptographic algorithms with the Cryptographic Message Syntax
(CMS).  The CMS is used to digitally sign, digest, authenticate, or
encrypt arbitrary message contents.

#### RFC 3401 Dynamic Delegation Discovery System (DDDS) Part One: The Comprehensive DDDS

**URL:** http://www.ietf.org/rfc/rfc3401.txt

This document specifies the exact documents
that make up the complete Dynamic Delegation Discovery System (DDDS). 
DDDS is an abstract algorithm for applying dynamically retrieved string
transformation rules to an application-unique string.  This document along
with RFC 3402, RFC 3403 and RFC 3404 obsolete RFC 2168 and RFC 2915,
as well as updates RFC 2276.

  

#### RFC 3402 Dynamic Delegation Discovery System (DDDS) Part Two: The Algorithm

**URL:** http://www.ietf.org/rfc/rfc3402.txt

This document describes the Dynamic
Delegation Discovery System (DDDS) algorithm for applying dynamically
retrieved string transformation rules to an application-unique string. 
Well-formed transformation rules will reflect the delegation of management of
information associated with the string.  This document is also part of a
series that is completely specified in "Dynamic Delegation Discovery System (DDDS) Part One: The Comprehensive DDDS"
(RFC 3401).  It is very important to note that it is impossible to
read and understand any document in this series without reading the others.

#### RFC 3403 Dynamic Delegation Discovery System (DDDS) Part Three: The Domain Name System (DNS) Database

**URL:** http://www.ietf.org/rfc/rfc3403.txt

This document describes a Dynamic Delegation
Discovery System (DDDS) Database using the Domain Name System (DNS) as a
distributed database of Rules.  The Keys are domain-names and
the Rules are encoded using the Naming Authority Pointer (NAPTR)
Resource Record (RR).

Since this document obsoletes RFC 2915, it is
the official specification for the NAPTR DNS Resource Record.  It is also
part of a series that is completely specified in "Dynamic
Delegation   Discovery System (DDDS) Part One: The Comprehensive
DDDS" (RFC 3401).  It is very important to note that it is impossible
to read and understand any document in this series without reading the others.

#### RFC 3404 Dynamic Delegation Discovery System (DDDS) Part Four: The Uniform Resource Identifiers (URI)

**URL:** http://www.ietf.org/rfc/rfc3404.txt

This document describes a specification for
taking Uniform Resource Identifiers (URI) and locating an
authoritative server for information about that URI.  The method
used to locate that   authoritative server is the Dynamic Delegation
Discovery System.  This document is part of a series that is specified in
"Dynamic Delegation Discovery System (DDDS) Part One: The Comprehensive DDDS"
(RFC 3401).  It is very important to note that it is impossible
to   read and understand any document in this series without reading
the others.

#### RFC 3405 Dynamic Delegation Discovery System (DDDS) Part Five: URI.ARPA Assignment Procedures

**URL:** http://www.ietf.org/rfc/rfc3405.txt

This document is fifth in a series that is
completely specified in "Dynamic Delegation Discovery System (DDDS) Part
One: The Comprehensive DDDS" (RFC 3401).  It is very important to note that it is impossible to read and understand any document
in this series without reading the others.

RFC 3414  User-based
Security Model (USM) for version 3 of the Simple Network Management Protocol
(SNMPv3)

**URL:** http://www.ietf.org/rfc/rfc3414.txt

This document describes the User-based
Security Model (USM) for Simple Network Management Protocol (SNMP) version 3
for use in the SNMP architecture.  It defines the Elements of Procedure
for providing SNMP message level security.  This document also includes
a   Management Information Base (MIB) for remotely
monitoring/managing the configuration parameters for this Security Model. 
This document obsoletes RFC 2574.

#### RFC 3447 Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.1

**URL:** http://www.ietf.org/rfc/rfc3447.txt

This memo represents a republication of PKCS
#1 v2.1 from RSA Laboratories' Public-Key Cryptography Standards (PKCS) series,
and change control is retained within the PKCS process.  The body of this
document is taken directly from the PKCS #1 v2.1 document, with certain
corrections made during the publication process.

#### RFC 3647 Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework

**URL:** http://www.ietf.org/rfc/rfc3647.txt

This document presents a framework to assist
the writers of certificate policies or certification practice statements for
participants within public key infrastructures, such as
certification   authorities, policy authorities, and communities of
interest that wish to rely on certificates.  In particular, the framework
provides a comprehensive list of topics that potentially (at the writer's   discretion) need to be covered in a
certificate policy or a certification practice statement.  This document
supersedes RFC 2527.

#### RFC 3761 The E.164 to Uniform Resource Identifiers (URI) Dynamic Delegation Discovery System (DDDS) Application (ENUM)

**URL:** http://www.ietf.org/rfc/rfc3761.txt

This document discusses the use of the Domain
Name System (DNS) for storage of E.164 numbers.  More specifically, how
DNS can be used for identifying available services
connected to one E.164 number.  It specifically obsoletes RFC 2916 to
bring it in line with the Dynamic   Delegation Discovery
System (DDDS) Application specification found in the document series specified
in RFC 3401.  It is very important to note that it is impossible to read
and understand this document without reading the documents discussed in RFC
3401.

### Other Security Technology Documents

#### IEEE Documents on Security Technologies

##### IEEE 802.11b Web Encryption Protocol

**URL:** http://www.ieee.org

From <http://cms.syr.edu/connecting/wireless/glossary.html>:

Also referred to as 802.11 High Rate or Wi-Fi Applies to wireless LANs and
provides 11 Mbps transmission (with a fallback to 5.5, 2 and 1 Mbps
depending on Range and Signal Strength) in the 2.4 GHz band. 802.11b uses only
DSSS (Acronym for direct-sequence spread spectrum. DSSS is one of two types of
spread spectrum radio.) 802.11b was a 1999 IEEE ratification to the original
802.11 standard, allowing wireless functionality comparable to Ethernet.

##### IEEE 802.11i Security for Wireless Networks (WPA2)

**URL:** http://standards.ieee.org/reading/ieee/std/lanman/drafts/P802.11i.pdf

The IEEE 802.11i protocol is the update to
802.11 security that includes all of the interim measures found in WPA (Wi-Fi Protected Access), and also adds a longer,
strong encryption key using AES and fast handoff through quick reauthentication among access points.

Confidentiality, Policy, Authorization for
Access Control, Encryption, Security

##### IEEE Personal and Private Information (PAPI) draft standard

**URL:** http://www.ieee.org

PAPI is a system for providing access control
to restricted information resources across the Internet. The authentication
mechanisms are designed to be as flexible as possible, allowing each
organization to use its own authentication schema, keeping user privacy, and
offering information providers data enough for statistics. Access control
mechanisms are transparent to the user and compatible with the most commonly
employed Web browsers and any operating system. Since PAPI uses
standard HTTP procedures, PAPI authentication and access control does not
require any specific hardware or software, thus providing users with ubiquitous
access to any resource they have right to.

#### RSA Documents on Security Technologies

##### RSA PKCS #8 Private-Key Information Syntax Standard

**URL:** ftp://ftp.rsasecurity.com/pub/pkcs/doc/pkcs-8.doc

This standard describes a syntax for
private-key information.  Private-key information
includes a private key for some public-key algorithm and a set of
attributes.  The standard also describes a syntax for encrypted private
keys.  A password-based encryption algorithm (e.g. one of those described
in PKCS #5) could be used to encrypt private-key information.

##### RSA PKCS #12 Personal Information Exchange Syntax Standard, version 1.0.

**URL:** ftp://ftp.rsasecurity.com/pub/pkcs/pkcs-12/pkcs-12v1.pdf

From:
https://selfservice.exostar.com/certenroll/client/help/concepts/glossary.htm

A standard that specifies a portable format
for storing or transporting a user's private keys and Digital IDs.

PRIVATE KEY A mathematical key (kept secret
by the holder) used to create digital signatures and, depending upon the
algorithm, to decrypt messages or files encrypted
(for confidentiality) with the
corresponding public key.

#### OASIS Documents on Security Technologies

##### Security for Grid Services

**URL:** http://www.globus.org/Security/GSI3/GT3-Security-HPDC.pdf

Provides policy directives for distributed
computing environments.

##### Attribute Profiles for SAML 2.0

**URL:** http://www.oasis-open.org/committees/download.php/6344/sstc-hughes-mishra-baseline-attributes-03.pdf

Provides flexible means of specifying
attribute names and values within SAML 2.0. Additionally, it provides a
flexible means of specifying queries.

##### SAML 2.0: Security Assertion Markup Language Version 2.0

**URL:** http://www.oasis-open.org/committees/download.php/2290/oasis-sstc-saml-1.0.zip

This document provides extensions to SAML 2.0
that allows for exchanging of authentication and authorization information
between security systems.

##### OASIS Security Assertion Markup Language (SAML) V2.0

**URL:** http://www.oasis-open.org/committees/download.php/6773/sstc-saml-bindings-2.0-draft-11-diff.pdf

This document specifies SAML protocol
bindings for the use of SAML assertions and request-response messages in communications protocols and
frameworks.

Protocol Binding Concepts:  Mappings of
SAML request-response exchanges onto standard messaging or communication protocols are call SAML protocol bindings.

##### Authentication Context

**URL:** http://www.oasis-open.org/committees/download.php/6539/sstc-saml-authn-context-2.0-draft-04a-diff.pdf

This specification defines an XML Schema for
the creation of Authentication Context statements that allow the
authentication authority to provide to the service provider this
additional information.  Additionally, this specification defines a number
of Authentication Context classes: categories into which many Authentication
Context will fall, thereby simplifying their interpretation.

##### Web Services Policy Framework (WS-Policy)

**URL:** http://xml.coverpages.org/ws-policyV11.pdf

The Web Services Policy Framework (WS-Policy)
provides a general-purpose model and corresponding syntax to describe an
communicate the policies of a Web Service.  WS-Policy defines a base set
of constructs that can be used and extended by other Web Sevices
specifications.

##### Web Services Policy Assertions Language (WS-PolicyAssertions)

**URL:** http://xml.coverpages.org/ws-policyassertionsV11.pdf

This
document specifies a set of common message policy assertions that can be
specified within a policy. 

By using the XML, SOAP, and WSDL
extensibility models, the WS\* specifications are designed to be composed with
each other to provide a rich Web services environment.  PolicyAssertions by itself does not provide a negotiation
solution for Web services. It is a building block that is used in conjunction
with other Web service and application-specific protocols to accommodate a wide
variety of policy exchange models.

##### Web Services Policy Attachment (WS-PolicyAttachment)

**URL:** http://xml.coverpages.org/ws-policyattachmentV11.pdf

This document specifies three specific
attachment mechanisms for using policy expressions with existing XML Web
service technologies. 

##### OASIS Extensible Access Control Markup Language (XACML)

**URL:** http://xml.coverpages.org/xacml-schema-policy-v15.pdf

The
objective of XACML is to provide a mechanism policy exchange by defining
a language capable of expressing policy statements for a wide variety of
information systems and devices.

#### World Wide Web Consortium (W3C) Documents on Security Technologies

##### WC3 XML Key Management Specification (XKMS 2.0) Bindings

**URL:** http://www.w3.org/TR/xkms2/

This document specifies protocols for distributing
and registering public keys, suitable for use in conjunction with the W3C
Recommendations for XML Signature [[XML-SIG]](http://www.w3.org/TR/xkms2/#XML-SIG) and
XML Encryption [[XML-Enc](http://www.w3.org/TR/xkms2/#XML-Enc)].
The XML Key Management Specification (XKMS) comprises two parts — the XML Key
Information Service Specification (X-KISS) and the XML Key Registration Service
Specification (X-KRSS).

##### W3C The Platform for Privacy Preferences 1.1 (P3P1.1) SpecificationW3C Working Draft 27 April 2004

**URL:** http://www.w3.org/TR/2004/WD-P3P11-20040427/

This is the specification of the Platform for
Privacy Preferences 1.1 (P3P 1.1). This document, along with its normative
references, includes all the specification necessary for the implementation of interoperable P3P 1.1 applications. P3P 1.1 is based on
[the P3P 1.0 Recommendation](http://www.w3.org/TR/P3P/) and
adds some features using the [P3P 1.0 Extension mechanism](http://www.w3.org/TR/P3P/#extension). It
also contains a new binding mechanism that can be used to bind policies for XML
Applications beyond HTTP transactions.

#### Miscellaneous Security Technologies

##### AGA-12 Cryptographic Protection of SCADA Communications General Recommendations.

**URL:** http://www.aga.org

The American Gas Association (AGA) represents
almost 200 local utilities that deliver natural gas to homes in the USA. These
utilities are part of the critical infrastructure and
rely on SCADA networks to control the operations. AGA, in conjunction
with GTI and other industry groups, created AGA 12 to develop cyber security
standards and protocols for the industry.

AGA 12 has taken a unique approach to focus
on securing the communications link between field devices and the control
servers or control center. While there certainly is a risk of data insertion
and modification in the communication channel, it may not be the most likely or
even easiest avenue of attack on a SCADA system.

The [first
Technical Report, TR-1](http://www.gtiservices.org/security/aga12_wkgdoc_homepg.shtml),
defines an add-on encryption module that also could be integrated
into an RTU or PLC. Oddly
enough, the most recent version includes significantly less technical detail
and removed the SCADA Link Security (SLS) protocol defined in Appendix K. If
you are interested in AGA 12, Digital Bond recommends you look at [Appendix
K of the March 2003 version](http://www.gtiservices.org/security/AGA%20Report%20No%2012%20Rev1.0.doc).
Note: hit cancel when the login request appears and the document will load.

The big hole in TR-1 is key management which
is to be addressed at a later date. This is a significant issue given the
number of encryptors that would be deployed in a
SCADA system. Until key management is addressed AGA 12-1 encryptors
can be considered a proof of concept solution at best.

The best news on the AGA 12 front is [sample implementation code exists](http://scadasafe.sourceforge.net/).
Andrew Wright of Cisco's Critical Infrastructure Assurance Group (CIAG) has
written and documented the code. There are also good technical papers on the
security of the protocol available through Andrew's ScadaSafe
site.

  Confidentiality, Authorization for
Access Control, Policy, Eavesdropping, Security

##### ANSI INCITS 359-2004 Role Based Access Control (RBAC)

**URL:** http://www.incits.org/

Security
administration can be costly and prone to error because administrators usually
specify access control lists for each user on the system individually. With
RBAC, security is managed at a level that corresponds closely to the
organization's structure. Each user is assigned one or more roles, and each
role is assigned one or more privileges that are permitted to users in that
role. Security administration with RBAC consists of determining the operations
that must be executed by persons in particular jobs, and assigning employees to
the proper roles. Complexities introduced by mutually exclusive roles or role
hierarchies are handled by the RBAC software, making security administration
easier. 

##### BCP 65 Dynamic Delegation Discovery System (DDDS) Part Five: URI.ARPA Assignment Procedures

**URL:** http://www.armware.dk/RFC/bcp/bcp65.html

See RFC 3405.

##### EPRI 1002596 ICCP TASE.2 Security Enhancements

**URL:**http://www.epri.com

Determines the security vulnerabilities for
IEC 60870-6 TASE.2 (ICCP) and provides recommended solutions to those
vulnerabilities.  This document is the basis for several of the IEC TC57
WG15 IEC 62351 documents.

##### Java Card Java Card Platform Specification v 2.2.1

**URL:** http://java.sun.com/products/javacard/specs.html

Java Card technology is the leading open,
interoperable platform for smart cards. The new version 2.2.1 of the Java Card
Specifications provides a small set of targeted enhancements to facilitate
alignment with smart card industry standards. In particular it ensures an
efficient integration of Java Card technology with the GlobalPlatform
2.1.1 and ETSI "UICC for Java Card" specifications.

Version 2.2.1 is an update to the Java Card
2.2 Specifications.
As such it provides the same benefits the previous release brought to
developers and smart cards issuers:

**Advanced support for wireless products** - Provides
access to more sophisticated and interoperable services through logical
channel support requested by standards organizations, such as European
Telecommunications Standards Institute (ETSI), Third Generation Partner Project
(3GPP) and Wireless Access Protocol (WAP).

**Improved memory management** - Enables issuers to optimize use of
memory space on a smart card.

**Easier design and development of
applications** - Java Card Remote Method Invocation allows developers to
design applications more easily by enabling the use of Java technology for both
the card and terminal.

**Improvements for compatibility** - Helps
manufacturers ensure compliance of implementations to provide issuers with
flexibility and choice in selecting interoperable smart card offerings.

**Next-generation security enhancements**
- Provides issuers with more security options by supporting additional
cryptographic algorithms AES and Elliptic Curve.

**Backward compatibility** - Java Card
version 2.1 applications will run on Java Card 2.2.1 products without any
modifications, thereby ensuring a smooth transition for scores of applications
available today on millions of Java Card technology-enabled smart cards.

Java Card technology, version 2.2.1 builds on
the success of previous versions, providing smart card vendors, issuers and
developers with proven technology for the deployment of secure and
interoperable card services.

##### NERC Certificate Policy for the Energy Market Access and Reliability Certificate (e MARC) Program Version 2.4

**URL:** ftp://www.nerc.com/pub/sys/all\_updl/cip/pkitf/e-MARC-PKI\_draft\_version\_V2-4b\_March\_2003-rev1.doc

Provides recommendations in regards to
certificate authority selection, certificate distribution, and other
certificate related issues.

##### NIST GSC-IS The NIST Interagency Report 6887 - 2003 edition (Government Smart Card-Interoperability Specification) Version 2.1

**URL:** http://csrc.nist.gov/publications/nistir/nistir-6887.pdf

The document defines an architectural model
for interoperable smart card service provider modules compatible with both file
system cards and virtual machine cards.  It includes a Basic Services
Interface which addresses interoperability of a core set of smart card services
at the interface layer between client applications and smart card service
provider modules.  It also defines a mechanism at the card edge layer for
interoperation with smart cards that use a wide variety of APDU sets,
including both file system cards and virtual machine cards.

##### NISTIR 6529 Common Biometric File Format (CBEFF)

**URL:** http://www.itl.nist.gov/div893/biometrics/documents/NISTIR-6529-A.pdf

The Common Biometric Exchange Formats
Framework (CBEFFF) describes a set of data elements necessary to support
biometric technologies in a common way.  These data
elements can be placed in a single file used to exchange biometric information
between different systems developed by different vendors.

##### Semantic Web Pervasive Computing Standard Ontology (PERVASIVE-SO) Guide -- Describing User Profile and Preferences

**URL:** http://pervasive.semanticweb.org/doc/2004-01-ont-guide/part1/

In a pervasive computing environment,
computer systems often need to access the profiles and the preferences of a
user in order to provide services and information that are tailored to the
user. The profile of a user includes typical contact information (telephone
numbers, email addresses, name, etc.) and information that describe other
computing entities that can act on the behalf of the user
(e.g., the personal agent of a user). The preference of a user is a
description of the environment state that the user desires the computer systems
to honor or achieve whenever it is possible.

 The purpose of this document is to show
how to describe the profile and the preferences of a user using the PERVASIVE-SO
ontologies, which are defined using [the
Web Ontology Language OWL.](http://www.w3.org/TR/2003/PR-owl-features-20031215/)
Readers are assumed to be familiar with the OWL language and its associated
terminologies. For details on the OWL language, readers can consult the listed
documents in the [References](http://pervasive.semanticweb.org/doc/2004-01-ont-guide/part1/#references)
section.

##### Smart Card Alliance Smart Card Primer

**URL:** http://www.smartcardalliance.org/industry\_info/smart\_cards\_primer.cfm

Provides a high level overview of Smart Card
technology and describes how the technology works.

##### Smart Card Alliance Privacy and Secure Identification Systems: The Role of Smart Cards as a Privacy-Enabling Technology

**URL:** http://www.smartcardalliance.org

Individuals are currently required to confirm
their identity for many diverse purposes, such as verifying eligibility within
a health care system, accessing a secure network or facility, or validating
their authority to travel. In almost every discussion about implementing
personal identification (ID) systems to improve identity verification
processes, concerns about privacy and the protection of personal information
quickly emerge as key issues. Government agencies and private businesses that
are implementing ID systems to improve the security of physical or logical
access must factor these issues into their system designs.
While technologies are available that can provide a higher level of
security and privacy than ever before, ID system complexity coupled with
increasing public awareness of the risks of privacy intrusion require that organizations focus on privacy and personal
information protection throughout the entire ID system design.

##### Smart Card Alliance Government Smart Card Handbook

**URL:** http://www.smartcardalliance.org/pdf/industry\_info/smartcardhandbook.pdf

Provides the use practices of the US
Government for Smart Cards.

##### WebDAV Access Control Extensions to WebDAV

**URL:** http://www.webdav.org/acl/protocol/draft-ietf-webdav-acl-13.htm

This document specifies a set of methods,
headers, message bodies, properties, and reports that define Access Control
extensions to the WebDAV Distributed Authoring
Protocol. This protocol permits a client to read and modify access control
lists that instruct a server whether to allow or deny operations upon a
resource (such as HyperText Transfer Protocol (HTTP) method invocations) by a
given principal. A lightweight representation of principals as Web resources
supports integration of a wide range of user management repositories. Search
operations allow discovery and manipulation of principals using human names.

##### WPA WI-FI Protected Access

See IEEE 802.11b

##### WPA2 WI-FI Protected Access Version 2

See
IEEE 802.11i

##### TMN PKI - Digital certificates and certificate revocation lists profiles

**URL:** http://webstore.ansi.org/ansidocstore/product.asp?sku=T1.268-2000

This standard is intended to
promote interoperability among TMN elements that use Public Key
Infrastructure (PKI) to support security-related functions. It applies to all
TMN interfaces and applications. It is independent of which communications
protocol stack or which network management protocol is being used. PKI
facilities can be used for a broad range of security functions, such as,
authentication, integrity, non-repudiation, and key exchange. However, this
standard does not specify how such functions should be implemented, with or
without PKI.

 

---

[[1]](IECSA_VolumeIV_AppendixA.htm#_ftnref1) This
is even potentially true within a single business entity.

[[2]](IECSA_VolumeIV_AppendixA.htm#_ftnref2)
Extracted and modified from reference [3]

[[3]](IECSA_VolumeIV_AppendixA.htm#_ftnref3)extracted from  http://sybooks.sybase.com/onlinebooks/groupsec/secg0253e/epsec/@Generic\_\_BookTextView/13539;pt=7509

[[4]](IECSA_VolumeIV_AppendixA.htm#_ftnref4) The
actual technology recommendation for Smart-Cards can be found in the Identity
Establish service section.

[[5]](IECSA_VolumeIV_AppendixA.htm#_ftnref5)
Image courtesy of Allegiant Data Systems

[[6]](IECSA_VolumeIV_AppendixA.htm#_ftnref6) The
definition was removed from RFC 2437.

[[7]](IECSA_VolumeIV_AppendixA.htm#_ftnref7) It
is worthy to note that initially the ability to record with enough quality was cost
and size prohibitive (from a security threat perspective).  But digital
recording technology is now inexpensive and small making it relatively easy to
spoof a system.  The voice biometric technology represents a good example of why re-evaluation of security policies,
procedures, and technologies need to be re-evaluated when there
are significant changes intechnology.

[[8]](IECSA_VolumeIV_AppendixA.htm#_ftnref8) PostWeek Tech Media, July 22, 2003, Vandana Sinha, Passports to get
facial biometrics.  Available from
http://www.washingtontechnology.com/news/1\_1/daily\_news/21271-1.html

[[9]](IECSA_VolumeIV_AppendixA.htm#_ftnref9) Extracted from
http://csrc.nist.gov/publications/nistpubs/800-7

[[10]](IECSA_VolumeIV_AppendixA.htm#_ftnref10) From: http://www.eon-commerce.com/riskanalysis/whatis.htm

[[11]](IECSA_VolumeIV_AppendixA.htm#_ftnref11) For electric utility infrastructures, a successful security attack could impactother
infrastructures.  Therefore, infrastructure impact on other
infrastructures and the public must be taken into account during the risk
assessment. EPRI Report 1008988 provides a more detailed discussion.

[[12]](IECSA_VolumeIV_AppendixA.htm#_ftnref12) Assuming the following characters: !, @, #, $,
%,^,&,\*,( , ), \_, -, +, =, {, }, [, ], |, \, :, ;, “,’, <, >, . ,
comma, ?, and /. For a total of 30.

[[13]](IECSA_VolumeIV_AppendixA.htm#_ftnref13) Extracted from RFC 3053 –IPv6
Tunnel Broker

[[14]](IECSA_VolumeIV_AppendixA.htm#_ftnref14) RFC 2246

[[15]](IECSA_VolumeIV_AppendixA.htm#_ftnref15) For the full
definition refer to the appropriate section of IntelliGrid Architecture document set.
