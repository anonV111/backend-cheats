## Deployment (CI/CD)

-   ### Cloud services

    Before you can deploy your code, you need to decide where you want to host it. You can rent your own server or use the services of cloud providers, which have great functionality for process automation, monitoring, load balancing, data storing and so on.

    -   [AWS (Amazon Web Services)](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html)
        > Provides a wide range of services for computing, storage, database management, networking, security, and more. AWS is one of the oldest and most established cloud service providers.
    -   [Google Cloud](https://cloud.google.com/docs/overview)
        > It is known for its focus on machine learning and artificial intelligence, as well as its integration with other Google services like Google Analytics and Google Maps.
    -   [Microsoft Azure](https://azure.microsoft.com/en-us/explore)
        > Azure is known for its integration with other Microsoft services like Office 365 and Dynamics 365, as well as its support for a wide range of programming languages and frameworks.
    -   [Digital Ocean](https://www.digitalocean.com/)
        > This service provides virtual private servers (VPS) for developers and small businesses. It is also known for its simplicity and ease of use, as well as its competitive pricing.
    -   [Heroku](https://www.heroku.com/what)
        > Heroku is known for its ease of use and integration with popular development tools like Git, as well as its support for multiple programming languages and frameworks. It was a very popular choice for open source projects as long as there was a free plan (it costs money now).

    As a rule, all of these services have an intuitive simple interface, detailed documentation, as well as many video tutorials on YouTube.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Big vs. Small Public Cloud Providers** – YouTube](https://youtu.be/LJomGBuBDaU)
2. 📺 [**Top 50+ AWS Services Explained in 10 Minutes** – YouTube](https://youtu.be/JIbIYCM48to)
3. 📺 [**AWS Certified Cloud Practitioner Certification Course** – YouTube](https://youtu.be/SOTamWNgDKc)
4. 📄 [**Awesome AWS (list of libraries, open source repos, guides, blogs) – GitHub**](https://github.com/donnemartin/awesome-aws)
5. 📺 [**Google Cloud Associate Cloud Engineer Course** – YouTube](https://youtu.be/jpno8FSqpc8)
6. 📄 [**Awesome Google Cloud Platform – GitHub**](https://github.com/GoogleCloudPlatform/awesome-google-cloud)
7. 📺 [**Microsoft Azure Fundamentals Certification Course** – YouTube](https://youtu.be/NKEFWyqJ5XA)
8. 📺 [**Full DigitalOcean Crash Course** – YouTube](https://youtu.be/9ZUHSW1tTiU)
9. 📄 [**Awesome Digital Ocean – GitHub**](https://github.com/jonleibowitz/awesome-digitalocean)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Container orchestration

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

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Automation tools

    To streamline the process of building, testing, deploying code changes, integrate with other tools in the development ecosystem, such as code repositories, issue trackers, monitoring systems to provide a more comprehensive development workflow you can use some automation tools and services.

    -   [GitHub Actions](https://docs.github.com/en/actions)
        > CI/CD tool built into the GitHub platform, which enables developers to automate workflows for their repositories. A great choice if you already use GitHub. There are a large number of pre-built actions. One of the most useful feature is ability to trigger workflows based on various events, such as pull requests or other repository activity.
    -   [Jenkins](https://en.wikipedia.org/wiki/Jenkins_(software))
        > Highly configurable and extensible open source tool with a large ecosystem of plugins available to customize its functionality. Jenkins can be used in various environments, including on-premise, cloud-based and hybrid setups.
    -   [Circle CI](https://en.wikipedia.org/wiki/CircleCI)
        > It is a cloud-based CI/CD platform designed to be fast and easy to set up, with a focus on developer productivity. Circle CI integrates with various cloud-based services, such as AWS, Google Cloud and Microsoft Azure. You can also host it locally on your network.
    -   [Travis CI](https://en.wikipedia.org/wiki/Travis_CI)
        > It is also a cloud-based CI/CD platform. It can be easily integrated with GitHub or Bitbucket. Travis CI supports multiple programming languages and frameworks. It also can be hosted as your local platform.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**GitHub Actions: The Full Course - Learn by Doing (playlist)** – YouTube](https://youtube.com/playlist?list=PLArH6NjfKsUhvGHrpag7SuPumMzQRhUKY)
2. 📄 [**Awesome GitHub Actions – GitHub**](https://github.com/sdras/awesome-actions)
3. 📺 [**Learn Jenkins! Complete Jenkins Course - Zero to Hero** – YouTube](https://youtu.be/6YZvp2GwT0A)
4. 📺 [**CircleCI Tutorial for Beginners | Learn CircleCI In 30 Minutes** – YouTube](https://youtu.be/_XaYv9zvHUk)
5. 📺 [**Travis CI Complete Tutorial for DevOps Engineers** – YouTube](https://youtu.be/xLWDOLhTH38)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Monitoring and logs

    Logs capture detailed information about events, errors, and activities within your applications, facilitating troubleshooting and debugging processes. They provide a historical record of system behavior, allowing you to investigate issues, understand root causes, and improve overall system reliability and stability.

    -   Libraries for your lang
        > The easiest way to log an application is to use the tools of the standard language library or third-party packages. For example, in Python you can use [logging module](https://docs.python.org/3/library/logging.html) or [Loguru](https://github.com/Delgan/loguru). In Node.js – [Winston](https://github.com/winstonjs/winston), [Pino](https://github.com/pinojs/pino). And in Go – [log package](https://pkg.go.dev/log), [Logrus](https://github.com/sirupsen/logrus).
    -   [Loki](https://go2.grafana.com/loki-grafana-cloud.html)
        > Designed to collect log data from various sources and provides fast searching and filtering capabilities.
    -   [Graylog](https://github.com/Graylog2/graylog2-server)
        > Comprehensive log management platform that also centralizes log data from different sources. Graylog offers features like log ingestion, indexing, searching, and analysis.
    -   ELK Stack ([Elasticsearch](https://en.wikipedia.org/wiki/Elasticsearch), [Logstash](https://www.elastic.co/logstash/), [Kibana](https://www.elastic.co/kibana/))
        > Is a combination of three open-source tools used for log management and analysis. Elasticsearch is a distributed search and analytics engine that stores and indexes logs. Logstash is a log ingestion and processing pipeline that collects, filters, and transforms log data. Kibana is a web interface that allows you to search, visualize, and analyze logs stored in Elasticsearch.

    Metrics help track key performance indicators, resource utilization, and system behavior, enabling you to identify bottlenecks, optimize performance, and ensure efficient resource allocation.

    -   [Prometheus](https://en.wikipedia.org/wiki/Prometheus_(software))
        > Open-source monitoring system that can collect metrics data from various sources. It employs a pull-based model, periodically scraping targets to collect metrics. The collected data is stored in a time-series database, allowing for powerful querying and analysis. Prometheus provides a flexible query language and a user-friendly interface to visualize and monitor metrics. It also includes an alerting system to define and trigger alerts based on specified rules and thresholds.
    -   [Grafana](https://en.wikipedia.org/wiki/Grafana)
        > Tool for visualization and monitoring. It allows you to create visually appealing dashboards and charts to analyze and monitor metrics data from various sources, including databases and monitoring systems like Prometheus and InfluxDB.
    -   [InfluxDB](https://en.wikipedia.org/wiki/InfluxDB)
        > Time-series database designed specifically for storing and querying metrics and events data. Offers a simple and flexible query language to extract valuable insights from the stored data. With its focus on time-series data, InfluxDB allows for easy aggregation, downsampling, and retention policies.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Grafana Loki a log aggregation system for everything** – YouTube](https://youtu.be/h_GGd7HfKQ8)
2. 📺 [**Graylog guide to getting started log management** – YouTube](https://youtu.be/DwYwrADwCmg)
3. 📺 [**Overview of the Elastic Stack (formerly ELK stack)** – YouTube](https://youtu.be/Hqn5p67uev4)
4. 📄 [**Awesome Elasticsearch – GitHub**](https://github.com/dzharii/awesome-elasticsearch)
5. 📺 [**How Prometheus Monitoring works** – YouTube](https://youtu.be/h4Sl21AKiDg)
6. 📄 [**Awesome Prometheus – GitHub**](https://github.com/roaldnefs/awesome-prometheus)
7. 📺 [**Server Monitoring: Prometheus and Grafana Tutorial** – YouTube](https://youtu.be/9TJx7QTrTyo)
8. 📺 [**InfuxDB: Overview, Key Concepts and Demo** – YouTube](https://youtu.be/gb6AiqCJqP0)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

