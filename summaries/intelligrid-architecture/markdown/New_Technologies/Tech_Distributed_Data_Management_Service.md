# Distributed Data Management Service

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Distributed_Data_Management_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Distributed Data Management Service

Management
of distributed data archives that are stored at multiple sides can be very
complex. In these cases the data can consists of a combination of flat files,
relational databases, as well as data stored internally by applications. Much
of the data changes over time, i.e. there are frequent updates. Users and
applications need access to all authorized data. Performance is critical, but
the data must “stay at home”. Coherence is critical, so caching must be done
with great care. Audit trails must exist for all data updates. Data management
and sharing is one of the most common and important uses of utility distributed
systems. How do we manage data stores so that they may be accessed across a
utility infrastructure? How do we cache data and manage its consistency? How do
we index and discover data and metadata? These are all questions that are
central to most current IntelliGrid Architecture deployments. They are likely to become more
important in the future.
