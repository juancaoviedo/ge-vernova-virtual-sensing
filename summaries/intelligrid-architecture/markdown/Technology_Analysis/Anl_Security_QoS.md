# Security Service vs. IECSA Quality of Service

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Security_QoS.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

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
| QOS-3 | Provide high speed messaging of less than 1 second        Provide medium speed messaging on the order of 10 seconds |
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
a system,
subsystem, or equipment is operable and in a committable state at the start of
a mission, when the mission is called for at an unknown, i.e., a random, time.
Note 1: The conditions determining operability and commitability
must be specified. Note 2: Expressed mathematically, availability is 1 minus the
unavailability. **2.**
The ratio of (a) the total time a functional unit is capable of being used during a given
interval to (b) the length of the interval. Note 1: An example of availability
is 100/168 if the unit is capable of being used for 100 hours in a week. Note
2: Typical availability objectives are specified in decimal fractions, such as
0.9998. **3.** Timely, reliable access to data and information services for authorized users.” [From ANSI
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
definitions, any security service that increases CPU utilization,
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

![](IECSA_VolumeIV_AppendixA_files/image022.png)

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
upon the Environment’s definition[[15]](Anl_Security_QoS.htm#_ftn15)

![](IECSA_VolumeIV_AppendixA_files/image025.gif)“This environment encompasses communications
between end customers and the utility, aggregator, or Energy Service Provider
(ESP) to which they are connected.  This environment includes the
requirements for what is traditionally known as Automatic Meter Reading (AMR).

Typical
applications: Customer metering, management of distributed energy resources
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

![](IECSA_VolumeIV_AppendixA_files/image027.gif)

Upon initial inspection, a simplistic
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

 

![](IECSA_VolumeIV_AppendixA_files/image029.gif)![](IECSA_VolumeIV_AppendixA_files/image031.gif)

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
| Communication | ESP to Gateway  (Inter-domain) | Gateway to Customer Premises Security Domains  (Inter-domain) | Customer Premises Network  (Intra-Domain) |
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

Step
1: Establish Identity Establishment Policies

It is
recommended, in previous section of this appendix, that each security domain establish
its own identity establishment policies and procedures.  The basic issue
to be resolved is whose credentials are acceptable for identity
establishment.  There are two options for inter-domain exchanges:

The
target security domain (e.g. the one to which the
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

![](IECSA_VolumeIV_AppendixA_files/image033.gif)

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

![](IECSA_VolumeIV_AppendixA_files/image035.gif)

Figure
10: Alternate Architecture that could allow direct 61850 communications

In
general, implementation of security requires that the policy
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
location of the agents could be co-located
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
the load management agent is located within the building/campus security
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
