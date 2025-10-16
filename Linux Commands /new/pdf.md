3.What are some common ways to troubleshoot a Linux server that won’t boot?

1. **Checking boot messages** using recovery mode or a live CD.
2. **Inspecting GRUB configuration** and kernel entries.
3. **Verifying disk/mount issues** with `fsck` or checking `/etc/fstab`.
4. **Reviewing system logs** (`/var/log/boot.log`, `dmesg`) for errors.
5. **Reinstalling or repairing the bootloader** if it’s corrupted.
---------------------

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
