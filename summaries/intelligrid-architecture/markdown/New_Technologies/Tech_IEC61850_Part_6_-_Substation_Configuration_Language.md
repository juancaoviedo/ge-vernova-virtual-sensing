# IEC61850 Part 6 - Substation Configuration Language

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_IEC61850_Part_6_-_Substation_Configuration_Language.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### IEC61850 Part 6 - Substation Configuration Language

Abstract configuration languages provide a mechanism
for describing how real-world components are actually connected to each other.
Two such configuration languages have been defined to date in the utility
industry:

·      
Substation Configuration Language SCL for the configuration of equipment
within substations

·      
Common Information Model (CIM) for the overall configuration of the
power system, from corporate ownership through the lines, substations, and
feeders, down to the customer sites.

The concept of a ***configuration language***
is that the configuration of the substation can be modeled electronically using
object models, not just the data in the substation. This model of the
substation configuration allows applications to “learn” how all the devices
within a substation are actually interconnected both electrically and from an
information point of view.

The Substation Configuration Language (SCL), IEC61850
Part 6, defines the interrelationship of the substation equipment to each other
and to the substation itself. Although the substation object models define each
of the devices in the substation, these device models do not define how the
models are interrelated. Therefore Part 6 was developed to provide a tool for
defining the substation configuration.

The SCL uses a standard file format for exchanging
information between proprietary configuration tools for substation devices.
This standard is based on Extensible Markup Language (XML), and draws on the
data modeling concepts found in the other parts of IEC 61850, and the
capability of the IEC 61850 protocols to “self-describe” the data to be
reported by a particular device.

An effort is underway to "harmonize" this
configuration language with the similar object models of the Common Information
Model (CIM). The work to do this is also still under development through the
IEC.  However, when it is completed, it may become very important in
future more sophisticated functions that would benefit from having substation configuration
information available and updated electronically.

Even if this configuration language is not
immediately used within a utility’s operations, it should be required from the
appropriate substation automation vendor, probably the vendor of the substation
master.

**Keywords:** Protocol, Substation Configuration Language, SCL, XML, IED
configuration, schema, substation automation system, communication system
configuration data
