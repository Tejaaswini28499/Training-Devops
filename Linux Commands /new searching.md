locate: is a fast command-line tool to search files and directories by name. It's faster than find because it uses a pre-built database

How locate Works
locate reads from a database (/var/lib/mlocate/mlocate.db) that stores paths of all files on the system.

The database is updated using updatedb.

locate passwd
# Might return:
/etc/passwd
/usr/share/doc/passwd

you will get command not found error so install below commands
sudo dnf install mlocate    # Install locate
sudo updatedb               # Build the file index
locate passwd               # Search for files containing "passwd"

Here are **practice and interview-style questions** on the `find` command, ranging from beginner to advanced, focused on real-world DevOps and Linux admin use cases:

---

## ✅ **Beginner-Level Practice Questions**

1. **Find all `.sh` files in your home directory:**

   ```bash
   find ~/ -name "*.sh"
   ```

2. **Find all empty files in `/tmp`:**

   ```bash
   find /tmp -type f -empty
   ```

3. **Find all directories named `backup`:**

   ```bash
   find / -type d -name "backup"
   ```

4. **Find all files larger than 10MB in `/var`:**

   ```bash
   find /var -type f -size +10M
   ```

5. **Find all files modified more than 30 days ago:**

   ```bash
   find . -type f -mtime +30
   ```

---

## 🔁 **Intermediate-Level Questions**

6. **Find and delete all `.tmp` files older than 7 days in `/tmp`:**

   ```bash
   find /tmp -type f -name "*.tmp" -mtime +7 -exec rm -f {} \;
   ```

7. **Find files owned by user `ubuntu`:**

   ```bash
   find / -user ubuntu
   ```

8. **Find all symbolic links in `/usr`:**

   ```bash
   find /usr -type l
   ```

9. **Find all files not accessed in the last 90 days:**

   ```bash
   find / -type f -atime +90
   ```

10. **Find all `.conf` files and list them with their size:**

```bash
find /etc -type f -name "*.conf" -exec ls -lh {} \;
```

---

## 🔒 **Security/DevOps-Oriented Questions**

11. **Find all files with SUID bit set:**

```bash
find / -type f -perm -4000
```

12. **Find all files with world-writable permissions:**

```bash
find / -type f -perm -0002
```

13. **Find files modified in the last 15 minutes:**

```bash
find / -type f -mmin -15
```

14. **Find files between 1MB and 100MB in `/var`:**

```bash
find /var -type f -size +1M -size -100M
```

---

## 💬 **Interview Questions**

1. What is the difference between `-mtime`, `-atime`, and `-ctime`?
2. How does `-exec` work in `find`? How does it differ from `xargs`?
3. What is the use of `{}` in `find ... -exec`?
4. How do you find all `.log` files and search them for "ERROR" in a single command?
5. What happens if you omit `-type f` in a `find` command?
6. How do you use `find` to delete only empty directories?

---
Here's a 5-hour study guide covering **Searching & Text Processing** commands in Linux, including explanations, usage examples, practice questions, and potential interview questions.

---

### 🧠 **1st Hour – File Searching: `find`, `locate`, `which`**

#### ✅ `find`

* **Use**: Search files/directories by name, size, type, modified time, etc.
* **Syntax**: `find [path] [criteria] [action]`
* **Examples**:

  * `find /etc -name "hosts"` → Find file named `hosts` in `/etc`.
  * `find . -type f -size +10M` → Find files >10MB in current directory.
  * `find /var/log -mtime -1` → Find files modified in last 24 hours.

#### ✅ `locate`

* **Use**: Fast file search using an index (`updatedb` needed).
* **Example**:

  * `locate passwd` → Lists all paths with "passwd" in the name.

#### ✅ `which`

* **Use**: Find location of executables in `$PATH`.
* **Example**:

  * `which python3` → `/usr/bin/python3`

---

### 🧪 Practice (Hour 1):

1. Find all `.log` files in `/var/log` modified in the last 2 days.
2. Use `which` to check location of `bash` and `ls`.

---

### 🧩 Interview Questions (Hour 1):

* What's the difference between `find` and `locate`?
* How would you find the 5 largest files in `/home`?

---

### 🧠 **2nd Hour – Text Searching: `grep`**

#### ✅ `grep`

* **Use**: Search for patterns in files.
* **Syntax**: `grep [options] pattern file`
* **Examples**:

  * `grep "error" syslog.txt` → Find lines with "error"
  * `grep -i "Error"` → Case insensitive
  * `grep -r "password" /etc/` → Recursively search in dir
  * `grep -v "DEBUG"` → Show lines that don’t match
  * `grep -n "root" /etc/passwd` → Show line numbers

#### 🔥 Common patterns:

* `^root` → Lines starting with "root"
* `root$` → Lines ending with "root"
* `[0-9]{4}` → Lines with 4 digits

---

### 🧪 Practice (Hour 2):

1. Use `grep` to find all lines starting with "root" in `/etc/passwd`.
2. Find lines with the word "fail" (case-insensitive) in `auth.log`.

---

### 🧩 Interview Questions (Hour 2):

* How do you exclude lines in `grep`?
* What’s the difference between `grep` and `egrep`?

---

### 🧠 **3rd Hour – Sorting & Counting: `sort`, `uniq`, `wc`**

#### ✅ `sort`

* **Use**: Sort file lines.
* **Examples**:

  * `sort names.txt` → Alphabetical sort
  * `sort -r` → Reverse order
  * `sort -n` → Numeric sort

#### ✅ `uniq`

* **Use**: Remove adjacent duplicates.
* **Examples**:

  * `sort file.txt | uniq` → Remove all duplicates
  * `uniq -c` → Count duplicate lines

#### ✅ `wc`

* **Use**: Count lines, words, characters.
* **Examples**:

  * `wc file.txt` → lines, words, bytes
  * `wc -l file.txt` → line count

---

### 🧪 Practice (Hour 3):

1. Find the number of users in `/etc/passwd`: `wc -l /etc/passwd`
2. Sort `file.txt` and count unique words.

---

### 🧩 Interview Questions (Hour 3):

* How do you find the most common lines in a log?
* Why sort before `uniq`?

---

### 🧠 **4th Hour – Cutting & Processing: `cut`, `awk`, `sed`**

#### ✅ `cut`

* **Use**: Extract columns/fields from text.
* **Examples**:

  * `cut -d ":" -f 1 /etc/passwd` → Print usernames
  * `cut -c 1-5` → First 5 characters of each line

#### ✅ `awk`

* **Use**: Pattern scanning and processing.
* **Examples**:

  * `awk -F ':' '{print $1}' /etc/passwd` → Usernames
  * `awk '{sum+=$2} END {print sum}'` → Sum 2nd column

#### ✅ `sed`

* **Use**: Stream editor (find and replace, delete lines, etc.)
* **Examples**:

  * `sed 's/root/admin/' /etc/passwd` → Replace first "root"
  * `sed -n '5,10p' file.txt` → Print lines 5 to 10

---

### 🧪 Practice (Hour 4):

1. Use `cut` to display only usernames from `/etc/passwd`.
2. Replace "Error" with "Warning" in a file using `sed`.
3. Use `awk` to display only lines where 3rd column > 100.

---

### 🧩 Interview Questions (Hour 4):

* Difference between `awk` and `sed`?
* Use `awk` to calculate average of column in CSV.

---

### 🧠 **5th Hour – Combining Commands with Pipes (`|`)**

#### ✅ Pipes (`|`)

* **Use**: Pass output of one command as input to another.
* **Examples**:

  * `ps aux | grep nginx`
  * `cat access.log | grep "404" | wc -l` → Count 404s
  * `df -h | grep "/dev/sda1"`

---

### 🧪 Practice (Hour 5):

1. Count how many users have `/bin/bash` shell:

   * `grep "/bin/bash" /etc/passwd | wc -l`
2. Find top 5 IPs from access log:

   * `cut -d ' ' -f 1 access.log | sort | uniq -c | sort -nr | head -5`

---

### 🧩 Interview Questions (Hour 5):

* Explain how pipes work.
* How would you extract and sort errors from logs?

---

### 📘 Summary Table

| Command  | Use                        |                  |
| -------- | -------------------------- | ---------------- |
| `find`   | Search files by attributes |                  |
| `locate` | Fast indexed file search   |                  |
| `which`  | Find path of executables   |                  |
| `grep`   | Search text using regex    |                  |
| `sort`   | Sort lines                 |                  |
| `uniq`   | Remove duplicate lines     |                  |
| `wc`     | Count lines/words          |                  |
| `cut`    | Extract specific fields    |                  |
| `awk`    | Field-wise processing      |                  |
| `sed`    | Text transformation        |                  |
| \`       | \` (pipe)                  | Combine commands |

---

Would you like this as a printable **PDF or Google Sheet** for daily revision?

