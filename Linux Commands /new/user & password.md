Excellent 👏 — this is a **core Linux user management** topic and very common in interviews.
Let’s break it down clearly 👇

---

## 🧩 **1️⃣ /etc/passwd — User Account Information**

📍 **Path:** `/etc/passwd`

This file stores **basic user account details**.
Each line represents **one user** in this format:

```
username:x:UID:GID:comment:home_directory:shell
```

### Example:

```
teja:x:1001:1001:Teja User:/home/teja:/bin/bash
```

### Field breakdown:

| Field            | Meaning                                        |
| ---------------- | ---------------------------------------------- |
| `username`       | Login name of the user                         |
| `x`              | Placeholder (password stored in `/etc/shadow`) |
| `UID`            | User ID number                                 |
| `GID`            | Group ID number                                |
| `comment`        | Optional (full name or description)            |
| `home_directory` | User’s home directory                          |
| `shell`          | Default shell (like `/bin/bash`)               |

✅ All users can read `/etc/passwd`, but **only root can modify it**.

---

## 🔐 **2️⃣ /etc/shadow — Password and Expiration Information**

📍 **Path:** `/etc/shadow`

This file stores **encrypted passwords and password aging info**.
It is **readable only by root** (for security).

### Example:

```
teja:$6$abc123$...:19675:0:99999:7:::
```

### Field breakdown:

| Field                | Meaning                                               |
| -------------------- | ----------------------------------------------------- |
| `username`           | Same as in `/etc/passwd`                              |
| `encrypted_password` | The hashed password                                   |
| `last_change`        | Days since Jan 1, 1970 when password was last changed |
| `min`                | Minimum days before password can be changed again     |
| `max`                | Maximum days before password expires                  |
| `warn`               | Days before expiry to warn user                       |
| `inactive`           | Days after expiry before account disabled             |
| `expire`             | Date when account is disabled                         |
| `reserved`           | (unused)                                              |

---

## ⚙️ **3️⃣ Change a User’s Password Expiration**

You can manage this using the `chage` command.

### 🔍 View current password aging info

```bash
sudo chage -l username
```

Example output:

```
Last password change                                    : Oct 14, 2025
Password expires                                        : never
Password inactive                                       : never
Account expires                                         : never
Minimum number of days between password change          : 0
Maximum number of days between password change          : 90
Number of days of warning before password expires       : 7
```

---

### 🔧 Change password expiration settings

| Task                                                  | Command                               | Example                         |
| ----------------------------------------------------- | ------------------------------------- | ------------------------------- |
| Set **maximum** days before password expires          | `sudo chage -M <days> username`       | `sudo chage -M 90 teja`         |
| Set **minimum** days before password can change again | `sudo chage -m <days> username`       | `sudo chage -m 1 teja`          |
| Set **warning** days before expiry                    | `sudo chage -W <days> username`       | `sudo chage -W 7 teja`          |
| Set **account expiration date**                       | `sudo chage -E <YYYY-MM-DD> username` | `sudo chage -E 2025-12-31 teja` |

---

### Example full command:

```bash
sudo chage -M 90 -m 1 -W 7 teja
```

→ Password expires every 90 days, can’t change again within 1 day, warns 7 days before expiry.

---

✅ **In short:**

| File          | Purpose                                     |
| ------------- | ------------------------------------------- |
| `/etc/passwd` | Stores basic user info                      |
| `/etc/shadow` | Stores encrypted password & expiry data     |
| `chage`       | Used to view or set password aging policies |

---

Would you like me to explain how to **lock/unlock a user account** or **force a password reset** next?
