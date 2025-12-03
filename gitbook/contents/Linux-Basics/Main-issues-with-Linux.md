### Main issues with Linux

-   Software installation and package management issues
    > - [Unmet dependencies](https://fedingo.com/how-to-resolve-unmet-dependencies-in-ubuntu/) - occurs when package fails to install or update.
    > - [Dependency errors and conflicts](https://ubunlog.com/en/how-to-fix-dependency-errors-in-ubuntu-and-derivatives/)
-   [Problems with drivers](https://askubuntu.com/a/496654)
    > All free Linux drivers are built right into its kernel. Therefore, everything should work "out of the box" after installing the system (problems may occur with brand new hardware which has just been released on the market). Drivers whose source code is closed are considered proprietary and are not included in the kernel but are installed manually (like Nvidia graphics drivers).
-   File system issues
    > - Check disk space availability using the `df` command and ensure that critical partitions are not full.
    > - Use the `fsck` command to check and repair [file system inconsistencies](https://www3.rocketsoftware.com/rocketd3/support/documentation/d3nt/91/refman/index.htm#definitions/file_inconsistency.htm).
    > - In case of data loss or accidental deletion, use data recovery tools like [`extundelete`](https://extundelete.sourceforge.net/) or [`testdisk`](https://github.com/cgsecurity/testdisk).
-   Performance and resource management
    > - Check system resource usage, including CPU, memory, and disk space, using `free`, `df`, or `du` commands.
    > - Identify resource-intensive processes using tools like `top`, `htop`, or `systemd-cgtop`.
    > - Disable unnecessary [startup services](https://askubuntu.com/questions/48321/how-do-i-start-applications-automatically-on-login) or [background processes](https://askubuntu.com/questions/636129/how-can-i-see-background-process-in-ubuntu-and-kill-unnecessary-processes) to improve performance.
-   Network connectivity issues
    > - Use the ping command to check network connectivity to a specific host or IP address.
    > - Check the [network settings](https://ubuntu.com/server/docs/network-configuration), such as IP configuration, [DNS settings](https://unix.stackexchange.com/questions/494324/how-to-setup-dns-manually-on-linux), and [firewall rules](https://www.redhat.com/sysadmin/firewalld-linux-firewall).
-   Problems with kernel
    > [Kernel panic](https://en.wikipedia.org/wiki/Kernel_panic) - can occur due to an error when mounting the root file system.
    > This is best helped by the skill of reading the logs to find problems (`dmesg` command).

<details>
<summary>🔗 <b>References</b></summary>

1. 📺 [**Linux Drivers Explained** – YouTube](https://youtu.be/s8t0AWmHvUM)
2. 📺 [**How Do Linux Kernel Drivers Work?** – YouTube](https://youtu.be/juGNPLdjLH4)
 </details>



