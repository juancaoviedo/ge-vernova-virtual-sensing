# Data Storage and Access Management

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Data_Storage_and_Access_Management.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Data Storage and Access Management

Data
storage and access management is another critical area in the design of
systems. Often systems have been developed for one purpose, then added-to for
another purpose. Later, other applications need data, so an additional jury-rig
is added. Some key recommendations for avoiding this problem (or migrating away
from it) include:

·       The real-time
database in the SCADA system, which is focused on providing timely but limited
amounts of data to operators, should not be used as a source of data for other
systems. Rather the front-end data acquisition and control (DAC) system should
be structured to supply the required real-time data to SCADA system, but also
provide other kinds of data to other applications without impacting the SCADA
system itself.

·       The DAC should
support access to field equipment by planners, protection engineers, and
technicians

·       Object-oriented
protocols should be used for all data exchanges between systems. With data
having well-defined names, managing the access to the data is easier and more
likely to be correct. These object-oriented protocols include the UCA
(IEC61850), the CIM, and XML information exchange models (see next section).

·       Currently some
of these object-oriented protocols are not completely interoperable or
consistent in their structure. In particular, the data names and structures of
IEC61850 and the CIM need to be harmonized. This activity is taking place in
the IEC.

·       Standard formats
and methodologies for Application Program Interfaces (APIs) for data access
also need to be formalized. Currently the CIM specifies the Generic Interface
Definition (GID). The GID identifies explicitly which features of existing APIs
(such as DAF and DAIS) will be implemented to exchange data implemented in
CIM-based databases, to extend these capabilities to include features needed in
utility operations, and to specify the exact formats to use when implemented
over different types of middleware (e.g. CORBA or Microsoft COM).

·       Electronic
registers should be developed which contain the metadata models of the
object-oriented data. This is discussed in more detail in the section on
Information Exchange Management.

·       As major assets
are purchased, their characteristics should be entered into an electronic asset
database (e.g. AM/FM system), possibly using bar codes (to avoid the fallible
human data entry process). They should then be tracked throughout their life as
they move from the warehouse to one or more field locations over time. This
method could provide the accuracy so often missing but badly needed in the
asset databases.

**Keywords:**keywords
