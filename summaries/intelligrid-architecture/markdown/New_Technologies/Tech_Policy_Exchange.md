# Policy Exchange

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Policy_Exchange.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Policy Exchange

Allow
service requestors and providers to exchange dynamically security (among other)
policy information to establish a negotiated security context between them.
Such policy information can contain authentication requirements, supported
functionality, constraints, privacy rules etc.

Typically,
there has been no defined framework or policy exchange mechanism available that
is technology neutral and therefore such exchanges have not occurred or have
been performed manually. There are several issues that have prevented the
development of such a framework:

·      
Agreement in regards to what constitutes security policy varies.
Therefore, such an exchange mechanism would need to provide basic attribute
definitions and also allow for a large amount of customization.

·      
There has not been a single secure and ubiquitous technology available
over which to perform such an exchange.

Technology Assessment and Relevant
Specifications

When
analyzing how to exchange policies in IntelliGrid Architecture environment, the problem of
having a ubiquitous technology has not been solved. There still does not appear
to be a solution that can solve policy exchange issues in the Transmission
& Distribution environment (especially serially connected devices),
spanning to databases, to web technology. However, there are emerging
specifications in how to perform such exchanges when web services/SOAP
infrastructures are available.

For
policy exchanges via SOAP, it is recommended that the WS-Policy,
WS-PolicyAssertions, and WS-PolicyAttachment specifications form the basis of
such exchanges. It is also recommended that customizations be kept to a minimum
in order to maximize interoperability and interworkability.

Table 24: Relevant Specification regarding Policy Exchange

| Identification Number | Name | Comment |
| --- | --- | --- |
| OASIS | Web Services Policy Framework (WS-Policy)  Available from:  http://xml.coverpages.org/ws-policyV11.pdf | Recommended |
| OASIS | Web Services Policy Assertions Language (WS-PolicyAssertions)  Available from:   http://xml.coverpages.org/ws-policyassertionsV11.pdf | Recommended |
| OASIS | Web Services Policy Attachment (WS-PolicyAttachment)  Available from:  http://xml.coverpages.org/ws-policyattachmentV11.pdf | Recommended |
