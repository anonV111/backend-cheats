### Server development

-   Understand sockets
    > A socket is an endpoint of a two-way communication link between two programs running over a network. You need to know how to create, connect, send, and receive data over sockets.
-   Running a local TCP, UDP and HTTP servers
    > These protocols are the most important, you need to understand the intricacies of working with each of them.
-   Handing out static files
    > You need to know how to host HTML pages, pictures, PDF documents, music/video files, etc.
-   Routing
    > Creation of endpoints (URLs) which will call the appropriate handler on the server when accessed.
-   Processing requests
    > As a rule, HTTP handlers have a special object which receives all information about user request (headers, method, request body, query parameters and so on)
-   Processing responses
    > Sending an appropriate message to a received request (HTTP status and code, response body, headers, etc.)
-   Error handling
    > You should always be prepared for the possibility that something will go wrong: the user will send incorrect data, the database will not perform the operation, or an unexpected error will simply occur in the application. It is necessary for the server not to crash, but to send a response with information about the error.
-   [Middleware](https://www.ibm.com/topics/middleware)
    > An intermediate component between the application and the server. It used for handling authentication, validation, caching data, logging requests, and so on.
-   Sending requests
    > Often, within one application, you will need to access another application over the network. That's why it's important to be able to send HTTP requests using the built-in features of the language.
-   [Template processor](https://en.wikipedia.org/wiki/Template_processor)
    > Is a special module that uses a more convenient syntax to generate HTML based on dynamic data.

<details>
<summary>🔗 <b>References</b></summary>

1. 📄 [**Learn Django – Python-based web framework**](https://www.djangoproject.com/start/)
2. 📺 [**Python Django 7 Hour Course** – YouTube](https://youtu.be/PtQiiknWUcI)
3. 📄 [**A curated list of awesome things related to Django** – GitHub](https://github.com/wsvincent/awesome-django)
4. 📺 [**Python Web Scraping for Beginners** – YouTube](https://youtu.be/mBoX_JCKZTE)
5. 📺 [**Build servers in pure Node.js** – YouTube](https://youtu.be/_1xa8Bsho6A)
6. 📄 [**Node.js HTTP Server Examples – GitHub**](https://github.com/HowProgrammingWorks/NodeServer)
7. 📄 [**Learn Express – web framework for Node.js**](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs)
8. 📺 [**Express.js 2022 Course** – YouTube](https://youtube.com/playlist?list=PL_cUvD4qzbkwp6pxx27pqgohrsP8v1Wj2)
9. 📄 [**A curated list of awesome Express.js resources** – GitHub](https://github.com/rajikaimal/awesome-express)
10. 📄 [**How to build servers in Go**](https://eli.thegreenplace.net/2021/rest-servers-in-go-part-1-standard-library/)
11. 📺 [**Golang server development course** – YouTube](https://youtube.com/playlist?list=PLzUGFf4GhXBL4GHXVcMMvzgtO8-WEJIoY)
12. 📄 [**Web services in Go** – GitBook](https://astaxie.gitbooks.io/build-web-application-with-golang/content/en/08.0.html)
13. 📄 [**List of libraries for working with network in Go** – GitHub](https://github.com/avelino/awesome-go#networking)
14. 📄 [**Learn Ktor – web framework for Kotlin**](https://ktor.io/learn/)
15. 📺 [**Ktor - REST API Tutorials** – YouTube](https://youtube.com/playlist?list=PLFmuMD2V4CkyR0Pa42Cqu5mIhH17uG8nN)
16. 📄 [**Kotlin for server side**](https://kotlinlang.org/docs/server-overview.html)
</details>


