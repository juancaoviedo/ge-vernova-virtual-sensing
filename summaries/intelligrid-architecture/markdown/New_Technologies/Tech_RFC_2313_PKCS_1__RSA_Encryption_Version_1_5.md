# RFC 2313 PKCS #1: RSA Encryption Version 1.5

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_2313_PKCS_1__RSA_Encryption_Version_1_5.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 2313 PKCS #1: RSA Encryption Version 1.5

**URL:** http://www.ietf.org/rfc/rfc2313.txt

This
document describes a method for encrypting data using the RSA public-key
cryptosystem. Its intended use is in the construction of digital signatures and
digital envelopes, as described in PKCS #7:

·        For
digital signatures, the content to be signed is first reduced to a message
digest with a message-digest algorithm (such as MD5), and then an octet string
containing the message digest is encrypted with the RSA private key of the
signer of the content. The content and the encrypted message digest are
represented together according to the syntax in PKCS #7 to yield a digital
signature. This application is compatible with Privacy-Enhanced Mail (PEM)
methods.

·        For digital
envelopes, the content to be enveloped is first encrypted under a
content-encryption key with a content-encryption algorithm (such as DES), and
then the content-encryption key is encrypted with the RSA public keys of the
recipients of the content. The encrypted content and the encrypted
content-encryption key are represented together according to the syntax in PKCS
#7 to yield a digital envelope. This application is also compatible with PEM
methods.

The
document also describes a syntax for RSA public keys and private keys. The
public-key syntax would be used in certificates; the private-key syntax would
be used typically in PKCS #8 private-key information. The public-key syntax is
identical to that in both X.509 and Privacy-Enhanced Mail. Thus X.509/PEM RSA
keys can be used in this document.

The
document also defines three signature algorithms for use in signing X.509/PEM
certificates and certificate-revocation lists, PKCS #6 extended certificates,
and other objects employing digital signatures such as X.401 message tokens.

Details
on message-digest and content-encryption algorithms are outside the scope of
this document, as are details on sources of the pseudorandom bits required by
certain methods in this document.

**Keywords:**
