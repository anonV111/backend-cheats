## Optimization

-   ### Profiling

    [Profiling](<https://en.wikipedia.org/wiki/Profiling_(computer_programming)>) is a program performance analysis, which reveals bottlenecks where the highest CPU and/or memory load occurs.

    -   What is it for?
        > The information obtained after profiling can be very useful for performance optimization. Profiling can also be useful for debugging the program to find bugs and errors.
    -   When should this be done?
        > As needed - when there are obvious problems or suspicions.
    -   What specific tools are there for this?
        > For Python, use: [cProfile](https://docs.python.org/3/library/profile.html), [line_profiler](https://github.com/pyutils/line_profiler). <br>
        > For Node.js: [built-in Profiler](https://nodejs.org/en/docs/guides/simple-profiling/), [Clinic.js](https://github.com/clinicjs/node-clinic), [Trace events module](https://nodejs.org/api/tracing.html). <br>
        > For Go: [runtime/pprof](https://go.dev/blog/pprof), [trace utility](https://go.dev/doc/diagnostics#tracing).

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Optimize Your Python Programs: Code Profiling with cProfile** – YouTube](https://youtu.be/BZzb_Wpag_M)
2. 📺 [**A New Way to Profile Node.js** – YouTube](https://youtu.be/ASv8188AkVk)
3. 📺 [**Go (Golang) Profiling Tutorial** – YouTube](https://youtu.be/HEwSkhr_8_M)
4. 📄 [**Awesome utilities for performance profiling** – GitHub](https://github.com/msaroufim/awesome-profiling)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Benchmarks

    [Benchmark](<https://en.wikipedia.org/wiki/Benchmark_(computing)>) (in software) is a tool for measuring the execution time of program code. As a rule, the measurement is done by multiple runs of the same code (or a certain part of it), where the average time is then calculated, and can also provide information about the number of operations performed and the amount of memory allocated.

    -   What is it for?
        > Benchmarks are useful for both evaluating performance and choosing the most effective solution to the problem at hand.
    -   What specific tools are there for this?
        > For Python: [timeit](https://docs.python.org/3/library/timeit.html), [pytest-benchmark](https://github.com/ionelmc/pytest-benchmark). <br>
        > For Node.js: [console.time](https://nodejs.org/api/console.html#consoletimelabel), [Artillery](https://github.com/artilleryio/artillery). <br>
        > For Go: [testing.B](https://pkg.go.dev/testing#hdr-Benchmarks), [Benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat).

    There are benchmarks to measure the performance of networked applications, where you can get detailed information about the average request processing time, the maximum number of supported connections, data transfer rates and so on ([see list of HTTP benchmarks](https://github.com/denji/awesome-http-benchmark)).

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Premature Optimization** – YouTube](https://youtu.be/tKbV6BpH-C8)
2. 📺 [**Professional Benchmarking in Python** – YouTube](https://youtu.be/DBoobQxqiQw)
3. 📺 [**JavaScript tips — Measuring performance using console.time** – YouTube](https://youtu.be/WumrqNOO8dk)
4. 📺 [**Go (Golang) Benchmark Tutorial** – YouTube](https://youtu.be/L-BkH-_lXpk)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Caching

    [Caching](https://aws.amazon.com/caching) is one of the most effective solutions for optimizing the performance of web applications. With caching, you can reuse previously received resources (static files), thereby reducing latency, reducing network traffic, and reducing the time it takes to fully load content.

    <p align="center"><img src="./files/optimization/cdn_eng.png" alt="CDN"/></p>

    -   [CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network)
        > A system of servers located around the world. Such servers allow you to store duplicate static content and deliver it much faster to users who are in close geographical proximity. Also when using CDN reduces the load on the main server.
    -   Browser-based (client-side) caching
        > Based on loading pages and other static data from the local cache. To do this, the browser (client) is given special headers: [304 Not Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/304), [Expires](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expires), [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security).
    -   [Memcached](https://en.wikipedia.org/wiki/Memcached)
        > A daemon program that implements high-performance RAM caching based on _key-value_ pairs. Unlike [Redis](#redis) it cannot be a reliable and long-term storage, so it is only suitable for caches.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**How Caching Works? | Why is Caching Important?** – YouTube](https://youtu.be/ASP7O5fDpSg)
2. 📺 [**Basic Caching Techniques Explained** – YouTube](https://youtu.be/ccemOqDrc2I)
3. 📺 [**HTTP Caching with E-Tags - (Explained by Example)** – YouTube](https://youtu.be/TgZnpp5wJWU)
4. 📺 [**What Is A CDN? How Does It Work?** – YouTube](https://youtu.be/RI9np1LWzqw)
5. 📺 [**Everything you need to know about HTTP Caching** – YouTube](https://youtu.be/HiBDZgTNpXY)
6. 📺 [**Memcached Architecture - Crash Course with Docker, Telnet, Node.js** – YouTube](https://youtu.be/NCePGsRZFus)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Load balancing

    <p align="center"><img src="./files/optimization/load-balancer_eng.png" alt="CDN"/></p>

    When the entire application code is maximally optimized and the server capacity is reaching its limits, and the load keeps growing, you have to resort to the [clustering](https://en.wikipedia.org/wiki/Computer_cluster) and [balancing](https://en.wikipedia.org/wiki/Load_balancing_(computing)) mechanisms. The idea is to combine groups of servers into clusters, where the load is distributed between them using special methods and algorithms, called balancing.

    -   Balancing at the network level
        > -   **DNS Balancing**. For one domain name is allocated several IP-addresses and the server to which the request will be redirected is determined by an algorithm [Round Robin](https://en.wikipedia.org/wiki/Round-robin_DNS).
        > -   **Building a [NLB cluster](https://learn.microsoft.com/en-us/windows-server/networking/technologies/network-load-balancing)**. Used to manage two or more servers as one virtual cluster.
        > -   **Balancing by territory**. An example is the [Anycast mailing method](https://en.wikipedia.org/wiki/Anycast).
    -   Balancing on the transport level
        > Communication with the client is locked to the balancer, which acts as a proxy. It communicates with servers on its own behalf, passing information about the client in additional data and headers. Example – [HAProxy](https://en.wikipedia.org/wiki/HAProxy).
    -   Balancing at the application level
        > The balancer analyzes client requests and redirects them to different servers depending on the nature of the requested content. Examples are [Upstream module in Nginx](https://nginx.org/en/docs/http/ngx_http_upstream_module.html) (which is responsible for balancing) and [pgpool](https://www.pgpool.net/mediawiki/index.php/Main_Page) from the PostgreSQL database (for example, it can be used to distribute read requests to one server and write requests to another).
    -   Balancing algorithms
        > -   [**Round Robin**](https://en.wikipedia.org/wiki/Round-robin_scheduling). Each request is sent in turn to each server (first to the first, then to the second and so on in a circle).
        > -   [**Weighted Round Robin**](https://en.wikipedia.org/wiki/Weighted_round_robin). Improved algorithm Round Robin, which also takes into account the performance of the server.
        > -   **Least Connections**. Each subsequent request is sent to the server with the smallest number of supported connections.
        > -   **Destination Hash Scheduling**. The server that processes the request is selected from a static table based on the recipient's IP address.
        > -   **Source Hash Scheduling**. The server that will process the request is selected from the table by the sender's IP address.
        > -   [**Sticky Sessions**](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/sticky-sessions.html). Requests are distributed based on the user's IP address. Sticky Sessions assumes that requests from the same client will be routed to the same server rather than bouncing around in a pool.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**What is a Load Balancer?** – YouTube](https://youtu.be/sCR3SAVdyCc)
2. 📺 [**Learn Load Balancing right now** – YouTube](https://youtu.be/LlbTSfc4biw)
3. 📺 [**Load Balancing with NGINX** – YouTube](https://youtu.be/a41jxGP9Ic8)
4. 📺 [**Load Balancers id depth** – YouTube](https://youtu.be/galcDRNd5Ow)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

