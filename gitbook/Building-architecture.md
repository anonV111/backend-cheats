## Building architecture

-   ### Architectural patterns

    -   [Layered](https://ducmanhphan.github.io/2020-02-20-Layered-architecture-pattern/)
        > Used to structure programs that can be decomposed into groups of subtasks, each of which is at a particular level of abstraction. Each layer provides services to the next higher layer.
    -   [Client-server](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
        > The server component will provide services to multiple client components. Clients request services from the server and the server provides relevant services to those clients.
    -   [Master-slave](<https://en.wikipedia.org/wiki/Master/slave_(technology)>)
        > The master component distributes the work among identical slave components, and computes a final result from the results which the slaves return.
    -   [Pipe-filter](https://learn.microsoft.com/en-us/azure/architecture/patterns/pipes-and-filters)
        > Each processing step is enclosed within a filter component. Data to be processed is passed through pipes. These pipes can be used for buffering or for synchronization purposes.
    -   [Broker pattern](https://en.wikipedia.org/wiki/Broker_pattern)
        > A broker component is responsible for the coordination of communication among components.
    -   [Peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer)
        > Peers may function both as a client, requesting services from other peers, and as a server, providing services to other peers. A peer may act as a client or as a server or as both, and it can change its role dynamically with time.
    -   [Event-bus](https://medium.com/elixirlabs/event-bus-implementation-s-d2854a9fafd5)
        > Has 4 major components; event source, event listener, channel and event bus. Sources publish messages to particular channels on an event bus.
    -   [Model-view-controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
        > Separate internal representations of information from the ways information is presented to, and accepted from, the user.
    -   [Blackboard](<https://en.wikipedia.org/wiki/Blackboard_(design_pattern)>)
        > Useful for problems for which no deterministic solution strategies are known.
    -   [Interpreter](https://en.wikipedia.org/wiki/Interpreter_pattern)
        > Used for designing a component that interprets programs written in a dedicated language.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**10 Common Software Architectural Patterns in a nutshell**](https://towardsdatascience.com/10-common-software-architectural-patterns-in-a-nutshell-a0b47a1e9013)
2. 📺 [**10 Architecture Patterns Used In Enterprise** – YouTube](https://youtu.be/BrT3AO8bVQY)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Design patterns

    -   Creational Patterns
        > Provide various object creation mechanisms, which increase flexibility and reuse of existing code.
        -   [Factory](https://refactoring.guru/design-patterns/factory-method)
        -   [Abstract factory](https://refactoring.guru/design-patterns/abstract-factory)
        -   [Builder](https://refactoring.guru/design-patterns/builder)
        -   [Prototype](https://refactoring.guru/design-patterns/prototype)
        -   [Singleton](https://refactoring.guru/design-patterns/singleton)
    -   Structural Patterns
        > Explain how to assemble objects and classes into larger structures, while keeping these structures flexible and efficient.
        -   [Adapter](https://refactoring.guru/design-patterns/adapter)
        -   [Bridge](https://refactoring.guru/design-patterns/bridge)
        -   [Composite](https://refactoring.guru/design-patterns/composite)
        -   [Decorator](https://refactoring.guru/design-patterns/decorator)
        -   [Facade](https://refactoring.guru/design-patterns/facade)
        -   [Flyweight](https://refactoring.guru/design-patterns/flyweight)
        -   [Proxy](https://refactoring.guru/design-patterns/proxy)
    -   Behavioral Patterns
        > Concerned with algorithms and the assignment of responsibilities between objects.
        -   [Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility)
        -   [Command](https://refactoring.guru/design-patterns/command)
        -   [Iterator](https://refactoring.guru/design-patterns/iterator)
        -   [Mediator](https://refactoring.guru/design-patterns/mediator)
        -   [Memento](https://refactoring.guru/design-patterns/memento)
        -   [Observer](https://refactoring.guru/design-patterns/observer)
        -   [State](https://refactoring.guru/design-patterns/state)
        -   [Strategy](https://refactoring.guru/design-patterns/strategy)
        -   [Template](https://refactoring.guru/design-patterns/template-method)
        -   [Visitor](https://refactoring.guru/design-patterns/visitor)

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Design Patterns Cheat Sheet**](http://www.lug.or.kr/files/cheat_sheet/design_pattern_cheatsheet_v1.pdf)
2. 📄 [**Free book on design patterns for building powerful web apps**](https://www.patterns.dev/)
3. 📺 [**10 Design Patterns Explained in 10 Minutes** – YouTube](https://youtu.be/tv-_1er1mWI)
4. 📺 [**Design Patterns with examples in Python** – YouTube](https://youtu.be/tAuRQs_d9F8)
5. 📺 [**Design Patterns with examples in JavaScript** – YouTube](https://youtube.com/playlist?list=PLFKDYTlP3abzwWleHq1WHcKyi8nCPY74s)
6. 📺 [**Design Patterns with examples in Go** – YouTube](https://youtube.com/playlist?list=PLfyLecA5DLOcUXmgk3BLDgWQvBoHbea2m)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Monolithic and microservice architecture

    <p align="center"><img src="./files/building-architecture/monolith-microservices_eng.png" alt="Monolith and microservices"/></p>

    A monolith is a complete application that contains a single code base (written in a single technology stack and stored in a single repository) and has a single entry point to run the entire application. This is the most common approach for building applications alone or with a small team.

    -   Advantages:
        > -   Ease of development (everything in one style and in one place). <br>
        > -   Ease of deployment. <br>
        > -   Easy to scale at the start.
    -   Disadvantages:
        > -   Increasing complexity (as the project grows, the entry threshold for new developers increases). <br>
        > -   Time to assemble and start up is growing. <br>
        > -   Making it harder to add new functionality that affects old functionality. <br>
        > -   It is difficult (or impossible) to apply new technologies.

    A microservice is also a complete application with a single code base. But, unlike a monolith, such an application is responsible for only one functional unit. That is, it is a small service that solves only one task, but well.

    -   Advantages:
        > -   Each individual microservice can have its own technology stack and be developed independently. <br>
        > -   Easy to add new functionality (just create a new microservice). <br>
        > -   A lower entry threshold for new developers. <br>
        > -   Low time required for buildings and startups.
    -   Disadvantages:
        > -   The complexity of implementing interaction between all microservices. <br>
        > -   More difficult to operate than several copies of the monolith. <br>
        > -   Complexity of performing transactions. <br>
        > -   Changes affecting multiple microservices must be coordinated.

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

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Horizontal and vertical scaling

    <p align="center"><img src="./files/building-architecture/horizontal-vertical-scaling_eng.png" alt="Horizontal and vertical scaling"/></p>

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

<div align="right"><a href="#top">Contents ⬆️</a></div>

