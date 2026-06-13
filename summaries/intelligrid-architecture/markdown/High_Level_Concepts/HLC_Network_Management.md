# System and Network Management Services

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/High_Level_Concepts/HLC_Network_Management.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# System and Network Management Services

As can be seen in Figure 11 and Figure 12, two
infrastructures must now be managed: the Power System Infrastructure and the
Information Infrastructure. The management of the power system infrastructure
is increasingly reliant on the information infrastructure as automation
continues to replace manual operations, and is therefore affected by any
problems that the information infrastructure might suffer.

[![](../images/Two_Infrastructures_Must_Be_Managed_small.jpg)](../images/Two_Infrastructures_Must_Be_Managed.jpg)

**Figure 11: Two Infrastructures must be managed**

Each of the
two infrastructures has its own paradigms used for management.

[![](../images/Power_Infrastructure_Relies_On_Information_small.jpg)](../images/Power_Infrastructure_Relies_On_Information.jpg)

**Figure
12: Power
Infrastructure Relies on Information Infrastructure**

 Integrated
Infrastructure Management: 
Both
the Power System Infrastructure and the Information Infrastructure must be
managed as an integrated whole.

**Typical
Simplistic Network Management by SCADA Systems**–Electric power systems have been monitored
and controlled by SCADA systems for many years. On the other hand, the
information systems in the electric power industry have not been treated as a
coherent infrastructure, but instead have been viewed as a collection of
individual communication channels, separate databases, multiple systems, and
different protocols.

Typically SCADA systems, in varying degrees,
monitor whether communications are available with their (Remote Terminal Units
(RTUs) and flag data as ‘unavailable’ if communications are lost. However, it
is then up to maintenance personnel to track down the problem, which is a
lengthy and ad hoc process. Every utility is different in the information
available to its maintenance staff. Telecommunication technicians are generally
responsible for tracking down any microwave or fiber cable problems;
telecommunication service providers must track their networks; database
administrators must determine if data is being retrieved correctly from
substation automation systems or from GIS
databases; protocol engineers must correct protocol errors; application
engineers must determine if applications have crashed, have not converged, or
are in an endless loop; and operators must filter through large amounts of data
to determine if a possible ‘power system problem’ is really an ‘information
system problem’.

**System
and Network Management Vision**–Network
and systems management are those functions required to manage the communication
networks and the connected communications equipment. Systems management
includes managing remote equipment. These are functions a system administrator
uses in managing the distributed computing infrastructure and connected
equipment. The development of these functions is taking place both within and
outside of the energy community.

In the future, the problem of network and
systems management will become increasingly complex as a variety of systems are
anticipated as well as greater demands on the capabilities of these systems to
assist system administrators. Traditional SCADA systems will no longer have
exclusive control over the communications to the field, which may be provided
by telecommunication providers, or by the corporate networks, or by other
utilities. Intelligent Electronic Devices (IEDs) will have applications executing
within them whose proper functioning is critical to power system reliability.
Field devices will be communicating with other field devices, using channels
not monitored by any SCADA system. Information networks in substations will
rely on local ‘self-healing’ procedures that will also not be explicitly
monitored or controlled by today’s SCADA systems.

The technology industry has developed two
network management technologies: Simple Network Management Protocol (SNMP) for
the Internet-based functions, and Common Management Information Protocol (CMIP)
as an ISO standard. In each of these technologies, Management Information Base
(MIB) objects must be specified representing the state of different equipment,
applications, and systems. Although many MIB objects are generic enough to be
used by electric power systems, some specialized MIB objects will need to be
developed to represent some of the very specialized equipment used in power
system operations.

**Object
Models for Network and System Management**–Systems and network management functions are also
supported by the application of object based communications. The IEC is
currently working to develop network management objects for power system
operations. In addition, the networking and telecommunications industries are
working toward more sophisticated system administration infrastructures.
Examples of possible types of network and systems management functions and
objects for energy industry related IEDs are shown in Table 4 below.

|  |  |
| --- | --- |
| Table 4: Possible types of networks and systems management functions. | |
| Possible types of network and system functions: | Possible responses or actions could include: |
| §    Numbers and times of all stops and starts of systems, controllers, and applications  §    Status of each application and/or software module: stopped, suspended, running, not responding, inadequate or inconsistent input, errors in outputs, error state, etc.  §    Status of all network connections to an IED, including numbers and times of temporary and permanent failures  §    Status of any ‘keep-alive’ heartbeats, including any missed heartbeats  §    Status of backup or failover mechanisms, such as numbers and times these mechanisms were unavailable  §    Status of data reporting: normal, not able to keep up with requests, missing data, etc.  §    Status of access: numbers, times, and types of unauthorized attempts to access data or issue controls  §    Anomalies in data access (e.g. individual request when normally reported periodically) | §      Start or stop reporting  §      Restart IED  §      Kill and/or restart application  §      Re-establish connection to another IED  §      Shut down another IED  §      Provide event log of information events  §      Change password  §      Change backup or failover options |
