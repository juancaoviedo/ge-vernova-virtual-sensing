# Benefits

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Benefits.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Benefits

## Reusable Infrastructure

By sharing a common design framework, device, IT resource
management, application, data warehousing and energy trading integration
solutions can be built simultaneously. This approach reuses shared adapters to
leverage the investment in each. Separately, the cost of developing individual
adapters for all the integration tasks can be exorbitant. By exposing adapters
directly to the data analysis infrastructure without requiring an intervening
copy of all the data in an intermediate warehouse for analysis, flexibility is
maximized while costs are minimized.

## Standards

It is said that
the average age of utility employees in the US is close to 50 years old. If one
combines the number of people that will retire over the next 5 to 10 years with
average utility power system engineer turnover, then it is a fairly safe
assumption that utilities need to carefully consider how system knowledge
continuity will be accomplished. This situation is compounded by the fact that
many utilities rely on systems that are customized for their particular
installation. For example, many utilities model a network differently even
though they may use the same modeling tool as their neighbor. A solution to
this problem can include agreement by utilities on standardized best practices.
Not only will agreement between utilities enlarge the knowledge pool so that
more effective integration and analysis can be accomplished, it will allow
utilities to wean themselves off customized solutions. The IEC and DMTF
standards can play an important role in the move towards non-biased
standardized solutions. The IntelliGrid Architecture compatible architecture presented here is
entirely based on standardized interfaces – free of political tugs-of-war and
vendor lock-in. Adoption of this architecture can help provide the continuity
that utilities need.

## Off the shelf Adapters

As stated above, the cost of application adapters required
to for an infrastructure for integration and analysis is the most significant
cost of deploying these technologies. An integration infrastructure based on
the IntelliGrid Architecture described here helps enable the availability of
off-the-shelf wrappers because application vendors and 3rd parties
can now reasonably expect that a IntelliGrid Architecture based solution developed for one
location could be used in others too. Furthermore these wrappers can be
deployed independently of what integration infrastructure the utility happens
to choose.

## 3rd Party Applications

Standardization of
the IEC and DMTF technologies fosters interoperability of components for many
uses. One market that will likely be created as a result of this
standardization is the market for CIM/GID based analysis applications or
application add-ons. Today, every analysis applications or application add-on
must be extensively customized for every deployment. If an analysis or add-on
application supplier can assume the existence of the CIM and GID, then the
supplier can sell the same tool to different utilities with a minimal amount of
customization. Decreased development cost, together with competition, should
help drive down prices.

## Extensible

As discussed previously, traditional integration
techniques are limited by not providing the capability to discover information.
The approach proposed in this report facilitates inclusion of unstructured data
and avoids preordaining how data will be organized and analyzed.  In doing so, this approach provides a
flexible approach for the future.

## Incremental approach

Fundamentally, integration with the using the IntelliGrid Architecture involves looking at the big picture. However, integration may
encompass data from a large or small set of applications. One does not need to
undertake a major project that requires many months to complete. The issue here
is the development of a long-term enterprise wide integration strategy so that
a small integration project does not become just another slightly larger island
of automation. Thinking at the enterprise level while integrating at the department
level minimizes risk and maximizes the chances for long-term success. Within
the context of a long-term plan, the IntelliGrid Architecture makes it possible to
tackle the problem of integration in a staged approach. Rather than having to
understand the relative mapping of all of the shared model for each application
that you may need in the future, IntelliGrid Architecture approach lets you start with a more focused approach
and expand the solution over time. For example, the GID can be used to provide
a CIM wrapper on existing data warehouses. You could start with one existing
data warehouse to enable the CIM based integration of only that specific data
warehouse. You can then increase the scope of the CIM and GID incrementally
until, eventually, all data in the various data marts, warehouses and
applications are all available via a unified CIM view. The inevitable
inconsistencies in meaning or content between existing databases and
applications can be gradually discovered and addressed as needed. In this
manner, the CIM and GID delivers incremental value with staged effort
throughout the process.

## Conclusion

The sections above have described how the use of the IntelliGrid Architecture can allow components to connect and exchange information
automatically. However, there is one problem that cannot be resolved via
standards. The remaining problem is that every utility typically names objects
such as a breaker, substation, or any other resource in a non-uniform manner.
The ID used to refer to an individual breaker in one application will
frequently not match the name in a second application. To get the two
applications to exchange data, a name mapping must be created. This remains a
persistent road block to complete “plug and play”.  However, creating a name mapping table does
not require custom programming and can frequently be partially automated by
using the name conventions that do exist within most applications.

The benefits of standardized data models and component
interfaces are clear. Utilities can significantly lower the cost of performing
integration by leveraging off-the-shelf components and wrappers from
application vendors or third parties. Furthermore, the standard models and the
standard interfaces provide a power system specific mechanism to more easily
deploy, configure and use an integration infrastructure. As a result, a utility
can achieve greater efficiencies and adaptability at a cost that is not
prohibitive.

if !supportFootnotes?  

---

endif?

[if !supportFootnotes?[1]endif?](Anl_Benefits.htm#_ftnref1) Booch,
Jacobson, Rumbaugh; *The Unified Modeling Language User Guide*,
Addison-Wesley, 2001

[if !supportFootnotes?[2]endif?](Anl_Benefits.htm#_ftnref2) *The Reference
Model of Open Distributed Processing, ITU-T Rec. X.901 | ISO/IEC 10746-1 to
ITU-T Rec. X.904 | ISO/IEC 10746-4, commonly referred to as RM-ODP, provides a
framework to support the development of standards that will support distributed
processing in heterogeneous environments. It is based, as far as possible, on
the use of formal description techniques for specification of the architecture.
In support of the generic design goals, it facilitates specifying integration architecture
with the following properties: openness, flexibility, modularity, federation,
manageability, and provisions for quality of service, security and
transparency.  For more info on RM RM-ODP
see Janis Putman’s “Architecting with RM-ODP” published by Prentice Hall, ISBN
0-13-019116-7.*

[if !supportFootnotes?[3]endif?](Anl_Benefits.htm#_ftnref3)
Extracted and modified from reference [3]

[if !supportFootnotes?[4]endif?](Anl_Benefits.htm#_ftnref4) Distributed
Data Warehousing Using Web Technology, R. A. Moeller, Amacom 2001
www.amacombooks.org

[if !supportFootnotes?[5]endif?](Anl_Benefits.htm#_ftnref5) [RFC 2578] McCloghrie, K., Perkins, D.,
Schoenwaelder, J., Case, J., Rose, M. and S. Waldbusser, “Structure of
Management Information Version 2 (SMIv2)”, IETF

[if !supportFootnotes?[6]endif?](Anl_Benefits.htm#_ftnref6) [RFC 2578] McCloghrie, K., Perkins, D.,
Schoenwaelder, J., Case, J., Rose, M. and S. Waldbusser, “Structure of
Management Information Version 2 (SMIv2)”, IETF RFC 2578, April 1999 and [RFC
2579] McCloghrie, K., Perkins, D., Schoenwaelder, J., Case, J., Rose, M. and S.
Waldbusser, “Textual Conventions for SMIv2”, IETF RFC 2579, April 1999

[if !supportFootnotes?[7]endif?](Anl_Benefits.htm#_ftnref7) [ITU X720] ITU-T Recommendation X.720,
"Information Technology – Open Systems Interconnection – Structure of
Management Information: Management Information

Model," January 1992. [ITU X721] ITU-T Recommendation X.721, “Information Technology -
Open Systems Interconnection - Structure of Management Information - Part 2:
Definition of Management Information”, February 1992.

[if !supportFootnotes?[8]endif?](Anl_Benefits.htm#_ftnref8) [WBEM]  
www.dmtf.org

[if !supportFootnotes?[9]endif?](Anl_Benefits.htm#_ftnref9) It
should be noted that the WBEM/DTMF CIM is not the same as the Common
Information Model developed during EPRI’s Control Center API project and now
being standardized in the IEC.  While both
are similar in nature and intent, the content of the DTMF CIM is focused on
system and network management while the IEC CIM is focused on power system
operation.

[if !supportFootnotes?[10]endif?](Anl_Benefits.htm#_ftnref10)
[Chiueh 03] Tzi-cker Chiueh, "Unification of Network Management
Technologies for Next-Generation Digitally Controlled Power Grid," draft
of the final report for a mini-EPRI project, 2003

[if !supportFootnotes?[11]endif?](Anl_Benefits.htm#_ftnref11)
[de Vergara 03] J.E.L. de Vergara, V.A. Villagra and J. Berrocal, "An
ontology-based method to merge and map management information models",
Procs. of HP Openview University Association Tenth Plenary Workshop, Geneva,
Switzerland, July 2003.

[if !supportFootnotes?[12]endif?](Anl_Benefits.htm#_ftnref12)
[Noy 99] N.F. Noy, M.A. Musen, "An Algorithm for Merging and Aligning
Ontologies: Automation and Tool Support," Procs. of the Workshop on
Ontology Management, Sixteenth National Conference on Artificial Intelligence
(AAAI-99), Orlando, Florida, U.S.A., July 1999

[if !supportFootnotes?[13]endif?](Anl_Benefits.htm#_ftnref13)
IEC60870-5 was originally released under an older numbering system used by IEC
at the time as IEC 870-5. IEC60870-5 and IEC 870-5 refer to the exact same
standards.

[if !supportFootnotes?[14]endif?](Anl_Benefits.htm#_ftnref14)
Unlike UCA2.0, there were no profiles for serial link communications. IEC61850
is strictly a network based protocol.

[if !supportFootnotes?[15]endif?](Anl_Benefits.htm#_ftnref15)
For more information see IEC 61970 Parts 401 – 405.

[if !supportFootnotes?[16]endif?](Anl_Benefits.htm#_ftnref16)
All DAIS as well as OPC DA, HDA, and A&E clients are by definition
compliant.  All DAIS as well as OPC DA,
HDA, and A&E servers are compliant if they present their data within the
context of the TC57 Namespaces.

[if !supportFootnotes?[17]endif?](Anl_Benefits.htm#_ftnref17)
This is particularly true for utilities in North America or Western European
countries that are early adopters of IP-based technologies.

[if !supportFootnotes?[18]endif?](Anl_Benefits.htm#_ftnref18)
In 1:N protection, there are N+1parallel set of diverse network elements and
links  connecting between the source
destination. N out of these N+1 paths are carrying active traffic while the
remaining one path just stands by, waiting 
to take over in case any one of the N paths fail.

[if !supportFootnotes?[19]endif?](Anl_Benefits.htm#_ftnref19)
In 1+1 protection, there are 2 parallel diverse paths between the source and
destination and a copy of every user data is always sent along each of the 2
parallel paths to allow the destination for selection.

[if !supportFootnotes?[20]endif?](Anl_Benefits.htm#_ftnref20)
Note that this does not mean that the infrastructure done not need to manage
the transformations from native to common semantics.  Management of these transformations is key to
their maintenance and reuse.  However,
the use of a common model greatly reduces their value to analysis applications.

[if !supportFootnotes?[21]endif?](Anl_Benefits.htm#_ftnref21)
For generation, and to a lesser extent transmission system assets, ROA can also
be driven by market factors.  For
example, the price of power or the difference in price between one region and
another can significantly increase the value of an asset and thus also increase
the opportunity cost when the asset is not in operation
