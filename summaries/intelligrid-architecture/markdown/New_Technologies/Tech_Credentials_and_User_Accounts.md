# Credentials and User Accounts

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Credentials_and_User_Accounts.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Credentials and User Accounts

Credentials

There
are some general issues for credentials that apply to many of the credential
types that have been discussed.

·       How many
credentials of a given type will a user be allocated?  
  
In general, it is recommended to allocate a single physical credential of each
type (e.g. Smart Card, Personal ID card, Token Generator). This recommendation
even applies to Digital certificates. Such a policy will minimize the effort
required for management, renewal, and revocation (if needed).

·       Upon revocation,
a policy/mechanism needs to be developed to detect and enunciate if that
credential, even a network address, has been used after revocation. The policy
must address the expected detection timeframe allowed and the type of response expected
from SMI.   
  
Note: Typically, the smaller the detection window the higher the cost to
implement.

·       The period at
which credentials need to be renewed/modified.

·       The
determination of an appropriate non-use time that causes an investigation and
potential revocation of the credential if the credential has not been used
within that non-use time period.

·       Determine a
policy for revoking the credentials.

Personal Identification

The
design and management of Personal Identification cards will impact the ability
to enforce physical access control.

It
is recommended that such ID cards require a photograph of the person and also
have an area where an easy modification can be made.

As
a minimum, it is suggested that these modifications occur on a monthly basis
and be a multi-colored/foil label with a valid through date printed on it.

Addresses

In
order to provide an infrastructure for monitor and revocation of addresses, it
is important to address the two (2) main address types: statically and
dynamically assigned.

Statically Assigned Addresses

For
statically address assigned computation resources:

·       The policy
should require that the physical (e.g. Media Access Control address or
equivalent) be recorded. The policy must also allow for tracking changes in
that address.

·       That the
communication segment has an Access Control List (ACL) that prevents off
segment communication if the address is revoked.  
  
It is recommended that this policy be enforced through the deployment of SNMP
manageable switches. So that an address can be associated with a switch port,
and upon revocation the port is disabled.

·       The
policy/implementation should allow for continuous monitoring/detection of
addresses that should not be present and that have not been used for a policy
specified period of time.  
  
The policy/implementation infrastructure must provide the technology to detect
usage and determine periods of inactivity.

·       A
policy/procedure is needed that allows renewal/reactivation of the address if
the address has been revoked incorrectly.

·       A
policy/procedure is needed that allows re-assignment of a previously assigned
addressed.

Dynamically Assigned Addresses

For
dynamically addressed computation resources:

·       The policy
should prohibit dynamically assigned addresses from being used as single-factor
identification credentials. The probability of incorrect identity establishment
is high; therefore it should not be allowed.

·       The policy
should not allow off-segment communication unless a challenge-response is
performed.

·       The
policy/procedures/SMI must be able to provide an audit record/trail regarding
the address assigned to the challenge/response so that actual identification of
the user can occur.

·       The challenge-response
should be on an individual basis (e.g. no group assigned passwords).

Username/Passwords

There
are a couple of recommendations in regards to the use of usernames/passwords:

·       In general, a
particular user should be allowed one and only one password for a given
computational resource.

·       The size of the password,
and its required characters/format needs to be specified and enforced.  
  
The first question that needs to be answered is the character set. It is
recommended that upper, lower, punctuation, and numeric characters be allowed.
This increases the possible permutations of passwords dramatically:  
  
Example assumes ANSI Character Set:  
  
Number upper case
characters:                
24  
Number of lower case
characters:                          
24  
Number of numeric
characters:                 
10  
Number of punctuation characters[[9]](Tech_Credentials_and_User_Accounts.htm#_ftn9):                       
30  
  
Based upon a four(4) character password, then number of possible permutations
is shown to be:  
  
Permutations if upper case
only:                             
331,776  
Permutations if upper and lower case
:                   
5,308,416  
Permutations if upper, lower, numeric case
:                        
11,316,496  
Permutations if using all
characters:                                     
59,969,536  
  
It should be noted that some computational resources may not be able to accept
punctuation characters within passwords, but it is strongly recommended to
include upper, lower, and numeric characters within the password character set.

The
policy needs to determine the minimum size of a password in order to provide
adequate protection.   
  
Unfortunately, many existing policies assume that password size is the criteria, however protection comes from the number of
possible permutations. It is suggested that the minimum number of password
permutations be approximately 1 trillion for any computational resource.  
  
This means, based upon allowed characters, the minimum password size is :

Table 33: Recommended Minimum Password size

|  |  |
| --- | --- |
| Character Set Allowed | Recommended Password Size |
|  |  |
| Upper Case Characters Only | 9 |
| Upper/lower case characters only | 8 |
| Upper/lower/numeric characters | 7 |
| All characters | 6 |

It
is further recommended that seven(7) characters be the
absolute minimum.

·       The policy needs
to require at least one numeric character, if numeric characters are allowed.
Additionally, the policy should not allow numeric characters as the last
character of the password. Such a policy will eliminate the natural tendency to
append a number to a base password when revision of the password is required.

·       The policy needs
to address the period of time that requires password changing.

Smart Cards

Smart
cards can be used to contain personal identification information (e.g.
username/passwords), digital certificates, biometric information, and other types
of information. Therefore, the credential types they contain typically address
the credential aspects of a smart card.

The
major policy issue, specifically related to smart cards, is the development of
policies/procedures relating to the serialization of the smart cards.

Digital Certificates

There
is a major issue regarding digital certificates, and that is the handling of
revocation. Certificate Authorities (CAs) typically maintain Certificate
Revocation Lists (CRLs) that are updated on a twenty-four (24) hour interval. A
certificate that has been placed on a CRL is no longer trustworthy and
therefore should not be useable.

Policies
and procedures should be developed to:

·      
Specify a periodicity to check
the CAs CRLs and how to disseminate this information within the security
domain.  
  
The NERC DEWG has expressed a major concern in this area and further policy
study in order to develop a specific recommendation is warranted.

Virus Protection

The
developed policy should address virus and worm protection. It is suggested that
the following NIST guide be used as part of the policy development.

NIST,
NIST SP 500-166, August 1989, Computer Viruses and
Related Threats: A Management Guide, Springfield, Springfield, VA: NTIS.
