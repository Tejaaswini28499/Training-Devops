https://blocks-images-prod.btw.so/66-linux-devops-interview-questions-to-ask-your-candidates-1726038933797qy3.pdf

3.What are some common ways to troubleshoot a Linux server that won’t boot?

1. **Checking boot messages** using recovery mode or a live CD.
2. **Inspecting GRUB configuration** and kernel entries.
3. **Verifying disk/mount issues** with `fsck` or checking `/etc/fstab`.
4. **Reviewing system logs** (`/var/log/boot.log`, `dmesg`) for errors.
5. **Reinstalling or repairing the bootloader** if it’s corrupted.
---------------------
10.What steps would you take to secure a Linux server?
To secure a Linux server, keep the system **updated** and remove unused packages or services.
Set up a **firewall (ufw/iptables)**, use **SSH key authentication** instead of passwords, and disable root login.
Regularly **monitor logs**, enforce **strong permissions**, and use tools like **fail2ban** for intrusion prevention.

-----------------------

12.How would you check the current running processes on a Linux system?

To check current running processes, I usually start with ps -ef for a full snapshot, or use top or htop for real-time monitoring. For specific processes, I filter with pgrep or ps -ef | grep <name>.

-----------------------

13.What is the significance of the root user in Linux, and why is it generally advised to
avoid using it for routine tasks?

The **root user** in Linux is the **superuser** with full control over the system, including access to all files and commands.
It’s advised to **avoid using root for routine tasks** because mistakes (like deleting system files) can cause **serious damage or security risks**.

--------------------
14.How would you go about troubleshooting a slow-performing Linux server?

To troubleshoot a slow Linux server, check **CPU, memory, and disk usage** using tools like `top`, `htop`, `free`, and `iostat`.
Then review **running processes, logs, and network activity** to identify what’s consuming resources or causing bottlenecks.

---------------
18.How would you handle package management in a Linux environment using tools like
apt or yum?

apt and yum/dnf help you install, update, remove, and manage packages efficiently, keeping your Linux system up-to-date and secure.

---------------
19.Describe the process of setting up passwordless SSH between two Linux systems.

To set up passwordless SSH, generate a key pair on the client using `ssh-keygen`, which creates a public and private key.
Then copy the public key to the server using `ssh-copy-id user@server`.
After that, you can log in to the server via SSH without entering a password.

-----------------
30. What steps would you take to optimize a Linux server for better performance?
To optimize a Linux server, first **monitor resource usage** with tools like `top`, `vmstat`, and `iostat` to find bottlenecks.
Then **tune system parameters** (CPU, memory, disk I/O), **disable unused services**, and enable **caching or load balancing** if needed.
Regularly update software, use **optimized filesystems**, and adjust **kernel or network settings** for better performance.
------------------------

32.How would you secure a Linux-based web server to prevent common vulnerabilities and
attacks?

To secure a Linux-based web server, keep the **OS and web software updated** and **remove unused modules or services**.
Use a **firewall** to restrict access, enable **HTTPS (SSL/TLS)**, and **harden file permissions**.
Also, implement **intrusion detection (fail2ban, auditd)**, **disable directory listing**, and **regularly monitor logs** for suspicious activity.

--------------------
