### Package manager

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


