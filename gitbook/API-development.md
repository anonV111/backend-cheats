## API development

[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API) an interface which describes a certain set of rules by which different programs (applications, bots, websites...) can interact with each other. With API calls you can execute certain functions of a program without knowing how it works.

When developing server applications, [different API formats](https://youtu.be/4vLxWqE94l4) can be used, depending on the tasks and requirements.

-   ### REST API

    [REST (Representational State Transfer)](https://ru.wikipedia.org/wiki/REST) an architectural approach that describes a set of rules for how a programmer organizes the writing of server application code so that all systems can easily exchange data and the application can be easily scaled. When building a REST API, HTTP protocol methods are widely used.

    Basic rules for writing a good REST API:

    -   Using HTTP methods
        > As a rule, a single URL route is used to work on a particular data model (e.g., for users - `/api/user`). To perform different operations (get/create/edit/delete), this route must implement handlers for the corresponding HTTP methods (GET/POST/PUT/DELETE).
    -   Use of plural names
        > For example, a URL to retrieve one user by ID looks like this: `/user/42`, and to retrieve all users like this: `/users`.
    -   Sending the appropriate HTTP response codes
        > The most commonly used: [200](https://developer.mozilla.org/en/docs/Web/HTTP/Status/200), [201](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201), [204](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/204), [304](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/304), [400](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400), [401](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401), [403](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403), [404](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404), [405](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/405), [410](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/410), [415](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/415), [422](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422), [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429).
    -   [Versioning](https://github.com/NationalBankBelgium/REST-API-Design-Guide/wiki/REST-API-Versioning)
        > Over time you may want or need to fundamentally change the way your REST API service works. To avoid breaking applications using the current version, you can leave it where it is and implement the new version over a different URL route, e.g., `/api/v2`.

    [API Design](https://twirl.github.io/The-API-Book/index.html)
    > API development and design is a very important and responsible moment, as your API functionality will be used by other developers and systems to integrate with your service. Mistakes made during design can negatively affect not only the growth opportunities of your service, but also many others that depend on yours.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**What Is RESTful API?** – AWS](https://aws.amazon.com/what-is/restful-api/?nc1=h_ls)
2. 📺 [**What is REST API?** – YouTube](https://youtu.be/lsMQRaeKNDk)
3. 📺 [**APIs for Beginners 2023 - How to use an API (Full Course)** – YouTube](https://youtu.be/WXsD0ZgxjRw)
4. 📺 [**Build Web APIs with Python – Django REST Framework Course** – YouTube](https://youtu.be/tujhGdn1EMI)
5. 📺 [**Build an API from Scratch with Node.js Express** – YouTube](https://youtu.be/-MTSQjw5DrM)
6. 📺 [**Build REST API on Vanilla Node.js** – YouTube](https://youtu.be/_1xa8Bsho6A)
7. 📺 [**Build a REST API with Go** – YouTube](https://youtu.be/d_L64KT3SFM)
8. 📺 [**Spring Kotlin - Building a REST API Tutorial** – YouTube](https://youtube.com/playlist?list=PLNnNHr-wCfobAxSkuxMqFGdpA8E5cLR6w)
9. 📄 [**REST API design full guide** – GitHub](https://github.com/NationalBankBelgium/REST-API-Design-Guide/wiki)
10. 📄 [**Awesome REST** – GitHub](https://github.com/marmelab/awesome-rest)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### GraphQL

    [GraphQL](https://en.wikipedia.org/wiki/GraphQL) is a query language and server-side runtime for APIs that allows you to retrieve and modify data from a server using a single URL endpoint. It provides several benefits, including the ability to retrieve only the data you need (reducing traffic consumption), aggregation of data from multiple sources and a strict type system for describing data.

    -   [Schema and types](https://graphql.org/learn/schema/)
        > Learn how to describe data using GraphQL schema and general types.
    -   [Queries and Mutations](https://graphql.org/learn/queries/)
        > Queries are used to retrieve data from a server, while Mutations are used to modify (create, update or delete) data on a server.
    -   [Resolvers](https://www.apollographql.com/docs/apollo-server/data/resolvers/)
        > Resolvers are functions that determine how to retrieve the data for a particular field in the GraphQL schema.
    -   [Data sources](https://www.apollographql.com/docs/apollo-server/v2/data/data-sources/)
        > Are places where you retrieve data from, such as databases or APIs. Data sources are connected to the GraphQL server through resolvers.
    -   [Performance optimization](https://www.toptal.com/graphql/graphql-internal-api-optimization)
    -   [Best Practices](https://graphql.org/learn/best-practices/)

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**What Is GraphQL? REST vs. GraphQL** – YouTube](https://youtu.be/yWzKJPw_VzM)
2. 📄 [**Why use GraphQL?**](https://www.apollographql.com/blog/graphql/basics/why-use-graphql/)
3. 📄 [**Learn GraphQL from zero to production**](https://www.howtographql.com/)
4. 📺 [**Python with GraphQL tutorial** – YouTube](https://youtu.be/ZUrNFhG3LK4)
5. 📺 [**Modern GraphQL with Node.js Crash Course** – YouTube](https://youtu.be/qux4-yWeZvo)
6. 📺 [**GraphQL in Go - GQLGen Tutorial** – YouTube](https://youtu.be/O6jYy421tGw)
7. 📄 [**Awesome list of GraphQL** – GitHub](https://github.com/chentsulin/awesome-graphql)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### WebSockets

    [WebSockets](https://en.wikipedia.org/wiki/WebSocket) is an advanced technology that allows you to open a persistent bidirectional network connection between the client and the server. With its API you can send a message to the server and receive a response without making an HTTP request, thereby implementing real-time communication.

    The basic idea is that you do not need to send requests to the server for new information. When the connection is established, the server itself will send a new batch of data to connected clients as soon as that data is available. Web sockets are widely used to create chat rooms, online games, trading applications, etc.

    -   Opening a web socket
        > Sending an HTTP request with a specific set of headers: `Connection: Upgrade`, `Upgrade: websocket`, `Sec-WebSocket-Key`, `Sec-WebSocket-Version`.
    -   Connection states
        > `CONNECTING`, `OPEN`, `CLOSING`, `CLOSED`.
    -   Events
        > `Open`, `Message`, `Error`, `Close`.
    -   Connection closing codes
        > `1000`, `1001`, `1006`, `1009`, `1011`, [etc.](https://github.com/Luka967/websocket-close-codes)

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**A Beginner's Guide to WebSockets** – YouTube](https://youtu.be/8ARodQ4Wlf4)
2. 📺 [**WebSockets Crash Course - Handshake, Use-cases, Pros & Cons and more** – YouTube](https://youtu.be/2Nt-ZrNP22A)
3. 📄 [**Introducing WebSockets - Bringing Sockets to the Web**](https://web.dev/websockets-basics)
4. 📺 [**WebSockets with Python tutorial** – YouTube](https://youtu.be/lv0oEnQY1pM)
5. 📺 [**WebSockets with Node.js tutorial** – YouTube](https://youtu.be/1BfCnjr_Vjg)
6. 📺 [**WebSockets with Go tutorial** – YouTube](https://youtu.be/JuUAEYLkGbM)
7. 📄 [**Awesome WebSockets** – GitHub](https://github.com/facundofarias/awesome-websockets)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### RPC (Remote Procedure Call)

    [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) is simply a function call to the server with a set of specific arguments, which returns the response usually encoded in a certain format, such as JSON or XML. There are several protocols that implement RPC.

    -   XML-based protocols
        > There are two main protocols: [XML-RPC](https://en.wikipedia.org/wiki/XML-RPC) and [SOAP (Simple Object Access Protocol)](https://en.wikipedia.org/wiki/SOAP) <br>
        > They are considered deprecated and not recommended for new projects because they are heavyweight and complex compared to newer alternatives such as REST, GraphQL and newer RPC protocols.
    -   [JSON-RPC](https://en.wikipedia.org/wiki/JSON-RPC)
        > A protocol with a very simple [specification](https://www.jsonrpc.org/specification). All requests and responses are serialized in JSON format.
        > - A request to the server includes: `method` - the name of the method to be invoked; `params` - object or array of values to be passed as parameters to the defined method; `id` - identifier used to match the response with the request.
        > - A response includes: `result` - data returned by the invoked method; `error` - object with error or null for success; `id` - the same as in the request.
    -   [gRPC](https://en.wikipedia.org/wiki/GRPC)
        > RPC framework developed by Google. It works by defining a service using [Protocol Buffers](https://en.wikipedia.org/wiki/Protocol_Buffers), a language-agnostic binary serialization format, that generates to client and server code for various programming languages.
        > - Understand [protobuf fundamentals](https://protobuf.dev/programming-guides/proto3/).
        > - See tutorials for your language: [Python](https://grpc.io/docs/languages/python/quickstart/), [Node.js](https://grpc.io/docs/languages/node/basics/), [Go](https://grpc.io/docs/languages/go/quickstart/), [Kotlin](https://grpc.io/docs/languages/kotlin/quickstart/), etc.
        > - Learn [style guides](https://protobuf.dev/programming-guides/style/).
<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**What is RPC? gRPC Introduction** – YouTube](https://youtu.be/gnchfOojMk4)
2. 📄 [**Learning gRPC with an Example**](https://blog.devgenius.io/learning-grpc-with-an-example-8b4931bd90c8)
3. 📺 [**gRPC Crash Course - Modes, Examples, Pros & Cons and more** – YouTube](https://youtu.be/Yw4rkaTc0f8)
4. 📺 [**This is why gRPC was invented** – YouTube](https://youtu.be/u4LWEXDP7_M)
5. 📺 [**gRPC with Python - microservice complete tutorial** – YouTube](https://youtu.be/E0CaocyNYKg)
6. 📺 [**Implementing a gRPC client and server in TypeScript with Node.js** – YouTube](https://youtu.be/H0c4Wjl4kRQ)
7. 📺 [**Build a gRPC server with Go - Step-by-step tutorial** – YouTube](https://youtu.be/gbrPMv_GuQY)
8. 📄 [**Awesome gRPC** – GitHub](https://github.com/grpc-ecosystem/awesome-grpc)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### WebRTC

    [WebRTC](https://en.wikipedia.org/wiki/WebRTC) an open-source project for streaming data (video, audio) in a browser. WebRTC operation is based on [peer to peer connection](https://en.wikipedia.org/wiki/Peer-to-peer), however, there are implementations that allow you to organize complex group sessions. For example, the video-calling service [Google Meet](https://en.wikipedia.org/wiki/Google_Meet) makes extensive use of WebRTC.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**WebRTC Crash Course** – YouTube](https://youtu.be/FExZvpVvYxA)
2. 📄 [**Everything You Ever Wanted To Know About WebRTC**](https://blog.openreplay.com/everything-you-ever-wanted-to-know-about-webrtc/)
3. 📄 [**HTTP, WebSocket, gRPC or WebRTC: Which Communication Protocol is Best For Your App?**](https://getstream.io/blog/communication-protocols/)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

