### REST API

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


