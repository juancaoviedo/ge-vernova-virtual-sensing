# Management of Data Acquisition

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Management_of_Data_Acquisition.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Management of Data Acquisition

Data
acquisition has many pitfalls as well for data management. Some of these
pitfalls can be ameliorated by new information technologies, while others
require old-fashioned carefulness. The main problem is the sheer volume of data
now required. Some IED controllers contain hundreds (even thousands) of points.
Although many are not needed by SCADA operations, they are useful for engineers
and maintenance personnel. Given this magnitude of data items, data management
must be viewed as a significant aspect in the design of new and upgraded
systems. In particular:

·       Object-oriented
protocols (e.g. UCA (IEC61850) for field equipment, CIM for power system data,
and XML for general data) should be required. These protocols require that the
IEDs that control the field devices are organized with well-known point names
which are self-describing and can be “browsed” for information much like Web
pages. This self-description allows applications to link automatically to the
correct data with minimal human intervention (thus avoiding one of the main
causes of error).

·       Data objects
required by SNMP MIBs should be retrieved from field equipment, regardless
whether object-oriented or point-oriented protocols are used.

**Keywords:**keywords
