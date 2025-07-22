Here’s your **5-hour study plan** on:

* **Users, groups, permissions**
* `whoami`, `id`, `groups`, `chmod`, `chown`, `chgrp`, `sudo`
* **SUID**, **Sticky Bit**, **File permissions**
* **SUDO vs root**, and **Executable rights**

Each section includes:

* 🧠 Detailed explanation
* 💡 Examples
* ✅ Practice/test questions
* 💬 Interview-style questions

---

## 🕐 **Hour 1: Understanding Users, Groups, Permissions**

### 🔹 What Are Users and Groups?

* **Users**: Individuals/accounts in the system
* **Groups**: Collections of users with shared permissions
* Users are defined in `/etc/passwd`
* Groups are in `/etc/group`

### 🔹 Permissions

Linux permissions:

* 3 types: **Owner**, **Group**, **Others**
* 3 access levels:

  * `r` – read
  * `w` – write
  * `x` – execute

Check using:

```bash
ls -l file.txt
# -rwxr-xr-- 1 user group size date file.txt
```

### 🔹 Who is Who?

```bash
whoami      # Shows current username
id          # Shows UID, GID, groups
groups      # Shows groups of user
```

#### 💡 Examples:

```bash
whoami
id
groups
```

### ✅ Practice:

* Run `id` and explain each value
* Find your current group(s)
* Create a new user and assign to a group (if you can)

### 💬 Interview Questions:

* What does UID 0 mean?
* What’s the purpose of `/etc/passwd` and `/etc/shadow`?

---

## 🕑 **Hour 2: chmod – Change File Permissions**

### 🔹 `chmod` – Change permissions

```bash
chmod [permissions] file
```

You can set permissions in:

* **Symbolic mode**: `chmod u+x file.sh`
* **Numeric mode**: `chmod 755 file.sh`

### 🔹 Numeric permissions:

| Number | Binary | Meaning |
| ------ | ------ | ------- |
| 7      | 111    | rwx     |
| 6      | 110    | rw-     |
| 5      | 101    | r-x     |
| 4      | 100    | r--     |
| 0      | 000    | ---     |

```bash
chmod 755 script.sh
# Owner: rwx, Group: r-x, Others: r-x
```

### ✅ Practice:

* Create a file and remove execute permission
* Give all users full access (`777`)
* Restrict a file to only user read/write (`600`)

### 💬 Interview Questions:

* Difference between `chmod 755` and `chmod 700`?
* When would you give `x` permission to a script?

---

## 🕒 **Hour 3: chown, chgrp – Change Ownership**

### 🔹 `chown` – Change file owner

```bash
chown newuser file.txt
chown newuser:newgroup file.txt
```

### 🔹 `chgrp` – Change only group

```bash
chgrp devteam file.txt
```

### 🔹 View ownership:

```bash
ls -l
```

### 💡 Examples

```bash
sudo chown root:root important.conf
sudo chgrp developers project/
```

### ✅ Practice:

* Change ownership of a test file to a new user
* Change group of a directory
* Observe difference between `chown` and `chgrp`

### 💬 Interview Questions:

* When would you use `chgrp` instead of `chown`?
* Can non-root users change ownership?

---

## 🕓 **Hour 4: sudo, root, and Special Permission Bits**

### 🔹 `sudo` – Run command as superuser

```bash
sudo apt update
```

### 🔹 Difference: `sudo` vs `su`

* `sudo`: Single command as root
* `su`: Switch user session entirely (to root)

### 🔹 Special Permissions

| Special Bit | Symbol                | Meaning                    |
| ----------- | --------------------- | -------------------------- |
| **SUID**    | `s` in owner execute  | Execute as file owner      |
| **SGID**    | `s` in group execute  | Execute as group           |
| **Sticky**  | `t` in others execute | Only file owner can delete |

### 🔹 Examples

* **SUID example** (e.g. `passwd`):

```bash
ls -l /usr/bin/passwd
# -rwsr-xr-x 1 root root ...
```

* **Sticky bit** (e.g. `/tmp`):

```bash
ls -ld /tmp
# drwxrwxrwt
```

* Set sticky bit:

```bash
chmod +t shared_folder
```

* Set SUID:

```bash
chmod u+s filename
```

### ✅ Practice:

* Check if `/tmp` has sticky bit
* Find files with SUID using `find / -perm -4000`
* Set SUID bit to a script (try it with caution)

### 💬 Interview Questions:

* What does `chmod 4755` mean?
* Why is `passwd` using SUID?
* What’s the use of sticky bit in `/tmp`?

---

## 🕔 **Hour 5: Executable Rights & Permission Mastery**

### 🔹 Making Scripts Executable

```bash
chmod +x script.sh
./script.sh
```

If not executable:

```bash
bash script.sh
```

### 🔹 Permission Bits Review

| Position | Permissions | Who               |
| -------- | ----------- | ----------------- |
| 1        | `-` or `d`  | File or directory |
| 2-4      | `rwx`       | Owner             |
| 5-7      | `rwx`       | Group             |
| 8-10     | `rwx`       | Others            |

Example:

```
-rwxr--r-- 1 user group 0 Jul 22 test.sh
```

### 🔹 Combine Commands

```bash
chmod 755 script.sh
chown tejaaswini:devops script.sh
```

### ✅ Practice:

* Create a script, make it executable, and change ownership
* List all scripts with execute permission in `/usr/bin`
* Set SGID on a folder

### 💬 Interview Questions:

* How do you make a file executable?
* What is the effect of `chmod 000 file`?
* What are the permission bits in `drwxrwxrwt`?

---

## 📘 Summary Sheet

| Command  | Purpose                 |
| -------- | ----------------------- |
| `whoami` | Current user            |
| `id`     | User ID, group ID       |
| `groups` | Groups of user          |
| `chmod`  | Change file permissions |
| `chown`  | Change file owner       |
| `chgrp`  | Change file group       |
| `sudo`   | Run as superuser        |
| `ls -l`  | View permissions        |

---

## 📝 Quiz & Test Yourself

### ✅ MCQs

1. What permission does `chmod 644` give?

   * A) rwxrwxrwx
   * B) rw-r--r-- ✅
   * C) rwxr-xr-x
   * D) rwx------

2. What does SUID mean?

   * A) Run with group’s permission
   * B) Run as file’s owner ✅
   * C) No execution
   * D) Requires sudo

3. What does the `t` in `drwxrwxrwt` mean?

   * A) SUID
   * B) Temp folder
   * C) Sticky Bit ✅
   * D) No permission

### ✍️ Exercises

* Use `chmod` to give yourself full rights but read-only to others.
* Use `find` to locate files with SUID set.
* Make a script that says "Hello" and ensure only the owner can execute it.

---

Would you like me to:

* Generate this in **Google Sheet** format?
* Provide a **quiz** as a downloadable file?
* Prepare a **hands-on lab exercise list**?

Let me know how you want to practice further.
