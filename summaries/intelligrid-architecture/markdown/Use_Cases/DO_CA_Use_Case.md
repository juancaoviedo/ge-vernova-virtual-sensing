# Contingency Analysis

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/DO_CA_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Distribution Operations - Contingency Analysis Function

## Contents

* [Narrative](DO_CA_Use_Case.htm#Narrative)

## Narrative

This application performs an N-m contingency
analysis in the relevant portion of distribution. The function runs in
the following manners:

1.      Periodically

2.      By event (topology
change, load change, availability of control change)

3.      Study mode, in which the
conditions are defined and the application is started by the user.

The application informs the operator on the
status of real-time distribution system reliability.

The contingency
analysis (CA) with significant DER in distribution has an increased
dimension due to several alternatives of DER operations in response to
the initial contingency.  The CA application typically starts from an
outage of a feeder segment or device.  With DER in distribution, the
fault, which brings the section down, should be analyzed and the
reaction of DER associated with this fault should be simulated.  This
simulation should address the issues like the following:

* Will the DERs impacted by the subject fault withstand
  the fault, or will some or all DERs disconnect?
* Will the adequacy be preserved, or should the load be
  disconnected together with the DER?
* Can the disconnected tail of feeder with DER be restored
  without the DER or should the section be restored with
  temporary overload of the backup circuits and with fast DER
  synchronization?
* Should the section be divided for balanced islanding?
* How to restore the normal operating conditions with
  given points of synchronization?  (Will it need another
  interruption when the loading permits?)

In addition to the information
about the synchronization capabilities at Point of Common Coupling (PCC),
information about other points of synchronization, which can be used
for reconnection of the intentional island with DERs should be made
available to the ADA application.  In some cases, when the DERs can
support load beyond the PCC, the intentional island created for this
purpose should be separated from the rest of distribution system by
switches equipped with synchronization devices to avoid customer
interruption during restoration of normal connectivity.
