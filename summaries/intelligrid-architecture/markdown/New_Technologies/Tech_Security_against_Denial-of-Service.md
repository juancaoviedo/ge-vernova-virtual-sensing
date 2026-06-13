# Denial-of-Service

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Security_against_Denial-of-Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Security against Denial-of-Service

This
service is for assisting in preventing a denial of service. This is not a
service that can be invoked programmatically; rather it is a service that must
be designed into the capabilities of a Security Domain or the implementations
deployed within the domain.

Key
definitions:

**denial
of service: 1.** The prevention of authorized access to resources or the
delaying of time-critical operations. [2382-pt.8] **2.** The result of any
action or series of actions that prevents any part of an information system
(IS) from functioning. [INFOSEC-99]

The
overall issue is to understand what can allow denial-of-service and then to
take steps to mitigate the causes. There are several general categories of
denial-of-service attacks that need to be well understood:

·      
Resource exhaustion: Resource exhaustion is a denial-of-service attack
that causes required resources to be un-available for the intended use when a
valid transaction needs to be processed. The recent SYN FLOOD attacks
represents a well known denial-of-service attack.  
  
Resources that can be exhausted are virtual connections, memory, serial ports,
TCP ports, etc. However these could be generalized into two categories:
connectivity resources and computational resources.

·      
Buffer overflow: This type of attack causes a memory overrun to occur
within a computational resource. The end result is typically the computational
process terminates or becomes unstable. In reality, this attack exploits poorly
implemented programs that actually allow for the overrun to occur without being
properly trapped. Recent examples of this type of attack are the PING OF DEATH
and some attacks on SNMP.

·      
Protocol oversights: In some protocols, not all state transitions may be
defined. Exploitation of such oversights could allow a denial of service attack
to cause a protocol deadlock situation.  
  
As an example, from STD 62 (SNMP):

“Denial
of Service

A
Security Model need not attempt to address the broad range of attacks by which
service on behalf of authorized users is denied. Indeed, such denial-of-service
attacks are in many cases indistinguishable from the type of network failures
with which any viable management protocol must cope as a matter of course.”

Basically
is a statement that no DOS countermeasures need to be taken within the
specification. This is typical of most standards.

·      
Improper Coding Practice: Both the Buffer Overflow and Protocol
Oversight threats are sub-categories of the improper coding practice category.
However, this category includes improper use of semaphores, threads, etc. that
could be utilized to decrease performance/resource available to the point that
a valid transaction could not be processed in a timely manner.

Technological Assessment and
Relevant Specifications

In
order to provide a denial-of-service attack protection, inter-domain connection
points need to be well designed and monitored.

For
connectivity resources, it is recommended that timeouts be implemented that are
based upon valid traffic being transmitted/received through the connection
point. Additionally, it is recommended that through policy or coding practice
that a peer remote is limited to the number of connectivity resources that it
is allowed to consume.

For
protocol oversights, it is recommended that prior to implementation the
protocol(s) are analyzed for vulnerabilities and that these be addressed during
the implementation phase. It is recommended that appropriate coding methodology
be employed to prevent CPU resource exhaustion as well as protocol oversight
vulnerabilities.

It
is also recommended that as part of the policy/SMI of a security domain that
implementations are tested for vulnerabilities with tools that are publicly
available.

Table 30: Relevant Specifications regarding
Denial-of-Service

| Identification Number | Name | Comment |
| --- | --- | --- |
| ISO/IEC 17799:2000 | Information technology -- Code of practice for information security management |  |
| ISO/IEC TR 13335-1:1996 | Information technology -- Guidelines for the management of IT Security -- Part 1: Concepts and models for IT Security |  |
| ISO/IEC TR 13335-2:1997 | Information technology -- Guidelines for the management of IT Security -- Part 2: Managing and planning IT Security |  |
