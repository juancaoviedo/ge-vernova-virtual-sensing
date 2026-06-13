# Key Requirements

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Requirements/Req_Requirements.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Key Requirements Used to Define IntelliGrid Architecture Environments

Key distributed computing infrastructure
requirements were extracted from the power system functions and used to
categorize IntelliGrid Architecture Environments. These requirements, which eventually were
termed the ‘aggregated requirements,’ comprise the following:

**1.****Communication
Configuration Requirements**

§      
Provide point-to-point interactions between two entities

§      
Support interactions between a few ‘clients’ and many ‘servers’

§      
Support interactions between a few ‘servers’ and many ‘clients’

§      
Support peer to peer interactions

§      
Support interactions within a contained environment (e.g. substation or
control center)

§      
Support interactions across widely distributed sites

§      
Support multi-cast or broadcast capabilities

§      
Support the frequent change of configuration and/or location of end
devices or sites

§      
Support mandatory mobile communications

§      
Support compute-constrained and/or media constrained communications

**2.****Quality of Service
Requirements**

§      
Provide ultra high speed messaging (short latency) of less than 4
milliseconds

§      
Provide very high speed messaging of less than 10 milliseconds

§      
Provide high speed messaging of less than 1 second

§      
Provide medium speed messaging on the order of 10 seconds

§      
Support contractual timeliness (data must be available at a specific
time or within a specific window of time)

§      
Support ultra high availability of information flows of 99.9999+ (~1/2
second)

§      
Support extremely high availability of information flows of 99.999+ (~5
minutes)

§      
Support very high availability of information flows of 99.99+ (~1 hour)

§      
Support high availability of information flows of 99.9+ (~9 hours)

§      
Support medium availability of information flows of 99.0+ (~3.5 days)

§      
Support high precision of data (< 0.5 variance)

§      
Support time synchronization of data for age and time-skew information

§      
Support high frequency of data exchanges

**3.****Security Requirements**

§      
Provide Identity Establishment (you are who you say you are)

§      
Provide Authorization for Access Control (resolving a policy-based
access control decision to ensure authorized entities have appropriate access
rights and authorized access is not denied)

§      
Provide Information Integrity (data has not been subject to unauthorized
changes or these unauthorized changes are detected)

§      
Provide Confidentiality (only authorized access to information,
protection against eavesdropping)

§      
Provide Security Against Denial-of-Service (unimpeded access to data to
avoid denial of service)

§      
Provide Inter-Domain Security (support security requirements across
organizational boundaries)

§      
Provide Non-repudiation (cannot deny that interaction took place)

§      
Provide Security Assurance (determine the level of security provided by
another environment)

§      
Provide for Audit (responsible for producing records, which track
security relevant events)

§      
Provide Identity Mapping (capability of transforming an identity which
exists in one identity domain into an identity within another identity domain)

§      
Provide Credential Conversion (provides credential conversion between
one type of credential to another type or form of credential)

§      
Provide Credential Renewal (notify users prior to expiration of their
credentials)

§      
Provide a Security Policy (concerned with the management of security
policies)

§      
Provide for Policy Exchange (allow service requestors and providers to
exchange dynamically security (among other) policy information to establish a
negotiated security context between them)

§      
Provide Single Sign-On (relieve an entity having successfully completed
the act of authentication once from the need to participate in
re-authentications upon subsequent accesses to managed resources for some
reasonable period of time)

§      
Provide Trust Establishment Security (security verification across multiple
organizations)

§      
Provide Path and Routing Quality of Security (being able to determine a
secure communication path)

§      
Provide Firewall Transversal

§      
Provide Privacy Service (the ability to ensure person information is not
disclosed)

§      
Provide User Profile and User Management (combination of several other
security services)

§      
Provide Security Protocol mapping (the ability to convert from one
protocol to another)

§      
Provide Quality of Identity (the ability to determine the merit of
converted credentials)

§      
Provide Security Discovery (the ability to determine what security
services are available for use)

§      
Provide Delegation (delegation of access rights from requestors to
services, as well as to allow for delegation policies to be specified)

**4.****Data
Management Requirements**

§      
Provide Network Management (management of media, transport, and
communication nodes)

§      
Provide System Management (management of end devices and applications)

§      
Support the management of large volumes of data flows

§      
Support keeping the data up-to-date

§      
Support extensive data validation procedures

§      
Support keeping data consistent and synchronized across systems and/or
databases

§      
Support timely access to data by multiple different users

§      
Support frequent changes in types of data exchanged

§      
Support management of data whose types can vary significantly in
different implementations

§      
Support specific standardized or de facto object models of data

§      
Support the exchange of unstructured or special-format data (e.g. text,
documents, and oscillographic data)

§      
Support transaction integrity (consistency and rollback capability)

§      
Provide for service discovery (discovering available services and their
characteristics)

§      
Provide for spontaneously finding and joining a community

§      
Provide protocol conversion and mapping

§      
Support the management of data across organizational boundaries
