# User and Group Account Management

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_User_and_Group_Account_Management.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### User and Group Account Management

This
service allows the ability to define, assign, organize, control
and maintain mapping for user and group identifiers within the security domain.
There is no authoritative technology that is applicable to providing this
service and therefore must be rigorously addressed via policy.

However,
there are several relevant articles that may prove of assistance.

Table 34: Relevant Articles concerning User and Group
Account Management

|  |  |
| --- | --- |
| Oblix | Best Practices in Extranet Portals and Identity Management |
| Oblix | Mastering Supply Chain Partnerships: Achieving Core Business Objectives through Effective Identity Management  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | Lowering eBusiness Administrative Costs with Effective Group Management  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | An Overview of Federated Identity Architecture  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | Creating a Secure and Unified eBusiness Infrastructure  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | An Overview of Federated Identity Architecture  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | Creating a Secure and Unified eBusiness Infrastructure  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Computerworld | Five rules for top-notch user management and provisioning  Available from:  http://www.computerworld.com/securitytopics/security  /story/0,10801,90407,00.html?f=x10 |

If
thoroughly reviewed, the articles clearly indicate that the basic premise of
User and Group Management has its foundations in Identity management (e.g.
Identity Establishment and Mapping services). Thus, the technological
recommendations from those security services needs to be part of the User and
Group Management service. Additionally, the following are key recommendations
from the literature:

·       Deprecation or
changing of all default accounts is needed.  
  
This would mean that for Operating Systems, that the default user accounts
should be removed or a least have the credentials changed (e.g. passwords).
This should include ALL user accounts, including remote diagnostic accounts.

·       Accounts that
are not frequently used should be de-activated.  
  
One of the most prevalent issues is determining the usage of a particular user
account. The Security Domain’s policy should specify a period of inactivity
that causes user accounts to become inactive (e.g. no longer valid but
available to be renewed/re-activated).

·       Group Accounts
should be granular enough to provide appropriate access privilege restriction.  
  
At a general level, the following privileges need to be addressed:  
  
Remote Login: Does the User belong to a group that has the privilege to make
use of the computational resource remotely.   
  
Execute: Does the User belong to a group that has the privilege to execute a
particular program/application.   
  
Access: Does the User belong to a group that has the privilege to access the
information contained in a computational resource (e.g. file, database, etc…).
There is a need for further granularity based upon the particular instance of
file/resource.  
  
Modification: Does the User belong to a group that has the privilege to modify
the information contained in a computational resource. Similar granularity to
Access is typically needed.  
  
View: Does the User belong to a group that is allowed to view the existence of
a particular resource (e.g. the ability to have a directory with particular
files appearing in the directory response).  
  
Within the IntelliGrid Architecture, there are two additional privileges that need to
be considered. These are privileges that typically relate to interactions with
field devices and not business level computational resources, although they may
be needed in some cases (e.g. User Management): Configuration and Control
Privileges.  
  
Configuration: Does the user belong to a group that has the privilege to change
the configuration of a computational resource. There may be further granularity
required based upon the types of configuration supported by the computational
resource (e.g. users, protective schemes, control settings, initial values,
setting groups, etc.).  
  
Control: Does the user belong to a group that has the privilege to change
/control real-time process aspects of a computational resource. Further
granularity may need to be provided based upon the class of controllable resources
available on a computational resource.

·       Within a
Security Domain, there needs to be centralized management and storage of the
user/account information, typically in a directory like environment.

·       Single Sign-On
is a typical objective of intra-domain management.

This service can be subdivided into a policy part and an actual security
service: Setting and Verifying User Accounts.

Setting and Verifying User
Accounts Service

This
service is for assigning and validating authority given to a user or a group of
users in accessing/utilizing specific enterprise resources.

There
is no authoritative technology to evaluate for this service. However, from an
abstract security service level such a service needs to exist. The service
needs to provide the functionality of:

·       Lifecycle
management of user and group account. This includes the ability to create,
renew, deprecate, modify, and delete users and groups.

·       Credential
Management is required so that passwords, certificates, etc. can be
replaced/renewed/deprecated as required.
