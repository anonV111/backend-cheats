### WebSockets

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


