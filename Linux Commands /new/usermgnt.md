Here’s a clear and practical explanation of **how to manage user permissions in a Linux environment** — suitable for interviews and real DevOps work 👇

---

## 🧠 1. **Understand Linux Permission Basics**

Each file and directory in Linux has **three permission types** for **three categories of users**:

| Category       | Description                 |
| -------------- | --------------------------- |
| **Owner (u)**  | The user who owns the file  |
| **Group (g)**  | Users in the same group     |
| **Others (o)** | Everyone else on the system |

Each can have these **permissions**:

| Permission | Symbol | Numeric Value | Meaning                                     |
| ---------- | ------ | ------------- | ------------------------------------------- |
| Read       | r      | 4             | View file content / list directory          |
| Write      | w      | 2             | Modify file / create or delete in directory |
| Execute    | x      | 1             | Run file / access directory                 |

Example:

```
-rwxr-x---
```

means:
Owner = read/write/execute, Group = read/execute, Others = no access.

---

## 🛠️ 2. **Manage Ownership**

### Change File Owner:

```bash
chown username file.txt
```

### Change Group:

```bash
chown :groupname file.txt
```

### Change Both:

```bash
chown username:groupname file.txt
```

---

## ⚙️ 3. **Modify Permissions**

### Using Symbolic Mode:

```bash
chmod u+rwx,g+rx,o-r file.txt
```

### Using Numeric Mode:

Each permission value is summed:

* rwx = 7
* rw- = 6
* r-- = 4

Example:

```bash
chmod 755 script.sh
```

➡️ Owner = 7 (rwx), Group = 5 (r-x), Others = 5 (r-x)

---

## 🧩 4. **Set Default Permissions (umask)**

`umask` defines default permissions for new files/directories.

View current umask:

```bash
umask
```

Example:

```bash
umask 022
```

→ New files = `644`, directories = `755`

---

## 🔐 5. **Advanced Permission Controls**

### a. **Setuid (4)**

Run a file with the owner’s privileges.

```bash
chmod 4755 /usr/bin/someapp
```

### b. **Setgid (2)**

Files created in a directory inherit the group.

```bash
chmod 2755 /shared/folder
```

### c. **Sticky Bit (1)**

Only the file owner can delete their files in shared directories.

```bash
chmod 1777 /tmp
```

---

## 👥 6. **Group Management**

Create and manage user groups to control access collectively.

```bash
groupadd devteam
usermod -aG devteam teja
chown :devteam /project
chmod 770 /project
```

➡️ Only members of `devteam` can access `/project`.

---

## 🧱 7. **Access Control Lists (ACLs)** – Fine-grained permissions

For complex scenarios where basic owner/group/others aren’t enough:

Enable ACLs:

```bash
mount -o remount,acl /
```

Set specific user permission:

```bash
setfacl -m u:john:rwx /project
```

View ACLs:

```bash
getfacl /project
```

---

## 🧰 8. **Best Practices for Managing Permissions**

✅ Principle of least privilege — give only what’s needed.
✅ Use groups for managing team access instead of per-user changes.
✅ Protect sensitive files (like `/etc/shadow`) strictly (e.g., `640`).
✅ Regularly audit permissions with:

```bash
find / -perm -4000
```

(to find all SUID binaries).

---

Would you like me to give a **scenario-based explanation** (e.g., managing permissions for a shared project folder among developers and testers)? That’s often asked in DevOps/Linux interviews.
