# Data Consistency across Multiple Systems

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Data_Consistency_across_Multiple_Systems.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Data Consistency across Multiple Systems

Data
consistency across multiple systems is vital for reliable automation of
functions. If data is inconsistent, then the applications will have
inconsistent and probably incorrect results. Many factors impact data
consistency, but some methodologies can be used to help insure consistency.
These include:

·       Use of publish/subscribe
application services, in which every application that requires certain data
“subscribes” to it. Then, whenever the source data is updated, it is
“published” to all subscribers simultaneously.

·       Data should
carry “quality” indications as it is passed from its source to other systems.
These quality indications could include “invalid”, “out-of-date”,
“manually-entered”, and “calculated”. More complex indications could include
multiple timestamps indicating when the data was first created, as well as when
it arrived at each database, or indications of what parameters where used in
calculating its value, etc.

·       Applications
should validate the input data, possibly by analysis (e.g. State Estimation),
possibly by accessing multiple sources of similar data that can be
cross-checked.

·       Error handling
mechanisms should be in place to notify the Network Manager of loss of data,
inaccessibility of data, invalid data, and other data quality indications.

**Keywords:**keywords
