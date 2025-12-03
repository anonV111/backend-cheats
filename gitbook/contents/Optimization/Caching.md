### Caching

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


