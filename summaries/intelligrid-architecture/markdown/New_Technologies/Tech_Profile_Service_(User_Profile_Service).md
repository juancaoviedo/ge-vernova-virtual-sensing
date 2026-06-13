# User Profile Service

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Profile_Service_(User_Profile_Service).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Profile Service (User Profile Service)

The
profile service is concerned with managing service requestor’s preferences and
data which my not be directly consumed by the authorization service. This may
be service requestor specific personalization data, which for example can be
used to tailor or customize the service requestor’s experience (if incorporated
into an application which interfaces with end-users.) It is expected that primarily
this data will be used by applications that interface with a person.

Technological Assessment and
Relevant Specifications

Research
and experience indicates the web user profiles are the trend. To experience
this, use any of the commercial web portals (e.g. Yahoo®, MSN®, etc…). These
all offer the ability to personalize the information displayed and the actual
display format. However, it is doubtful that any of the current portal
technologies make use of the Semantic Web specification.

It
is recommended, when possible, that the Semantic Web specification be utilized
when possible. If such an implementation is not feasible or costly, it is
recommended to implement based upon some local means.

Table 27: Relevant Specifications regarding the Profile Service

|  |  |  |
| --- | --- | --- |
| Identification Number | Name | Comment |
| Semantic Web | Pervasive Computing Standard Ontology (PERVASIVE-SO) Guide -- Describing User Profile and Preferences    Available from: http://pervasive.semanticweb.org/doc/2004-01-ont-guide/part1/ | Highly Recommended |
| IEEE | IEEE Personal and Private Information (PAPI) draft standard |  |
