### OSI network model

| №   | Level              | Used protocols       |
| --- | ------------------ | -------------------- |
| 7   | Application layer  | HTTP, DNS, FTP, POP3 |
| 6   | Presentation layer | SSL, SSH, IMAP, JPEG |
| 5   | Session layer      | APIs Sockets         |
| 4   | Transport layer    | TCP, UDP             |
| 3   | Network layer      | IP, ICMP, IGMP       |
| 2   | Data link layer    | Ethernet, MAC, HDLC  |
| 1   | Physical layer     | RS-232, RJ45, DSL    |

[OSI (The Open Systems Interconnection model)](https://en.wikipedia.org/wiki/OSI_model) is a set of rules describing how different devices should interact with each other on the network. The model is divided into 7 layers, each of which is responsible for a specific function. All this is to ensure that the process of information exchange in the network follows the same pattern and all devices, whether it is a smart fridge or a smartphone, can understand each other without any problems.

-   [Physical layer](https://en.wikipedia.org/wiki/Physical_layer)
    > At this level, bits (ones/zeros) are encoded into physical signals (current, light, radio waves) and transmitted further by wire ([Ethernet](https://en.wikipedia.org/wiki/Ethernet)) or wirelessly ([Wi-Fi](https://en.wikipedia.org/wiki/Wi-Fi)).
-   [Data link layer](https://en.wikipedia.org/wiki/Data_link_layer)
    > Physical signals from layer 1 are decoded back into ones and zeros, errors and defects are corrected, and the sender and receiver [MAC addresses](https://en.wikipedia.org/wiki/MAC_address) are extracted.
-   [Network layer](https://en.wikipedia.org/wiki/Network_layer)
    > This is where traffic routing, DNS queries and [IP packet](https://en.wikipedia.org/wiki/Internet_Protocol) generation take place.
-   [Transport layer](https://en.wikipedia.org/wiki/Transport_layer)
    > The layer responsible for data transfer. There are two important protocols: <br>
    >
    > -   [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) is a protocol that ensures reliable data transmission. TCP guarantees data delivery and preserves the order of the messages. This has an impact on the transmission speed. This protocol is used where data loss is unacceptable, such as when sending mail or loading web pages. <br>
    > -   [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol) is a simple protocol with fast data transfer. It does not use mechanisms to guarantee the delivery and ordering of data. It is used e.g., in online games where partial packet loss is not crucial, but the speed of data transfer is much more important. Also, requests to DNS servers are made through UDP protocol.
-   [Session layer](https://en.wikipedia.org/wiki/Session_layer)
    > Responsible for opening and closing communications (sessions) between two devices. Ensures that the session stays open long enough to transfer all necessary data, and then closes quickly to avoid wasting resources.
-   [Presentation layer](https://en.wikipedia.org/wiki/Presentation_layer)
    > Transmission, encryption/decryption and data compression. This is where data that comes in the form of zeros and ones are converted into desired formats (PNG, MP3, PDF, etc.)
-   [Application layer](https://en.wikipedia.org/wiki/Application_layer)
    > Allows the user's applications to access network services such as database query handler, file access, email forwarding.

<details>
<summary>🔗 <b>References</b></summary>

1. 📄 [**Layers of OSI Model** – geeksForGeeks](https://www.geeksforgeeks.org/layers-of-osi-model/)
2. 📺 [**The OSI Model - Explained by Example** – YouTube](https://youtu.be/7IS7gigunyI)
3. 📺 [**TCP vs. UDP Crash Course** – YouTube](https://youtu.be/qqRYkcta6IE)
 </details>


