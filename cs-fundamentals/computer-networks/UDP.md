# The UDP Service Model
## The UDP Datagram Format
```
0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|             Length            |            Checksum           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
|                        Data (Payload)                         |
|                    (variable length)                          |
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```
## Properties
- Connectionless: no established connection and data may show in any order
- Unreliable delivery
  - No acknowledgement
  - No mechanism to detect missing datagrams
  - No flow control

<!-- related:start -->
## 相关笔记

- [计算机网络索引](%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C%E7%B4%A2%E5%BC%95.md)
- [1-The4LayerModel](1-The4LayerModel.md)
- [TCP](TCP.md)
<!-- related:end -->
