----------------------
How do you monitor disk usage and handle full disk issues?
---------------


## 🧠 1. **How to Monitor Disk Usage**

### 🔹 Basic Linux Commands

| Command                      | Purpose                                           | Example           |
| ---------------------------- | ------------------------------------------------- | ----------------- |
| `df -h`                      | Shows disk space usage of all mounted filesystems | `df -h`           |
| `du -sh /var/log`            | Shows total size of a directory                   | `du -sh /var/log` |
| `lsblk`                      | Lists all block devices (disks, partitions)       | `lsblk`           |
| `ncdu /`                     | Interactive disk usage viewer (if installed)      | —                 |
| `find / -type f -size +500M` | Find large files over 500 MB                      | —                 |

**Key flags:**

* `df -i` → check inode usage (if full, you can’t create new files even with free space)
* `du -ah --max-depth=1 /` → breakdown by directories

---

## ⚙️ 2. **How to Monitor Automatically (Prevent Full Disk)**

### 🔸 System-level monitoring tools

* **`iostat`** (from `sysstat`) → shows disk I/O performance
* **`vmstat`**, **`dstat`**, **`iotop`** → for real-time monitoring
* **`journalctl --disk-usage`** → shows systemd log disk usage

### 🔸 Continuous Monitoring / Alerting

* **CloudWatch** (AWS) → create an alarm for `DiskUsedPercent > 80%`
* **Prometheus + Node Exporter + Grafana** → visualize and alert
* **Datadog / New Relic / ELK Stack** → enterprise monitoring solutions

💡 **Set threshold-based alerts**:
Example:

* Warning at 75%
* Critical alert at 90%
* Auto-cleanup job at 95%

---

## 🚨 3. **Handling Full Disk Issues (Troubleshooting Steps)**

### Step 1️⃣: Identify which partition is full

```bash
df -h
```

### Step 2️⃣: Find large directories

```bash
du -sh /* | sort -rh | head -n 10
```

### Step 3️⃣: Dig deeper

```bash
du -sh /var/* | sort -rh | head
du -sh /home/* | sort -rh | head
```

### Step 4️⃣: Find large files

```bash
find / -type f -size +500M -exec ls -lh {} \;
```

### Step 5️⃣: Check logs

Logs usually cause disk fill-ups:

```bash
cd /var/log
ls -lh
```

If huge:

```bash
sudo truncate -s 0 /var/log/filename.log
```

or rotate logs:

```bash
sudo logrotate -f /etc/logrotate.conf
```

### Step 6️⃣: Remove old files

* `/tmp` and `/var/tmp`
* Docker images/containers:

  ```bash
  docker system prune -af
  ```
* Journal logs:

  ```bash
  journalctl --vacuum-size=500M
  ```

---

## 🧩 4. **Prevention Strategies**

| Method                                        | Description                                     |
| --------------------------------------------- | ----------------------------------------------- |
| **Log rotation**                              | Configure `/etc/logrotate.d/` properly          |
| **Separate partitions**                       | `/var`, `/home`, `/`, `/tmp` on different disks |
| **Cloud Auto-scaling / Auto-cleanup scripts** | E.g., Lambda or cron job to cleanup             |
| **Retention policies**                        | Delete old artifacts, backups, temp files       |
| **Monitoring + Alerts**                       | Automated alerts via Prometheus or CloudWatch   |

---

## 🧠 5. **Example Interview Answer (Concise)**

> “I monitor disk usage using `df -h` and `du -sh` commands, and automate alerts via Prometheus and CloudWatch.
> When disk usage crosses 80%, I check which directories are consuming space using `du` and clean logs, Docker images, or temporary files.
> For prevention, I configure log rotation, retention policies, and alerts. I also use `journalctl --vacuum-size` for system logs and ensure separate partitions for `/var` and `/tmp`.”

---

## 💬 6. **Bonus: Common Real-world Causes**

* Application log files growing uncontrolled
* Docker images or containers not cleaned up
* Backups stored locally instead of S3
* Misconfigured temp directories or caches
* Jenkins workspaces not purged

---

Would you like me to give you **a hands-on practice lab** (step-by-step commands on how to simulate and fix a full disk issue in Linux)?
It’s great for DevOps interview + real troubleshooting confidence.
