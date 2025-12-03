### Load balancing

<p align="center"><img src="../../../original/files/optimization/load-balancer_eng.png" alt="CDN"/></p>

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



