## Security

-   ### Web application vulnerabilities

    -   [Cross-site scripting (XSS)](https://en.wikipedia.org/wiki/Cross-site_scripting)
        > An attack that allows an attacker to inject malicious code through a website into the browsers of other users.
    -   [SQL injection](https://en.wikipedia.org/wiki/SQL_injection)
        > An attack is possible if the user input that is passed to the SQL query is able to change the meaning of the statement or add another query to it.
    -   [Cross-site request forgery (CSRF)](https://en.wikipedia.org/wiki/Cross-site_request_forgery)
        > When a site uses a POST request to perform a transaction, the attacker can forge a form, such as in an email, and send it to the victim. The victim, who is an authorized user interacting with this email, can then unknowingly send a request to the site with the data that the attacker has set.
    -   [Clickjacking](https://en.wikipedia.org/wiki/Clickjacking)
        > The principle is based on the fact that an invisible layer is placed on top of the visible web page, in which the page the intruder wants is loaded, while the control (button, link) needed to perform the desired action is combined with the visible link or button the user is expected to click on.
    -   [Denial of Service (DoS attack)](https://en.wikipedia.org/wiki/Denial-of-service_attack)
        > A hacker attack that overloads the server running the web application by sending a huge number of requests.
    -   [Man-in-the-Middle attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)
        > A type of attack in which an attacker gets into the chain between two (or more) communicating parties to intercept a conversation or data transmission.
    -   Incorrect security configuration
        > Using default configuration settings can be dangerous because it is common knowledge. For example, a common vulnerability is that network administrators leave the default logins and passwords _admin:admin_.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**7 Security Risks and Hacking Stories for Web Developers** – YouTube](https://youtu.be/4YOpILi9Oxs)
2. 📄 [**Top 10 Web Application Security Risks**](https://owasp.org/www-project-top-ten/)
3. 📺 [**Web App Vulnerabilities - DevSecOps Course for Beginners** – YouTube](https://youtu.be/F5KJVuii0Yw)
4. 📺 [**DDoS Attack Explained** – YouTube](https://youtu.be/ilhGh9CEIwM)
5. 📺 [**Securing Web Applications – MIT lecture** – YouTube](https://youtu.be/WlmKwIe9z1Q)
6. 📺 [**Scan for Vulnerabilities on Any Website Using Nikto** – YouTube](https://youtu.be/K78YOmbuT48)
7. 📺 [**OWASP API Security Top 10 Course** – YouTube](https://youtu.be/YYe0FdfdgDU)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Environment variables

    Often your applications may use various tokens (e.g., to access a third-party paid API), logins and passwords (to connect to a database), various secret keys for signatures and so on. All this data should not be known and available to outsiders, so you can't leave them in the program code in any case. To solve this problem, there are environment variables.

    -   The `.env` file
        > A special file in which you can store all environment variables.
    -   Parsing the `.env` file
        > Variables are passed to the program using command line arguments. To do the same with the `.env` file, you need to use a special library for your language.
    -   Storage and transfer `.env` files
        > Learn how to upload `.env` files to the hosting services and remember that such files cannot be committed to remote repositories, so do not forget to add them to exceptions via the `.gitignore` file.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**How to use environment variables in a Python script** – YouTube](https://youtu.be/ed2NGpsws8Y)
2. 📺 [**Configure Node.js Environment Variables for Local Development & Production** – YouTube](https://youtu.be/gfyQzeBlLTI)
3. 📺 [**Golang Environment Variables** – YouTube](https://youtu.be/mnCgl-iwPak)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Hashing

    <p align="center"><img src="./files/security/hashing_eng.png" alt="Hashing"/></p>

    Cryptographic algorithms based on [hash functions](https://en.wikipedia.org/wiki/Hash_function) are widely used for network security.

    -   Hashing
        > The process of converting an array of information (from a single letter to an entire literary work) into a unique short string of characters (called hash), which is unique to that array of information. Moreover, if you change even one character in this information array, the new hash will differ dramatically. <br>
        > Hashing is an irreversible process, that is, the resulting hash cannot be recovered from the original data.
    -   [Checksums](https://en.wikipedia.org/wiki/Checksum)
        > Hashes can be used as checksums that serve as proof of data integrity.
    -   [Collisions](https://en.wikipedia.org/wiki/Hash_collision)
        > Cases where hashing different sets of information results in the same hash.
    -   [Salt (in cryptography)](<https://en.wikipedia.org/wiki/Salt_(cryptography)>)
        > A random string of data, which is added to the input data before hashing, to calculate the hash. This is necessary to make brute-force hacking more difficult.

    Popular hashing algorithms:

    -   [SHA family (Secure Hash Algorithm)](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms)
        > [SHA-256](https://en.wikipedia.org/wiki/SHA-2) is the most popular encryption algorithm. It is used, for example, in [Bitcoin](https://en.wikipedia.org/wiki/Bitcoin).
    -   MD family (Message Digest)
        > The most popular algorithm of the family is [MD5](https://en.wikipedia.org/wiki/MD5). It is now considered very vulnerable to collisions (there are even collision generators for MD5).
    -   [BLAKE](<https://en.wikipedia.org/wiki/BLAKE_(hash_function)>) family
    -   [RIPEMD](https://en.wikipedia.org/wiki/RIPEMD) family
    -   [Streebog](https://en.wikipedia.org/wiki/Streebog)

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**What is Hashing? Hash Functions Explained Simply** – YouTube](https://youtu.be/2BldESGZKB8)
2. 📺 [**Passwords & hash functions (Simply Explained)** – YouTube](https://youtu.be/cczlpiiu42M)
3. 📺 [**Hashing Algorithms and Security - Computerphile** – YouTube](https://youtu.be/b4b8ktEV4Bg)
4. 📺 [**SHA: Secure Hashing Algorithm - Computerphile** – YouTube](https://youtu.be/DMtFhACPnTY)
5. 📺 [**How secure is 256 bit security?** – YouTube](https://youtu.be/DMtFhACPnTY)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Authentication and authorization

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

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### SSL/TLS

    [SSL (Secure Socket Layer)](https://en.wikipedia.org/wiki/Transport_Layer_Security#SSL_1.0,_2.0,_and_3.0) and [TLS (Transport Layer Security)](https://en.wikipedia.org/wiki/Transport_Layer_Security) are cryptographic protocols that allow secure transmission of data between two computers on a network. These protocols work essentially the same and there are no differences. SSL is considered obsolete, although it is still used to support older devices.

    -   [Certificate Authority (CA)](https://en.wikipedia.org/wiki/Certificate_authority)
        > TLS/SSL uses digital certificates issued by a certificate authority. One of the most popular is [Let’s Encrypt](https://en.wikipedia.org/wiki/Let%27s_Encrypt).
    -   Certificate configuration and installation
        > You need to know how to generate certificates and install them properly to make your server work over HTTPS.
    -   [Handshake process](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_handshake)
        > To establish a secure connection between the client and the server, a special process must take place which includes the exchange of secret keys and information about encryption algorithms.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**SSL, TLS, HTTPS Explained** – YouTube](https://youtu.be/j9QmMEWmcfo)
2. 📺 [**Transport Layer Security, TLS 1.2 and 1.3 (Explained by Example)** – YouTube](https://youtu.be/AlE5X1NlHgg)
3. 📺 [**Let's Encrypt Explained: Free SSL** – YouTube](https://youtu.be/jrR_WfgmWEw)
4. 📺 [**How to Install a Free SSL Certificate with Let's Encrypt** – YouTube](https://youtu.be/PGDx3xxLGgA)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

