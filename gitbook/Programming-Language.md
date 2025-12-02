## Programming Language

At this stage you have to choose one programming language to study. There is plenty of information on various languages in the Internet (books, courses, thematic sites, etc.), so you should have no problem finding information.

> Below is a list of specific languages that [personally, in my opinion](https://github.com/cheatsnake) are good for backend development (⚠️ may not agree with the opinions of others, including those more competent in this matter).

-   [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)
    > A very popular language with a wide range of applications. Easy to learn due to its simple syntax.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    > No less popular and practically the only language for full-fledged Web-development. Thanks to the platform [Node.js](https://en.wikipedia.org/wiki/Node.js) last few years is gaining popularity in the field of backend development as well.
-   [Go](<https://en.wikipedia.org/wiki/Go_(programming_language)>)
    > A language created internally by Google. It was created specifically for high-load server development. Minimalist syntax, high performance and rich standard library.
-   [Kotlin](<https://en.wikipedia.org/wiki/Kotlin_(programming_language)>)
    > A kind of modern version of [Java](<https://en.wikipedia.org/wiki/Java_(programming_language)>). Simpler and more concise syntax, better type-safety, built-in tools for multi-threading. One of the best choices for Android development.

Find a good book or online tutorial in English at [this repository](https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-langs.md). There is a large collection for different languages and frameworks.

Look for a special [awesome repository](https://github.com/sindresorhus/awesome#programming-languages) - a resource that contains a huge number of useful links to materials for your language (libraries, cheat sheets, blogs, and other various resources).

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Classification of programming languages

    There are many programming languages. They are all created for a reason. Some languages may be very specific and used only for certain purposes. Also, different languages may use different approaches to writing programs. They may even run differently on a computer. In general, there are many different [classifications](https://en.wikipedia.org/wiki/Category:Programming_language_classification), which would be useful to understand.

    -   Depending on language level
        -   [Low level languages](https://en.wikipedia.org/wiki/Low-level_programming_language)
            > As close to [machine code](https://en.wikipedia.org/wiki/Machine_code), complex to write, but as productive as possible. As a rule, it provides access to all of the computer's resources.
        -   [High-level languages](https://en.wikipedia.org/wiki/High-level_programming_language)
            > They have a fairly high level of abstraction, which makes them easy to write and easy to use. As a rule, they are safer because they do not provide access to all of the computer's resources.
    -   Depending on [implementation](https://en.wikipedia.org/wiki/Programming_language_implementation)
        -   [Compilation](https://en.wikipedia.org/wiki/Compiler)
            > Allows you to convert the source code of a program to an executable file.
        -   [Interpretation](<https://en.wikipedia.org/wiki/Interpreter_(computing)>)
            > The source code of a program is translated and immediately executed (interpreted) by a special interpreter program.
        -   [Virtual machine](https://en.wikipedia.org/wiki/Virtual_machine)
            > In this approach, the program is not compiled into a machine code, but into machine-independent low-level code - [bytecode](https://en.wikipedia.org/wiki/Bytecode). This bytecode is then executed by the virtual machine itself.
    -   [Depending on the programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)
        -   [Imperative](https://en.wikipedia.org/wiki/Imperative_programming)
            > Focuses on describing the steps to solve a problem through a sequence of statements or commands.
        -   [Declarative](https://en.wikipedia.org/wiki/Declarative_programming)
            > Focuses on describing what the program should do, rather than how it should do it. Examples of declarative languages include SQL and HTML.
        -   [Functional](https://en.wikipedia.org/wiki/Functional_programming)
            > Based on the idea of treating computation as the evaluation of mathematical functions. It emphasizes [immutability](https://en.wikipedia.org/wiki/Immutable_object), avoiding [side effects](https://en.wikipedia.org/wiki/Side_effect_(computer_science)), and using [higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function). Examples of functional languages include Haskell, Lisp, and Clojure.
        -   [Object-Oriented](https://en.wikipedia.org/wiki/Object-oriented_programming)
            > Revolves around creating objects that contain both data and behavior, with the goal of modeling real-world concepts. Examples of object-oriented languages include Java, Python, and C++.
        -   [Concurrent](https://en.wikipedia.org/wiki/Concurrent_computing)
            > Focused on handling multiple tasks or threads at the same time, and is used in systems that require high performance and responsiveness. Examples of concurrent languages include Go and Erlang.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Classifying Programming Languages**](https://cs.lmu.edu/~ray/notes/pltypes/)
2. 📺 [**What are the Types of Programming Languages?** – YouTube](https://youtu.be/Mo4vesaut8g)
3. 📺 [**Functional Programming in 40 Minutes** – YouTube](https://youtu.be/0if71HOyVjY)
4. 📺 [**The Art of Functional Programming** – YouTube](https://youtu.be/pNIWiTdsPV4)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Language Basics

    By foundations are meant some fundamental ideas present in every language.

    -   Variables and constants
        > Are names assigned to a memory location in the program to store some data.
    -   Data types
        > Define the type of data that can be stored in a variable. The main data types are integers, floating point numbers, symbols, strings, and boolean.
    -   Operators
        > Used to perform operations on variables or values. Common operators include arithmetic operators, comparison operators, logical operators, and assignment operators.
    -   Flow control
        > Loops, conditions `if else`, `switch case` statements.
    -   Functions
        > Are blocks of code that can be called multiple times in a program. They allow for code reusability and modularization. Functions are an important concept for understanding the scope of variables.
    -   Data structures
        > Special containers in which data are stored according to certain rules. Main data structures are arrays, maps, trees, graphs.
    -   Standard library
        > This refers to the language's built-in features for manipulating data structures, working with the file system, network, cryptography, etc.
    -   Error handling
        > Used to handle unexpected events that can occur during program execution.
    -   [Regular expressions](https://github.com/cheatsnake/regex-by-example)
        > A powerful tool for working with strings. Be sure to familiarize yourself with it in your language, at least on a basic level.
    -   Modules
        > Writing the code of the whole program in one file is not at all convenient. It is much more readable to break it up into smaller modules and import them into the right places.
    -   Package Manager
        > Sooner or later, there will be a desire to use third-party libraries.

    After mastering the minimal base for writing the simplest programs, there is not much point in continuing to learn without having specific goals (without practice, everything will be forgotten). You need to think of/find something that you would like to create yourself (a game, a chatbot, a website, a mobile/desktop application, whatever). For inspiration, check out these repositories: [Build your own x](https://github.com/codecrafters-io/build-your-own-x) and [Project based learning](https://github.com/practical-tutorials/project-based-learning).

    At this point, the most productive part of learning begins: You just look for all kinds of information to implement your project. Your best friends are Google, YouTube, and Stack Overflow.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**CS50 2022 – Harvard University's course about programming** – YouTube](https://youtube.com/playlist?list=PLeLzIg9tqA3LQW-RiFA8zJUBcTKqUVLMU)
2. 📺 [**Harvard CS50’s Web Programming with Python and JavaScript** – YouTube](https://youtu.be/vzGllw18DkA)
3. 📄 [**Free Interactive Python Tutorial**](https://www.learnpython.org/)
4. 📺 [**Harvard CS50’s Introduction to Programming with Python** – YouTube](https://youtu.be/nLRL_NcnK-4)
5. 📺 [**Python Tutorial for Beginners** – YouTube](https://youtu.be/8124kv-632k)
6. 📄 [**Python cheatsheet** – Learn X in Y minutes](https://learnxinyminutes.com/docs/python/)
7. 📄 [**Python cheatsheet** – quickref.me](https://quickref.me/python)
8. 📄 [**Free Interactive JavaScript Tutorial**](https://www.learn-js.org/)
9. 📺 [**JavaScript Programming - Full Course** – YouTube](https://youtu.be/jS4aFq5-91M)
10. 📄 [**The Modern JavaScript Tutorial**](https://javascript.info/)
11. 📄 [**JavaScript cheatsheet** – Learn X in Y minutes](https://learnxinyminutes.com/docs/javascript/)
12. 📄 [**JavaScript cheatsheet** – quickref.me](https://quickref.me/javascript)
13. 📄 [**Go Tour – learn most important features of the language**](https://go.dev/tour/list)
14. 📺 [**Learn Go Programming - Go Tutorial for Beginners** – YouTube](https://youtu.be/YS4e4q9oBaU)
15. 📄 [**Go cheatsheet** – Learn X in Y minutes](https://learnxinyminutes.com/docs/go/)
16. 📄 [**Go cheatsheet** – quickref.me](https://quickref.me/golang)
17. 📄 [**Learn Go by Examples**](https://golangbyexample.com/)
18. 📄 [**Get started with Kotlin**](https://kotlinlang.org/docs/getting-started.html)
19. 📺 [**Learn Kotlin Programming – Full Course for Beginners** – YouTube](https://youtu.be/EExSSotojVI)
20. 📄 [**Kotlin cheatsheet** – Learn X in Y minutes](https://learnxinyminutes.com/docs/kotlin/)
21. 📄 [**Kotlin cheatsheet** – devhints.io](https://devhints.io/kotlin)
22. 📄 [**Learn Regex step by step, from zero to advanced**](https://regexlearn.com)
23. 📄 [**Projectbook – The Great Big List of Software Project Ideas**](https://projectbook.code.brettchalupa.com/)
</details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Object-oriented programming

    [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) is one of the most successful and convenient approaches for modeling real-world things. This approach combines several very important principles which allow writing modular, extensible, and loosely coupled code.

    -   Understanding [Classes](<https://en.wikipedia.org/wiki/Class_(computer_programming)>)
        > A class can be understood as a custom data type (a kind of template) in which you describe the structure of future objects that will implement the class. Classes can contain `properties` (these are specific fields in which data of a particular data type can be stored) and `methods` (these are functions that have access to properties and the ability to manipulate, modify them).
    -   Understanding [objects](<https://en.wikipedia.org/wiki/Object_(computer_science)>)
        > An object is a specific implementation of a class. If, for example, the _name_ property with type _string_ is described in a class, the object will have a specific value for that field, for example _"Alex"_.
    -   [Inheritance principle](<https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)>)
        > Ability to create new classes that inherit properties and methods of their parents. This allows you to reuse code and create a hierarchy of classes.
    -   [Encapsulation principle](<https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)>)
        > Ability to hide certain properties/methods from external access, leaving only a simplified interface for interacting with the object.
    -   [Polymorphism principle](<https://en.wikipedia.org/wiki/Polymorphism_(computer_science)>)
        > The ability to implement the same method differently in descendant classes.
    -   [Composition](https://en.wikipedia.org/wiki/Composition_over_inheritance) over inheritance
        > Often the principle of `inheritance` can complicate and confuse your program if you do not think carefully about how to build the future hierarchy. That is why there is an alternative (more flexible) approach called composition. In particular, Go language lacks classes and many OOP principles, but widely [uses composition](https://golangbyexample.com/oop-inheritance-golang-complete).
    -   [Dependency injection (DI)](https://en.wikipedia.org/wiki/Dependency_injection)
        > Dependency injection is a popular OOP pattern that allows objects to receive their dependencies (other objects) from the outside rather than creating them internally. It promotes loose coupling between classes, making code more modular, maintainable, and easier to test.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Intro to Object Oriented Programming - Crash Course** – YouTube](https://youtu.be/SiBw7os-_zI)
2. 📄 [**OOP Meaning – What is Object-Oriented Programming?** – freeCodeCamp](https://www.freecodecamp.org/news/what-is-object-oriented-programming/)
3. 📺 [**OOP in Python (CS50 lecture)** – YouTube](https://youtu.be/SiBw7os-_zI)
4. 📄 [**OOP tutorial from Python docs**](https://docs.python.org/3/tutorial/classes.html)
5. 📺 [**OOP in JavaScript: Made Super Simple** – YouTube](https://youtu.be/PFmuCDHHpwk)
6. 📄 [**OOP in Go by examples**](https://golangbyexample.com/golang-comprehensive-tutorial/#OOPS_in_Golang)
7. 📺 [**Object Oriented Programming is not what I thought - Talk by Anjana Vakil** – YouTube](https://youtu.be/TbP2B1ijWr8)
8. 📺 [**The Flaws of Inheritance (tradeoffs between Inheritance and Composition)** – YouTube](https://youtu.be/hxGOiiR9ZKg)
9. 📺 [**Dependency Injection, The Best Pattern** – YouTube](https://youtu.be/J1f5b4vcxCQ?si=9kgJNwZgMFd7r7fX)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Server development

    -   Understand sockets
        > A socket is an endpoint of a two-way communication link between two programs running over a network. You need to know how to create, connect, send, and receive data over sockets.
    -   Running a local TCP, UDP and HTTP servers
        > These protocols are the most important, you need to understand the intricacies of working with each of them.
    -   Handing out static files
        > You need to know how to host HTML pages, pictures, PDF documents, music/video files, etc.
    -   Routing
        > Creation of endpoints (URLs) which will call the appropriate handler on the server when accessed.
    -   Processing requests
        > As a rule, HTTP handlers have a special object which receives all information about user request (headers, method, request body, query parameters and so on)
    -   Processing responses
        > Sending an appropriate message to a received request (HTTP status and code, response body, headers, etc.)
    -   Error handling
        > You should always be prepared for the possibility that something will go wrong: the user will send incorrect data, the database will not perform the operation, or an unexpected error will simply occur in the application. It is necessary for the server not to crash, but to send a response with information about the error.
    -   [Middleware](https://www.ibm.com/topics/middleware)
        > An intermediate component between the application and the server. It used for handling authentication, validation, caching data, logging requests, and so on.
    -   Sending requests
        > Often, within one application, you will need to access another application over the network. That's why it's important to be able to send HTTP requests using the built-in features of the language.
    -   [Template processor](https://en.wikipedia.org/wiki/Template_processor)
        > Is a special module that uses a more convenient syntax to generate HTML based on dynamic data.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Learn Django – Python-based web framework**](https://www.djangoproject.com/start/)
2. 📺 [**Python Django 7 Hour Course** – YouTube](https://youtu.be/PtQiiknWUcI)
3. 📄 [**A curated list of awesome things related to Django** – GitHub](https://github.com/wsvincent/awesome-django)
4. 📺 [**Python Web Scraping for Beginners** – YouTube](https://youtu.be/mBoX_JCKZTE)
5. 📺 [**Build servers in pure Node.js** – YouTube](https://youtu.be/_1xa8Bsho6A)
6. 📄 [**Node.js HTTP Server Examples – GitHub**](https://github.com/HowProgrammingWorks/NodeServer)
7. 📄 [**Learn Express – web framework for Node.js**](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs)
8. 📺 [**Express.js 2022 Course** – YouTube](https://youtube.com/playlist?list=PL_cUvD4qzbkwp6pxx27pqgohrsP8v1Wj2)
9. 📄 [**A curated list of awesome Express.js resources** – GitHub](https://github.com/rajikaimal/awesome-express)
10. 📄 [**How to build servers in Go**](https://eli.thegreenplace.net/2021/rest-servers-in-go-part-1-standard-library/)
11. 📺 [**Golang server development course** – YouTube](https://youtube.com/playlist?list=PLzUGFf4GhXBL4GHXVcMMvzgtO8-WEJIoY)
12. 📄 [**Web services in Go** – GitBook](https://astaxie.gitbooks.io/build-web-application-with-golang/content/en/08.0.html)
13. 📄 [**List of libraries for working with network in Go** – GitHub](https://github.com/avelino/awesome-go#networking)
14. 📄 [**Learn Ktor – web framework for Kotlin**](https://ktor.io/learn/)
15. 📺 [**Ktor - REST API Tutorials** – YouTube](https://youtube.com/playlist?list=PLFmuMD2V4CkyR0Pa42Cqu5mIhH17uG8nN)
16. 📄 [**Kotlin for server side**](https://kotlinlang.org/docs/server-overview.html)
</details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Asynchronous programming

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

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Multitasking

    Computers today have processors with several physical and virtual cores, and if we take into account server machines, their number can reach up to hundreds. All of these available resources would be good to use to the fullest, for maximum application performance. That is why modern server development cannot do without implementing [multitasking](https://en.wikipedia.org/wiki/Computer_multitasking) and [paralleling](https://en.wikipedia.org/wiki/Parallel_computing).

    -   How it works
        > Multitasking refers to the concurrent execution of multiple [threads](#processes-and-threads) of control within a single program. A thread is a lightweight process that runs within the context of a [process](#processes-and-threads), and has its own stack, program counter, and register set. Multiple threads can share the resources of a single process, such as memory, files, and I/O devices. Each thread executes independently and can perform a different task or part of a task.
    -   Multitasking types
        > - [Cooperative multitasking](https://en.wikipedia.org/wiki/Cooperative_multitasking): each program or task voluntarily gives up control of the CPU to allow other programs or tasks to run. Each program or task is responsible for yielding control to other programs or tasks at appropriate times. This approach requires programs or tasks to be well-behaved and to avoid monopolizing the CPU. If a program or task does not yield control voluntarily, it can cause the entire system to become unresponsive. Cooperative multitasking was commonly used in early operating systems and is still used in some embedded systems or real-time operating systems.
        > - [Preemptive multitasking](https://en.wikipedia.org/wiki/Preemption_(computing)): operating system forcibly interrupts programs or tasks at regular intervals to allow other programs or tasks to run. The operating system is responsible for managing the CPU and ensuring that each program or task gets a fair share of CPU time. This approach is more robust than cooperative multitasking and can handle poorly behaved programs or tasks that do not yield control. Preemptive multitasking is used in modern operating systems, such as Windows, macOS, Linux, and Android.
    -   Main problems and difficulties
        > - [Race conditions](https://en.wikipedia.org/wiki/Race_condition): When multiple threads access and modify shared data concurrently, race conditions can occur, resulting in unpredictable behavior or incorrect results.
        > - [Deadlocks](https://en.wikipedia.org/wiki/Deadlock): Occur when two or more threads are blocked waiting for resources that are held by other threads, resulting in a deadlock.
        > - Debugging: Multitasking programs can be difficult to debug due to their complexity and non-deterministic behavior. You need to use advanced debugging tools and techniques, such as thread dumps, profilers, and logging, to diagnose and fix issues.
    -   Synchronizing primitives
        > Needed to securely exchange data between different threads.
        > - [Semaphore](https://en.wikipedia.org/wiki/Semaphore_(programming)): It is essentially a counter that keeps track of the number of available resources and can block threads or processes that try to acquire more than the available resources.
        > - [Mutex](https://en.wikipedia.org/wiki/Mutual_exclusion): (short for mutual exclusion) allows only one thread or process to access the resource at a time, ensuring that there are no conflicts or race conditions.
        > - [Atomic operations](https://en.wikipedia.org/wiki/Linearizability): operations that are executed as a single, indivisible unit, without the possibility of interruption or interference by other threads or processes.
        > - [Condition variables](https://en.wikipedia.org/wiki/Monitor_(synchronization)): allows threads to wait for a specific condition to be true before continuing execution. It is often used in conjunction with a mutex to avoid busy waiting and improve efficiency.
    -   Working with particular language
        > - In Python you can see [threading](https://docs.python.org/3/library/threading.html) and [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) modules.
        > - In Node.js you can work with [worker threads](https://nodejs.org/api/worker_threads.html#worker-threads), [cluster module](https://nodejs.org/api/cluster.html#cluster) and [shared array buffers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer).
        > - Go has incredible [goroutines and channels](https://go.dev/tour/concurrency/1).
        > - Kotlin provides [coroutines](https://kotlinlang.org/docs/coroutines-overview.html).

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Multithreading Code - Computerphile** – YouTube](https://youtu.be/7ENFeb-J75k)
2. 📺 [**Threading vs. multiprocessing in Python** – YouTube](https://youtu.be/AZnGRKFUU0c)
3. 📺 [**When is Node.js Single-Threaded and when is it Multi-Threaded?** – YouTube](https://youtu.be/gMtchRodC2I)
4. 📺 [**How to use Multithreading with "worker threads" in Node.js?** – YouTube](https://youtu.be/MuwJJrfIfsU)
5. 📺 [**Concurrency in Go** – YouTube](https://youtube.com/playlist?list=PLsc-VaxfZl4do3Etp_xQ0aQBoC-x5BIgJ)
6. 📺 [**Kotlin coroutines** – YouTube](https://youtube.com/playlist?list=PLQkwcJG4YTCQcFEPuYGuv54nYai_lwil_)
7. 📄 [**Multithreading in practice** – GitHub](https://github.com/thanhit95/multi-threading)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Advanced Topics

    -   [Garbage collector](<https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)>)
        > A process that has made high-level languages very popular - it allows the programmer not to worry about memory allocation and freeing. Be sure to familiarize yourself with the subtleties of its operation in your own language.
    -   [Debugger](https://en.wikipedia.org/wiki/Debugging)
        > Handy tool for analyzing program code and identifying errors.
    -   [Compilers](https://en.wikipedia.org/wiki/Compiler), [interpreters](https://en.wikipedia.org/wiki/Interpreter_(computing)) and [virtual machines](https://en.wikipedia.org/wiki/Virtual_machine)
        > Depending on what your language uses, you can explore in detail the process of converting your code to machine code (a set of zeros and ones). As a rule, compilation/interpretation/virtualization processes consist of several steps. By understanding them you can optimize your programs for faster builds and efficient execution.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Garbage Collection (Mark & Sweep)** – YouTube](https://youtu.be/c32zXYAK7CI)
2. 📺 [**How to Use a Debugger - Debugger Tutorial** – YouTube](https://youtu.be/7qZBwhSlfOo)
3. 📄 [**Understanding The Python Interpreter** – medium](https://medium.com/fintechexplained/understanding-the-python-interpreter-7ecf8ac9f34c)
4. 📄 [**How Node.js works - JavaScript runtime environment** – freeCodeCamp](https://www.freecodecamp.org/news/what-exactly-is-node-js-ae36e97449f5/)
5. 📄 [**How Compilers Work**](https://www.baeldung.com/cs/how-compilers-work)
6. 📄 [**The Magic Behind Compilers** – medium](https://medium.com/swlh/the-magic-behind-compilers-part-1-f99bf45688f7)
7. 📄 [**Overview of the сompiler in Go** – medium](https://medium.com/swlh/the-magic-behind-compilers-part-1-f99bf45688f7)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Code quality

    During these long years that programming has existed, a huge amount of code, programs, and entire systems have been written. And as a consequence, there have been all sorts of problems in the development of all this. First of all they were related to scaling, support, and the entry threshold for new developers. Clever people, of course, did not sit still and started to solve these problems, thus creating so-called patterns/principles/approaches for writing high-quality code.

    By learning programming best practices, you will not only make things better for yourself, but also for others, because other developers will be working with your code.

    -   [DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
    -   [KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)
    -   [YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)
    -   [SOLID principles](https://en.wikipedia.org/wiki/SOLID)
    -   [GRASP (General Responsibility Assignment Software Patterns)](<https://en.wikipedia.org/wiki/GRASP_(object-oriented_design)>)

    For many languages there are special style guides and coding conventions. They usually compare the right and wrong way of writing code and explain why this is the case.

    -   [Python style guide by Google](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
    -   [Python best practices guidebook](https://github.com/realpython/python-guide)
    -   [JavaScript style guide by Airbnb](https://github.com/airbnb/javascript)
    -   [Node.js best practices list](https://github.com/goldbergyoni/nodebestpractices)
    -   [Effective Go - official coding conventions](https://go.dev/doc/effective_go)
    -   [Go style guide by Uber](https://github.com/uber-go/guide)
    -   [Kotlin official coding conventions](https://kotlinlang.org/docs/coding-conventions.html)
    -   [and other…](https://github.com/kciter/awesome-style-guide)

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**KISS, SOLID, YAGNI And Other Fun Acronyms**](https://blog.bitsrc.io/kiss-solid-yagni-and-other-fun-acronyms-b5d207530335)
2. 📺 [**Naming Things in Code** – YouTube](https://youtu.be/-J3wNP6u5YU)
3. 📺 [**Why You Shouldn't Nest Your Code** – YouTube](https://youtu.be/CFRhGnuXG-4)
4. 📺 [**Why you shouldn't write comments in your code** – YouTube](https://youtu.be/Bf7vDBBOBUA)
5. 📺 [**How principled coders outperform the competition** – YouTube](https://youtu.be/q1qKv5TBaOA)
6. 📺 [**Uncle Bob SOLID principles** – YouTube](https://youtu.be/zHiWqnTWsn4)
7. 📄 [**SOLID Principles explained in Python** – medium](https://towardsdev.com/solid-principles-explained-635ad3608b20)
8. 📄 [**SOLID Principles in JavaScript** – freeCodeCamp](https://www.freecodecamp.org/news/solid-principles-for-programming-and-software-design/)
9. 📄 [**Google style guides** – GitHub](https://github.com/google/styleguide)

 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

