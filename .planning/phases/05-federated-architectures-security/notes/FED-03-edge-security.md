# FED-03: Edge Security — OTA Integrity, TPM Attestation & SPIFFE/SPIRE

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Cover OTA update integrity, TPM attestation, and SPIFFE/SPIRE workload identity — naming the concrete grid threat each counters and connecting each to work Juan has shipped — so you can describe and bridge all three in a 60-second spoken answer.

---

> **Depth strategy:** AWARENESS depth only (per D-05). One crisp paragraph per concept + the grid threat it counters + an honest bridge. NO SPIRE config, NO TPM register internals, NO PKI deep-dive — the criterion only asks to describe and connect.

## 1. Mental Model — Edge Security Beyond "Just TLS"

An autonomous K3s substation fleet needs three guarantees beyond an encrypted channel: that the code it runs is genuine (OTA signing), that the hardware booted untampered (TPM attestation), and that each workload is who it claims to be (SPIFFE/SPIRE). TLS encrypts the pipe; these three mechanisms answer a prior question — "should this node be trusted *at all*?" — before any data flows through that pipe.

---

## 2. OTA Update Integrity (Awareness)

**What it is:** Over-the-air firmware or software update with cryptographic signing. The build pipeline signs the update image with a private key held in an HSM; the edge device verifies the signature before applying it. Only images that pass signature verification are installed — unsigned or invalidly signed images are rejected before execution.

**The concrete grid threat it counters:** A malicious actor pushes a firmware image to a fleet of substation K3s nodes that disables protection relays or exfiltrates PMU data. Without code signing, any image that arrives via the update channel is applied. With signing, the attacker must compromise the signing key itself — not just the update distribution channel — and the edge node refuses any image that does not pass that check.

**Interview sentence:** *"OTA signing means an attacker must compromise the signing key, not just the update channel — the edge node rejects any image that doesn't pass signature verification before execution."*

**→ Bridge to your work:** Juan has shipped OTA updates (CV). The upgrade is to add a signing step in the build pipeline and a signature-check at the node — the same deployment mechanism, now with a grid-safety guarantee.

---

## 3. TPM Attestation (Awareness)

**What it is:** A Trusted Platform Module (TPM 2.0) is a dedicated hardware security chip on the edge device. During boot, each firmware and software stage measures the next stage and records the measurement in Platform Configuration Registers (PCRs) — a tamper-resistant running hash of everything that executed since power-on. Remote attestation lets a remote verifier (a fog aggregator or SPIRE server) challenge the device: it must return its current PCR values signed by its TPM endorsement key. If those PCR values match the known-good hash for unmodified, trusted software, the node is admitted to the federated learning round.

**The concrete grid threat it counters:** A relay, protection IED, or K3s edge node that has been physically tampered with or whose OS has been compromised requests to join the federated aggregation. Without TPM attestation, the aggregator cannot distinguish a clean node from a rooted one and accepts its gradient updates. With attestation, the node must prove its boot-chain hash matches the known-good configuration before any update is accepted — a hardware root-of-trust, not a password.

**Interview sentence:** *"TPM attestation proves a relay is running unmodified trusted code before it joins the control loop — a hardware root-of-trust, not a password."*

**→ Bridge to your work:** Juan runs K8s and edge device fleets. The upgrade is TPM-attested node admission so only verified-clean nodes join the federated aggregation.

*(Awareness only — PCR indices, the quote protocol, and attestation flow internals are not needed for this criterion.)*

---

## 4. SPIFFE / SPIRE Workload Identity (Awareness)

**What it is:** SPIFFE (Secure Production Identity Framework for Everyone) is a CNCF-graduated standard for cryptographic workload identity — each running process (a K3s pod, a NATS subscriber, a FastAPI service) gets a short-lived X.509 certificate whose Subject Alternative Name URI encodes a SPIFFE ID (`spiffe://trust-domain/path`). SPIRE is the production implementation: a SPIRE server issues SVIDs (SPIFFE Verifiable Identity Documents); SPIRE agents run on each node and attest the node's identity (optionally via TPM) before issuing credentials to local workloads. SVIDs are short-lived — minutes to hours — and auto-rotate, eliminating static shared secrets.

**Not just TLS:** TLS encrypts the channel between two endpoints. SPIFFE identifies *which specific workload* is on each end — and rotates that identity automatically. A stolen long-lived API key breaks TLS-level trust; a stolen SVID expires in minutes and cannot be renewed without re-attestation.

**The concrete grid threat it counters:** An attacker who has compromised a device on the NATS network (or intercepted a long-lived API key) tries to impersonate a real substation's EKF service and inject false state estimates into the federated aggregation. Without workload identity, the aggregator cannot distinguish the real substation-7 EKF pod from a spoofed one with the same IP address or stolen credential. With SPIFFE/SPIRE, the legitimate pod holds a short-lived SVID the attacker cannot forge without compromising the SPIRE server itself; the spoofed connection is rejected at the mTLS handshake.

**Interview sentence:** *"SPIFFE gives each workload a short-lived, auto-rotating cryptographic identity so a spoofed node can't impersonate a real IED — identity, not just an encrypted channel."*

**→ Bridge to your work:** Juan runs an MQTT device fleet with K8s identity. The upgrade path is SPIFFE/SPIRE workload identity replacing static keys — same fleet infrastructure, no more long-lived secrets.

---

## <3-min say-aloud version

> "When I talk about edge security for a K3s substation fleet, I mean three things on top of TLS. First, **OTA signing**: the build pipeline signs every firmware image with a key held in an HSM, and the edge node refuses to apply any image that doesn't pass signature verification — so an attacker has to own the signing key, not just the update channel. Second, **TPM attestation**: the TPM chip measures every boot stage into tamper-resistant registers, and before a node joins the federated aggregation the aggregator challenges it to prove those measurements match known-good values — a hardware root-of-trust, not a password, which stops a rooted relay from quietly poisoning the control loop. Third, **SPIFFE/SPIRE workload identity**: each K3s pod gets a short-lived X.509 SVID with a process identity URI that auto-rotates every few minutes, so a spoofed node can't impersonate a real IED by presenting a stolen static key — the stolen SVID expires before the attacker can use it. TLS encrypts the wire; these three mechanisms answer whether the node on the other end of that wire should be trusted at all. Edge security is about trusting the node, not just encrypting the wire."

---

## → Bridge to your work

> **"Juan has shipped OTA updates and run MQTT device fleets on K8s. The deltas are clear and concrete: add image signing in the pipeline (OTA integrity), add TPM-attested node admission to the aggregator (hardware root-of-trust), and replace static keys with SPIFFE/SPIRE short-lived SVIDs (workload identity). These are upgrades he can describe precisely and implement — honestly framed as next steps, not already built."**

---

## Quick-Recall Card (Recite Before the Interview)

- **OTA integrity:** Signed firmware image; attacker must own the HSM signing key, not just the update channel — stops a malicious firmware push bricking or weaponizing a substation fleet.
- **TPM attestation:** Boot-chain PCR hash proves every stage ran unmodified trusted code; aggregator challenges the device before admitting it to the FL round — stops a rooted relay joining the control loop.
- **SPIFFE/SPIRE:** Short-lived auto-rotating workload SVID encodes a process identity URI; stolen static credentials expire in minutes — stops a spoofed node impersonating a real IED at the mTLS handshake.
- **The key distinction:** TLS encrypts the wire; OTA/TPM/SPIFFE answer "should this node be trusted at all?" They stack, not substitute.

---

*Sources: IETF RFC 9683 (TPM remote attestation); CNCF SPIFFE/SPIRE (graduated project); Promwad/DeviceAuthority (OTA signing pipeline); CV (OTA updates shipped, MQTT/K8s fleet)*
