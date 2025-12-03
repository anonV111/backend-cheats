### Benchmarks

[Benchmark](<https://en.wikipedia.org/wiki/Benchmark_(computing)>) (in software) is a tool for measuring the execution time of program code. As a rule, the measurement is done by multiple runs of the same code (or a certain part of it), where the average time is then calculated, and can also provide information about the number of operations performed and the amount of memory allocated.

-   What is it for?
    > Benchmarks are useful for both evaluating performance and choosing the most effective solution to the problem at hand.
-   What specific tools are there for this?
    > For Python: [timeit](https://docs.python.org/3/library/timeit.html), [pytest-benchmark](https://github.com/ionelmc/pytest-benchmark). <br>
    > For Node.js: [console.time](https://nodejs.org/api/console.html#consoletimelabel), [Artillery](https://github.com/artilleryio/artillery). <br>
    > For Go: [testing.B](https://pkg.go.dev/testing#hdr-Benchmarks), [Benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat).

There are benchmarks to measure the performance of networked applications, where you can get detailed information about the average request processing time, the maximum number of supported connections, data transfer rates and so on ([see list of HTTP benchmarks](https://github.com/denji/awesome-http-benchmark)).

<details>
<summary>🔗 <b>References</b></summary>

1. 📺 [**Premature Optimization** – YouTube](https://youtu.be/tKbV6BpH-C8)
2. 📺 [**Professional Benchmarking in Python** – YouTube](https://youtu.be/DBoobQxqiQw)
3. 📺 [**JavaScript tips — Measuring performance using console.time** – YouTube](https://youtu.be/WumrqNOO8dk)
4. 📺 [**Go (Golang) Benchmark Tutorial** – YouTube](https://youtu.be/L-BkH-_lXpk)
 </details>


