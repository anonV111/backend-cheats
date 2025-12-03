### Message brokers

<p align="center"><img src="./files/software/message-queue_eng.png" alt="Message queue"/></p>

When creating a large-scale backend system, the problem of communication between a large number of microservices may arise. In order not to complicate existing services (establish a reliable communication system, distribute the load, provide for various errors, etc.) you can use a separate service, which is called a [message broker](https://en.wikipedia.org/wiki/Message_broker) (or message queue).

The broker takes the responsibility of creating a reliable and fault-tolerant system of communication between services (performs balancing, guarantees delivery, monitors recipients, maintains logs, buffering, etc.)

A message is an ordinary HTTP request/response with data of a certain format.

-   [RabbitMQ](https://en.wikipedia.org/wiki/RabbitMQ) - specializes in message queuing and supports various messaging patterns, including publish/subscribe and point-to-point communication.
-   [Apache Kafka](https://en.wikipedia.org/wiki/Apache_Kafka) - excels in handling large-scale, real-time data streams and offers high throughput, fault tolerance, and horizontal scalability.
-   [NATS](https://nats.io/) - known for its simplicity, speed, and lightweight design, making it ideal for building fast and efficient distributed systems.

<details>
<summary>🔗 <b>References</b></summary>

1. 📺 [**What is a Message Queue and When should you use Messaging Queue Systems** – YouTube](https://youtu.be/W4_aGb_MOls)
2. 📺 [**What is a Message Queue?** – YouTube](https://youtu.be/xErwDaOc-Gs)
3. 📄 [**Understanding RabbitMQ** – medium](https://medium.com/swlh/understanding-rabbitmq-11d710e40a38)
4. 📺 [**RabbitMQ course (playlist)** – YouTube](https://youtube.com/playlist?list=PLrwNNiB6YOA3Z3JfOUMKE6PmnpmVAJgTK)
 </details>


