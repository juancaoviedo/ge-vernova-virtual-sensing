# NERC e-tagging

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_NERC_e-tagging.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### NERC e-tagging

**URL:**http://reg.tsin.com/Tagging/e-tag/Tagging%20Essentials.pdf

The electronic Transaction Information System (TIS)
implemented by NERC is a process of electronically communicating a request for,
securing approval of, and recording an energy transaction via the Internet. The
process is more commonly referred to as Electronic Tagging, or ETAG.

The scheduling of
energy transfers has historically been done on a coordinated basis between
control areas. The path chosen, where more than one adjacent control
area was involved, was arranged in a sequential manner from control area to
control area (contract path). However, since electricity follows the laws of
physics and not economics, some of the energy transferred would flow through
other systems not involved in the “contract path”, resulting in what are called
“parallel flows” on those systems.

The shortcomings of the contract path approach were
known to utilities from its inception. However, the limitations were acceptable
because the transfers were limited and small in nature. As energy transfers
became more numerous and complex, however, the parallel flows on systems off
the contract path began to cause serious economic and operational problems.
Many utilities began experiencing overloads on
their transmission lines without any idea of the source of the additional
flows. Firm and non-firm energy schedules had to be canceled, resulting in lost
revenues, because the origin of non-compensated flows was unknown.

NERC has implemented a
Transaction Information System (TIS) in an effort to provide system operators
with the identity of the source of parallel flows impacting their systems. Each
energy transaction is identified through a “tag” and its impact on the
transmission grid calculated utilizing power transfer distribution factors in a
process called the Interchange Distribution Calculator (IDC). This calculation
generally is performed “after the fact” in case of an overload, and not before
the transaction is initiated. The object is to provide a rational and
economically equitable basis for curtailing transactions. While minimizing the
need for curtailments, the process does not, however, eliminate the need for
them.

The first attempt to
secure energy transaction information was by means of an Excel
spreadsheet-based tag entry and retrieval system, which utilized faxes and Internet
e-mail to transport tags between parties involved in a transaction. However,
e-mail had inherent problems with timely delivery of the tag information and
the concern that multiple copies of the tag were distributed and sometimes
corrupted or changed. At the same time the specification of the tag information
was not rigorous and thus the data could be interpreted in different ways.

What was needed was an
electronic system, which would ensure that tags get sent, received, and
approved in a timely, reliable manner. Such a system would take full advantage
of automation of processes such as data validation and reduce the need for
operator intervention.

In its November, 1998
resolution adopting the Constrained Path Method (CPM) as the basis for
determining interchange transaction curtailment priorities as part of the
Transmission Line Loading Relief (TLR) procedure, the NERC Operating Committee
directed that such an electronic system be developed. A document, Electronic
Tagging - Functional Specifications, was subsequently produced by the NERC
Transaction Information System Working Group. The document describes the
functional requirements and detailed technical specifications for the
implementation of ETAG. The document did not specify the type of software or
graphical interfaces to be used, leaving these up to the vendor community.
Numerous vendors are currently offering ETAG products and a list of them can be
found on the NERC website.

**Keywords:** NERC, Reliability, Constrained Paths, Line Loading Relief, Etagging
