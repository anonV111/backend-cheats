### Working with processes

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


