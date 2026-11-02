# Error Detection
![ed](./imgs/ed.png)
## Checksum

Sums all data words using ones'-complement arithmetic and appends the result; the receiver re-computes and checks for consistency.

**Pros:** Simple to implement; low computational overhead.  
**Cons:** Weak protection — certain multi-bit error patterns cancel out and go undetected.

---

## CRC (Cyclic Redundancy Check)

Treats the data as a polynomial, divides by a generator polynomial, and appends the remainder (FCS) to the frame.

**Pros:** Detects all **single-bit errors** and most burst errors; widely standardized (CRC-32).  
**Cons:** Higher computational cost than checksum; cannot correct errors, only detect them.

---

## MAC (Message Authentication Code)

Applies a secret key and a hash function to a message to produce a cryptographic tag that travels with the data.

**Pros:** Detects both accidental corruption and **deliberate tampering**; provides sender authentication.  
**Cons:** Requires shared secret key management; higher overhead than CRC or checksum.

<!-- related:start -->
## 相关笔记

- [计算机网络索引](%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C%E7%B4%A2%E5%BC%95.md)
- [TCP](TCP.md)
- [link](link.md)
<!-- related:end -->
