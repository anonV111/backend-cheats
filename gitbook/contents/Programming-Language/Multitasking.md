### Multitasking

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


