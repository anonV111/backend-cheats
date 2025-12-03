### HTTP Protocol

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


