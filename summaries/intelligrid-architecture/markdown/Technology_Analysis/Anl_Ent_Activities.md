# Enterprise Activities and Domain Use Cases

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Ent_Activities.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Enterprise Activities and Domain Use Cases

IntelliGrid Architecture is designed
to provide an architecture to be used across all of the utility.  The first task that IntelliGrid Architecture Team undertook
was the creation of a comprehensive list of over 400 Enterprise
Activities.  Simultaneously with the
development of this list, some common themes quickly became apparent as the
project team analyzed the requirements. 
It was clear that the architecture would need to provide common
strategies in the following areas that underlay nearly all of the requirements
that were gathered:

if !supportLists?·      
endif?**Network and System (Enterprise) Management**.For an area that is relatively mature in
commercial networks, the science of monitoring and controlling the
communications network itself is surprisingly unknown or at the very least,
primitive, in power system automation. 
The key here will be to harmonize network monitoring technologies and
network object models with the functional equivalents in the power industry,
and to integrate both with security management.

if !supportLists?·      
endif?**Data Management and exchange**.  The sheer volume and variety of data required
in order to operate a power system within the Digital Society poses staggering
challenges in standardizing interfaces for reading, writing, publishing, and
subscribing to data.  In this area, the
key solution will be to identify specific commonality and diversity of how data
is managed and exchanged.

if !supportLists?·      
endif?**Basic networking and connectivity**
infrastructure.  How are the myriads of
device and communications technologies to connect?  In general, IP-based networks were the
obvious solution, but utility requirements posed unique requirements of
reliability, wireless access, changing configurations, and quality of service.

if !supportLists?·      
endif?**Security** and access control.  Deregulation and other effects of the Digital
Society are forcing utilities to rely on public networks provided by third
parties, communicate with their competitors, cross organizational boundaries,
and expand their communications networks inward to their own organizations and
outward to the customer.  All of these
forces make the need for cyber-security ubiquitous in power system operations.  Encryption and authentication technologies
abound, but the chosen strategy is to tailor security solutions to particular
problem domains, and link them together with shared security management
services.

The Team used the
list of requirements to select a set of functions from the list of Enterprise
Activities on the basis of their architectural significance  -- that is the architectural sophistication
necessary to achieve their implementation. 
Called Domain Use Cases, this small set of functions more intensively
analyzed consist of:

if !supportLists?·      
endif?**Wide Area Measurement and Control** – in
particular, the requirements for developing a self-healing, self-optimizing
grid that could predict emergencies rather than just react to them, and
automate many reliability functions currently done manually or not at all.

if !supportLists?·      
endif?**Advanced Distribution Automation** –the
challenges raised by the use of Distributed Energy Resources, renewable energy
sources, and the use of fault detection, fault location, sectionalization and
automatic service restoration over wide areas of the service territory and
multiple organizational boundaries.

if !supportLists?·       
endif?**Customer
Interface** – including the challenges of real-time pricing, demand response,
automatic metering, integration of the utility communications network with
building automation, and the requirements needed to integrate real-time data
gathered from the power network with business policies in order to securely
enable trading of energy in a deregulated environment.

 

This process
illustrated in Figure 2:

if !vml?![](Anl_Ent_Activities_files/image002.gif)endif?

Figure
2 Domain Use Cases From List of Business Functions
