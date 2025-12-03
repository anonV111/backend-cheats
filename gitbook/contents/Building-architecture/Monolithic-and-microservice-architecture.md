### Monolithic and microservice architecture

<p align="center"><img src="../../../original/files/building-architecture/monolith-microservices_eng.png" alt="Monolith and microservices"/></p>

A monolith is a complete application that contains a single code base (written in a single technology stack and stored in a single repository) and has a single entry point to run the entire application. This is the most common approach for building applications alone or with a small team.

- Advantages:
  
  > - Ease of development (everything in one style and in one place). <br>
  > - Ease of deployment. <br>
  > - Easy to scale at the start.

- Disadvantages:
  
  > - Increasing complexity (as the project grows, the entry threshold for new developers increases). <br>
  > - Time to assemble and start up is growing. <br>
  > - Making it harder to add new functionality that affects old functionality. <br>
  > - It is difficult (or impossible) to apply new technologies.

A microservice is also a complete application with a single code base. But, unlike a monolith, such an application is responsible for only one functional unit. That is, it is a small service that solves only one task, but well.

- Advantages:
  
  > - Each individual microservice can have its own technology stack and be developed independently. <br>
  > - Easy to add new functionality (just create a new microservice). <br>
  > - A lower entry threshold for new developers. <br>
  > - Low time required for buildings and startups.

- Disadvantages:
  
  > - The complexity of implementing interaction between all microservices. <br>
  > - More difficult to operate than several copies of the monolith. <br>
  > - Complexity of performing transactions. <br>
  > - Changes affecting multiple microservices must be coordinated.

<details>
<summary>🔗 <b>References</b></summary>

1. 📺 [**What are Microservices?** – YouTube](https://youtu.be/CdBtNQZH8a4)

2. 📺 [**Microservices Explained and their Pros & Cons** – YouTube](https://youtu.be/T-m7ZFxeg1A)

3. 📺 [**Microservice Architecture and System Design with Python & Kubernetes – Full Course** – YouTube](https://youtu.be/hmkF77F9TLw)

4. 📺 [**Node.js Microservices Full Course - Event-Driven Architecture with RabbitMQ** – YouTube](https://youtu.be/Zc2mQSQXoS4)

5. 📺 [**Building Microservices in Go (playlist)** – YouTube](https://youtube.com/playlist?list=PL7yAAGMOat_Fn8sAXIk0WyBfK_sT1pohu)

6. 📄 [**Awesome Microservices: collection of principles and technologies** – GitHub](https://github.com/mfornos/awesome-microservices)

7. 📄 [**Patterns for Microservices**](https://microservices.io/patterns/index.html)
   
   </details>
