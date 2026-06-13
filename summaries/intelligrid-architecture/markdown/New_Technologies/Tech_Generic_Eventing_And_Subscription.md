# Generic Eventing And Subscription

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Generic_Eventing_And_Subscription.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Generic Eventing And Subscription

A
collection of dynamic, distributed services that must be able to notify each
other asynchronously of interesting changes to their state.  This service
is generally thought of in terms of a publish/subscribe model. This
event-driven, or notification-based, interaction service is a commonly used
service for inter-object communications.  In the notification service an
entity disseminates information to a set of other services or devices without
having to have prior knowledge of these other Services or devices. 
Characteristics of this service include:

·       The entities
that wish to consume information (which we call Notification Consumers) are
registered dynamically with the service/entity that is capable of distributing
information.  As part of this registration process the Notification
Consumers may provide some indication of the nature of the information that
they wish to receive.

·       The distributing
entity disseminates information by sending one-way messages to the Notification
Consumers that are registered to receive the information. It is possible that
more than one Notification Consumer is registered to consume the same
information. In such cases, each Notification Consumer that is registered
receives a separate copy of the information.

·       The distributing
entity may send any number of messages to each registered Notification
Consumer; it is not limited to sending just a single message. Note also that a
given Notification Consumer may receive zero or more Notification Messages
throughout the time during which it is registered.
