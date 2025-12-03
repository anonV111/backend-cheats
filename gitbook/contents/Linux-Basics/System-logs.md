### System logs

[Log files](https://en.wikipedia.org/wiki/Logging_(computing)) are special text files that contain all information about the operation of a computer, program, or user. They are especially useful when bugs and errors occur in the operation of a program or server. It is recommended to periodically review log files, even if nothing suspicious happens.

-   Main log files
    ```bash
    /var/log/syslog or /var/log/messages # information about the kernel,
    # various services detected, devices, network interfaces, etc.
    /var/log/auth.log or /var/log/secure # user authorization information
    /var/log/faillog # failed login attempts
    /var/log/dmesg # information about device drivers
    /var/log/boot.log # operating system boot information
    /var/log/cron # cron task scheduler report
    ```
-   [lnav utility](https://lnav.org/)
    > Designed for easy viewing of log files (highlighting, reading different formats, searching, etc.)
-   Log rotation with [logrotate](https://github.com/logrotate/logrotate)
    > Allows you to configure automatic deletion (cleaning) of log files so as not to clog memory.
-   [Demon journald](https://manpages.ubuntu.com/manpages/bionic/man1/journalctl.1.html)
    > Collects data from all available sources and stores it in binary format for convenient and dynamic control.

<details>
<summary>🔗 <b>References</b></summary>

1. 📺 [**Linux Crash Course - Understanding Logging** – YouTube](https://youtu.be/6uP_f_z3CbM)
2. 📺 [**Linux Monitoring and Logging** – YouTube](https://youtu.be/kZ5LhS6fThM)
3. 📄 [**3 ways to watch logs in real time on Linux**](https://linuxhandbook.com/watch-logs-real-time/)
4. 📄 [**Analyzing logs on Linux with journalctl command**](https://linuxhandbook.com/journalctl-command/)
5. 📄 [**Linux File Structure Explained**](https://shubhsharma19.hashnode.dev/linux-file-structure-explained)
 </details>


