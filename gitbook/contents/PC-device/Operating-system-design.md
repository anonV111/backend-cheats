### Operating system design

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


