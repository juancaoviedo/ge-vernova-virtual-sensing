# Synchronous Optical Network (SONET) and Synchronous Digital Hierarchy (SDH)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Synchronous_Optical_Network_(SONET)_and_Synchronous_Digital_.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Synchronous Optical Network (SONET) and Synchronous Digital Hierarchy (SDH)

**URL:**http://www.ansi.org  
http://webstore.ansi.org/ansidocstore/default.asp

Synchronous Optical Network (SONET) and Synchronous
Digital Hierarchy (SDH) are two virtually identical standards that specify
synchronous data transmission over a fiber optic network. They are a **physical
layer** technology designed to provide a universal transmission and
multiplexing scheme, with transmission rates in the gigabit per second range,
and a sophisticated operations and management system.

SONET, primarily used in the US and Japan, is
published by **ANSI T1.105, 117 and 119**. while SDH, the international
version, is published by the by **ITU-T** (G.707, 708, 709, and 783). The most
commonly used speed categories are shown in the table below.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Optical Level | Electrical Level | Line Rate (Mbps) | SDH Equivalent | Capacity |
| OC-1 | STS-1 | 51.840 | - | 28 DS1s (T-1) or 1 DS3 (T-3) |
| OC-3 | STS-3 | 155.520 | STM-1 | 84 DS1s or 3 DS3s or 1 E4 |
| OC-12 | STS-12 | 622.080 | STM-4 | 336 DS1s or 12 DS3s or 4 E4 |
| OC-48 | STS-48 | 2488.320 | STM-16 | 1344 DS1s or 48 DS3s or 16 E4 |
| OC-192 | STS-192 | 9953.280 | STM-64 | 5376 DS1s or 192 DS3s or 64 E$ |
| OC-768 | STS-768 | 39813.12 | STM-256 | 21504 DS1s or 768 DS3s or 256 E4 |

OC = Optical Carrier, STS = Synchronous Transport
Signal, STM = Synchronous Transport Module

SONET data rates are from OC-1 (51+ Mbps) to OC-768
(768 times OC-1). OC-1 is one-third the STM-1 rate of SDH. Aside from ANSI,
other forums such as SONET Interpretability Forum (SIF), ATM Forum (for ATM
over SONET) and IETF (for Packet Over SONET, POS) work or have worked on
various aspects of SONET. One of the very important aspects of SONET is the
restoration work that has gone into it and has made networks as resilient as
they are to failures. SONET is typically deployed in dual redundant ring
topologies. SONET offers the ability to provide protection from physical and
logical failures in the ring in 50 ms based on the automatic
protection-switching (APS) standard.

**Keywords:** media, fiber optic, physical layer
