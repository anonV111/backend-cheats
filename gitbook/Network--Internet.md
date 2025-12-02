## Network & Internet

[Internet](https://en.wikipedia.org/wiki/Internet) is a worldwide system that connects computer networks from around the world into a single network for storing/transferring information. The Internet was originally developed for the military. But soon it began to be implemented in universities, and then it could be used by private companies, which began to organize networks of providers that provide Internet access services to ordinary citizens. By early 2020, the number of Internet users exceeded 4.5 billion.

-   ### How the Internet works

    <p align="center"><img src="./files/network-internet/Internet.png" alt="Internet"/></p>

    Your computer does not have direct access to the Internet. Instead, it has access to your local network to which other devices are connected via a wired ([Ethernet](https://en.wikipedia.org/wiki/Ethernet)) or wireless (Wi-Fi) connection. The organizer of such a network is a special minicomputer - [router](<https://en.wikipedia.org/wiki/Router_(computing)>). This device connects you to your [Internet Service Provider (ISP)](https://en.wikipedia.org/wiki/Internet_service_provider), which in turn is connected to other higher-level ISPs. Thus, all these interactions make up the Internet, and your messages always transit through different networks before reaching the final recipient.

    -   [Host](<https://en.wikipedia.org/wiki/Host_(network)>)
        > Any device that is on any network.
    -   [Server](<https://en.wikipedia.org/wiki/Server_(computing)>)
        > A special computer on the network that serves requests from other computers.

    <p align="center"><img src="./files/network-internet/topologies.png" alt="Network topologies"/></p>

    -   [Network topologies](https://en.wikipedia.org/wiki/Network_topology)
        > There are several topologies (ways of organizing a network): [Point to point](<https://en.wikipedia.org/wiki/Point-to-point_(telecommunications)>), [Daisy chain](<https://en.wikipedia.org/wiki/Daisy_chain_(electrical_engineering)>), [Bus](https://en.wikipedia.org/wiki/Bus_network), [Ring](https://en.wikipedia.org/wiki/Ring_network), [Star](https://en.wikipedia.org/wiki/Star_network) and [Mesh](https://en.wikipedia.org/wiki/Mesh_networking). The Internet itself cannot be referred to any one topology, because it is an incredibly complex system mixed with different topologies.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**How does the Internet work?** – MDN](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/How_does_the_Internet_work)
2. 📺 [**How does the internet work? (Full Course)** – YouTube](https://youtu.be/zN8YNNHcaZc)
3. 📺 [**What is a Server? Servers vs. Desktops Explained** – YouTube](https://youtu.be/UjCDWCeHCzY)
4. 📺 [**Network Topology** – YouTube](https://youtu.be/lnFeG4DOMcE)
5. 📺 [**Network Topologies (Star, Bus, Ring, Mesh, Ad hoc, Infrastructure, & Wireless Mesh Topology)** – YouTube](https://youtu.be/zbqrNg4C98U)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### What is a domain name

    <p align="center"><img src="./files/network-internet/domain_eng.png" alt="Domain name"/></p>

    [Domain Names](https://en.wikipedia.org/wiki/Domain_name) are human-readable addresses of web servers available on the Internet. They consist of parts (levels) separated from each other by a dot. Each of these parts provides specific information about the domain name. For example country, service name, localization, etc.

    -   Who owns domain names
        > [The ICANN Corporation](https://en.wikipedia.org/wiki/ICANN) is the founder of the distributed domain registration system. It gives accreditations to companies that want to sell domains. In this way a competitive domain market is formed.
    -   How to buy a domain name
        > A domain name cannot be bought forever. It is leased for a certain period of time. It is better to buy domains from [accredited registrars](https://www.icann.org/en/accredited-registrars?filter-letter=a&sort-direction=asc&sort-param=name&page=1) (you can find them in almost any country).

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**What is a Domain Name?** – MDN](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_domain_name)
2. 📺 [**A Beginners Guide to How Domain Names Work!** – YouTube](https://youtu.be/Y4cRx19nhJk)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### IP address

    <p align="center"><img src="./files/network-internet/IPv4-IPv6.png" alt="IPv4-IPv6"/></p>

    [IP address](https://en.wikipedia.org/wiki/IP_address) is a unique numeric address that is used to recognize a particular device on the network.

    -   Levels of visibility
        > -   External and publicly accessible IP address that belongs to your ISP and is used to access the Internet by hundreds of other users.
        > -   The IP address of your router in your ISP's local network, the same IP address from which you access the Internet.
        > -   The IP address of your computer in the local (home) network created by the router, to which you can connect your devices. Typically, it looks like 192.168.XXX.XXX.
        > -   The internal IP address of the computer, inaccessible from the outside and used only for communication between the running processes. It is the same for everyone - 127.0.0.1 or just _localhost_.
    -   [Port](<https://en.wikipedia.org/wiki/Port_(computer_networking)>)
        > One device (computer) can run many applications that use the network. In order to correctly recognize where and which data coming over the network should be delivered (to which of the applications) a special numerical number - a port is used. That is, each running process on a computer which uses a network connection has its own personal port.
    -   [IPv4](https://en.wikipedia.org/wiki/IPv4)
        > Version 4 of the IP protocol. It was developed in 1981 and limits the address space to about 4.3 billion (2^32) possible unique addresses.
    -   [IPv6](https://en.wikipedia.org/wiki/IPv6)
        > Over time, the allocation of address space began to happen at a much faster rate, forcing the creation of a new version of the IP protocol to store more addresses. IPv6 is capable of issuing 2^128 (is huge number) unique addresses.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**IP addresses. Explained** – YouTube](https://youtu.be/7_-qWlvQQtY)
2. 📺 [**Public IP vs. Private IP and Port Forwarding (Explained by Example)** – YouTube](https://youtu.be/92b-jjBURkw)
3. 📺 [**Network Ports Explained** – YouTube](https://youtu.be/g2fT-g9PX9o)
4. 📺 [**What is IP address and types of IP address - IPv4 and IPv6** – YouTube](https://youtu.be/8npT9AALbrI)
5. 📺 [**IP Address - IPv4 vs. IPv6 Tutorial** – YouTube](https://youtu.be/ThdO9beHhpA)
6. 📄 [**IP Address Subnet Cheat Sheet** – freeCodeCamp](https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### What is DNS

    <p align="center"><img src="./files/network-internet/dns.png" alt="DNS"/></p>

    [DNS (Domain Name System)](https://en.wikipedia.org/wiki/DNS) is a decentralized Internet address naming system that allows you to create human-readable alphabetical names (domain names) corresponding to the numeric [IP addresses](#ip-address) used by computers.

    -   Structure of DNS
        > DNS consists of many independent nodes, each of which stores only those data that fall within its area of responsibility.
    -   [DNS Resolver](https://www.computerhope.com/jargon/d/dns-resolver.htm)
        > A server that is located in close proximity to your Internet Service Provider. It is the server that searches for addresses by domain name, and also caches them (temporarily storing them for quick retrieval in future requests).
    -   [DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types)
        > -   A record - associates the domain name with an IPv4 address.
        > -   AAAA record - links a domain name with an IPv6 address.
        > -   CNAME record - redirects to another domain name.
        > -   and others - MX record, NS record, PTR record, SOA record.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**What is DNS? Domain Name System explained** – freeCodeCamp](https://www.freecodecamp.org/news/what-is-dns/)
2. 📺 [**DNS (Domain Name System) explained. Types of Domain Name Servers** – YouTube](https://youtu.be/JkEYOt08-rU)
3. 📺 [**DNS as Fast As Possible** – YouTube](https://youtu.be/Rck3BALhI5c)
4. 📄 [**All about DNS records** – Cloudflare](https://www.cloudflare.com/learning/dns/dns-records/)
5. 📺 [**DNS records explained (playlist)** – YouTube](https://youtube.com/playlist?list=PL_vyuxE-AO-DD94NKcCqd4iqwy5ah_pwq)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Web application design

    Modern [web applications](https://en.wikipedia.org/wiki/Web_application) consist of two parts: [Frontend and Backend](https://en.wikipedia.org/wiki/Frontend_and_backend). Thus implementing a [client-server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model).

    The tasks of the Frontend are:

    -   Implementation of the user interface (appearance of the application)
        > - A special markup language [HTML](https://en.wikipedia.org/wiki/HTML) is used to create web pages.
        > - [CSS](https://en.wikipedia.org/wiki/CSS) style language is used to style fonts, layout of content, etc.
        > - [JavaScript](https://en.wikipedia.org/wiki/JavaScript) programming language is used to add dynamics and interactivity. <br>
        > As a rule, these tools are rarely used in their pure form, as so-called [frameworks](https://2020.stateofjs.com/en-US/technologies/front-end-frameworks/) and [preprocessors](https://www.freecodecamp.org/news/css-preprocessors/) exist for more convenient and faster development. <br>
    -   Creating functionality for generating requests to the server
        > These are usually different types of input forms that can be conveniently interacted with.
    -   Receives data from the server and then processes it for output to the client

    Tasks of the Backend:

    -   Handling client requests
        > Checking for permissions and access, all sorts of validations, etc.
    -   Implementing business logic
        > A wide range of tasks can be implied here: working with databases, information processing, computation, etc. This is, so to speak, the heart of the Backend world. This is where all the important and interesting stuff happens.
    -   Generating a response and sending it to the client

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Front-End vs. Back-End explained**](https://blog.teamtreehouse.com/i-dont-speak-your-language-frontend-vs-backend)
2. 📺 [**Everything You NEED to Know About WEB APP Architecture** – YouTube](https://youtu.be/sDlCSIDwpDs)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Browsers and how they work

    <p align="center"><img src="./files/network-internet/browser_eng.png" alt="Browser"/></p>

    [Browser](https://en.wikipedia.org/wiki/Web_browser) is a client which can be used to send requests to a server for files which can then be used to render web pages. In simple terms, a browser can be thought of as a program for viewing HTML files, which can also search for and download them from the Internet.

    -   Working Principle
        > Query handling, page rendering, and the tabs feature (each tab has its own process to prevent the contents of one tab from affecting the contents of the other).
    -   [Extensions](https://developer.chrome.com/docs/extensions/)
        > Allow you to change the browser's user interface, modify the contents of web pages, and modify the browser's network requests.
    -   [Chrome DevTools](https://developer.chrome.com/docs/devtools/overview/)
        > An indispensable tool for any web developer. It allows you to analyze all possible information related to web pages, monitor their performance, logs and, most importantly for us, track information about network requests.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**How browsers work** – MDN](https://developer.mozilla.org/en-US/docs/Web/Performance/How_browsers_work)
2. 📄 [**How browsers work: Behind the scenes of modern web browsers** – web.dev](https://web.dev/howbrowserswork/)
3. 📄 [**Inside look at modern web browser** – Google](https://developer.chrome.com/blog/inside-browser-part1/)
4. 📺 [**What is a web browser?** – YouTube](https://youtu.be/QzohDuGk4mM)
5. 📺 [**Anatomy of the browser 101 (Chrome University 2019)** – YouTube](https://youtu.be/PzzNuCk-e0Y)
6. 📺 [**Chrome DevTools - Crash Course** – YouTube](https://youtu.be/gTVpBbFWry8)
7. 📺 [**Demystifying the Browser Networking Tab in DevTools** – YouTube](https://youtu.be/LBgfSwX4GDI)
8. 📺 [**21+ Browser Dev Tools & Tips You Need To Know** – YouTube](https://youtu.be/TcTSqhpm80Y)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### VPN and Proxy

    <p align="center"><img src="./files/network-internet/proxy-vpn_eng.png" alt="Proxy & VPN"/></p>

    The use of VPNs and Proxy is quite common in recent years. With the help of these technologies, users can get basic anonymity when surfing the web, as well as bypass various regional blockages.

    -   [VPN (Virtual Private Network)](https://en.wikipedia.org/wiki/VPN)
        > A technology that allows you to become a member of a private network (similar to your local network), where requests from all participants go through a single public IP address. This allows you to blend in with the general mass of requests from other participants. <br>
        >
        > -   Simple procedure for connection and use. <br>
        > -   Reliable traffic encryption. <br>
        > -   There is no guarantee of 100% anonymity, because the owner of the network knows the IP-addresses of all participants. <br>
        > -   VPNs are useless for dealing with multi-accounts and some programs because all accounts operating from the same VPN are easily detected and blocked. <br>
        > -   Free VPNs tend to be heavily loaded, resulting in unstable performance and slow download speeds. <br>
    -   [Proxy (proxy server)](https://en.wikipedia.org/wiki/Proxy_server)
        > A proxy is a special server on the network that acts as an intermediary between you and the destination server you intend to reach. When you are connected to a proxy server all your requests will be performed on behalf of that server, that is, your IP address and location will be substituted. <br>
        >
        > -   The ability to use an individual IP address, which allows you to work with multi-accounts. <br>
        > -   Stability of the connection due to the absence of high loads. <br>
        > -   Connection via proxy is provided in the operating system and browser, so no additional software is required. <br>
        > -   There are proxy varieties that provide a high level of anonymity. <br>
        > -   The unreliability of free solutions, because the proxy server can see and control everything you do on the Internet. <br>

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**What is VPN? How It Works, Types of VPN** – kaspersky.com](https://www.kaspersky.com/resource-center/definitions/what-is-a-vpn)
2. 📺 [**VPN (Virtual Private Network) Explained** – YouTube](https://youtu.be/R-JUOpCgTZc)
3. 📺 [**What Is a Proxy and How Does It Work?** – YouTube](https://youtu.be/ayo2EUPTEkE)
4. 📺 [**What is a Proxy Server?** – YouTube](https://youtu.be/5cPIukqXe5w)
5. 📺 [**Proxy vs. Reverse Proxy (Explained by Example)** – YouTube](https://youtu.be/ozhe__GdWC8)
6. 📺 [**VPN vs. Proxy Explained Pros and Cons** – YouTube](https://youtu.be/npnqyRT77Zc)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Hosting

    <p align="center"><img src="./files/network-internet/Hosting.png" alt="Hosting"/></p>

    [Hosting](https://en.wikipedia.org/wiki/Web_hosting_service) is a special [service provided](https://en.wikipedia.org/wiki/Internet_hosting_service) by hosting providers, which allows you to rent space on a server (which is connected to the Internet around the clock), where your data and files can be stored. There are different options for hosting, where you can use not only the disk space of the server, but also the CPU power to run your network applications.

    -   [Virtual hosting](https://en.wikipedia.org/wiki/Virtual_hosting)
        > One physical server that distributes its resources to multiple tenants.
    -   [VPS/VDS](https://en.wikipedia.org/wiki/Virtual_private_server)
        > Virtual servers that emulate the operation of a separate physical server and are available for rent to the client with maximum privileges.
    -   [Dedicated server](https://en.wikipedia.org/wiki/Dedicated_hosting_service)
        > Renting a full physical server with full access to all resources. As a rule, this is the most expensive service.
    -   [Cloud hosting](https://en.wikipedia.org/wiki/Cloud_storage)
        > A service that uses the resources of several servers. When renting, the user pays only for the actual resources used.
    -   [Colocation](https://en.wikipedia.org/wiki/Colocation_centre)
        > A service that gives the customer the opportunity to install their equipment on the provider's premises.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**What is Web Hosting?** – namecheap.com](https://www.namecheap.com/hosting/what-is-web-hosting-definition/)
2. 📺 [**What is Web Hosting and How Does It Work?** – YouTube](https://youtu.be/H8oAvyqQwew)
3. 📺 [**Different Hosting Types Explained** – YouTube](https://youtu.be/CtNWVmt9U1M)
4. 📄 [**Awesome Hosting** – GitHub](https://github.com/dalisoft/awesome-hosting)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### OSI network model

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

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### HTTP Protocol

    [HTTP (HyperText Transport Protocol)](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) is the most important protocol on the Internet. It is used to transfer data of any format. The protocol itself works according to a simple principle: request -> response.

    -   [Structure of HTTP messages](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages)
        > HTTP messages consist of a header section containing metadata about the message, followed by an optional message body containing the data being sent.

    <p align="center"><img src="./files/network-internet/http_eng.png" alt="HTTP"/></p>

    -   [Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
        > Additional service information that is sent with the request/response. <br>
        > Common headers: [Host](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host), [User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent), [If-Modified-Since](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Modified-Since), [Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie), [Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer), [Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization), [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control), [Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type), [Content-Length](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Length), [Last-Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Last-Modified), [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie), [Content-Encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding).
    -   [Request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
        > Main: [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET), [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST), [PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT), [DELETE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE). <br> Others: [HEAD](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD), [CONNECT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/CONNECT), [OPTIONS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS), [TRACE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/TRACE), [PATCH](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH).
    -   [Response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
        > Each response from the server has a special numeric code that characterizes the state of the sent request. These codes are divided into 5 main classes:
        > -   **1хх** - Service information
        > -   **2хх** - Successful request
        > -   **3хх** - Redirect to another address
        > -   **4хх** - Client side error
        > -   **5хх** - Server side error
    -   [HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/https)
        > Same HTTP, but with encryption support. Your apps should use HTTPS to be secure.
    -   [Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
        > The HTTP protocol does not provide the ability to save information about the status of previous requests and responses. Cookies are used to solve this problem. Cookies allow the server to store information on the client side that the client can send back to the server. For example, cookies can be used to authenticate users or to store various settings.
    -   [CORS (Cross origin resource sharing)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
        > A technology that allows one domain to securely receive data from another domain.
    -   [CSP (Content Security Policy)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
        > A special header that allows you to recognize and eliminate certain types of web application vulnerabilities.
    -   [Evolution of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Evolution_of_HTTP)
        > - **HTTP/1.0**: Uses separate connections for each request/response, lacks caching support, and has plain text headers.
        > - **HTTP/1.1**: Introduces persistent connections, pipelining, the Host header, and chunked transfer encoding.
        > - **HTTP/2**: Supports multiplexing, header compression, server push, and support a binary data.
        > - **HTTP/3**: Built on [QUIC](https://developer.mozilla.org/en-US/docs/Glossary/QUIC), offers improved multiplexing, reliability, and better performance over unreliable networks.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**How HTTP Works and Why it's Important** – freeCodeCamp](https://www.freecodecamp.org/news/how-the-internet-works/)
2. 📄 [**Hypertext Transfer Protocol (HTTP)** – MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP)
3. 📺 [**Hyper Text Transfer Protocol Crash Course** – YouTube](https://youtu.be/0OrmKCB0UrQ)
4. 📺 [**Full HTTP Networking Course (5 hours)** – YouTube](https://youtu.be/2JYT5f2isg4)
5. 📄 [**HTTP vs. HTTPS – What's the Difference?** – freeCodeCamp](https://www.freecodecamp.org/news/http-vs-https/)
6. 📺 [**HTTP Cookies Crash Course** – YouTube](https://youtu.be/sovAIX4doOE)
7. 📺 [**Cross Origin Resource Sharing (Explained by Example)** – YouTube](https://youtu.be/Ka8vG5miErk)
8. 📺 [**When to use HTTP GET vs. POST?** – YouTube](https://youtu.be/K8HJ6DN23zI)
9. 📺 [**How HTTP/2 Works, Performance, Pros & Cons and More** – YouTube](https://youtu.be/fVKPrDrEwTI)
10. 📺 [**HTTP/2 Critical Limitation that led to HTTP/3 & QUIC** – YouTube](https://youtu.be/GriONb4EfPY)
11. 📺 [**304 Not Modified HTTP Status (Explained with Code Example and Pros & Cons)** – YouTube](https://youtu.be/0QHmHR55_Lo)
12. 📺 [**What is the Largest POST Request the Server can Process?** – YouTube](https://youtu.be/0QHmHR55_Lo)
</details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### TCP/IP stack

    <p align="center"><img src="./files/network-internet/tcp-ip_eng.png" alt="TCP/IP"/></p>

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

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Network problems

    <p align="center"><img src="./files/network-internet/problems_eng.gif" alt="Problems"/></p>

    The quality of networks, including the Internet, is far from ideal. This is due to the complex structure of networks and their dependence on a huge number of factors. For example, the stability of the connection between the client device and its router, the quality of service of the provider, the power, and performance of the server, the physical distance between the client and the server, etc.

    -   [Latency](https://developer.mozilla.org/en-US/docs/Web/Performance/Understanding_latency)
        > The time it takes for a data packet to travel from sender to receiver. It depends more on the physical distance.
    -   [Packet loss](https://en.wikipedia.org/wiki/Packet_loss)
        > Not all packets traveling over the network can reach their destination. This happens most often when using wireless networks or due to [network congestion](https://en.wikipedia.org/wiki/Network_congestion).
    -   [Round Trip Time (RTT)](https://en.wikipedia.org/wiki/Round-trip_delay)
        > The time it takes for the data packet to reach its destination + the time to respond that the packet was received successfully.
    -   [Jitter](https://www.ir.com/guides/what-is-network-jitter)
        > Delay fluctuations, unstable ping (for example, 50ms, 120ms, 35ms...).
    -   [Packet reordering](https://wiki.geant.org/display/public/EK/PacketReordering)
        > The IP protocol does not guarantee that packets are delivered in the order in which they are sent.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Understanding latency** – MDN](https://developer.mozilla.org/en-US/docs/Web/Performance/Understanding_latency)
2. 📺 [**What is latency? What affects latency?** – YouTube](https://youtu.be/epAXDsq5SbE)
3. 📺 [**Basics of network bandwidth, latency, and jitter** – YouTube](https://youtu.be/WdbJdUh6W08)
4. 📺 [**Round Trip Time (RTT)** – YouTube](https://youtu.be/nT9F-USjtBg)
5. 📺 [**What Causes Packet Loss and How to Eliminate It In Your Network** – YouTube](https://youtu.be/Cg656nGbXe4)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Network diagnostics

    <p align="center"><img src="./files/network-internet/Traceroute.png" alt="Traceroute"/></p>

    -   [Traceroute](https://en.wikipedia.org/wiki/Traceroute)
        > A procedure that allows you to trace to which nodes, with which IP addresses, a packet you send before it reaches its destination. Tracing can be used to identify computer network related problems and to examine/analyze the network.
    -   [Ping scan](<https://en.wikipedia.org/wiki/Ping_(networking_utility)>)
        > The easiest way to check the server for performance.
    -   [Checking for packet loss](https://www.dnsstuff.com/packet-loss-test)
        > Due to dropped connections, not all packets sent over the network reach their destination.
    -   [Wireshark](https://en.wikipedia.org/wiki/Wireshark)
        > A powerful program with a graphical interface for analyzing all traffic that passes through the network in real time.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**How does traceroute work?** – YouTube](https://youtu.be/G05y9UKT69s)
2. 📺 [**Traceroute (tracert) Explained - Network Troubleshooting** – YouTube](https://youtu.be/up3bcBLZS74)
3. 📺 [**Nmap - Host Discovery With Ping Sweep** – YouTube](https://youtu.be/LvCDaftsMwI)
4. 📺 [**Internet Troubleshooting - Pathping Packet Loss** – YouTube](https://youtu.be/VPdotNIXOgI)
5. 📺 [**Wireshark crash course (playlist)** – YouTube](https://youtube.com/playlist?list=PLBf0hzazHTGPgyxeEj_9LBHiqjtNEjsgt)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

