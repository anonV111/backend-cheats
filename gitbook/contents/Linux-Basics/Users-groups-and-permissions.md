### Users, groups, and permissions

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


