## PC device

-   ### Main components (hardware)

    -   [Motherboard](https://en.wikipedia.org/wiki/Motherboard)
        > The most important PC component to which all other elements are connected.
        >
        > -   [Chipset](https://en.wikipedia.org/wiki/Chipset) - set of electronic components that responsible for the communication of all motherboard components.
        > -   [CPU socket](https://en.wikipedia.org/wiki/CPU_socket) - socket for mounting the processor.
        > -   [VRM (Voltage Regulator Module)](https://en.wikipedia.org/wiki/Voltage_regulator_module) – module that converts the incoming voltage (usually 12V) to a lower voltage to run the processor, integrated graphics, memory, etc.
        > -   Slots for RAM.
        > -   Expansion slots [PCI-Express](https://en.wikipedia.org/wiki/PCI_Express) - designed for connection of video cards, external network/sound cards.
        > -   Slots [M.2](https://en.wikipedia.org/wiki/M.2) / [SATA](https://en.wikipedia.org/wiki/SATA) - designed to connect hard disks and SSDs.
    -   [CPU (Central processing unit)](https://en.wikipedia.org/wiki/Central_processing_unit)
        > The most important device that executes instructions (programme code). Processors only work with 1 and 0, so all programmes are ultimately a set of binary code.
        >
        > -   [Registers](https://en.wikipedia.org/wiki/Processor_register) - the fastest memory in a PC, has an extremely small capacity, is built into the processor and is designed to temporarily store the data being processed.
        > -   [Cache](https://en.wikipedia.org/wiki/CPU_cache) - slightly less fast memory, which is also built into the processor and is used to store a copy of data from frequently used cells in the main memory.
        > -   Processors can have different [architectures](https://en.wikipedia.org/wiki/Processor_design). Currently, the most common are the [x86](https://en.wikipedia.org/wiki/X86-64) architecture (desktop and laptop computers) and [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family) (mobile devices as well as the latest Apple computers).
    -   [RAM (Random-access memory)](https://en.wikipedia.org/wiki/Random-access_memory)
        > Fast, low capacity memory (4-16GB) designed to temporarily store program code, as well as input, output and intermediate data processed by the processor.
    -   [Data storage](https://en.wikipedia.org/wiki/Data_storage)
        > Large capacity memory (256GB-1TB) designed for long-term storage of files and installed programmes.
    -   [GPU (Graphics card)](https://en.wikipedia.org/wiki/Graphics_card)
        > A separate card that translates and processes data into images for display on a monitor. This device is also called a discrete graphics card. Usually needed for those who do 3D modelling or play games. <br> [Built-in graphics card](https://en.wikipedia.org/wiki/Graphics_processing_unit#Integrated_graphics_processing_unit) is a graphics card built into the processor. It is suitable for daily work.
    -   [Network card](https://en.wikipedia.org/wiki/Network_interface_controller)
        > A device that receives and transmits data from other devices connected to the [local network](https://en.wikipedia.org/wiki/Local_area_network).
    -   [Sound card](https://en.wikipedia.org/wiki/Sound_card)
        > A device that allows you to process sound, output it to other devices, record it with a microphone, etc.
    -   [Power supply unit](<https://en.wikipedia.org/wiki/Power_supply_unit_(computer)>)
        > A device designed to convert the AC voltage from the mains to DC voltage.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Everything You Need to Know About Computer Hardware**](https://www.lifewire.com/computer-hardware-2625895)
2. 📄 [**Putting the "You" in CPU: explainer how your computer runs programs, from start to finish**](https://github.com/hackclub/putting-the-you-in-cpu)
3. 📺 [**What does what in your computer? Computer parts Explained** – YouTube](https://youtu.be/ExxFxD4OSZ0)
4. 📺 [**Motherboards Explained** – YouTube](https://youtu.be/b2pd3Y6aBag)
5. 📺 [**The Fetch-Execute Cycle: What's Your Computer Actually Doing?** – YouTube](https://youtu.be/Z5JC9Ve1sfI)
6. 📺 [**How a CPU Works in 100 Seconds // Apple Silicon M1 vs. Intel i9** – YouTube](https://youtu.be/vqs_0W-MSB0)
7. 📺 [**Arm vs. x86 - Key Differences Explained** – YouTube](https://youtu.be/AADZo73yrq4)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Operating system design

    <p align="center"><img src="./files/os/os-layer_eng.png" alt="OS"/></p>

    [Operating system (OS)](https://en.wikipedia.org/wiki/Operating_system) is a comprehensive software system designed to manage a computer's resources. With operating systems, people do not have to deal directly with the processor, RAM, or other parts of the PC.

    OS can be thought of as an abstraction layer that manages the hardware of a computer, thereby providing a simple and convenient environment for user software to run.

    -   Main features
        > -   RAM management (space allocation for individual programs)
        > -   Loading programs into RAM and their execution
        > -   Execution of requests from user's programs (inputting and outputting data, starting and stopping other programs, freeing up memory or allocating additional memory, etc.)
        > -   Interaction with input and output devices (mouse, keyboard, monitor, etc.)
        > -   Interaction with storage media (HDDs and SSDs)
        > -   Providing a user's interface (console shell or graphical interface)
        > -   Logging of software errors (saving logs)
    -   Additional functions (may not be available in all OSs)
        > -   Organize [multitasking](https://en.wikipedia.org/wiki/Computer_multitasking) (simultaneous execution of several programs)
        > -   Delimiting access to resources for each process
        > -   [Inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) (data exchange, synchronisation)
        > -   Organize the protection of the operating system itself against other programs and the actions of the user
        > -   Provide multi-user mode and differentiate rights between different OS users (admins, guests, etc.)
    -   [OS kernel](<https://en.wikipedia.org/wiki/Kernel_(operating_system)>)
        > The central part of the operating system which is used most intensively. The kernel is constantly in memory, while other parts of the OS are loaded into and unloaded from memory as needed.
    -   [Bootloader](https://en.wikipedia.org/wiki/Bootloader)
        > The system software that prepares the environment for the OS to run (puts the hardware in the right state, prepares the memory, loads the OS kernel there and transfers control to it (the kernel).
    -   [Device drivers](https://en.wikipedia.org/wiki/Device_driver)
        > Special software that allows the OS to work with a particular piece of equipment.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**What is an OS? Operating System Definition for Beginners** – freeCodeCamp](https://www.freecodecamp.org/news/what-is-an-os-operating-system-definition-for-beginners/)
2. 📄 [**Windows vs. macOS vs. Linux – Operating System Handbook** – freeCodeCamp](https://www.freecodecamp.org/news/an-introduction-to-operating-systems/)
3. 📺 [**Operating Systems: Crash Course Computer Science** – YouTube](https://youtu.be/26QPDBe-NB8)
4. 📺 [**Operating System Basics** – YouTube](https://youtu.be/9GDX-IyZ_C8)
5. 📺 [**Operating System in deep details (playlist)** – YouTube](https://youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O)
6. 📄 [**Awesome Operating System Stuff** – GitHub](https://github.com/jubalh/awesome-os)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Processes and threads

    <p align="center"><img src="./files/os/process_eng.png" alt="Process"/></p>

    -   [Process](<https://en.wikipedia.org/wiki/Process_(computing)>)
        > A kind of container in which all the resources needed to run a program are stored. As a rule, the process consists of:
        >
        > -   Executable program code <br>
        > -   Input and output data <br>
        > -   [Call stack](https://en.wikipedia.org/wiki/Call_stack) (order of instructions for execution) <br>
        > -   [Heap](https://en.wikipedia.org/wiki/Memory_management#Manual_memory_management) (a structure for storing intermediate data created during the process) <br>
        > -   [Segment descriptor](https://en.wikipedia.org/wiki/Segment_descriptor) <br>
        > -   [File descriptor](https://en.wikipedia.org/wiki/File_descriptor) <br>
        > -   Information about the set of permissible powers <br>
        > -   Processor status information
    -   [Thread](<https://en.wikipedia.org/wiki/Thread_(computing)>)
        > An entity in which sequences of program actions (procedures) are executed. Threads are within a process and use the same address space. There can be multiple threads in a single process, allowing multiple tasks to be performed. These tasks, thanks to threads, can exchange data, use shared data or the results of other tasks.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Difference Between Process and Thread** – YouTube](https://youtu.be/O3EyzlZxx3g)
2. 📺 [**How Do CPUs Use Multiple Cores** – YouTube](https://youtu.be/S3I5WNHbnJ0)
3. 📺 [**What is Hyper Threading Technology** – YouTube](https://youtu.be/wnS50lJicXc)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Concurrency and parallelism

    <p align="center"><img src="./files/os/concurrency-parallel.png" alt="Concurrency-parallelism"/></p>

    -   [Parallelism](https://en.wikipedia.org/wiki/Parallel_computing)
        > The ability to perform multiple tasks simultaneously using multiple processor cores, where each individual core performs a different task.
    -   [Concurrency](<https://en.wikipedia.org/wiki/Concurrency_(computer_science)>)
        > The ability to perform multiple tasks, but using a single processor core. This is achieved by dividing tasks into separate blocks of commands which are executed in turn, but switching between these blocks is so fast that for users it seems as if these processes are running simultaneously.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Concurrency, parallelism, and the many threads of Santa Claus** – freeCodeCamp](https://www.freecodecamp.org/news/concurrency-parallelism-and-the-many-threads-of-santa-claus/)
2. 📺 [**Concurrency vs. Parallelism** – YouTube](https://youtu.be/Y1pgpn2gOSg)
3. 📺 [**Concurrency is not Parallelism by Rob Pike** – YouTube](https://youtu.be/oV9rvDllKEg)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Inter-process communication

    A mechanism which allows to exchange data between threads of one or different processes. Processes can be run on the same computer or on different computers connected by a network. [Inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) can be done in different ways.

    -   [File](https://en.wikipedia.org/wiki/Computer_file)
        > The easiest way to exchange data. One process writes data to a certain file, another process reads the same file and thus receives data from the first process.
    -   [Signal (IPC)](<https://en.wikipedia.org/wiki/Signal_(IPC)>)
        > Asynchronous notification of one process about an event which occurred in another process.
    -   [Network socket](https://en.wikipedia.org/wiki/Network_socket)
        > In particular, IP addresses and ports are used to communicate between computers using the TCP/IP protocol stack. This pair defines a socket (_socket_ corresponding to the address and port).
    -   [Semaphore](<https://en.wikipedia.org/wiki/Semaphore_(programming)>)
        > A counter over which only 2 operations can be performed: increasing and decreasing (and for 0 the decreasing operation is blocked).
    -   [Message passing](https://en.wikipedia.org/wiki/Message_passing) & [Message queue](https://en.wikipedia.org/wiki/Message_queue)
    -   [Pipelines](<https://en.wikipedia.org/wiki/Pipeline_(Unix)>)
        > Redirecting the output of one process to the input of another (similar to a pipe).

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Interprocess Communications** – Microsoft](https://learn.microsoft.com/en-us/windows/win32/ipc/interprocess-communications)
2. 📺 [**Interprocess Communication** – YouTube](https://youtu.be/dJuYKfR8vec)
3. 📺 [**Inter Process Communication** – YouTube](https://youtu.be/W0BX6geRCDQ)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

