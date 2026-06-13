# Example

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Overview_Guidelines/Gud_Example_Protection_Engineer.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Example of Using the IntelliGrid Architecture

## ***Protection Engineer Reviews and Modify Protection Settings***

Among the many potential IntelliGrid Architecture uses, this section presents
but one example, in some detail, to illustrate how one can obtain benefits from
IntelliGrid Architecture.

### Statement of the Problem – Protection Planning Engineer

A protection engineer wants to review fault
recorder information and modify settings in a protection device in a
substation. She currently uses a dial-up modem from her workstation (which is
connected to a modem bank through the corporate network) to the substation to
review the information, but then must physically travel (or send someone) to the
substation to modify the settings. This system has been in place a number of
years and has worked reasonably well. However, the engineer has been told that
all dial-up modems must be eliminated due to security concerns. Also, as
staffing has been reduced, traveling to the substation herself, or sending
someone, must be minimized. What to do?

The protection engineer goes to the Power System
Functions on IntelliGrid Architecture website (or the Use Cases narratives in Volume 2) and
finds a function (Transmission Operations – Automated Control Baseline) that is
similar to her situation. She does note some differences, however. First, the
Automated Control function assumes that protection devices can be accessed
through a ‘substation master’, but in her situation, each protection device
must be accessed separately. She is also aware that most of the protection
devices are not configured to allow remote updating of settings (for security
reasons), while the function assumes remote updates can be made. While this
function is therefore not a perfect solution for the engineer, it is a strong
start.

### Engineering the Solution – Project Engineer

The protection engineer goes to the project
engineer for help in the next steps. She shows him the Automated Control
function on his computer by linking to IntelliGrid Architecture website and quickly jumping to
the appropriate page. She explains what she needs and now it is similar but
still somewhat different from the description of the function.

The project engineer quickly scrolls down to the
Steps section of the Automated Control function and starts reviewing the steps
until he finds the step that is closest to the problem she has identified.
Scanning over to the Environments column, he realizes that the closest IntelliGrid Architecture
Environment to what she needs is the Critical Operations Intra-Substation
Environment. He clicks on the link in the step.

### Requirements

The Automated Control function’s requirements have
identified the following as key requirements which links to the Critical
Operations Intra-Substation Environment:

§      
Configuration Requirements

–   Provide
point-to-point interactions between two entities

–   Support
peer to peer interactions

–   Support
interactions within a contained environment (e.g. substation or control center)

§      
Quality of Service Requirements

–   Provide
high speed messaging of less than 1 second

–   Support
very high availability of information flows of 99.99+ (~1 hour)

–   Support
time synchronization of data for age and time-skew information

§      
Security Requirements

–   Provide
Authorization Service for Access Control (resolving a policy-based access
control decision to ensure authorized entities have appropriate access rights
and authorized access is not denied)

–   Provide
Information Integrity Service (data has not been subject to unauthorized
changes or these unauthorized changes are detected)

–   Provide
Audit Service (responsible for producing records, which track security
relevant events)

–   Provide
Credential Renewal Service (notify users prior to expiration of their
credentials)

–   Provide
Security Policy Service (concerned with the management of security policies)

–   Provide
Single Sign-On Service (relieve an entity having successfully completed the act
of authentication once from the need to participate in re-authentications upon
subsequent accesses to managed resources for some reasonable period of time)

–   Provide
Security Discovery (the ability to determine what security services are available
for use)

§      
Network and System Management Requirements

–   Provide
Network Management (management of media, transport, and communication nodes)

–   Provide
System Management (management of end devices and applications)

§      
Data Management Requirements

–   Support
the management of large volumes of data flows

–   Support
keeping the data up-to-date

–   Support
extensive data validation procedures

–   Support
specific standardized or de facto object models of data

–   Provide
discovery service (discovering available services and their characteristics)

–   Provide
conversion and protocol mapping

### IntelliGrid Architecture High Level Concepts

These requirements link to a number of recommended
technologies, services, and best practices that are based on the IntelliGrid Architecture High Level Concepts. Therefore, the project engineer
first reads through the IntelliGrid Architecture High Level Concepts by
clicking on the different topics under ‘IntelliGrid Architecture Framework’. These
topics include:

§      
Abstract modeling

§      
Security services, risk assessment, and policies

§      
System and network management services

§      
Data management issues

§      
Integration and interoperability

The project engineer notes that they have been
advocating object-oriented approaches for a few years, but has run into ‘legacy
system’ issues and lack of management support that have prevented him from
moving forward in that direction.

### Platform Independent Model

The project engineer should understand how the high
level concepts are realized in a technology independent way.  While the
exact technology used to implement the architecture may vary from vendor to
vendor or over time, the Platform Independent Model provides continuity to ensure
that a unified approach is maintained.  Additionally, the Platform
Independent Model provides for a level of interoperability that cannot be
achieved via just the specification of high-level concepts and technology.

### Recommended Technologies, Services, and Best Practices

Next, he examines the technologies identified as
recommended and alternative solutions for the Critical Operations
Intra-Substation Environment. These recommended technologies and alternative
solutions include the following (in part).

§      
Energy Industry-Specific Technologies

–   ISO
9506 MMS–Manufacturing Messaging
Specification - Configuration, Quality of Service,

–   IEC61850–Substation
Automation Communications - Configuration,

–   IEC61850
Part 7-2–GSE (GOOSE and GSSE - Configuration,
Quality of Service,

–   IEC61850
Part 7-2–SMV (Sampled Measured Values) -
Configuration,

–   IEC61850
Part 7-2–Abstract Common Services Interface (ACSI) - Configuration, Quality of
Service, Data Management

–   IEC61850
Parts 7-3 and 7-4–Substation Object Modeling - Network Management, Data
Management

–   IEC61850
Part 6–Substation Configuration Language - Network Management, Data Management

–   IEC61850
Power Quality Object Models - Data Management

§      
Security Functionality

–   FIPS
197 for Advanced Encryption Standard (AES) -
Security,

–   Role-Based
Access Control - Security,

–   FIPS
186 Digital Signatures Standard (DSS) -
Security,

–   Intrusion
Detection Technologies - Security, Network Management,

–   Intrusion
Prevention Systems (IPS) - Security, Network
Management,

–   Service
Level Agreements (SLA) - Security,

§       
Network and System Management Functionality

–   Simple
Network Management Protocol (SNMP) - Network Management,

–   IEC
62351-7 Objects for Network Management - Quality of Service, Network
Management, Data Management

The project engineer has heard of AES
but isn’t really sure what it is and where it stands in terms of being
implemented by vendors. IEC61850 is just a number and he hasn’t a clue what it
is. He is quite familiar with SNMP, but has never heard of it being used within
a substation. This intrigues him, because he has been under increasing pressure
from the IT department to implement Internet-based technologies. If it really
pans out that SNMP could help him solve her problem, then he will have killed
two birds with one stone.

### Use of UML to Develop Specific Use Case

However, spurred by the IntelliGrid Architecture concept of using UML for abstract modeling of functions, and with
the help of one of his IT colleagues, he reviews the UML diagrams of the
Automated Control function by going to the detailed UML-based Use Case links on
IntelliGrid Architecture website, and finding the detailed analysis of the Automated Control
Use Case. He creates a similar one that reflects the situation in his utility
and the specific needs of the protection engineer. He reviews this with the
protection engineer who, after adding some more details, agrees that
conceptually it meets her requirements. But the question of *how* has
still not been resolved.

### Use of Environments to Determine Solutions

The project engineer now delves into the
technologies, services, and best practices that were associated with IntelliGrid Architecture
Environment. Ultimately he decides to:

1.    
Recommend using VPNs between the corporate network and the substation
router, along with very strict role-based access control, passwords, and a
strongly worded and enforced security policy. This will allow protection
engineers to have direct access to the substation equipment again, now that the
modems have been taken out.

2.    
Recommend the time synchronization of all substation protection devices
using GPS devices. However, other devices
can be time synched using the SNTP protocol.

3.    
Recommend using IEC61850 for all new protection IEDs, but with dual
ports so that the SCADA system can continue to receive its data from the
protection IED via DNP. This approach will provide protection engineers with
more information, more accurate timestamp information, and more easily
maintained data management.

4.    
Recommend that all data, including IEC61850 objects and CIM-based
objects, use XML schemas to represent their metadata. This approach would
permit protection engineers to browse the XML-structured metadata objects, pick
the information of interest, and have this data automatically included in their
access list (if permitted under the security access control).

5.    
Recommend the implementation of data ‘brokers’ using the
publish/subscribe service to update databases. These brokers will manage data
across multiple networks, thus ensuring that key data is consistent across all
databases. This data management system would include backup systems, automatic
update of databases if they were off-line, roll-back of data if warranted, and
other tools for managing data.

### Architecting for the Future – Automation Architect

After the project engineer completes his tasks in
supporting the protection engineer, he sets up a meeting with the CIO of his
company. He shows her IntelliGrid Architecture website and the web pages describing IntelliGrid Architecture
high level concepts. She acknowledges that she has heard about IntelliGrid Architecture
project and that it was making architectural recommendations, but that she had
not quite gotten around to checking it out. She agrees it is time for her and
her staff to do so.

She clicks on the Executive Summary and the Project
Summary to get a very quick overview of the project, and then jumps to the
Recommendations. She sees there the recommendations to:

§      
“Adopt the IntelliGrid Architecture as the strategic vision for your
information infrastructure”

§      
“Create systems architect positions”

§      
“Think in architectures, not projects”

After reviewing these recommendations in more
detail, and discussing the concepts and possibilities with her staff, she
develops a position paper using many of the arguments discussed in IntelliGrid Architecture
recommendations. She presents this to the other executives, shows them the
Executive Summary from IntelliGrid Architecture website, and gets their overall concurrence,
with the understanding that although IntelliGrid Architecture concepts are indeed the
strategic vision, individual decisions will need to be made on actually
implementing specific technologies, based on financial and technical
situations.

The CIO agrees with these provisos, appoints an
‘Automation Architect’, and requests that he develop a more detailed plan for
implementing IntelliGrid Architecture recommendations.
