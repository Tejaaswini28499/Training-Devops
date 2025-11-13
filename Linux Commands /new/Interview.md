https://www.scribd.com/document/402113773/Linux-Interview-Question-for-DevOps

<img width="847" height="697" alt="image" src="https://github.com/user-attachments/assets/3d695921-7ccd-4ea2-a0e6-2a3c6fbcdf69" />
<img width="400" height="170" alt="image" src="https://github.com/user-attachments/assets/11e26b48-43fc-4f5a-8117-2f7532506577" />
<img width="374" height="145" alt="image" src="https://github.com/user-attachments/assets/56120f92-a261-440b-9e8a-9c3bfbb1091c" />

Perfect! Let’s go **section by section** with **short, concise answers** for all 100 Linux interview questions for a **5-year experienced DevOps engineer**. I’ll keep each answer 2–3 lines with commands or brief explanations.

Perfect 👍 Let’s go through answers for all questions (23–32) one by one — clear and simple 👇

---

### **23. How to get the Java thread dump?**

Use the `jstack` command on the Java process ID.

```bash
jstack <pid> > threaddump.txt
```

➡️ Saves all running threads and stack traces to a file.

---

### **24. How to check the running ports?**

Use any of these:

```bash
ss -tuln
# or
netstat -tuln
```

➡️ Shows all open TCP/UDP ports and listening services.

---

### **25. How to declare a variable in a shell script?**

Simply assign value (no spaces around `=`).

```bash
name="Teja"
echo $name
```

---

### **26. What is `$?`, `$#`, `$*` ?**

| Symbol | Meaning                                       | Example   |
| ------ | --------------------------------------------- | --------- |
| `$?`   | Exit status of last command (0 = success)     | `echo $?` |
| `$#`   | Number of command-line arguments passed       | `echo $#` |
| `$*`   | All command-line arguments as a single string | `echo $*` |

---

### **27. How to read a command line input in shell script?**

Use the `read` command:

```bash
echo "Enter your name:"
read name
echo "Hello $name"
```

---

### **28. What is umask?**

`umask` sets the **default file permission mask** — controls what permissions are *not* given when new files are created.
Example:

```bash
umask 022
```

➡️ Default file = 644, directory = 755.

---

### **29. How to change file permission in Linux?**

Use `chmod`:

```bash
chmod 755 file.sh
```

➡️ Gives owner full rights, others read & execute.

---

### **30. How to connect remote servers without password? How to achieve this?**

Use **SSH key-based authentication**.

Steps:

```bash
ssh-keygen -t rsa
ssh-copy-id user@remote-server
```

Now you can SSH without entering a password.

---

### **31. How to open file in read-only mode in VI editor?**

```bash
vi -R filename
```

➡️ Opens file in **read-only** mode (cannot edit).

---

### **32. What is the purpose of export command?**

`export` makes a variable **available to child processes** (subshells).
Example:

```bash
name="Teja"
export name
```

➡️ Now `$name` can be used by other scripts or programs run from this shell.

---

Here are the answers for questions **33–36** 👇

---

### **33. How to send error logs and stdout logs in different files?**

You can redirect **stdout** and **stderr** separately:

```bash
command > output.log 2> error.log
```

➡️ `>` → standard output (stdout)
➡️ `2>` → error output (stderr)

If you want to store both in the same file:

```bash
command > all.log 2>&1
```

---

### **34. What is `nohup` command?**

`nohup` means **no hang up** — it allows a command to **keep running even after you log out**.
Example:

```bash
nohup ./myscript.sh &
```

➡️ Runs in background and doesn’t stop when terminal closes. Output goes to `nohup.out`.

---

### **35. What is `netstat` command in Linux?**

`netstat` shows **network connections, routing tables, and open ports**.
Example:

```bash
netstat -tuln
```

➡️ Lists all listening TCP/UDP ports.

Alternative modern command:

```bash
ss -tuln
```

---

### **36. How to run a script at boot level?**

You can make a script run automatically at startup using any of these:

| Method              | Description                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| **`/etc/rc.local`** | Add script path before `exit 0` (older systems)                                                       |
| **Crontab**         | Add to cron: `@reboot /path/to/script.sh`                                                             |
| **Systemd service** | Create a `.service` file under `/etc/systemd/system/` and enable it with `systemctl enable <service>` |

Example (crontab):

```bash
@reboot /home/user/startup.sh
```

---

Would you like me to combine **Q23–Q36** into a single clean interview notes sheet (one-liner answers)?

