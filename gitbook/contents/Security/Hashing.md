### Hashing

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


