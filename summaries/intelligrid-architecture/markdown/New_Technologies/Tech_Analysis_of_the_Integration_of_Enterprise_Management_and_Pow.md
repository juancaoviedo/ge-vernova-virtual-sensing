# Analysis of the Integration of Enterprise Management and Power Systems

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Analysis_of_the_Integration_of_Enterprise_Management_and_Pow.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Analysis of the Integration of Enterprise Management and Power Systems

Specific
to power systems operations, the team developed the list of abstract enterprise
management services needed to support these operations. This list was
originally derived from the generic enterprise management functions described
under Enterprise Management Services and subsequently focused to meet IntelliGrid Architecture’s requirements addressed in the Use Cases Architectural Issues (see Vol.
2, Appendix E) for the various domain functions and abstract use cases. These
requirements do not explicitly raise the need for enterprise management.
However, the need can be derived. Examples of these requirements and the
derived enterprise management services are listed below:

·       For the Field
Device Integration, the requirements of SCADA communicating with thousands of
devices imply the need to perform configuration and fault management of
numerous local and remote devices.

·       In Field Device
Integration, the requirements for *any* communications media: wireline,
wireless; raises the need for the enterprise management system to be able to
manage multi-protocol, multi-technology systems and networks.

·       In Field Device
Integration, the requirements of the fault to be communicated to sub-station
computer within one second, raises the need for tight performance management
and appropriate configuration management.

·       In Field Device
Integration, the requirements for the communications of IED and the sub-station
master to be 99.999% reliable, implies tight performance and alarm monitoring,
substantial effort in survivable network design and traffic engineering, and
fast fault detection and recovery services.

·       In Integrated
Security Across Domains, the requirements that the communication media can have
any forms of ownership: utility-owned, jointly owned, commercially provided,
Internet; implies the need for policy management, establishing and enforcing
SLAs, and fairly tight security management.

·       In Integrated
Security and Energy Markets, the requirements for the communications to take
place between various organizations and different administrative domains imply
the need for extensive policy management and enforcements of inter-domain
management policies.

·       The various
functional aspects of the domain tasks implied similarities with generic
enterprise management functions and the need for integration of these services
for ease of operations and cost reductions.

From
an abstract modeling perspective, it is worth considering the OSI architecture
model of enterprise management that can be described from the four views of:
(i) organizational model, (ii) Information model, (iii) communication model,
and (iv) functional model. In RM-ODP terms: The OSI Organization Model can be
seen as a RM-ODP Engineering Model; The OSI Information Model can be seen as a
RM-ODP Information View The OSI communication Model can be seen as a RM-ODP
Computational View; And the OSI Functional Model can be seen as a RM-ODP Enterprise
Model

The
*organization model* includes the various components of the enterprise
management system, namely *managed object, agent, manager*, *user
interface* and the *management database*. The managed objects include
the network elements, devices, applications, processors, memories, storage
devices, etc. The agent runs on the managed object and provides data on the
managed object to the manager. The manager manages the managed objects. The
database contains information on the managed objects. The organization model is
fairly common within various enterprise management technologies.

Complementary
to this organizational model, are a Functional Model consisting of Common
Services, an Information model, and a Communication Model consisting of Generic
Interfaces/Protocols. With regard to where components are deployed, both the
OSI Enterprise Management Organization Model and IntelliGrid Architecture Deployment model are
flexible enough to allow implementers to deploy managers, agents, and gateways
as needed. The important point is that both the OSI Enterprise Management Model
and IntelliGrid Architecture treat their models orthogonally.

Although
there are differences between the various models for enterprise management and
power system management, the similarities in the functional aspects of the
management tasks and the need for coordination of these tasks implies the need
for integration of the services for ease of operations and cost reductions.
