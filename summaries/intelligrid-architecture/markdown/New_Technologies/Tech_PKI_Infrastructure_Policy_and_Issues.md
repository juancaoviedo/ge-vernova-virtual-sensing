# PKI Infrastructure Policy and Issues

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_PKI_Infrastructure_Policy_and_Issues.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### PKI Infrastructure Policy and Issues

Note:
This section is intended as a simple discussion of the issues regarding PKI.
There are more authoritative documents available from NIST or NERC.

The
purpose of the Public Key Infrastructure is to allow the establishment of Trust
through the binding of encryption keys (typically “public” keys) and
identities. In order to understand how PKI works, it is first important to that
PKI to understand the three prevalent types of encryption: symmetric,
asymmetric, and public/private.

·       Symmetric
encryption refers to the fact that both peers have the knowledge and use the
same encryption key. Since both peers have and use the same key, symmetric
encryption does not lend itself to unambiguous bindings (e.g. one key to a
particular application/entity), thus symmetric encryption should not be used as
the Trust establishment binding (e.g. should not be used within a PKI
environment).

·       Asymmetric
encryption refers to the fact that each entity has its own key. Unlike
symmetric encryption, asymmetric keys can allow for unambiguous identity
establishment. However, since cooperating peers would need to have knowledge of
the other peer’s key, it is often difficult to protect the identifying key.
Although asymmetric keys could facilitate a PKI environment, the use of such
keys for identity binding is not recommended since the keys must be disseminated/configured on multiple peers and therefore a
prone to being compromised.

·       Public/Private
key encryption works on the basis that the use of the public key allows the
decryption of information encrypted with the private key. Conversely,
information encrypted with the public key can only be decrypted with the
private key. It represents a specialization of asymmetric encryption.

The
use of public/private key encryption can be used for two purposes: encryption
and digital signatures.

![](../IECSA_Volumes/IECSA_VolumeIV_AppendixD_files/image010.wmz.html)![](../IECSA_Volumes/IECSA_VolumeIV_AppendixD_files/image011.gif)

Figure 6: Simplified diagram of Public/Private Key
encryption and Digital Signature

Figure
6 shows in order to Node A to encrypt data to be sent to Node B, the use of
Node B’s public key is required. It also shows that only the holder of Node B’s
private key can decrypt the information (neglecting encryption attacks).
Likewise, the Digital Signature exchange shows that Node A’s signature is
decoded by Node B through the use of Node A’s public key. Thus for both
encryption and digital signatures, only public keys need to be exchanged and
therefore it becomes easier to control and protect the private keys. Thus
public/private key based PKI systems should be the preferred approach.

Obviously,
it is critical to have a robust PKI infrastructure:

·       Create the
appropriate bindings between public/private keys and identification.  
  
The typical mechanism for the bindings is through a digital X.509 certificate.
A public certificate that includes the public key is created, and an equivalent
is created as the “private certificate” that contains both the private and
public keys. It is the creation of these two “certificates” that are typically
the responsibility of a Certificate Authority (CA).  
  
The protection of the public certificate/key is not that important, but the
protection of the private key/certificate is. It is the responsibility of the
CA to provide adequate protection during the generation process and to protect
this information even if the certificate has been sent to the actual user.  
  
Since the CA is the “root” source of the certificate, it is important that the
CA also provide Certificate Revocation List (CRL) ability so that compromised
or stolen certificates can be revoked.

·       The user of a
“private certificate” must provide security mechanism to protect the private
information.   
  
The actual mechanism for Security Domain/user archiving is a local issue, but
great care needs to be taken during the policy establishment to be able to
quickly and properly detect if there has been un-authorized access to the
Security Domain private certificates. The policy must include the appropriate
mechanism/procedures for reporting the compromised certificate and revoking its
use locally.

·       Even though the
public certificates do not have the same criticality, the Security Domain
policy should address the procedures for releasing the public certificate for
use.

·       A mechanism for
tracking the lifetime expiration date in advance to actual expiration needs to
be addressed.

·       Policies/procedures
for replacement and renewal of older certificates (prior to expiration) or
revoked certificates needs to be developed.

Of
particular concern in IntelliGrid Architecture, and the utility industry, is how to provide an
appropriate revocation capability for a Security Domain. There are several
design criteria for such an infrastructure:

·       The
infrastructure must be able to accommodate revocations of certificates that
have been issued from more than one CA.  
  
There is no central CA for the utility industry, or the world, and it does not
appear that there is movement towards such an entity. Even NERC, in its e-Marc
program, intends to allow certificates from multiple (although “certified”) CAs
to be used.

·       Many of the
certificate using computational resources will not be allowed direct access to
the Internet that would be required in order to query the CRL of a particular
CA.  
  
Additionally, CRLs can be large and can consume bandwidth and be computationally
intensive.

·       An ability to
determine if a particular Certificate has been revoked.  
  
The X.509 Internet Public Key Infrastructure Online Certificate Status Protocol
- OCSP (RFC 2560) allows such a capability. It is worthwhile to note that OCSP
is a request/response-oriented protocol (e.g. the certificate user must request
to check if a certificate has been revoked).

However,
the fact that OCSP is request/response means that there is an issue of
timeliness in revocation information. However such a protocol/procedure does
not exist today. In a future time, it could be envisioned that a central
Security Domain revocation server (not a CRL server) could be created with the
following attributes:

·       Allows
certificate users to register that certificates are in the user certificate
cache.

·       The Revocation
Server would query the CAs CRL servers and process the revocation list(s).

·       Based upon the
CRL processing, the Revocation Server would notify the certificate user that
the particular certificate has been revoked.

·       Optionally, such
a Revocation Server could alert Security Domain management that a certificate
of a particular user is about to expire so that corrective action could be
taken.

·       Optionally, such
a Revocation Server could respond to OCSP requests so that newly configured
certificates could be validated as still being valid.

It
is believed that work on such an entity is needed to allow more timely delivery
of revocation information and to allow automation of such tasks.

#### Specific Policy Issues and Recommendations per Service

Some
security services merit specific policy recommendations that were not expressed
within the security service section explicitly.
