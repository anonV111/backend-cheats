### Task scheduler

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


