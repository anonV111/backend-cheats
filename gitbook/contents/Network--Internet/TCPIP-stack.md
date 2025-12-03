### TCP/IP stack

<p align="center"><img src="../../../original/files/network-internet/tcp-ip_eng.png" alt="TCP/IP"/></p>

Compared to the [OSI model](#osi-network-model), the [TCP/IP](https://en.wikipedia.org/wiki/Internet_protocol_suite) stack has a simpler architecture. In general, the TCP/IP model is more widely used and practical, and the OSI model is more theoretical and detailed. Both models describe the same principles, but differ in the approach and protocols they include at their levels.

- [Link layer](https://en.wikipedia.org/wiki/Link_layer)
    > Defines how data is transmitted over the physical medium, such as cables or wireless signals. <br>
    > Protocols: [Ethernet](https://en.wikipedia.org/wiki/Ethernet), [Wi-Fi](https://en.wikipedia.org/wiki/Wi-Fi), [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth), [Fiber optic](https://en.wikipedia.org/wiki/Optical_fiber).
- [Internet Layer](https://en.wikipedia.org/wiki/Internet_layer)
    > Routing data across different networks. It uses IP addresses to identify devices and routes data packets to their destination. <br>
    > Protocols: [IP](https://en.wikipedia.org/wiki/Internet_Protocol), [ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol), [ICMP](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol), [IGMP](https://en.wikipedia.org/wiki/Internet_Group_Management_Protocol)
- [Transport Layer](https://en.wikipedia.org/wiki/Transport_layer)
    > Data transmission between two devices. It uses protocols such as [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) - reliable, but slow and [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol) - fast, but unreliable.
- [Application Layer](https://en.wikipedia.org/wiki/Application_layer)
    > Provides services to the end user, such as web browsing, email, and file transfer. It interacts with the lower layers of the stack to transmit data over the network. <br>
    > Protocols: [HTTP](#http-protocol), [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol), [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol), [DNS](https://en.wikipedia.org/wiki/Domain_Name_System), [SNMP](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol).

<details>
<summary>🔗 <b>References</b></summary>

1. 📄 [**What is the TCP/IP Model? Layers and Protocols Explained** – freeCodeCamp](https://www.freecodecamp.org/news/what-is-tcp-ip-layers-and-protocols-explained/)
2. 📺 [**What is TCP/IP?** – YouTube](https://youtu.be/PpsEaqJV_A0)
3. 📺 [**How TCP really works. Three-way handshake. TCP/IP Deep Dive** – YouTube](https://youtu.be/rmFX1V49K8U)
 </details>


