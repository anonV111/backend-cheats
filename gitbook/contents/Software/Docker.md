### Docker

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


