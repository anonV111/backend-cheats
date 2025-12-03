### Asynchronous programming

[Asynchronous programming](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)) is an efficient way to write programs with a large number of [I/O (input/output) operations](https://en.wikipedia.org/wiki/Input/output). Such operations may include reading files, requesting to a database or remote server, reading user input, and so on. In these cases, the program spends a lot of time waiting for external resources to respond, and asynchronous programming allows the program to perform other tasks while waiting for the response.

-   [Callback](https://en.wikipedia.org/wiki/Callback_(computer_programming))
    > This is function that is passed as an argument to another function and is intended to be called by that function at a later time. The purpose of a callback is to allow the calling function to continue executing while the called function performs a time-consuming or asynchronous task. Once the task is complete, the called function will invoke the callback function, passing it any necessary data as arguments.
-   [Event-driven architecture (EDA)](https://en.wikipedia.org/wiki/Event-driven_architecture)
    > A popular approach to writing asynchronous programs. The logic of the program is to wait for certain events and process them as they arrive. This can be useful in web applications that need to handle a large number of concurrent connections, such as chat applications or real-time games.
-   Asynchronous in particular languages
    > - In Python, asynchronous programming can be done using the [asyncio module](https://docs.python.org/3/library/asyncio.html), which provides an event loop and coroutine-based API for concurrency. There are also other third-party libraries like [Twisted](https://github.com/twisted/twisted) and [Tornado](https://github.com/tornadoweb/tornado) that provide asynchronous capabilities.
    > - In JavaScript, asynchronous programming is commonly achieved through the use of [promises](https://javascript.info/promise-basics), [callbacks](https://javascript.info/callbacks), [async/await syntax](https://javascript.info/async-await) and the [event loop](https://javascript.info/event-loop).
    > - Go has built-in support for concurrency through [goroutines and channels](https://go.dev/tour/concurrency/1), which allow developers to write asynchronous code that can communicate and synchronize across multiple threads.
    > - Kotlin provides [coroutines](https://kotlinlang.org/docs/coroutines-overview.html) are similar to JavaScript's async/await and Python's asyncio, and can be used with a variety of platforms and frameworks.

<details>
<summary>🔗 <b>References</b></summary>

1. 📺 [**Synchronous vs. Asynchronous Applications (Explained by Example)** – YouTube](https://youtu.be/N5Ky-mz6n-8)
2. 📄 [**Async IO in Python: A Complete Walkthrough**](https://realpython.com/async-io-python/)
3. 📄 [**Asynchronous Programming in JavaScript – Guide for Beginners** – freeCodeCamp](https://www.freecodecamp.org/news/asynchronous-programming-in-javascript/)
4. 📄 [**A roadmap for asynchronous programming in JavaScript**](https://exploringjs.com/impatient-js/ch_async-js.html#roadmap-async-functions)
5. 📺 [**Master Go Programming With These Concurrency Patterns** – YouTube](https://youtu.be/qyM8Pi1KiiM)
6. 📺 [**Kotlin coroutines: new ways to do asynchronous programming** – YouTube](https://youtu.be/WlGEOu-Ka-E)
 </details>


