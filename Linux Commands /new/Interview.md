https://www.scribd.com/document/402113773/Linux-Interview-Question-for-DevOps

<img width="847" height="697" alt="image" src="https://github.com/user-attachments/assets/3d695921-7ccd-4ea2-a0e6-2a3c6fbcdf69" />
<img width="400" height="170" alt="image" src="https://github.com/user-attachments/assets/11e26b48-43fc-4f5a-8117-2f7532506577" />
<img width="374" height="145" alt="image" src="https://github.com/user-attachments/assets/56120f92-a261-440b-9e8a-9c3bfbb1091c" />

Perfect! Let’s go **section by section** with **short, concise answers** for all 100 Linux interview questions for a **5-year experienced DevOps engineer**. I’ll keep each answer 2–3 lines with commands or brief explanations.

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
