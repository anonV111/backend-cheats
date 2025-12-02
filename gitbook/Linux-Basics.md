## Linux Basics

Operating systems based on [Linux kernel](https://en.wikipedia.org/wiki/Linux_kernel) are the standard in the world of server development, since most servers run on such operating systems. Using Linux on servers is profitable because it is free and open source, secure and works fast on cheap hardware.

There are a huge number of [Linux distributions](https://en.wikipedia.org/wiki/Linux_distribution) (preinstalled software bundles) to suit all tastes. One of the most popular is [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu). This is where you can start your dive into server development.

[Install Ubuntu](https://ubuntu.com/download/desktop) on a separate PC or laptop. If this is not possible, you can use a special program [Virtual Box](https://www.virtualbox.org/wiki/Downloads) where you can [run other OS](https://www.virtualbox.org/manual/ch01.html#create-vm-wizard) on top of the main OS. You can also run [Docker](https://www.docker.com/products/docker-desktop) [Ubuntu image container](https://hub.docker.com/_/ubuntu) (Docker is a [separate topic](#docker) that is exists in this repository).

-   ### Working with shell

    [Shell](https://en.wikipedia.org/wiki/Shell_(computing)) (or console, terminal) is a computer program which is used to operate and control a computer by entering special text commands. Generally, servers do not have [graphical interfaces (GUI)](https://en.wikipedia.org/wiki/Graphical_user_interface), so you will definitely need to learn how to work with shells. The are many [Unix shells](https://en.wikipedia.org/wiki/Unix_shell), but most Linux distributions come with a [Bash shell](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) by default.

    -   Basic commands for navigating the file system
        ```sh
        ls # list directory contents
        cd [PATH] # go to specified directory
        cd .. # move to a higher level (to the parent directory)
        touch [FILE] # create a file
        cat > [FILE] # enter text into the file (overwrite)
        cat >> [FILE] # enter text at the end of the file (append)
        cat/more/less [FILE] # to view the file contents
        head/tail [FILE] # view the first/last lines of a file
        pwd # print path to current directory
        mkdir [NAME] # create a directory
        rmdir [NAME] # delete a directory
        cp [FILE] [PATH] # copy a file or directory
        mv [FILE] [PATH] # moving or renaming
        rm [FILE] # deleting a file or directory
        find [STRING] # file system search
        du [FILE] # output file or directory size
        grep [PATTERN] [FILE] # print lines that match patterns
        ```
    -   Commands for help information
        ```sh
        man [COMMAND] # allows you to view a manual for any command
        apropos [STRING] # search for a command with a description that has a specified word
        man -k [STRING] # similar to the command above
        whatis [COMMAND] # a brief description of the command
        ```
    -   [Super user rights](https://en.wikipedia.org/wiki/Sudo)
        > Analogue to running as administrator in Windows
        ```sh
        sudo [COMMAND] # executes a command with superuser privileges
        ```
    -   Text editor
        > Study any in order to read and edit files freely through the terminal.
        > The easiest – [nano](https://en.wikipedia.org/wiki/GNU_nano).
        > Something in the middle - [micro](https://micro-editor.github.io/).
        > The most advanced – [Vim](<https://en.wikipedia.org/wiki/Vim_(text_editor)>).

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**31 Linux Commands Every Ubuntu User Should Know**](https://itsfoss.com/essential-ubuntu-commands/)
2. 📄 [**The Linux Command Handbook** – freeCodeCamp](https://www.freecodecamp.org/news/the-linux-commands-handbook/)
3. 📄 [**A to Z: List of Linux commands**](https://linuxhandbook.com/a-to-z-linux-commands/)
4. 📺 [**The 50 Most Popular Linux & Terminal Commands** – YouTube](https://youtu.be/ZtqBQ68cfJc)
5. 📺 [**Nano Editor Fundamentals** – YouTube](https://youtu.be/gyKiDczLIZ4)
6. 📺 [**Vim Tutorial for Beginners** – YouTube](https://youtu.be/RZ4p-saaQkc)
7. 📄 [**Awesome Terminals** – GitHub](https://github.com/cdleon/awesome-terminals)
8. 📄 [**Awesome CLI-apps** – GitHub](https://github.com/agarrharr/awesome-cli-apps)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Package manager

    The package manager is a utility that allows you to install/update software packages from the terminal.

    Linux distributions can be divided into several groups, depending on which package manager they use: [apt](<https://en.wikipedia.org/wiki/APT_(software)>) (in [Debian](https://en.wikipedia.org/wiki/Debian) based distributions), [RPM](https://en.wikipedia.org/wiki/RPM_Package_Manager) (the [Red Hat](https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux) package management system) and [Pacman](https://en.wikipedia.org/wiki/Arch_Linux#Pacman) (the package manager in [Arch-like distributions](https://en.wikipedia.org/wiki/Arch_Linux))

    Ubuntu is based on Debian, so it uses apt (advanced packaging tool) package manager.

    -   Basic commands
        ```sh
        apt install [package] # install the package
        apt remove [package] # remove the package, but keep the configuration
        apt purge [package] # remove the package along with the configuration
        apt update # update information about new versions of packages
        apt upgrade # update the packages installed in the system
        apt list --installed # list of packages installed on the system
        apt list --upgradable # list of packages that need to be updated
        apt search [package] # searching for packages by name on the network
        apt show [package] # package information
        ```
    -   [aptitude](https://en.wikipedia.org/wiki/Aptitude_(software))
        > Interactive console utility for easy viewing of packages to install, update and uninstall them.
    -   Repository management
        > Package managers typically work with software repositories. These repositories contain a collection of software packages that are maintained and provided by the distribution's community or official sources.
        ```sh
        add-apt-repository [repository_url] # add a new repository
        add-apt-repository --remove [repository_url] # remove a repo
            # don\'t forget to update after this operations - apt update
        ```
        ```sh
        /etc/apt/sources.list # a file contains a list of configured repo links
        /etc/apt/sources.list.d # a directory contains files for third party repos
        ```
    -   [dpkg](https://en.wikipedia.org/wiki/Dpkg)
        > Low-level tool to install, build, remove and manage Debian packages.


<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Linux Crash Course - The apt Command** – YouTube](https://youtu.be/1kicKTbK768)
2. 📺 [**Linux Package Management | Debian, Fedora, and Arch Linux** – YouTube](https://youtu.be/lkii2cGuKao)
3. 📄 [**sudo apt-get update vs. upgrade – What is the Difference?** – freeCodeCamp](https://www.freecodecamp.org/news/sudo-apt-get-update-vs-upgrade-what-is-the-difference)
4. 📄 [**Repositories in Ubuntu**](https://help.ubuntu.com/community/Repositories/Ubuntu)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Bash scripts

    You can use scripts to automate the sequential input of any number of commands. In [Bash](<https://en.wikipedia.org/wiki/Bash_(Unix_shell)>) you can create different conditions (branching), loops, timers, etc. to perform all kinds of actions related to shell input.

    -   [Basics of Bash Scripts](https://github.com/cheatsnake/bash-scripts-by-example)
        > The most basic and frequently used features such as: variables, I/O, loops, conditions, etc.
    -   Practice
        > Solve challenges on sites like [HackerRank](https://www.hackerrank.com/domains/shell) and [Codewars](https://www.codewars.com/join?language=shell).
        > Start using Bash to automate routine activities on your computer. If you're already a programmer, create scripts to easily build your project, to install settings, and so on.
    -   [ShellCheck](https://github.com/koalaman/shellcheck) script analysis tool
        > It will point out possible mistakes and teach you best practices for writing really good scripts.
    -   Additional resources
        > Repositories such as [awesome bash](https://github.com/awesome-lists/awesome-bash) and [awesome shell](https://github.com/alebcay/awesome-shell) have entire collections of useful resources and tools to help you develop even more skills with Bash and shell in general.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Shell Scripting for Beginners** – freeCodeCamp](https://www.freecodecamp.org/news/shell-scripting-crash-course-how-to-write-bash-scripts-in-linux/)
2. 📺 [**Bash Scripting Full Course 3 Hours** – YouTube](https://youtu.be/e7BufAVwDiM)
3. 📄 [**HackerRank challenges for Bash with solutions**](https://github.com/Thomas-George-T/HackerRank-The-Linux-Shell-Challenges-Solutions)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Users, groups, and permissions

    Linux-based operating systems are multi-user. This means that several people can run many different applications at the same time on the same computer. For the Linux system to be able to "recognize" a user, he must be logged in, and therefore each user must have a unique name and a secret password.

    -   Working with users
        ```sh
        useradd [name] [flags] # create a new user
        passwd [name] # set a password for the user
        usermod [name] [flags] # edit a user
        usermod -L [name] # block a user
        usermod -U [name] # unblock a user
        userdel [name] [flags] # delete a user
        su [name] # switch to other user
        ```
    -   Working with groups
        ```sh
        groupadd [group] [flags] # create a group
        groupmod [group] [flags] # edit group
        groupdel [group] [flags] # delete group
        usermod -a -G [groups] [user] # add a user to groups
        gpasswd --delete [user] [groups] # remove a user from groups
        ```
    -   System files
        ```sh
        /etc/passwd # a file containing basic information about users
        /etc/shadow # a file containing encrypted passwords
        /etc/group # a file containing basic information about groups
        /etc/gshadow # a file containing encrypted group passwords
        ```

    On Linux, it is possible to share privileges between users, limit access to unwanted files or features, control available actions for services, and much more. On Linux, there are only three kinds of rights - read, write and execute - and three categories of users to which they can be applied - file owner, file group and everyone else.

    <p align="center"><img src="./files/linux/chmod_eng.png" alt="chmod"/></p>

    -   Basic commands for working with rights
        ```sh
        chown <user> <file> # changes the owner and/or group for the specified files
        chmod <rights> <file> # changes access rights to files and directories
        chgrp <group> <file> # allows users to change groups
        ```
    -   Extended rights [SUID and GUID](https://en.wikipedia.org/wiki/Setuid), [sticky bit](https://en.wikipedia.org/wiki/Sticky_bit)
    -   [ACL (Access control list)](https://en.wikipedia.org/wiki/Access-control_list)
        > An advanced subsystem for managing access rights.


<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Managing Users, Groups, and Permissions on Linux**](https://omarrrz-lounge.hashnode.dev/managing-users-groups-and-permissions-in-linux)
2. 📄 [**Linux User Groups Explained** – freeCodeCamp](https://www.freecodecamp.org/news/linux-user-groups-explained-how-to-add-a-new-group-a-new-group-member-and-change-groups/)
3. 📺 [**Linux Users and Groups** – YouTube](https://youtu.be/b-9j2jiCOEA)
4. 📄 [**An Introduction to Linux Permissions** – Digital Ocean](https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-permissions)
5. 📄 [**File Permissions on Linux – How to Use the chmod Command** – freeCodeCamp](https://www.freecodecamp.org/news/file-permissions-in-linux-chmod-command-explained/)
6. 📺 [**Understanding File & Directory Permissions** – YouTube](https://youtu.be/4e669hSjaX8)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Working with processes

    Linux processes can be described as containers in which all information about the state of a running program is stored. Sometimes programs can hang and in order to force them to close or restart, you need to be able to manage processes.

    -   Basic Commands
        ```sh
        ps # display a snapshot of the processes of all users
        top # real-time task manager
        [command] & # running the process in the background, (without occupying the shell)
        jobs # list of processes running in the background
        fg [PID] # return the process back to the active mode by its number
         # You can press [Ctrl+Z] to return the process to the background
        bg [PID] # start a stopped process in the background
        kill [PID] # terminate the process by PID
        killall [program] # terminate all processes related to the program
        ```

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**How to Show Process Tree on Linux**](https://linuxhandbook.com/show-process-tree/)
2. 📄 [**How to Manage Linux Processes** – freeCodeCamp](https://www.freecodecamp.org/news/how-to-manage-linux-processes/)
3. 📄 [**How To Use ps, kill, and nice to Manage Processes on Linux** – Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-ps-kill-and-nice-to-manage-processes-in-linux)
4. 📺 [**Linux processes, init, fork/exec, ps, kill, fg, bg, jobs** – YouTube](https://youtu.be/TJzltwv7jJs)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Working with SSH

    [SSH](https://en.wikipedia.org/wiki/Secure_Shell) allows remote access to another computer's terminal. In the case of a personal computer, this may be needed to solve an urgent problem, and in the case of working with the server, remote access via SSH is an integral and regularly used practice.

    -   Basic commands
        ```sh
        apt install openssh-server # installing SSH (out of the box almost everywhere)
        service ssh start # start SSH
        service ssh stop # stop SSH
        ssh -p [port] [user]@[remote_host] # connecting to a remote machine via SSH
        ```
    -   [Passwordless login](https://www.redhat.com/sysadmin/passwordless-ssh)
        ```sh
        ssh-keygen -t rsa # RSA key generation for passwordless login
        ssh-copy-id -i ~/.ssh/id_rsa [user]@[remote_host] # copying a key to a remote machine
        ```
    -   Config files
        ```sh
        /etc/ssh/sshd_config # ssh server global config
        ~/.ssh/config # ssh server local config
        ~/.ssh/authorized_keys # file with saved public keys
        ```

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**What the hell is SSH?**](https://codingpastor.hashnode.dev/what-the-hell-is-ssh)
2. 📺 [**Learn SSH In 6 Minutes - Beginners Guide to SSH Tutorial** – YouTube](https://youtu.be/v45p_kJV9i4)
3. 📺 [**SSH Crash Course | With Some DevOps** – YouTube](https://youtu.be/hQWRp-FdTpc)
4. 📄 [**SSH config file for OpenSSH client**](https://www.ssh.com/academy/ssh/config)
5. 📄 [**Awesome SSH** – GitHub](https://github.com/moul/awesome-ssh)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Network utils

    For Linux there are many built-in and third-party utilities to help you configure your network, analyze it and fix possible problems.

    -   Simple utils
        ```bash
        ip address # show info about IPv4 and IPv6 addresses of your devices
        ip monitor # real time monitor the state of devices
        ifconfig # config the network adapter and IP protocol settings
        traceroute <host> # show the route taken by packets to reach the host
        tracepath <host> # traces the network host to destination discovering MTU
        ping <host> # check connectivity to host
        ss -at # show the list of all listening TCP connections
        dig <host> # show info about the DNS name server
        host <host | ip-address> # show the IP address of a specified domain
        mtr <host | ip-address> # combination of ping and traceroute utilities
        nslookup # query Internet name servers interactively
        whois <host> # show info about domain registration
        ifplugstatus # detect the link status of a local Linux ethernet device
        iftop # show bandwidth usage
        ethtool <device name> # show detalis about your ethernet device
        nmap # tool to explore and audit network security
        bmon # bandwidth monitor and rate estimator
        firewalld # add, configure and remove rules on firewall
        ipref # perform network performance measurement and tuning
        speedtest-cli # check your network download/upload speed
        wget <link> # download files from the Internet
        ```
    -   [`tcpdump`](https://en.wikipedia.org/wiki/Tcpdump)
        > A console utility that allows you to intercept and analyze all network traffic passing through your computer.
    -   [`netcat`](https://en.wikipedia.org/wiki/Netcat)
        > Utility for reading from and writing to network connections using TCP or UDP. It includes port scanning, transferring files, and port listening: as with any server, it can be used as a [backdoor](<https://en.wikipedia.org/wiki/Backdoor_(computing)>).
    -   [`iptables`](https://en.wikipedia.org/wiki/Iptables)
        > User-space utility program that allows to configure the IP packet filter rules of the Linux kernel firewall, implemented as different Netfilter modules. The filters are organized in different tables, which contain chains of rules for how to treat network traffic packets.
    -   [`curl`](https://en.wikipedia.org/wiki/CURL)
        > Command-line tool for transferring data using various network protocols.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**21 Basic Linux Networking Commands You Should Know**](https://itsfoss.com/basic-linux-networking-commands/)
2. 📄 [**Using tcpdump Command on Linux to Analyze Network**](https://linuxhandbook.com/tcpdump-command/)
3. 📺 [**tcpdump - Traffic Capture & Analysis** – YouTube](https://youtu.be/1lDfCRM6dWk)
4. 📺 [**tcpdumping Node.js server** – YouTube](https://youtu.be/g_tmQ5G-T2w)
5. 📄 [**Beginner’s guide to Netcat for hackers**](https://medium.com/@HackTheBridge/beginners-guide-to-netcat-for-hackers-55abe449991d)
6. 📄 [**Iptables Tutorial**](https://linuxhint.com/iptables-tutorial/)
7. 📄 [**An intro to cURL: The basics of the transfer tool**](https://blog.logrocket.com/an-intro-to-curl-the-basics-of-the-transfer-tool/)
8. 📺 [**Basic cURL Tutorial** – YouTube](https://youtu.be/7XUibDYw4mc)
9. 📺 [**Using cURL better - tutorial by cURL creator Daniel Stenberg** – YouTube](https://youtu.be/I6id1Y0YuNk)
10. 📄 [**Awesome console services** – GitHub](https://github.com/chubin/awesome-console-services)
</details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Task scheduler

    <p align="center"><img src="./files/linux/cron_eng.png" alt="cron"/></p>

    Schedulers allow you to flexibly manage the delayed running of commands and scripts. Linux has a built-in [cron](https://en.wikipedia.org/wiki/Cron) scheduler that can be used to easily perform necessary actions at certain intervals.

    -   Main commands
        ```bash
        crontab -e # edit the crontab file of the current user
        crontab -l # output the contents of the current schedule file
        crontab -r # deleting the current schedule file
        ```
    -   Files and directories
        ```sh
        /etc/crontab # base config
        /etc/cron.d/ # a dir with crontab files used to manage the entire system

         # dirs where you can store scripts that runs:
        /etc/cron.daily/ # every day
        /etc/cron.weekly/ # every week
        /etc/cron.monthly/ # every month
        ```

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**How to schedule and manage tasks using crontab** – dev.to](https://dev.to/shaikh/how-to-schedule-and-manage-tasks-using-crontab-20dj)
2. 📺 [**Cron Jobs For Beginners | Linux Task Scheduling** – YouTube](https://youtu.be/v952m13p-b4)
3. 📄 [**How to Check Crontab logs on Linux**](https://linuxhandbook.com/check-crontab-logs/)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### System logs

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

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Main issues with Linux

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

<div align="right"><a href="#top">Contents ⬆️</a></div>

