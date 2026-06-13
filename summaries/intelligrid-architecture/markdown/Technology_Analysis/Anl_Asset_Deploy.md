# Asset Management

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Asset_Deploy.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Asset Management Deployment Scenario

 

As recovery of money spent on asset related operations is
not guaranteed, it is critical that asset related costs be managed wisely.  Inevitably this leads to a need for analytic
applications including:

if !supportLists?·      
endif?Asset Risk Management – what is the risk
associated with operating an asset

if !supportLists?·      
endif?Calculation and optimization of asset lifecycle
costs

if !supportLists?·      
endif?Calculation of asset availability – what is the
projected reliability of an asset

if !supportLists?·      
endif?Asset replacement calculations – when to replace
a given asset

if !supportLists?·      
endif?Asset maintenance and diagnosis – when to
optimally schedule asset maintenance

if !supportLists?·      
endif?Asset performance – what is the value of an
asset

if !supportLists?·      
endif?Capital plan management –future asset related
investment forecasting

if !supportLists?·      
endif?Asset utilization analysis – how can assets be
more fully used

if !supportLists?·      
endif?Financial analysis – how markets affect asset
valuation[if !supportFootnotes?[21]endif?](Anl_Asset_Deploy.htm#_ftn21) 

This section describes how a deployment of the CIM and GID
can be used to create a platform for data warehousing. In this case, we
consider a complementary project to the application integration project with
apparently different goals. The project consists of substation asset data
analysis and integrates the following data:

if !supportLists?o      
endif?Asset/Equipment data

if !supportLists?o      
endif?Historical measurements

if !supportLists?o      
endif?Power system network models

Frequently, this type of data is in a database.  With regard to what data is exchanged, one
can suggest that the value to the utility of how a database natively models is
low. Again, analysis applications may only need to browse the lineage of data
(where it came from) for auditing/validation but not detail about native
semantics.  Consequently, data
integration provides a scenario where the semantics of each database may be
assimilated into the common model. 

With regard to how data is exchanged, generally IntelliGrid Architecture
based data integration seeks to abstract data access technology from the
underlying storage technology. 
Specifically, instead of using a cross industry data access API
such as ODBC to collect data, IntelliGrid Architecture based data integration employs a CIM
enabled such as IEC61970 Generic Data Access interfaces which is independent of
backend schemas and storage technology. 
Note that both cross industry and common model enabled data access API’s
are generic in that they can be applied to any data type and do not hard code
applications specific semantics into the API.  This architecture is illustrated in Figure 18.

if !vml?![](Anl_Asset_Deploy_files/image002.gif)endif?

Figure ‑18 CIM/GID
Based Data Warehouse With Message Bus

 

As described previously, it is important to note that GDA
includes the ability to notify clients when data has been updated in the
server. This functionality provides an important piece of the puzzle when
constructing an infrastructure that enables a single point of update for model
changes. For example, changes in an EMS
modeling server can be used to drive the configuration of an archive or
implement a synchronization routine with an asset management system.

The capability for the warehouse to be kept in sync via
GDA Model Change Events addresses a key interoperability issue.  There is no widely used cross vendor/open
standard interface for the propagation of data changes into data warehouses.
Furthermore, reuse of these events to keep applications in sync for the
application integration can provide a significant savings when integrating the
utility.

By sharing a common CIM/GID
design framework, a message based application integration and data warehouse
solution can be built simultaneously. Fortunately this approach reuses shared
application wrappers to leverage the investment in each without requiring all
data to be copied to a data warehouse. 
Separately, the cost of developing individual wrappers for data
warehousing and for application integration can be prohibitive.  By exposing application wrappers directly via
CIM/GID without requiring an intervening
copy of all the data in a warehouse, flexibility is maximized while costs are
minimized. 

Not necessarily copying all the data into a data warehouse
while still providing analysis application the appearance that all the data is
local is called “Virtual Data Warehousing”. 
A Virtual Data Warehouse enables distributed access to disparate, remote
data sources with the ability to run federated queries across such
sources.   To meet emerging business
requirements, data warehouses need to support lower data latency, reduce
storage of rarely used data, and allow access to remote structured and
unstructured data sources.  The solution
to these demands lies in the federation aspect of information integration.  Federation makes it possible to avoid
bringing all the data together by maintaining a logical view of a single
warehouse.  That doesn’t mean that data
is never duplicated centrally, only that duplication is minimized and not
stored in a warehouse optimized for a particular asset analysis
application.   The diagram below
illustrates the asset analysis project components.

if !vml?![](Anl_Asset_Deploy_files/image004.gif)endif?

Figure ‑19 Asset Management Integration Example

 

In this diagram, a collection of databases including Asset
Management System (AMS), Outage Management
System (OMS), Work Management System (WMS),
and others are integrated using the GID
Server.  The databases are aggregated
with power system modeling data supplied via the message bus. The databases are
tied directly to the Virtual Data Warehouse and not to the message bus for
performance.  By avoiding the XML
messaging required by the message bus and only using the binary
interface-to-interface remote procedure calls, query performance of the
analysis applications is maximized.  This
architecture highlights one of the advantages of using a transport neutral
interface such as GDA.  In this
architecture, links are optimized to meet project goals while still enabling a
single standard off-the-shelf wrapper for applications.   Application vendors can supply a single
standard wrapper for data warehousing and message based application
integration.

For example, an off the shelf Condition Based Monitoring
Application can connect directly into the CIM/GID
integration infrastructure using the GID
interfaces.  Periodically, this
application examines current transformer loading and temperatures and after
running calculations, publishes results on to the bus.  The Condition Based Monitoring Application
obtains required asset and power system information about equipment from the GID
server.  Figure 20 depicts the combined system.

 

if !vml?![](Anl_Asset_Deploy_files/image006.gif)endif?

Figure ‑20 Combined Application Integration And Data Integration
Architecture

 

Figure
21 illustrates the specific GID
interfaces required to integrate the applications and databases involved:

 

if !vml?![](Anl_Asset_Deploy_files/image008.gif)endif?

Figure ‑21 GID
Interfaces Used to Integrate Applications and Data

 

Using CIM/GID application
vendors can “shrink wrap” a CIM/GID
compliant wrapper, the use of the CIM and GID
can lower the cost of integration to utilities by fostering
the market for off-the-shelf connectors supplied by application vendors or 3rd
parties. The time and money associated with data warehousing/application
integration wrapper development and maintenance is high. Typically, most money
spent on integration is spent on the wrappers. An off-the-shelf CIM/GID
wrapper can replace the custom-built “Extraction and Transformation” steps of
an ETL process. The availability of off-the-shelf CIM/GID
compliant wrappers is a key to lowering data warehouse construction costs very
significantly. 

It is clear that utilities are under greater pressure to
simultaneously lower costs while at the same increase reliability and meet
shareholder expectations.  As a
capital-intensive industry, attention naturally focuses on optimization of
assets.  Effective and efficient use of
assets implies minimizing the total cost of ownership, i.e. minimizing the
purchase, installation, operation, and de-commission cost of assets.  More fundamentally this means utilities must
more effectively manage:

if !supportLists?·      
endif?Asset operations

if !supportLists?·      
endif?Work management operations related to asset life
cycles

While “return on investment” (ROI) is a more commonly
known metric for the value of an investment, “return on assets” (ROA) more
accurately represents the value of asset related activity and
expenditures.  ROA includes the actual
return from cost savings, increased asset utilization and productivity. 

If ROA provides a concise metric, physical variations in,
as well as the geographic and organizational distribution of assets, make it
difficult to effectively manage assets or establish a uniform ROA calculation
method.  In order to glean meaningful
information so that intelligent decisions and metrics can be derived from the
mass of data, analysis applications must be constructed.  Thus, key to increasing ROA is analysis of
asset and work management operations. This paper discusses how a utility may
increase ROA via the deployment of a platform for asset related analysis
applications.  This platform depends on
the use of standards and off-the-shelf EPRI applications.  Specifically, the proposed solution describes
how international standards such as the EPRI/IEC Common Information Model (CIM)
and Generic Interface Definition (GID) can
be combined with off the shelf analysis applications to create a utility asset
analysis platform designed to maximize ROA.
