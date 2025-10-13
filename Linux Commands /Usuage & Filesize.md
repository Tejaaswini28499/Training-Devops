size of file - ls -l filename.txt

du (Disk usuage)- du -h filename

stat- file size in Bytes 

Find size of a directory - du -sh /path

In Linux, there are multiple ways to **check the size of a file**. Here’s a clear breakdown:

---

## **1. Using `ls -l`**

Shows detailed information about files, including their size in **bytes**.

```bash
ls -l filename
```

**Example:**

```bash
ls -l file.txt
-rw-r--r-- 1 tejaaswini tejaaswini 2048 Oct 13 20:00 file.txt
```

* `2048` → size in **bytes**.

---

## **2. Using `du` (Disk Usage)**

Shows the **file size in blocks or human-readable format**.

```bash
du filename
```

**Human-readable format:**

```bash
du -h filename
```

**Example:**

```bash
du -h file.txt
4.0K    file.txt
```

* `4.0K` → size of the file on disk (may be slightly larger than actual size due to block allocation).

---

## **3. Using `stat`**

Provides detailed info including **file size in bytes**.

```bash
stat filename
```

**Example:**

```bash
stat file.txt
  File: file.txt
  Size: 2048        Blocks: 8          IO Block: 4096 regular file
  ...
```

* `Size: 2048` → size in bytes.

---

## **4. Using `wc -c`** (for text files)

Counts **number of bytes/characters** in a file.

```bash
wc -c filename
```

**Example:**

```bash
wc -c file.txt
2048 file.txt
```

---

✅ **Tip:**

* `ls -lh` is good for a quick view in **KB, MB, GB**.
* `du -h` shows **disk usage**, which may differ from actual file size.

---

If you want, I can also show a **one-liner command to check the size of all files in a directory in human-readable format**—super handy for big directories.

Do you want me to do that?
