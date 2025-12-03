### Environment variables

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


