## Software

-   ### Git version control system

    [Git](https://en.wikipedia.org/wiki/Git) a special system for managing the history of changes to the source code. Any changes that are made to Git can be saved, allowing you to rollback (revert) to a previously saved copy of the project. Git is currently the standard for development.

    -   [Basic commands](https://github.com/cheatsnake/quick-git#basic-commands)
    -   [Viewing commits & logs](https://github.com/cheatsnake/quick-git#information-about-commits)
        > Commit is a record in the repository history that represents information about changes to files.
    -   [Working with branches](https://github.com/cheatsnake/quick-git#working-with-branches)
        > Branch is a sequence of commits.
    -   [Remote repositories](https://github.com/cheatsnake/quick-git#remote-repositories)
        > A repository is a place where the source code and change history (commits) of your project is stored.
    -   [Commit deletions and rollbacks](https://github.com/cheatsnake/quick-git#commit-deletions-and-rollbacks)
    -   [Merge conflict](https://stackoverflow.com/a/163659/21100330)
        > A situation where two branches have different changes in the same location and Git cannot automatically merge them.
    -   [.gitignore](https://git-scm.com/docs/gitignore)
        > A special file to exclude specific files or patterns (e.g., build artifacts) from tracking.
    -   [Git style guide](https://github.com/agis/git-style-guide#table-of-contents)
        > Learn best practices popular in the community.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Git It? How to use Git and GitHub** – YouTube](https://youtu.be/HkdAHXoRtos)
2. 📺 [**Git and GitHub for Beginners - Crash Course** – YouTube](https://youtu.be/RGOj5yH7evk)
3. 📺 [**13 Advanced (but useful) Git Techniques and Shortcuts** – YouTube](https://youtu.be/RGOj5yH7evk)
4. 📄 [**Understanding Git through images** – dev.to](https://dev.to/nopenoshishi/understanding-git-through-images-4an1)
5. 📄 [**Learn Git concepts, not commands** – GitHub](https://github.com/UnseenWizzard/git_training)
6. 📄 [**Git Cheat Sheet – 50 Git Commands You Should Know** – freeCodeCamp](https://www.freecodecamp.org/news/git-cheat-sheet/)
7. 📄 [**Git Commit Patterns** – dev.to](https://dev.to/hornet_daemon/git-commit-patterns-5dm7)
8. 📄 [**Collection of .gitignore templates** – GitHub](https://github.com/github/gitignore)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Docker

    [Docker](<https://en.wikipedia.org/wiki/Docker_(software)>) a special program that allows you to run isolated sandboxes (containers) with different preinstalled environments (be it a specific operating system, a database, etc.). [Containerization](https://en.wikipedia.org/wiki/OS-level_virtualization) technology, that Docker provides is similar to virtual machines, but unlike virtual machines, containers use the host OS kernel, which requires far fewer resources.

    -   Docker image
        > A special fixed template that contains a description of the environment to run the application (OS, source code, libraries, environment variables, configuration files, etc.). The images can be downloaded from [official site](https://hub.docker.com/search?type=image) and used to create your own.
    -   Docker container
        > An isolated environment created from an image. It is essentially a running process on a computer which internally contains the environment described in the image.
    -   Console commands
        ```bash
        docker pull [image_name] # Download the image
        docker images  # List of available images
        docker run [image_id] # Running a container based on the selected image
            # Some flags for the run command:
            -d # Starting with a return to the console
            --name [name] # Name the container
            --rm # Remove the container after stopping
            -p [local_port][port_iside_container] # Port forwarding
        docker build [path_to_Dockerfile] # Creating an image based on a Dockerfile
        docker ps # List of running containers
        docker ps -a # List of all containers
        docker stop [id/container_name] # Stop the container
        docker start [id/container_name] # Start an existing container
        docker attach [id/container_name] # Connect to the container console
        docker logs [id/container_name] # Output the container logs
        docker rm [id/container_name] # Delete container
        docker container prune # Delete all containers
        docker rmi [image_id] # Delete image
        ```
    -   Instructions for [Dockerfile](https://docs.docker.com/engine/reference/builder/)
        > Dockerfile is a file with a set of instructions and arguments for creating images.
        ```bash
        FROM [image_name] # Setting a base image
        WORKDIR [path] # Setting the root directory inside the container
        COPY [path_relative_Dockerfile] [path_in_container] # Copying files
        ADD [path] [path] # Similar to the command above
        RUN [command] # A command that runs only when the image is initialized
        CMD ["command"] # The command that runs every time you start the container
        ENV KEY="VALUE" # Setting Environment Variables
        ARG KEY=VALUE # Setting variables to pass to Docker during image building
        ENTRYPOINT ["command"] # The command that runs when the container is running
        EXPOSE port/protocol # Indicates the need to open a port
        VOLUME ["path"] # Creates a mount point for working with persistent storage
        ```
    -   [Docker-compose](https://docs.docker.com/compose/)
        > A tool for defining and running multi-container Docker applications. It allows you to define the services that make up your application in a single file, and then start and stop all of the services with a single command. In a sense, it is a Dockerfile on maximal.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Learn Docker in 7 Easy Steps - Full Beginner's Tutorial** – YouTube](https://youtu.be/gAkwW2tuIqE)
2. 📺 [**Never install locally** – YouTube](https://youtu.be/J0NuOlA2xDc)
3. 📺 [**Docker Crash Course Tutorial (playlist)** – YouTube](https://youtube.com/playlist?list=PL4cUxeGkcC9hxjeEtdHFNYMtCpjNBm3h7)
4. 📄 [**The Ultimate Docker Cheat Sheet**](https://dockerlabs.collabnix.com/docker/cheatsheet/)
5. 📺 [**Docker Compose Tutorial** – YouTube](https://youtu.be/HG6yIjZapSA)
6. 📺 [**Docker networking – everything you need to know** – YouTube](https://youtu.be/bKFMS5C4CG0)
7. 📄 [**Awesome Docker** – GitHub](https://github.com/veggiemonk/awesome-docker)
8. 📄 [**What Is a Dockerfile And How To Build It – Best Practices** – Spacelift](https://spacelift.io/blog/dockerfile)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Postman/Insomnia

    When creating a server application, it is necessary to test its workability. This can be done in different ways. One of the easiest is to use the console utility [cURL](https://en.wikipedia.org/wiki/CURL). But this is good for very simple applications. Much more efficient is to use special software for testing, which have a user-friendly interface and all the necessary functionality to create collections of queries.

    -   [Postman](https://www.postman.com/)
        > A very popular and feature-rich program. It definitely has everything you might need and more: from the trivial creation of collections to raising mock-servers. The basic functionality of the application is free of charge.
    -   [Insomnia](https://insomnia.rest/)
        > Not as popular, but a very nice tool. The interface in Insomnia, minimalist and clear. It has less functionality, but everything you need: collections, variables, work with GraphQL, gRPC, WebSocket, etc. It is possible to install third-party plugins.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**What is Postman? How to use Postman? Tool For Beginners** – YouTube](https://youtu.be/E0f9DUEN_jI)
2. 📺 [**Postman Beginner's Course - API Testing** – YouTube](https://youtu.be/VywxIQ2ZXw4)
3. 📺 [**Postman API Test Automation for Beginners** – YouTube](https://youtu.be/zp5Jh2FIpF0?si=A1UMThcDUhxLj8ye)
4. 📺 [**Insomnia API Client Tutorial** – YouTube](https://youtu.be/x2AlTaFJJxs)
5. 📺 [**Insomnia Tutorial: API Design, Testing, and Collaboration** – YouTube](https://youtu.be/fzLPHpOP3Wc)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Web servers

    <p align="center"><img src="./files/software/web-server_eng.png" alt="Web server"/></p>

    A [web server](https://en.wikipedia.org/wiki/Web_server) is a program designed to handle incoming HTTP requests. In addition, it can keep error logs (logs), perform authentication and authorization, store rules for file processing, etc.

    -   What is it for?
        > Not all languages can have a built-in web server (e.g., PHP). Therefore, to run web applications written in such languages, a third-party one is needed. <br>
        > A single server (virtual or dedicated) can run several applications, but only one external IP address. A configured web server solves this problem and can redirect incoming requests to the right applications.
    -   Popular web servers
        > [Nginx](https://en.wikipedia.org/wiki/Nginx) – the most popular at the moment. <br>
        > [Apache](https://en.wikipedia.org/wiki/Apache_HTTP_Server) – also popular, but already giving up its position. <br>
        > [Caddy](<https://en.wikipedia.org/wiki/Caddy_(web_server)>) – a fairly young web server with great potential.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**What are web servers and how do they work** – YouTube](https://youtu.be/JhpUch6lWMw)
2. 📺 [**Web Server Concepts and Examples** – YouTube](https://youtu.be/9J1nJOivdyw)
3. 📺 [**The NGINX Crash Course** – YouTube](https://youtu.be/7VAI73roXaY)
4. 📺 [**Nginx Server Complete Course** – YouTube](https://youtu.be/tMtFZdaaIhk)
5. 📄 [**6 Best Courses to learn Nginx in depth** – medium](https://medium.com/javarevisited/best-courses-to-learn-nginx-in-36ed9ccca804)
6. 📄 [**NGINX: Advanced Load Balancer, Web Server, & Reverse Proxy** – dev.to](https://dev.to/lovepreetsingh/nginx-advanced-load-balancer-web-server-reverse-proxy-4i23)
7. 📄 [**Awesome NGINX** – GitHub](https://github.com/agile6v/awesome-nginx)
</details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Message brokers

    <p align="center"><img src="./files/software/message-queue_eng.png" alt="Message queue"/></p>

    When creating a large-scale backend system, the problem of communication between a large number of microservices may arise. In order not to complicate existing services (establish a reliable communication system, distribute the load, provide for various errors, etc.) you can use a separate service, which is called a [message broker](https://en.wikipedia.org/wiki/Message_broker) (or message queue).

    The broker takes the responsibility of creating a reliable and fault-tolerant system of communication between services (performs balancing, guarantees delivery, monitors recipients, maintains logs, buffering, etc.)

    A message is an ordinary HTTP request/response with data of a certain format.

    -   [RabbitMQ](https://en.wikipedia.org/wiki/RabbitMQ) - specializes in message queuing and supports various messaging patterns, including publish/subscribe and point-to-point communication.
    -   [Apache Kafka](https://en.wikipedia.org/wiki/Apache_Kafka) - excels in handling large-scale, real-time data streams and offers high throughput, fault tolerance, and horizontal scalability.
    -   [NATS](https://nats.io/) - known for its simplicity, speed, and lightweight design, making it ideal for building fast and efficient distributed systems.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**What is a Message Queue and When should you use Messaging Queue Systems** – YouTube](https://youtu.be/W4_aGb_MOls)
2. 📺 [**What is a Message Queue?** – YouTube](https://youtu.be/xErwDaOc-Gs)
3. 📄 [**Understanding RabbitMQ** – medium](https://medium.com/swlh/understanding-rabbitmq-11d710e40a38)
4. 📺 [**RabbitMQ course (playlist)** – YouTube](https://youtube.com/playlist?list=PLrwNNiB6YOA3Z3JfOUMKE6PmnpmVAJgTK)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Ngrok

    [Ngrok](https://ngrok.com/) is a tool for creating public [tunnels](https://en.wikipedia.org/wiki/Tunneling_protocol) on the Internet that allows local network applications (web servers, websites, bots, etc.) to be accessible from outside.

    - How does it work?
        > Ngrok creates a temporary public URL that can be used to access your local server from the Internet. Once Ngrok is started, you have access to the console, where you can monitor requests, handling, and responses to those requests, and configure additional features such as authentication and encryption.
    - What to use it for?
        > For example, to test web sites and APIs, to demonstrate running applications on a local server, to access local network applications over the Internet without having to set up a router, firewall, proxy server, etc.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Expose Local WebSocket, HTTP and HTTPS WebServers to the Public Internet with Ngrok** – YouTube](https://youtu.be/pR2qNnVIuKE)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### AI tools

    Artificial intelligence systems have made an incredible leap recently. Every day there are more and more tools that can write code for you, generate documentation, do code reviews, help you learn new technologies, and so on. Many people are still skeptical about the capabilities and quality of content that AI creates. But at least by now, a lot of time and resources can be saved to increase the productivity of any developer.

    -   [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT)
        > The highest quality [LLM](https://en.wikipedia.org/wiki/Large_language_model) at the moment. Works like a normal chatbot and has no problem understanding human speech in several languages.
    -   [Bard](https://en.wikipedia.org/wiki/Bard_(chatbot))
        > Developed by Google as an alternative and direct competitor to ChatGPT.
    -   [GitHub Copilot](https://en.wikipedia.org/wiki/GitHub_Copilot)
        > AI-powered code completion tool developed by GitHub in collaboration with developers of ChatGPT. It integrates with popular code editors and provides real-time suggestions and completions for code as you write.
    -   [Tabnine](https://www.tabnine.com/)
        > An alternative to GitHub Copilot that provides context-sensitive code suggestions based on patterns it learns from millions of publicly available code repositories.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Awesome ChatGPT Prompts** – GitHub](https://github.com/f/awesome-chatgpt-prompts)
2. 📺 [**ChatGPT Tutorial for Developers - 38 Ways to 10x Your Productivity** – YouTube](https://youtu.be/sTeoEFzVNSc)
3. 📺 [**GitHub Copilot in 7 Minutes** – YouTube](https://youtu.be/hPVatUSvZq0)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

