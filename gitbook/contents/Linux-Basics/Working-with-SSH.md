### Working with SSH

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


