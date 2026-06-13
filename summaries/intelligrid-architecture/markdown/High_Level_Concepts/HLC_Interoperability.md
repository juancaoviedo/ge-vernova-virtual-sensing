# Interoperability and Integration Issues

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/High_Level_Concepts/HLC_Interoperability.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Interoperability and Integration Issues

**Interoperability
Goals**–The ultimate
goal of interoperability is to enable two independently developed devices to
integrate their operations over a communications network. Interoperability has
been defined as:

“The ability of two or more systems or components to exchange
information and to use the information that has been exchanged”[**[7]**](HLC_Interoperability.htm#_ftn7)

While the concept appears simple on the surface,
the complexity of the systems or components requires a substantial amount of
agreement in the way they interact. Even relatively simple levels of interoperability
require not only adherence to standards and agreement on use of those
standards, but technicians are also necessary to participate in setting up and
configuring equipment. Higher levels of interoperability are a strategic goal
for advanced automation systems and include capabilities to enable the
equipment to participate in the management of the system. The concepts of ‘Plug
and Work’ (or ‘Plug and Play’) require more sophisticated levels of
interoperability. These capabilities enable you to plug in a new device,
application, or system into an existing system, and the existing system
automatically incorporates the new equipment. These levels of interoperability
are strongly desired since it simplifies the human intervention required to manage
systems. However, to achieve systems that are easier for humans to use requires
a higher degree of internal sophistication. Interoperability and
interworkability are terms that must be more tightly defined within the
industry.

The goal of interoperable systems can be very
hard to achieve in a diverse environment with many different requirements, many
different vendors, and a wide variety of standards. Interoperability is
particularly difficult where legacy systems prevent the use of more modern
approaches. No one answer exists on how to integrate these older, less flexible
systems, but the following technologies and best practices can help toward that
interoperability.

§      
Using object and services modeling

§      
Using technology independent techniques

§      
Using ‘Metadata’

§      
Using standards

§      
Using gateways and protocol converters

**Key
Points of Interoperability**–An
additional principlestates that while it is possible to standardize everything,
it is also possible to end up with so many standards that ultimately there are
no standards. Ultimately, there must be a balance between components of a
communications system that are rigidly standardized, and, those that are fairly
flexible to be pioneered by market participants -- vendors, customers, etc.

For example, the singular agreement on a 60Hz,
120 VAC electrical power system, and the physical shape of an AC wall outlet,
made possible a diversity of products that use electricity in the United
States. In the absence of such a well accepted standard, the growth of the
appliance industry would have been hampered by the requirements of various
power conversion adaptors and plug adaptors (as anyone knows who travels to
other countries).

For IntelliGrid Architecture, there will be an analogy between
those key points of interoperability for power (60Hz, 120VAC, plug shape) that
will be key to facilitating an explosion in goods and services that can
interact using components referenced in the architecture. Some key points of
interoperability are summarized below.

§      
**Manufacturing IDs**–Globally
unique identifiers for the source of a component in a utility or other
enterprise system.

§      
**Serial numbers**–Globally
unique identifiers for instances of products.

§      
**Standardized object models**–Standardized
object models with ‘well-known’ names and formats for exchanging data among
disparate applications and systems.

§      
**Metadata representation**–Metadata
is data that describes data. The term ‘Rose’ could be a persons name, a flower,
a color or an acronym. Metadata is the term that describes what the word Rose
refers to in a given application. Metadata is a powerful concept that can be
used for embedded devices to exchange information and achieve higher levels of
interoperability. . This ‘data’ that describes data permits users,
applications, and systems to access or ‘browse’ the names and structures of
object models in other systems as the key method for ‘data discovery’.

§      
**Internet and industry standards**–Using
the Internet and other industry standards to take advantage of the effort used
to develop them, the resulting decrease in prices, and the interoperability
provided by them.

§      
**Time synchronization over a
widespread geographic areas**–The ability to define a common
mechanism to obtain a reliable global time synchronization for devices of any
level of complexity
