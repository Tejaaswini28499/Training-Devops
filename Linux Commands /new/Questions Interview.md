Perfect 👍 Here’s a **comprehensive list of 100 Linux interview questions** tailored for a **DevOps Engineer with 5 years of experience** — covering practical, scenario-based, and conceptual questions often asked in real interviews.

---

## 🧩 **1. Linux Fundamentals**

1. What are the different types of files in Linux?
2. Explain the Linux directory structure.
3. What is the difference between absolute and relative paths?
4. How do you check the current working directory?
5. What is the purpose of the `/etc` directory?
6. How do you find the size of a directory?
7. Explain the difference between hard link and soft link.
8. What is the use of the `pwd`, `ls`, and `cd` commands?
9. How do you find hidden files in a directory?
10. What does the `.` and `..` represent in Linux?

---

## ⚙️ **2. File and Directory Management**

11. How do you copy files and directories in Linux?
12. What is the difference between `cp` and `mv`?
13. How do you delete files and directories?
14. How do you find files larger than 100MB?
15. What does `du -sh *` do?
16. How do you recursively search for a string inside files?
17. Explain how `find` and `locate` differ.
18. How do you sort files based on modification time?
19. How do you rename multiple files at once?
20. How do you view file permissions and change them?

---

## 🔐 **3. Permissions and Ownership**

21. What do the permission bits `rwxr-xr--` mean?
22. Explain numeric permissions (e.g., 755, 644).
23. How do you change file ownership and group ownership?
24. What is the difference between `chmod`, `chown`, and `chgrp`?
25. What does the `umask` command do?
26. How do you set default file permissions for all new files?
27. Explain the concept of SUID, SGID, and sticky bit.
28. How do you identify which user created a file?
29. How do you give execute permission to all users for a script?
30. What happens if a directory has the sticky bit set?

---

## 💻 **4. Processes and System Monitoring**

31. How do you list running processes?
32. What is the difference between `ps aux` and `top`?
33. What is `htop` and how is it different from `top`?
34. How do you kill a process by name or PID?
35. What is the difference between `kill` and `pkill`?
36. How do you check which process is using a specific port?
37. How do you find CPU and memory usage per process?
38. What does the `nice` and `renice` command do?
39. How do you check system uptime and load average?
40. How do you monitor logs in real time?

---

## 🌐 **5. Networking**

41. How do you check your IP address and default route?
42. What is the difference between `ip a` and `ifconfig`?
43. How do you check DNS resolution from Linux?
44. What does `ping` do?
45. How do you test connectivity to a specific port?
46. What is the difference between `curl` and `wget`?
47. How do you check listening ports on a system?
48. What is `traceroute` used for?
49. How do you check open network connections?
50. How do you restart networking service in Linux?

---

## 🧮 **6. Disk and Filesystem Management**

51. How do you check disk usage?
52. What does `df -h` show?
53. How do you check available inodes?
54. How do you find large files consuming disk space?
55. What is the difference between `df` and `du`?
56. How do you mount and unmount a filesystem?
57. How do you view currently mounted filesystems?
58. How do you format a partition in Linux?
59. What is LVM and how do you create one?
60. How do you extend an LVM volume?

---

## ⚡ **7. System Performance and Troubleshooting**

61. How do you check CPU and memory usage over time?
62. What is `vmstat` used for?
63. How do you check IO performance in Linux?
64. How do you identify high CPU usage processes?
65. How do you troubleshoot high memory usage?
66. How do you find system boot logs?
67. What is `dmesg` used for?
68. How do you find system load issues?
69. What does `sar` command do?
70. How do you monitor disk I/O?

---

## 🔁 **8. Services and Daemons**

71. How do you check if a service is running?
72. How do you start, stop, and restart a service?
73. What’s the difference between `systemctl` and `service`?
74. How do you check failed systemd units?
75. How do you enable a service to start on boot?
76. How do you check system logs for a specific service?
77. What is the role of `/etc/systemd/system/`?
78. How do you create a custom systemd service?
79. What is a daemon process?
80. How do you verify which services are enabled on startup?

---

## 🧰 **9. Users, Groups, and Authentication**

81. How do you create and delete a user?
82. How do you lock and unlock a user account?
83. How do you add a user to a group?
84. What is the purpose of `/etc/passwd` and `/etc/shadow`?
85. How do you change a user's password expiration?
86. How do you switch between users?
87. How do you view all groups a user belongs to?
88. How do you create a sudo user?
89. How do you restrict commands a user can run via sudo?
90. How do you check login history?

---

## 📦 **10. Scripting & Automation**

91. How do you schedule a cron job?
92. How do you list all scheduled cron jobs?
93. What is the difference between `cron` and `at`?
94. How do you redirect output to a file?
95. What’s the difference between `>` and `>>`?
96. How do you use pipes in Linux?
97. Write a script to monitor disk usage and send an alert.
98. How do you find and delete old log files automatically?
99. How do you make a script executable?
100. How would you debug a shell script?

---

---

## **1. Linux Fundamentals**

1. **Types of files:** Regular, directory, symbolic link, block, character, FIFO, socket.
2. **Directory structure:** `/` (root), `/etc` (configs), `/bin` (binaries), `/usr` (user apps), `/var` (logs), `/home` (user dirs), `/tmp` (temp).
3. **Absolute vs Relative path:** Absolute starts from `/`; relative starts from current directory.
4. **Current working directory:** `pwd`
5. **/etc directory purpose:** Stores system and application configuration files.
6. **Find directory size:** `du -sh /path/to/dir`
7. **Hard vs Soft link:** Hard links point to inode; soft links (symlinks) point to file path.
8. **pwd, ls, cd:** `pwd` shows current dir, `ls` lists files, `cd` changes directory.
9. **Hidden files:** `ls -a`
10. **. and ..:** `.` = current directory, `..` = parent directory

---

## **2. File and Directory Management**

11. **Copy files/dirs:** `cp file1 file2`, `cp -r dir1 dir2`
12. **cp vs mv:** `cp` copies, `mv` moves/renames
13. **Delete files/dirs:** `rm file`, `rm -r dir`
14. **Find files >100MB:** `find /path -size +100M`
15. **du -sh *:** Shows human-readable sizes of files/directories
16. **Recursive search:** `grep -r 'string' /path`
17. **find vs locate:** `find` searches live FS; `locate` searches database (`updatedb`)
18. **Sort by modification time:** `ls -lt`
19. **Rename multiple files:** `rename 's/old/new/' *`
20. **View/change permissions:** `ls -l`, `chmod 755 file`

---

## **3. Permissions and Ownership**

21. **rwxr-xr--:** Owner read/write/execute; group read/execute; others read only
22. **Numeric permissions:** 7=rwx, 6=rw, 5=r-x, 4=r
23. **Change owner/group:** `chown user:group file`
    Changing file ownership and group ownership in Linux is done using the `chown` command. Let’s break it down clearly:

---

### 1. **Change file owner**

```bash
chown newuser filename
```

* `newuser` → the username of the new owner
* `filename` → the file or directory you want to change

**Example:**

```bash
chown tejaaswini report.txt
```

Now `report.txt` is owned by user `tejaaswini`.

---

### 2. **Change group ownership**

```bash
chown :newgroup filename
```

* `newgroup` → the new group name
* `:` → tells `chown` you are changing **only the group**

**Example:**

```bash
chown :devops report.txt
```

Now `report.txt` belongs to the group `devops`.

---

### 3. **Change both owner and group at the same time**

```bash
chown newuser:newgroup filename
```

**Example:**

```bash
chown tejaaswini:devops report.txt
```

* Owner → `tejaaswini`
* Group → `devops`

---

### 4. **Change ownership recursively**

For directories and their contents, use `-R`:

```bash
chown -R tejaaswini:devops /home/tejaaswini/project
```

* `-R` → recursive (applies to all files and subdirectories inside `/project`)

---

### ✅ Quick Summary Table

| Action                  | Command Example                    |
| ----------------------- | ---------------------------------- |
| Change owner            | `chown tejaaswini file.txt`        |
| Change group only       | `chown :devops file.txt`           |
| Change owner & group    | `chown tejaaswini:devops file.txt` |
| Recursive for directory | `chown -R tejaaswini:devops /dir`  |

---

If you want, I can also explain **how to check the current owner and group of a file** before changing it—it’s very handy to avoid mistakes. Do you want me to show that?

25. **chmod vs chown vs chgrp:** `chmod` = change permissions, `chown` = owner, `chgrp` = group
26. **umask:** Sets default file creation permissions
27. **Default permissions:** Set via `umask`
28. **SUID, SGID, sticky:** SUID = exec as owner, SGID = exec as group, sticky = delete own files only
29. **Identify creator:** Check `ls -l` owner or use audit logs
30. **Execute permission for all:** `chmod a+x file`
31. **Sticky bit on dir:** Only file owner can delete files

---

## **4. Processes and System Monitoring**

31. **List processes:** `ps aux`
32. **ps aux vs top:** `ps aux` = snapshot, `top` = live
33. **htop vs top:** `htop` is interactive with colors and easier navigation
34. **Kill process:** `kill PID` or `pkill process_name`
35. **kill vs pkill:** `kill` uses PID; `pkill` uses process name
36. **Check port usage:** `lsof -i :PORT` or `netstat -tulnp`
37. **CPU/memory per process:** `top` or `ps aux --sort=-%mem`
38. **nice/renice:** Adjust process priority
39. **Uptime/load avg:** `uptime`
40. **Monitor logs real-time:** `tail -f /var/log/syslog`

---

## **5. Networking**

41. **IP & route:** `ip a`, `ip r`
42. **ip a vs ifconfig:** `ifconfig` deprecated; `ip a` is modern
43. **DNS resolution:** `nslookup example.com` or `dig example.com`
44. **Ping:** Test network connectivity
45. **Test port:** `telnet host port` or `nc -zv host port`
46. **curl vs wget:** Both fetch URLs; `curl` more flexible in scripting
47. **Check listening ports:** `ss -tuln` or `netstat -tuln`
48. **Traceroute:** `traceroute host` shows route packets take
49. **Open connections:** `ss -s` or `netstat -anp`
50. **Restart networking:** `systemctl restart network` or `systemctl restart NetworkManager`

---

## **6. Disk and Filesystem Management**

51. **Check disk usage:** `df -h`
52. **df -h:** Human-readable free/used space
53. **Check inodes:** `df -i`
54. **Find large files:** `find / -type f -size +1G`
55. **df vs du:** `df` = filesystem, `du` = directory/file size
56. **Mount/umount:** `mount /dev/sdX /mnt`, `umount /mnt`
57. **View mounted FS:** `mount` or `cat /proc/mounts`
58. **Format partition:** `mkfs.ext4 /dev/sdX`
59. **LVM:** Logical Volume Manager for flexible storage, use `lvcreate`, `vgcreate`
60. **Extend LVM:** `lvextend -L +5G /dev/vg/lv` then `resize2fs /dev/vg/lv`

---

## **7. System Performance and Troubleshooting**

61. **CPU/memory usage:** `top`, `htop`, `vmstat`
62. **vmstat:** Monitors memory, CPU, I/O stats
63. **Check I/O:** `iostat`, `iotop`
64. **High CPU:** `top` or `ps aux --sort=-%cpu`
65. **High memory:** `free -h`, `top`
66. **Boot logs:** `journalctl -b`
67. **dmesg:** Kernel messages
68. **System load issues:** `uptime`, `top`, `vmstat`
69. **sar:** Collects historical system metrics
70. **Monitor disk I/O:** `iostat -x 1`

---

## **8. Services and Daemons**

71. **Check service:** `systemctl status service`
72. **Start/stop/restart:** `systemctl start|stop|restart service`
73. **systemctl vs service:** `systemctl` = systemd; `service` = older init scripts
74. **Failed units:** `systemctl --failed`
75. **Enable on boot:** `systemctl enable service`
76. **Check service logs:** `journalctl -u service`
77. **/etc/systemd/system/:** Custom service unit files
78. **Create systemd service:** Create `.service` file + `systemctl daemon-reload`
79. **Daemon:** Background service process
80. **Check enabled services:** `systemctl list-unit-files | grep enabled`

---

## **9. Users, Groups, and Authentication**

81. **Create/delete user:** `useradd username`, `userdel username`
82. **Lock/unlock user:** `usermod -L username`, `usermod -U username`
83. **Add to group:** `usermod -aG group user`
84. **/etc/passwd & /etc/shadow:** passwd = user info, shadow = hashed passwords
85. **Change password expiration:** `chage -l username` / `chage -M 90 username`
86. **Switch user:** `su - username`
87. **View groups:** `groups username`
88. **Create sudo user:** `usermod -aG sudo username`
89. **Restrict sudo commands:** Edit `/etc/sudoers`
90. **Login history:** `last`, `lastb`

---

## **10. Scripting & Automation**

91. **Schedule cron:** `crontab -e`
92. **List cron jobs:** `crontab -l`
93. **cron vs at:** cron = recurring, at = one-time job
94. **Redirect output:** `command > file` or `command >> file`
95. **> vs >>:** `>` overwrite, `>>` append
96. **Pipes:** `ls -l | grep txt`
97. **Disk usage alert script:** `if [ $(df / | awk 'NR==2 {print $5}' | sed 's/%//') -gt 80 ]; then echo "Alert"; fi`
98. **Delete old logs:** `find /var/log -type f -mtime +30 -delete`
99. **Make script executable:** `chmod +x script.sh`
100. **Debug script:** `bash -x script.sh`

---

detalied understanding:
Sure! What you listed are the **standard directories under the root (`/`) in Linux**, each serving a specific purpose. I’ll explain each one clearly:

---

### 1. **`/bin`**

* **Stands for:** Binary
* **Purpose:** Contains essential user command binaries (programs) needed in **single-user mode** and for **all users**.
* **Examples:** `ls`, `cp`, `mv`, `cat`, `bash`.

---

### 2. **`/boot`**

* **Purpose:** Stores bootloader files and the kernel required to start Linux.
* **Examples:** `vmlinuz` (Linux kernel), `initrd.img`, GRUB files.

---

### 3. **`/dev`**

* **Purpose:** Contains **device files** that represent hardware (disk drives, USBs, terminals, etc.).
* **Examples:** `/dev/sda` (hard drive), `/dev/tty` (terminals).

---

### 4. **`/etc`**

* **Purpose:** System-wide configuration files. Usually **text files** you can edit.
* **Examples:** `passwd`, `hosts`, `fstab`, network configs.

---

### 5. **`/home`**

* **Purpose:** Contains **home directories of regular users**.
* **Example:** `/home/tejaaswini` for your personal files.

---

### 6. **`/lib`**

* **Purpose:** Essential **shared libraries** for binaries in `/bin` and `/sbin`.
* **Examples:** `libc.so.6` (C library).

---

### 7. **`/lib64`**

* **Purpose:** 64-bit libraries for systems running a 64-bit Linux OS.

---

### 8. **`/local`**

* Usually `/usr/local` (not just `/local`) — but if it exists at root:
* **Purpose:** Locally installed software and binaries not managed by the system package manager.

---

### 9. **`/media`**

* **Purpose:** Mount point for **removable media** like USB drives, CDs, etc.
* **Example:** `/media/usb`

---

### 10. **`/mnt`**

* **Purpose:** Temporary mount point for **manually mounted filesystems**.
* **Example:** Mounting an external disk temporarily.

---

### 11. **`/opt`**

* **Purpose:** Optional software packages installed **manually**.
* **Example:** Third-party applications like Google Chrome or proprietary software.

---

### 12. **`/proc`**

* **Purpose:** Virtual filesystem for **kernel and process information**.
* **Example:** `/proc/cpuinfo`, `/proc/meminfo`.
* **Note:** Files here are generated **on-the-fly**, not stored on disk.

---

### 13. **`/root`**

* **Purpose:** Home directory for the **root (superuser)**.
* **Example:** `/root/.bashrc`.

---

### 14. **`/run`**

* **Purpose:** Runtime data for **currently running processes**.
* **Examples:** PID files, sockets, system state info.

---

### 15. **`/sbin`**

* **Stands for:** System Binary
* **Purpose:** Contains **administrative binaries** required for system management.
* **Examples:** `fdisk`, `fsck`, `iptables`.

---

### 16. **`/srv`**

* **Purpose:** Data for **services provided by the system**, like web or FTP servers.
* **Example:** `/srv/www` for web server files.

---

### 17. **`/sys`**

* **Purpose:** Virtual filesystem for **kernel device and system info** (similar to `/proc`).
* **Example:** `/sys/class/net/` shows network devices.

---

### 18. **`/tmp`**

* **Purpose:** Temporary files for programs and users. Usually **cleared on reboot**.

---

### 19. **`/usr`**

* **Purpose:** Secondary hierarchy for **read-only user data**: binaries, libraries, documentation.
* **Subdirectories:**

  * `/usr/bin` → user commands
  * `/usr/lib` → libraries
  * `/usr/share` → documentation, icons

---

### 20. **`/var`**

* **Stands for:** Variable
* **Purpose:** Files that **change frequently**, like logs, caches, mail, and spool files.
* **Examples:** `/var/log`, `/var/spool`, `/var/tmp`.

---

✅ **Summary:**

* **Static system files:** `/bin`, `/sbin`, `/lib`, `/boot`, `/etc`
* **User files:** `/home`, `/root`
* **Temporary/runtime files:** `/tmp`, `/run`
* **Device info:** `/dev`, `/proc`, `/sys`
* **Software:** `/usr`, `/opt`, `/usr/local`
* **Mount points:** `/mnt`, `/media`
* **Variable data:** `/var`
* **Service data:** `/srv`

---


-----------------------------
