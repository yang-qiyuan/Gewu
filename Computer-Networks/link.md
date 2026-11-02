# Link Layer
## Statistical Multiplexing

- Multiple users **share** a link on demand instead of holding fixed bandwidth allocations
- Works because user traffic is **bursty** — peak demands rarely coincide simultaneously
- By the Law of Large Numbers, aggregate traffic is predictable, enabling **overselling** of bandwidth
- Trade-off: introduces **queuing delay and packet loss** (**no deterministic delay guarantee**)
- The Internet's **packet switching** is its direct implementation; contrasts with circuit switching

## Longest Prefix Match Algorithm for internet routers
Often multiple routing table entries match the destination IP address. LPM resolves the tie with a simple rule: use the most specific match, i.e., the entry whose prefix shares the longest common bit string with the destination.

**Example:**
![LPM](./imgs/LRM.png)

## Address Resolution Protocol
Maps an IP address to a MAC address within a local network.