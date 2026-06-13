# RFC 2040 The RC5, RC5-CBC, RC5-CBC-Pad, and RC5-CTS Algorithms

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_2040_The_RC5,_RC5-CBC,_RC5-CBC-Pad,_and_RC5-CTS_Algorith.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 2040 The RC5, RC5-CBC, RC5-CBC-Pad, and RC5-CTS Algorithms

**URL:** http://www.ietf.org/rfc/rfc2040.txt

This
document defines four ciphers with enough detail to ensure interoperability
between different implementations. The first cipher is the raw RC5 block
cipher. The RC5 cipher takes a fixed size input block and produces a fixed
sized output block using a transformation that depends on a key. The second
cipher, RC5-CBC, is the Cipher Block Chaining (CBC) mode for RC5. It can
process messages whose length is a multiple of the RC5 block size. The third
cipher, RC5-CBC-Pad, handles plaintext of any length, though the ciphertext
will be longer than the plaintext by at most the size of a single RC5 block.
The RC5-CTS cipher is the Cipher Text Stealing mode of RC5, which handles
plaintext of any length and the ciphertext length matches the plaintext length.

The
RC5 cipher was invented by Professor Ronald L. Rivest of the Massachusetts
Institute of Technology in 1994. It is a very fast and simple algorithm that is
parameterized by the block size, the number of rounds, and key length. These
parameters can be adjusted to meet different goals for security, performance,
and exportability.

RSA
Data Security Incorporated has filed a patent application on the RC5 cipher and
for trademark protection for RC5, RC5-CBC, RC5-CBC-Pad, RC5-CTS
and assorted variations.

**Keywords:**
