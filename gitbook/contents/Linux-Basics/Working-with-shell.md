### Working with shell

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


