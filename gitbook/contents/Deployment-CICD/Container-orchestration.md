### Container orchestration

Container orchestration is the process of managing and automating the deployment, scaling, and maintenance of containerized applications and dependencies into a portable, lightweight container format to use them in a cluster of machines.

-   Docker in production
    > The easiest way to manage containers is to use Docker directly, following a list of rules to keep your applications stable and safe in a production environment.
    > - Store your Docker images in a private registry to prevent unauthorized access and ensure security.
    > - Use secure authentication mechanisms for access to your Docker registry and implement security measures such as firewall rules to limit access to your Docker environment.
    > - Keep the size of your containers as small as possible by minimizing the number of unnecessary packages and dependencies.
    > - Use separate containers for different services (ex. application server, database, cache, metrics etc.).
    > - Use Docker volumes to store persistent data such as database files, logs, and configuration files.
-   [Docker swarm](https://docs.docker.com/engine/swarm/)
    > It is a native orchestration tool for Docker to manage, scale and automate tasks such as container updates, recovery, traffic balancing, [service discovery](https://devopscube.com/service-discovery-explained/) and so on.
-   [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) (K8s)
    > Is a very popular orchestration platform that can work with a variety of container runtimes including Docker. Kubernetes offers a more comprehensive set of features (than Docker swarm), including advanced scheduling, storage orchestration, and self-healing capabilities.

<details>
<summary>🔗 <b>References</b></summary>

1. 📄 [**How To Optimize Docker Images for Production** – Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-optimize-docker-images-for-production)
2. 📄 [**Docker Compose in production**](https://docs.docker.com/compose/production/)
3. 📄 [**Top 8 Docker Best Practices for using Docker in Production** – dev.to](https://dev.to/techworld_with_nana/top-8-docker-best-practices-for-using-docker-in-production-1m39)
4. 📺 [**Best practices around creating a production web app with Docker and Docker Compose** – YouTube](https://youtu.be/vYpPGCaKs3I)
5. 📺 [**Docker Swarm Tutorial** – YouTube](https://youtu.be/Tm0Q5zr3FL4)
6. 📄 [**Awesome Swarm** – GitHub](https://github.com/BretFisher/awesome-swarm)
7. 📄 [**Kubernetes vs. Docker Swarm – What is the Difference?**](https://www.freecodecamp.org/news/kubernetes-vs-docker-swarm-what-is-the-difference/)
8. 📄 [**Kubernetes Roadmap**](https://roadmap.sh/kubernetes)
9. 📄 [**Kubernetes Learning Roadmap** – GitHub](https://github.com/techiescamp/kubernetes-learning-path)
10. 📺 [**Docker Containers and Kubernetes Fundamentals – Full Hands-On Course** – YouTube](https://youtu.be/kTp5xUtcalw)
11. 📺 [**Kubernetes Course - Full Beginners Tutorial (Containerize Your Apps!)** – YouTube](https://youtu.be/d6WC5n9G_sM)
12. 📄 [**Awesome Kubernetes Resources – GitHub**](https://github.com/tomhuang12/awesome-k8s-resources)
 </details>


