### Monitoring and logs

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



