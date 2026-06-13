# Customer Portal

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_Consumer_Portal_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - Overview of Consumer Portal

## Contents

* [Narrative - Overview](CS_Consumer_Portal_Use_Case.htm#Narrative)
* [Telecommunications](CS_Consumer_Portal_Use_Case.htm#Telecommunications)
* [Systems](CS_Consumer_Portal_Use_Case.htm#Systems)
* [Security](CS_Consumer_Portal_Use_Case.htm#Security)

## Narrative

### Overview

This scenario attempts to describe key issues
relevant to the operation of Management Systems in a large Energy
Company (Electric and/or Gas and/or Water with several million
customers) that provide access to information from and access to
control devices located at customer sites.  Access to information
from devices and access to control one or more devices on the
customer premises is provided via Customer Communications Portals.

The entities involved in the communications have
separate ownership – meters by distribution companies, power quality
information by the customers and the distribution companies, load
control devices by the customer and portals by the telecommunications
service or other customer site equipment/services provider. Although
these owners collaborate on some utility related activities, the
nature and purpose of the devices is independent of these
applications. For this reason recognition of ownership boundaries and
independent management of devices and data needs to be recognized in
the management of services that involve their collaboration.

Because some of the information gathered has
economic and other consequences, and, since acquisition of information
is imperfect, the system needs to accommodate a process of
categorization of the quality of data; that categorization may also
change over time as data is processed by various entities responsible
for using it. A listing of some of the key common macroscopic issues
include:

1)      
Recognition of the needs of multiple business entities that need
access to Portals, data derived from these portals and related
telecommunications and computing infrastructures.

2)      
Ownership of data, i.e., clear identification of who’s responsible
(Company, person, internal energy business entity or external entity,
system) for ensuring that the customer data is correct, and for data
that will be used for billing or other business purposes is validated

3)      
Data obtained from customer purposes must be stored and processed in a
secure manner with appropriate levels of back up and access control

4)      
Clear identification of business entities (internal energy company or
external), applications and individuals that can access data and issue
control commands will be established and agreed to by the energy
company and the various entities making use of the portals/access
networks.

5)      
Access control procedures will be developed and agreed to by the
various business entities (internal energy company or external) that
obtain data from energy company customer portals or that implement
control commands for particular customers or customer classes

6)      
Security Policies will be developed and agreed to by the various
business entities (internal energy company or external) that obtain
data from energy company customer portals (or databases that store
this data) or that implement control commands for particular customers
or customer classes. Particular attention should be paid to security
requirements either mandated or recommended by both Government and
regulatory communities and gleaned from best practices developed by
the business community at large.

7)      
Recognition that there may be many existing and future potential
Business Models and Business “Standard Practices” for Energy Service
provisioning from Regulatory Communities. Requirements will need to be
robust for a variety of potential business models since implementation
of direct access and other forms of energy industry deregulation are
in flux.  Thus technical requirements for supporting access to
Customer Portals and the telecommunications access networks must be
flexible enough to accommodate future Energy Services provisioning
companies and various entities’ requirements for customer data access.

if !vml?![](CS_Consumer_Portal_Use_Case_files/image002.gif)endif?

**Legend:**  EO/CD
           Energy Company Observable/Controllable Devices (Systems,
Hardware, Software, Applications, etc.)

**Notes:**

1.       
EO/CD’s may be interconnected to the Customer Communications
Portal by various LANs or wired/wireless systems

2.       
Many diverse Telecommunications Access Networks may be used to
connect to Portals

3.       
Several different Energy Management Systems may be required
including an overall “System Manager” (that deals with overall
policies, views of various business entities, etc.) a Security
Management System (that deals with authorization, security, reporting
and related issues) and a Network Management System (that deals with
the Customer Portal Access Networks and data communications issues)

4.       
Several Governmental Entities will need to access certain
information that will be obtained via the Customer Communications
Portals. Some of these are: PUC’s, FERC, FTC, FCC, FBI, DHS, NIST,
various State and Local Governmental Agencies, etc.

5.       
Several Entities outside of the Energy Companies will need to
access certain information that will be obtained via the Customer
Communications Portals. Some of these are: ISO, RTO, Independent Power
Generators, various appliance manufacturers, etc

6.       
All of the Entities shown in the boxes are routed through the
various Key Management Systems. This is meant to signify that the
policies, procedures, access control rights, security and other
enablers and constraints of these Management Systems will tailor the
views of the data that these entities can access and the control
messages that they are authorized to initiate.  This does not imply
that there will actually be individual computer/software systems that
these entities must be routed through. The diagram represents a
logical view , not a physical view.

### Telecommunications

Many Energy
companies have extensive internal telecommunications networks, leased
telecommunications systems and the Internet, which are utilized for a
variety of operational and administrative business purposes.  The
extensive deployment of Customer Communications Portals will
significantly expand telecommunications networking use and thus both
existing and new networks must be effectively managed to ensure that
they meet the needs of the Customer Communications Portal
applications, external entities requiring access to specific customer
data and the Energy Company and its customers.  Many existing
telecommunications networks utilized have their own proprietary
management systems, which are specific to their domain. As the
complexity of the networks grow, a more integrated approach is
required that can utilize information from many diverse sources
including the existing and new Customer Communications Portals and
associated access networks as well as information from components and
systems utilizing the internet.

There are several
key components that are required in order to ensure effective
management of networking systems and attached components; knowledge of
applications that are utilized by Customer Communications Portals and
associated devices, access network performance and operational metrics
(data traffic patterns, usage by application, network anomalies,
performance degradation, etc.) usage patterns of the users that make
use of the data obtained along with many other components. Specific
attributes of the applications must be know in order to ascertain if
it is being used by individuals or other applications authorized to
utilize it. In addition the type of transactions that are being
performed by the application must be known so that the type of traffic
expected can be supported. The usage patterns of many diverse users
and applications must also be known on a statistical basis in order to
ensure that the network is adequately configured to support the
traffic and the response times needed by the applications and users.

Privacy needs of
business entities, Governmental Agencies, Regulatory Agencies, Energy
Company users and other users of the retrieved data and resources of
the telecommunications access network must be assured. In order to
satisfy these needs several issues must be addressed in the
Telecommunications Network Management System; The policies determined
by the various business entities for access control and security must
be clearly identified and recognized by the Telecommunications Network
Management System (TNMS) (this does not meant that the TNMS will
implement these polices, but that it is aware of these policies and
that the policies are taken into account in the operational
configuration of the networks and that the TNMS will be aware of any
breach of the polices and log any discrepancies, provide alarms of any
breach and take corrective actions if possible.

In order to manage
the operational aspects of the Customer Communications Portal, devices
and Access Networks tools will be part of the TNMS to monitor the
network for health, performance, availability and its capability to
meet service level agreements negotiated with the various users of the
network. These tools will also provide data, which can be used by
management to ensure rapid reconfiguration of Access Network resources
to restore service during any disruptions and to reconfigure network
resources as needed to meet user needs.  These tools are indispensable
in the current business and technical networking environment where
human resources are limited and near perfect reliability and
availability of the network is almost a given.

1)    
Every application supported or enabled by the Customer
Communications Portal and Energy Company Computer systems
communicating with the Portals must be formally identified and
recognized by the Network Management System

a)    
The purpose of the application and what it is intended to
accomplish must be clearly identified and recognized by the Network
Management System

b)    
The Status of the application and the version release must be
recognized

c)     
The type of data communications required by each application
must be recognized, i.e., 

i)       
Retrieval of batch data,

ii)     
Interactive inquiry/response data,

iii)   
Downloading of application updates to Portals and Devices

d)    
The Energy Company and other (Government, ISO/RTO’s and various
regulatory bodies) users of the data must be clearly identified and
recognized

2)    
The overall data load must be recognized by the Network
Management System for each application, including:

i)       
Average data uploaded from each Portal

ii)     
Average data download to each Portal

iii)   
Peak data load in each direction

iv)   
The number of transactions per day, hour, etc

v)     
The transaction message size in bytes in each direction

3)    
The privacy and security requirements for each application must
be identified and recognized by the Network Management System. Note
this does not imply that the Network Management System will have the
capability to set or change any security or privacy settings or
levels, only that the Network Management System knows what the
application and user security requirements are.

a)    
The location of each Portal and supported devices that make use
of each application must be known so that the topology of the various
system components on an application basis is recognized

4)    
Service Level data must be collected and logged, by application
and by user in order to ensure that service level agreements made with
the internal and external users of the data and the Energy Company
Customers is maintained. If any significant deviation is revealed by
the data obtained controlling actions on the telecommunications access
network, or components must be taken (note that some action will take
place in an automated basis, but in other cases design changes must be
undertaken)

5)    
Continuous data relative to the health of the network
components must be obtained from each major element of the
telecommunications access network in order to ensure that any downtime
of the network or of sub network components is kept to a minimum. This
is also necessary in order to ensure that problem resolution
activities are quickly implemented and escalation of problems is kept
to a minimum

a)    
Diagnostic tools will be an integral part of the Network
Management System in order to support the problem determination
portion of the system and to help evaluate the statistics obtained
from the network

b)    
Preventative maintenance procedure development will be based on
evaluation of data obtained

6)    
Network testing must be executed on a regularly scheduled basis
to ensure that each major component of the telecommunications network
is functioning properly and within design parameters (even though
alarm systems will notify the Network Management System of component
failures partial failures or performance degradations may not trigger
alarms).

7)    
Network recovery procedures must be in place to ensure that any
telecommunications access network failures will not impact receipt of
data from the Customer Communications Portals and associated devices.

a)    
Note that this function must be performed in an automated
fashion and must be consistent with the need as defined by the
application and service level agreements made with the users and
Energy Company customers.

8)    
Configuration management procedures will be enabled in order
to:

i)       
Maintain the proper service level agreements by application,
users and customers

ii)     
Appropriate utilization of telecommunications network access
resources

iii)   
Ensure that alternate routing is available for critical
services

iv)   
Defective components are bypassed

9)    
Telecommunication Access Network, Customer Communications
Portal and Customer Device activation, deactivation and connection set
up tools will be an integral component of the Network Management
System

### Systems

The management of many facets of obtaining data
from and sending commands or sending data to the Customer
Communications Portals/Devices is a necessary and very important
undertaking from a data protection, access control, security and
network management perspective. There are several key elements that
must be managed; issues and assumptions for these diverse areas will
be covered separately. The first area to be covered will be System
Management, the second Network Management and lastly, Security
Management. There are no assumptions made as to how these management
systems will be implemented; there may be one, two, three or many
separate computing systems or many distributed systems to accomplish
these management tasks.  What is important is that the principal
issues are identified and that essential tasks are defined well enough
to understand what must be done to manage the Customer Communications
Portals and the access networks.

System Management functions are functions that
deal with the highest-level issues that are required in order to
effectively manage the Customer Communications Portals and the access
networks. Many of these functions are critical, e.g., addressing of
all Customer Communications Portals, devices supported by the portals
and indeed every access network system, subsystem or functional
element. The ability to access any of these devices is necessary in
order to be able to communicate with the device as to its status, to
obtain stored data, to download software upgrades and patches, to
change set points, read registers, etc. Without a unique address for
each device this becomes a very difficult task, if not unmanageable
task.  It would seem on the surface that unique addresses would be
supplied by vendors of these products, however, many vendors have
proprietary addressing schemes, or feel that addresses should be
unique only on sub networks, i.e., replicate addresses for different
networks, etc. Thus one of the first critical steps that need to be
taken by a System Manger is to ensure that there are indeed unique
addresses for every element of the Customer Communications Portal and
access network that requires any form of intercommunications.

In order to support the many users of data within
the Energy company as well as Customers and external entities,
regulators and Governmental entities many different computer
applications will be employed in the gathering of data, management of
data and applications that provide needed functionality in the
Customer Portals and Devices. Many of these applications will be
written and supported by the Energy Company, others will be
commercially available applications, and third parties will develop
others. In all of these cases it is essential from an operational
perspective to ensure that applications are functioning correctly,
have the latest revisions running, are up to date in terms of security
and other patches and are accessible only by business entities, other
applications and individuals authorized to utilize them.

A key function that is needed to ensure efficient
operation of a large distributed network such as the Customer
Communications Portal network is the use of a common digital clock.
The clock should be referenced to a highly stable and accurate clock
such as ones maintained and operated by the National Institute of
Standards and Technology (NIST). This will ensure that each Portal and
Device is synchronized to an accurate time reference and enable any
event occurring (equipment fault, alarm, component switching, etc) on
the network to be accurately logged and any command issued to a
Portal/Device to be accurately time stamped. This is also necessary as
a means of analyzing data from many devices on the network to
investigate operational anomalies and for resolving complex
maintenance problems that might occur.

In addition to the utilization of a common clock
there is a clear need for identifying the location of each Portal,
Devices and key Communications Access systems and subsystems. Indeed
there are many Energy Company applications (such as Customer
Information Systems [CIS], and Geographic Information Systems [GIS])
that have location information by customer, some electrical elements
(such as distribution transformers) etc. Other Energy company systems,
including Outage Detection / Service Restoral Systems, may in fact
make use of some CIS or GIS information to aid in the rapid location
of outages so that service may be restored quickly.  Given that
Customer Communications Portals may be extensively deployed, it is
essential that a universal means of defining locations of the portals,
devices and key communications systems components be developed that
can be utilized for Customer Portal identification and applications
serving them and which can also be applied to existing applications
such as CIS and GIS.

1)      
Addressing of all Customer Communications Portals, EO/CDs and
Communications Systems observable and controllable elements,
applications and management entities must be unique and identified in
a consistent manner

2)       
Management Integration: Since there will be many different types of
communications systems and subsystems used to interconnect the Energy
Company to Customer Communications Portals, there will be many
different Network Management Systems used by the Communications
service providers. It is critical that the “Energy Company Management
Systems” be capable of communicating and interacting with the
Communications Service provider Network Management Systems and
especially with their “Network users management application entity”
(software in communications subsystems and devices providing network
management services) in a consistent manner[if !supportFootnotes?[1]endif?](CS_Consumer_Portal_Use_Case.htm#_ftn1).

3)       
Use of a consistent clock that is referenced to a primary time source.
It is absolutely critical that all communications systems, subsystems,
Customer Communications Portals and customer premises devices be
linked to this clock.

a)       
All transactions, communications messages, alarms, control actions,
network management system messages and control actions must be time
stamped

b)       
Different levels of time synchronization with consumer and energy
systems may need to be established depending on the requirements of
the applications.  Categories may include the
definition of operating environments linked to time management
requirements. Possible categories include:

i)         
“X” time range at the remote device (Tight Phasor Measurement
Quality). The exact deviation from the reference clock will be
determined by the requirements of the particular device. For example,
measuring phase differences of a Transmission Line voltage or current
at two different locations for protection purposes will require the
highest level of synchronization with respect to a reference clock.

ii)       
“Y” time range at the remote device (PQ event Measurement Quality).

iii)      
“Z” time range at the remote device (Transaction Management Quality

iv)     
“V” Other

4)       
All transactions, communications messages, alarms, control actions,
network management system messages and control actions must be logged

a)       
Since several diverse Energy Company Management Systems may be used to
manage different aspects of communicating with Customer Communications
Portals (e.g., Energy Conservation/Load Control Systems,
Telecommunications Network Management System, Security Management
System, etc) “log data” from diverse logging systems must be either
merged, or applications developed to intelligently audit and manage
various data sent to or received from the Customer Communications
Portals and/or the various telecommunications networks used to connect
with the Portals.

5)       
The location of all Customer Communications Portals (and for major
customers, critical devices), critical communications system
components and subsystems must be uniquely identified.

a)       
The method used to identify the location of the Customer
Communications Portals, communications systems and devices must be
compatible with or easily mapped to the method used by Energy Company

i)         
Geographical Information Systems.

ii)       
Customer Information Systems

iii)      
Outage Detection and Work Management Systems

iv)     
Transmission (electric and gas) and Distribution (electric and gas)
SCADA Systems

if !supportFootnotes?  
 

---

endif?

[if !supportFootnotes?

[1]endif?](CS_Consumer_Portal_Use_Case.htm#_ftnref1) Service providers
Network Management Systems will not allow users to
directly access and control their various systems
and subsystems, but they will generally enable
large users to access information from their
systems and many cases their subsystems. As
generally the protocols used in these Network
Management Systems (especially the protocols used
to interconnect to subsystems and devices in the
communications network) are proprietary,
substantial effort will be required to adequately
implement Energy Company access to service
provider telecommunications networks in a
consistent manner.

### Security

The key issue for the development of a security
strategy and a set of policies that guide the development of a
security plan is to clearly define the risks inherent in developing a
network as described in this paper. This networking model is one that
provides information and access to control actions involving
significant numbers of Customer Communications Portals and many users
both internal to the Energy Company and to outside entities.

In order to help frame the description of the
security management issues, four major components of security;
Confidentiality, Authentication, Non-repudiation and Data Integrity,
along with some examples of how they are pertinent to the Customer
Portal environment will be reviewed:

Confidentiality deals with the need to keep
information secret, i.e., keeping information from unauthorized users.
In the context of the Customer Communications Portal there will be a
great deal of information that will need to be kept confidential. For
example, a particular customer’s (say, a manufacturer of a certain
type of widget) energy usage would be of great interest to a
competitor as it would be an indication of inventory build up or
increased sales of their product, likewise a reduced level of energy
consumption could indicate problems. There are many other instances of
similar situations. For each of these situations, it is imperative
that no one other than the Energy Company, other authorized users and
the particular customer should have access to energy usage and/or
other information pertaining to that particular Customer. Given that
there are many different Access Network components, data storage
components, and internal Energy Company networks and perhaps several
wirelesses network components, weakness in each or any of these
components might enable someone desiring this information, access to
the information.

Authentication in the context of the Customer
Communications Portal environment is a mechanism that uniquely
identifies who or what entity is trying to access information over the
Customer Communications Portal networks and/or related databases. For
example, is a Customer who accesses Customer Portal information over
the Internet or the Customer Communications Portal Access Network(s)
really the individual or entity that is implied by the transaction
taking place? Or is it an imposter (perhaps an interested competitor)
who is trying to obtain information valuable for his or her own
purposes? There are many similar situations in a network and systems
as complex as the Customer Communications Portal/Access Networks.
Authentication is especially critical in those instances where the
users need to access Customer Portal information over the Internet or
via connections from another data communications network, as each
network has it’s own security domain, policies and thus, providing a
common level of security integration will be a very difficult task. 
For example a Regulator accessing Customer Communications Portal
information initiating a session from an agency network workstation
accessing an Energy Company server via the Internet is bridging
several networks with varying levels of security. Policies, access
control mechanisms and security mechanisms must be in place to enable
authenticated users access to the information that they need. But,
mechanisms must be in place to ensure that imposters cannot obtain
this access.  Authentication is a key component of this capability.

Nonrepudiation is a mechanism that provides the
means for a third party to verify the integrity and origin of data and
the proof of delivery of this data. For example, if an authorized
individual representing an ISO requests a large industrial customer to
provide a certain level of auxiliary power services, and the customer
agrees, the use of nonrepudiation services will provide a record of
the request and response and the fact that the transaction took place.
Neither the ISO representative nor the customer can at a later date
deny that the request and its acceptance was made. In other words, it
can be verified that the ISO representative indeed made the request,
the Customer indeed agreed to provide the services and that the
request, the individuals were in fact the ones being represented in
the transaction and that the requests and response did take place.  In
order to accomplish this, technologies such as public-key
cryptography, digital signatures and digital notary or equivalent must
be employed.

Data Integrity is protected if the Security
Management System if it ensures that data conveyed over a network is
complete and whole and that an unauthorized user or system has not
modified it, added to it, or deleted it during its transmission or
storage. In the context of the Customer Portal environment the
Security Management System Data must ensure that data transmitted over
the Customer Portal Access Network or data that has been stored in any
Computer System or storage device that is part of associated systems
is indeed whole and that it has not been modified or added to in any
way. Maintaining Data Integrity is an essential element in the
operation of the Customer Communications Portal, Access Network and
related computing systems. For example, If there are ISO requests for
local generation to meet system needs, it is critical that any records
of the transaction, along with data relative to the energy flows,
duration, etc. be accurately and transmitted in it’s entirety across
the network and accurately stored in appropriate databases. It will be
essential that the data is complete and whole and that it has not been
modified added to or deleted during its transmission and storage. As
many of these transactions may be taking place in a semi or fully
automated fashion, with little human interaction it is imperative that
security mechanisms such as Data Integrity be in place to ensure
accuracy and reliability of any critical data transmitted over the
Access Data networks and stored in Customer Communications
Portal/related databases.

Auditability in the context of the Customer
Communications Portal environment is a mechanism that provides records
of activities that can attest to the security services. In other words
a security audit tool or set of tools will enable logging of any
attempted security breach from within or outside of the Energy Company
networking environment. The audit trail should include information on
the type of breach such as host break-in, network break-in, multiple
incorrect passwords and user ID attempts, etc.

A Security System Manager through the use of a
Security Management System faces many difficult tasks in order to
provide access to Customer Communications Portal data in a manner that
ensures that only authorized uses have access to the data, and have
the capability to download software or issue commands to Customer
Portals. There are several broad concerns and actions the Security
Manager must undertake, to initially get the system up and running and
then to effectively operate the system on an ongoing basis. The
Security Management System must be configured to implement the
appropriate operating and security policies as determined and agreed
to by the key business entities and as defined in the System Manager
by:

1)      
Defining the risks to the Energy Company, external entities,
Government Agencies and Regulators and other users of Customer Portal
data. Each Energy Company will have different networking and computing
environments, so there will be different levels of risk depending on
each company’s particular environment.  Following is a listing of some
of the risks that are common to many corporate organizations. It is by
no means intended to be a comprehensive listing:

a)      
Data Theft. Any data stored on a computing device or routed or
transmitted through a network (and especially if the data can be
accessed via the Internet) is vulnerable to theft. The key issue to
consider is how valuable is the data and how much effort and cost is
it worth expending to protect this data. In an Energy Company
environment data theft can result in significant financial costs, some
data is protected by Regulatory statues the disclosure of this data
could result in fines or other penalties, competitive advantage could
be lost for it’s customers and there can be exposure to fraud for both
the company and its customers. It is critical that the owner(s) of
this data make an evaluation of how valuable the data is to them
before developing security plans. Security systems used to implement
Authentication and Data Integrity in the Customer Portal systems will
help mitigate Data Theft.

b)      
Data Destruction: It is possible that data can be deleted through some
action of a user. This will require that backup media be scanned to
retrieve the data or in a worst-case scenario, that the data must be
recreated (if possible).  In Energy Company environments data
destruction could lead to serious consequences. The key issue again,
is how valuable is the data and how much effort and cost is it worth
expending to protect this data. Security systems used to implement
Authentication and Data Integrity in the Customer Portal systems will
also help mitigate Data Destruction.

c)      
Loss of Network or System integrity: It is possible that by various
means that hackers have at their disposal (Trojan Horse, etc.) the
integrity of a key host or other device is compromised or disabled.
This can be a very serious problem that can take a significant amount
of time to analyze and repair, the cost of which can be quite
expensive. There is no one tool that can address these threats. Use of
firewalls and other perimeter defense mechanisms, Tools that uncover
and disable viruses, worms, Trojan horse software and other attack
software are critical to minimizing these risks.

d)      
Loss of Network or System accessibility and availability: If key
components of the Network are disabled by intruder action or by
configuration changes, accessibility and availability of the network
and access to the data can be lost for some time. There is no one tool
that can address these threats. Use of firewalls and other perimeter
defense mechanisms, Tools that uncover and disable viruses, worms,
Trojan horse software and other attack software are critical to
minimizing these risks. It is critical that access to any controlling
software residing in any portion of the Customer Portal Access
Networks be restricted to only authorized users. Authentication
mechanisms should be employed to enable access. Computing systems
should to the extent possible utilize access control mechanisms on any
network interface. Auditing tools should be provided on these
computing systems as well as integrity checking tools so that any
unauthorized activity can be quickly identified.

2)      
Assigning and managing Access Classes and authorization levels that
reflect the policies defined by the System Manager, including but not
limited to the following tasks:

a)      
Assigning User Identifications and Passwords and monitor password
usage to ensure that they are changed on a periodic basis by all
users,

b)      
Ensuring that application log-in procedures are followed by all users,

c)      
Ensuring that appropriate encryption mechanisms (Triple DES, AES,
Private Key, etc) are employed on a per entity, per user and
application basis

d)      
Implement a Security Key Management system for those situations that
make it appropriate to utilize Public Key Encryption in order to meet
the security requirements defined by the System Manager.

i)        
Provide mechanisms to recover lost keys. This could take the form of a
Key Escrow System where several parties hold portions of specific
encryption keys. For example if data from a Customer Portal is
especially sensitive and it was encrypted and the Customer Key was
lost, then the parties that held portions of the key can be enlisted
to provide their portions of the key in order to ensure that the
Customer’s data can be recovered. The portions of the key held by
other parties would not be sufficient to individually decrypt the
data, but when combined the key and the encrypted data can be
recovered. Note that this is only an example of what mechanisms might
be employed to cover this type of contingency.

3)      
Implementing firewalls and building perimeter protection systems that
will block unauthorized users from gaining access to networks,
databases and other resources that may impair the operation of the
Customer Portal System and integrity of the data. Note this is a task
that cannot be predefined, in any given Energy Company environment
there may be several computer systems and databases that must be
protected from unauthorized access from both internal and external
entities and individuals. Unfortunately, the more segmentation the
higher the engineering and maintenance costs.

4)      
Implementing Virtual Private Network connectivity for outside entities
and individuals Regulators, Governmental Agencies, etc. outside of the
Energy Company networking environment to enable access to data they
are authorized to obtain. Authentication mechanisms will need to be
used in many cases to enable adequate levels of security protection.
