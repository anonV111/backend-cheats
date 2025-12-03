### RPC (Remote Procedure Call)

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


