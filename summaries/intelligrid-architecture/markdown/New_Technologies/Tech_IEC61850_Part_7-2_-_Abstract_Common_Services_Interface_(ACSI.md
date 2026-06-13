# IEC61850 Part 7-2 - Abstract Common Services Interface (ACSI)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_IEC61850_Part_7-2_-_Abstract_Common_Services_Interface_(ACSI.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### IEC61850 Part 7-2 - Abstract Common Services Interface (ACSI)

**URL:**http://www.iec.ch/cgi-bin/procgi.pl/www/iecwww.p?wwwlang=E&wwwprog=dirwg.p&ctnum=1188

Communication Services are the ***Verbs.***
They provide the actions, such as sending and receiving data, reporting data
when some event occurs, logging data, and other “actions”. In SA, there are two
types of communication services: Abstract Communication Services, which must be
mapped to a particular protocol (such as MMS or OPS); and PICOM, which is a unique
set of services for protection relaying.

IEC61850-7-2 defines a set of abstract communication
services that addresses the basic requirements for the process of exchanging
information. These services include:

·      
Association services, where a logical connection is made between two
entities, such as a substation master with a new IED. In addition, multi-cast
associations are also handled. This group of services handles establishing
connections, deliberate breaking connections, aborting connections (usually due
to some error condition), and managing unexpected broken connections.

·      
Get, which requests information to be sent, including Get Logical Device
Directory, Get Logical Node Directory, Get Data Values, Get Data Values
Directory, and others. This service is used to monitor information.

·      
Set, which sends information to be used or stored, including Set Data
Values. This service is used for control commands, setting parameters, and
writing descriptions

·      
Data Sets, where data values are grouped into sets for efficient
transmittal. Data Sets can be manually created as well as automatically created
and deleted.

·      
Report Control, which manages the reporting of Data Sets upon request,
at a particular periodicity (e.g. integrity scan), and upon the occurrence of
pre-specified events, such as data change (e.g. closed to tripped status),
quality change (e.g. a problem causes data to be invalid), data update (e.g. an
accumulator value is “frozen” periodically), or integrity scan mismatch (e.g.
the integrity scan indicates a different status value from the value that was
last reported).

·      
Log Control, which manages logging and journaling of information, such
as sequence of events

·      
Substitution Values, which manages the substitution of values if these
are indicated in the Data Object classes

·      
GSE Messages, which handle special ultra-high-speed messaging to
multiple destinations, typically for protective relaying.

·      
Select-Before-Operate Control, which implements the safety mechanisms
used by most switch-related control commands. This procedure basically consists
of: an originator of the control command first issuing a select of the control
point, the receiver then performing a select and reporting the results
back to the originator, the originator then issuing an execute command which
the receiver performs only if it receives the execute command within a
pre-specified time from the originator.

·      
Time Management, which handles the synchronization of time across all
interconnected nodes.

·      
File Transfer, which handles the transfer of files between entities,
without treating them as data objects. This capability supports the uploading of
new applications into the IEDs and other servers.

Of these services, most are taken care of
automatically by the basic communications software. The key services that are
important for the substation engineer to become involved with are the Data
Sets. Basic Data Sets are pre-defined: each Logical Node has an associated Data
Set of all its data. However, these may not be appropriate for all users,
therefore, the substation engineer should help define the data groupings, based
on substation requirements as well as other user and software application
requirements.

Although clearly initial Data Sets must be defined,
they can be changed at any time. Therefore, one of the requirements from the
vendors must be an HMI (human-machine interface) tool that permits the easy
definition and modification of these Data Sets.

Piece of Information for COMmunications (PICOM) is a
term defined by CIGRE WG34.04 to describe the information passed between
Logical Nodes. The components of a PICOM are:

·      
Data, meaning the actual data items sent from one LN to another LN

·      
Type of data, meaning its format

·      
Performance of the information exchange

The PICOMs are used primarily to define what data
needs to be exchanged between protective relaying IEDs. The detailed exchange
parameters of PICOMs should be part of a protective relaying vendor’s package;
however, the substation engineer will need to specify very precisely what
protection events should trigger what actions.

The abstract objects and communication services have
to be “mapped” to real-world bits and bytes, in other words, to actual
communication protocols.

IEC61850 currently has two protocol mapping
specified, namely, the GSE protocol for transmissions between very high speed
devices (such as protection relays) and MMS over the TCP/IP suite of protocols.
However, the OM-DA object models can also be transmitted using some other
mappings to protocol profiles, although some protocols can manage objects
better than others. For instance, MMS and XML (over any lower layer network
protocols) can utilize the object models completely. However, XML does not
specify the communication services (when to send, triggered by what, etc.). So
an underlying service capability must be added, most of which do not handle
some of the more powerful services like data sets.

The initial protocol profiles for IEC 61850 are
nearly identical to those developed for IEC 60870-6 (TASE.2) between
substations, using the Manufacturing Message Specification (MMS) and both
Internet and OSI protocol stacks. These are mainly full 7-layer profiles, but
there are also high-speed profiles used directly over Ethernet (IEEE 802.x)
LANs for “process bus” and protection tripping.

**Keywords:** Protocol, ACSI, Abstract Common Services Interface, CASM, Common
Services, interoperability, Specific Communication Service Mappings, SCSM
