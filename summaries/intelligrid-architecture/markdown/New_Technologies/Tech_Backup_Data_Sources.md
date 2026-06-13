# Backup Data Sources

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Backup_Data_Sources.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Backup Data Sources

When
high availability of data is required, one of the better ways to ensure that
availability is to have backup data sources. These data sources could be:

·       Older versions
of the data. This is the most common for large sets of data or files that do
not intrinsically have another source than a copy of the original data.

·       Second sources
that can generate the same or very similar data. This is often used in
real-time monitoring by having alternate sensors to collect the same data from
(electrically) near-by sites

·       Calculated data.
This is possible if other data can be used to calculate the original value.

When
high accuracy of data is required, multiple sources can be used to check
against each other. Sometimes voting is included, for instance 2 out of 3 data
values must agree before the data is accepted as valid.

**Keywords:**Backup, high availability, high accuracy
