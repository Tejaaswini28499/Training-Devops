ls -l = meaning long list

Types of files in Linux
 '-' = File,
 d = Directory,
 l = link,
 C = Special File,
 s = Socket,
 p = pipe,
 hw = hardware information,

file <filename> = return the filetype.


Great question 👏 — this is one of the most **common Linux interview topics** and also a **fundamental concept** for working with the Linux filesystem.

Let’s go step by step 👇

---

## 🧩 **Types of Files in Linux**

In Linux, **everything is treated as a file** — even hardware devices, sockets, and directories.
There are **7 main types of files**.

---

### 🗂️ 1. **Regular File (`-`)**

These are the **most common** files — they store data, text, programs, scripts, etc.

* Includes:

  * Text files (`.txt`, `.log`, `.conf`)
  * Binary files (`/bin/ls`, `/usr/bin/bash`)
  * Scripts (`.sh`, `.py`)

#### 🔹 Example:

```bash
ls -l
```

Output:

```
-rw-r--r--  1 user user  4096 Oct 13  readme.txt
```

→ The first character is `-` → **Regular file**

---

### 📁 2. **Directory File (`d`)**

A directory is a **special file** that contains a list of other files and directories.

#### 🔹 Example:

```bash
ls -l /
```

Output:

```
drwxr-xr-x  5 root root  4096 Oct 13  etc
```

→ Starts with `d` → **Directory**

---

### 🧵 3. **Character Device File (`c`)**

Used for **character-oriented devices** — devices that handle data one character at a time (like keyboards, serial ports).

* Found in `/dev/`
* Example devices:

  * `/dev/tty` → terminal
  * `/dev/null` → data sink

#### 🔹 Example:

```bash
ls -l /dev/tty
```

Output:

```
crw-rw-rw-  1 root tty 5, 0 Oct 13  /dev/tty
```

→ Starts with `c` → **Character device**

---

### 💾 4. **Block Device File (`b`)**

Used for **block-oriented devices** — devices that handle data in blocks (like hard drives, USBs).

* Found in `/dev/`
* Example:

  * `/dev/sda` (disk)
  * `/dev/sdb1` (disk partition)

#### 🔹 Example:

```bash
ls -l /dev/sda
```

Output:

```
brw-rw----  1 root disk 8, 0 Oct 13 /dev/sda
```

→ Starts with `b` → **Block device**

---

### 🔗 5. **Symbolic Link (`l`)**

These are **shortcuts or pointers** to other files.
Works like Windows shortcuts.

#### 🔹 Example:

```bash
ls -l /bin/sh
```

Output:

```
lrwxrwxrwx  1 root root  4 Oct 13  /bin/sh -> bash
```

→ Starts with `l` → **Symbolic link**

---

### 🧩 6. **Socket File (`s`)**

Used for **inter-process communication (IPC)** between applications.
You’ll often see these in `/var/run/` or `/tmp/`.

#### 🔹 Example:

```bash
ls -l /var/run/docker.sock
```

Output:

```
srw-rw----  1 root docker 0 Oct 13 /var/run/docker.sock
```

→ Starts with `s` → **Socket file**

---

### 🧭 7. **Named Pipe (FIFO) (`p`)**

Used for **communication between processes** — data flows in one direction (first-in, first-out).

#### 🔹 Example:

```bash
mkfifo mypipe
ls -l
```

Output:

```
prw-r--r--  1 user user 0 Oct 13 mypipe
```

→ Starts with `p` → **Named pipe (FIFO)**

---

## 🔍 Quick Summary Table

| Symbol | Type              | Example                | Description                     |
| :----: | ----------------- | ---------------------- | ------------------------------- |
|   `-`  | Regular File      | `/etc/passwd`          | Normal text or binary file      |
|   `d`  | Directory         | `/home/user/`          | Contains files/subdirectories   |
|   `c`  | Character Device  | `/dev/tty`             | Character-based device          |
|   `b`  | Block Device      | `/dev/sda`             | Block-based device              |
|   `l`  | Symbolic Link     | `/bin/sh -> bash`      | Shortcut to another file        |
|   `s`  | Socket            | `/var/run/docker.sock` | Communication between processes |
|   `p`  | Named Pipe (FIFO) | `/tmp/mypipe`          | Data exchange between processes |

---

## 💡 Interview Tip:

**Q:** How can you find the type of a file?
**A:** Use the `ls -l` command (first character of permissions) or `file` command.

Example:

```bash
file /dev/sda
```

Output:

```
/dev/sda: block special
```

---

Would you like me to give you a **diagram + examples for each file type (visual explanation)** next?
It helps you remember faster for interviews.


