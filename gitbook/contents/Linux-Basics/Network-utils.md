### Network utils

For Linux there are many built-in and third-party utilities to help you configure your network, analyze it and fix possible problems.

-   Simple utils
    ```bash
    ip address # show info about IPv4 and IPv6 addresses of your devices
    ip monitor # real time monitor the state of devices
    ifconfig # config the network adapter and IP protocol settings
    traceroute <host> # show the route taken by packets to reach the host
    tracepath <host> # traces the network host to destination discovering MTU
    ping <host> # check connectivity to host
    ss -at # show the list of all listening TCP connections
    dig <host> # show info about the DNS name server
    host <host | ip-address> # show the IP address of a specified domain
    mtr <host | ip-address> # combination of ping and traceroute utilities
    nslookup # query Internet name servers interactively
    whois <host> # show info about domain registration
    ifplugstatus # detect the link status of a local Linux ethernet device
    iftop # show bandwidth usage
    ethtool <device name> # show detalis about your ethernet device
    nmap # tool to explore and audit network security
    bmon # bandwidth monitor and rate estimator
    firewalld # add, configure and remove rules on firewall
    ipref # perform network performance measurement and tuning
    speedtest-cli # check your network download/upload speed
    wget <link> # download files from the Internet
    ```
-   [`tcpdump`](https://en.wikipedia.org/wiki/Tcpdump)
    > A console utility that allows you to intercept and analyze all network traffic passing through your computer.
-   [`netcat`](https://en.wikipedia.org/wiki/Netcat)
    > Utility for reading from and writing to network connections using TCP or UDP. It includes port scanning, transferring files, and port listening: as with any server, it can be used as a [backdoor](<https://en.wikipedia.org/wiki/Backdoor_(computing)>).
-   [`iptables`](https://en.wikipedia.org/wiki/Iptables)
    > User-space utility program that allows to configure the IP packet filter rules of the Linux kernel firewall, implemented as different Netfilter modules. The filters are organized in different tables, which contain chains of rules for how to treat network traffic packets.
-   [`curl`](https://en.wikipedia.org/wiki/CURL)
    > Command-line tool for transferring data using various network protocols.

<details>
<summary>🔗 <b>References</b></summary>

1. 📄 [**21 Basic Linux Networking Commands You Should Know**](https://itsfoss.com/basic-linux-networking-commands/)
2. 📄 [**Using tcpdump Command on Linux to Analyze Network**](https://linuxhandbook.com/tcpdump-command/)
3. 📺 [**tcpdump - Traffic Capture & Analysis** – YouTube](https://youtu.be/1lDfCRM6dWk)
4. 📺 [**tcpdumping Node.js server** – YouTube](https://youtu.be/g_tmQ5G-T2w)
5. 📄 [**Beginner’s guide to Netcat for hackers**](https://medium.com/@HackTheBridge/beginners-guide-to-netcat-for-hackers-55abe449991d)
6. 📄 [**Iptables Tutorial**](https://linuxhint.com/iptables-tutorial/)
7. 📄 [**An intro to cURL: The basics of the transfer tool**](https://blog.logrocket.com/an-intro-to-curl-the-basics-of-the-transfer-tool/)
8. 📺 [**Basic cURL Tutorial** – YouTube](https://youtu.be/7XUibDYw4mc)
9. 📺 [**Using cURL better - tutorial by cURL creator Daniel Stenberg** – YouTube](https://youtu.be/I6id1Y0YuNk)
10. 📄 [**Awesome console services** – GitHub](https://github.com/chubin/awesome-console-services)
</details>


