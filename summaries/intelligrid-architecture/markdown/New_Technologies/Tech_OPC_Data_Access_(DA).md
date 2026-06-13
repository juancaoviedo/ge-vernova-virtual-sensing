# OPC Data Access (DA)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_OPC_Data_Access_(DA).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### OPC Data Access (DA)

**URL:**www.opcfoundation.org

OPC is a foundation dedicated to
open connectivity in industrial automation and the enterprise systems that
support industry. To this aim, OPC has created a series of open standards
specifications with the goal of assuring interoperability. Based on fundamental
standards and technology of the general computing market, the OPC Foundation
adapts and creates specifications that fill industry-specific needs. OPC will
continue to create new standards as needs arise and to adapt existing standards
to utilize new technology. There are currently seven standards specifications
completed or in development.

At a high level, an OPC Data
Access Server is comprised of several objects: the server, the group, and the
item. The OPC server object maintains information about the server and serves
as a container for OPC group objects. The OPC group object maintains
information about itself and provides the mechanism for containing and
logically organizing OPC items. The OPC Groups provide a way for clients to
organize data. For example, the group might represent items in a particular
operator display or report. Data can be read and written. Exception based
connections can also be created between the client and the items in the group
and can be enabled and disabled as needed. An OPC client can configure the rate
that an OPC server should provide the data changes to the OPC client. IEC TC57
WG13’s Part 403 High Speed Data Access is based on OPC DA.

**Keywords:** Computational VP, Widespread usage
