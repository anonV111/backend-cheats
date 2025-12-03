### Horizontal and vertical scaling

<p align="center"><img src="../../../original/files/building-architecture/horizontal-vertical-scaling_eng.png" alt="Horizontal and vertical scaling"/></p>

Over time, when the load on your application starts to grow (more users come, new functionality appears and, as a consequence, more CPU time is involved), it becomes necessary to increase the server capacity. There are [2 main approaches](<https://en.wikipedia.org/wiki/Scalability#Horizontal_(scale_out)_and_vertical_scaling_(scale_up)>) for this:

-   Vertical scaling
    > It means increasing the capacity of the existing server. For example, this may include increasing the size of RAM, installing faster storage or increasing its volume, as well as the purchase of a new processor with a high clock frequency and/or a large number of cores and threads. Vertical scaling has its own limit, because we cannot increase the capacity of a single server for a long time.
-   Horizontal scaling
    > The process of deploying new servers. This approach requires building a robust and scalable architecture that allows you to distribute the logic of the entire application across multiple physical machines.

<details>
<summary>🔗 <b>References</b></summary>

1. 📺 [**System Design: What is Horizontal vs. Vertical Scaling?** – YouTube](https://youtu.be/p1YQU5sEz4g)
2. 📄 [**Vertical vs. Horizontal Scaling: Which one to choose**](https://middleware.io/blog/vertical-vs-horizontal-scaling/)
 </details>



