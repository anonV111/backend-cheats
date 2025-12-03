### Authentication and authorization

[Authentication](https://en.wikipedia.org/wiki/Authentication) is a procedure that is usually performed by comparing the password entered by the user with the password stored in the database.
Also, this often includes [identification](<https://en.wikipedia.org/wiki/Identification_(information)>) - a procedure for identifying the user by his unique identifier (usually a regular login or email). This is needed to know exactly which user is being authenticated.

[Authorization](https://en.wikipedia.org/wiki/Authorization) - the procedure of granting access rights to a certain user to perform certain operations. For example, ordinary users of the online store can view products and add them to cart. But only administrators can add new products or delete existing ones.

-   [Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)
    > The simplest authentication scheme where the username and password of the user are passed in the [Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) header in unencrypted (base64-encoded) form. It is relatively secure when using HTTPS.
-   [SSO (Single Sign-On)](https://en.wikipedia.org/wiki/Single_sign-on)
    > Technology that implements the ability to move from one service to another (not related to the first), without reauthorization.
-   [OAuth / OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)
    > Authorization protocol, which allows you to register in various applications using popular services (Google, Facebook, GitHub, etc.)
-   [OpenID](https://en.wikipedia.org/wiki/OpenID)
    > An open standard that allows you to create a single account for authenticating to multiple unrelated services.
-   [JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)
    > An authentication standard based on access tokens. Tokens are created by the server, signed with a secret key and transmitted to the client, who then uses the token to verify his identity.

<details>
<summary>🔗 <b>References</b></summary>

1. 📺 [**HTTP Basic Authentication explained** – YouTube](https://youtu.be/EeNzWUcPaFY)
2. 📺 [**What Is Single Sign-on (SSO)? How It Works** – YouTube](https://youtu.be/O1cRJWYF-g4)
3. 📺 [**OAuth 2 explained in very simple terms** – YouTube](https://youtu.be/THs9QUUXVhk)
4. 📺 [**OpenID Connect explained** – YouTube](https://youtu.be/PsbIGfvX900)
5. 📺 [**What Is JWT and Why Should You Use JWT** – YouTube](https://youtu.be/7Q17ubqLfaM)
 </details>


