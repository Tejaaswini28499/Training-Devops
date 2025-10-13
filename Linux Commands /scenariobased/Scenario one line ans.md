Perfect! I’ll create a **comprehensive answer guide for all 100 Linux scenario-based DevOps questions**. To keep it structured and easy to follow, I’ll divide it into the same **10 categories** and provide:

* **Step-by-step solutions**
* **Linux commands/examples**
* **Best practices & notes**

Here’s the **complete guide**:

---

## **🖥️ 1. Linux System & Process Management – Answers**

1. **Process stuck in uninterruptible sleep**: Usually waiting for I/O. Check with `ps aux | grep D` and `iotop` to see disk I/O. Fix underlying disk/network issue.
2. **Slow process**: Use `top`, `htop` for CPU, `iotop`/`iostat` for I/O, `vmstat` for memory stats.
3. **Zombie processes**: Check with `ps aux | grep Z`. Kill the parent process or wait for it to exit.
4. **Limit CPU**: `nice -n 10 command`, `renice -n 10 PID`, or cgroups (`cgcreate -g cpu:/mygroup`).
5. **Identify memory hog**: `top`, `htop`, `free -h`, `ps aux --sort=-%mem | head`.
6. **Check port**: `lsof -i :PORT`, `netstat -tulnp`, `ss -tulnp`.
7. **Kill stubborn process**: Check `pstree -p PID` for child processes, kill children first. Use `kill -9 PID` as last resort.
8. **Daemon hang**: `journalctl -u service_name`, `systemctl status service_name`, check config files.
9. **Monitor usage**: `top`, `htop`, `vmstat 2`, `sar -u 2` for CPU trends.
10. **Daemon restart failure**: `systemctl status service`, check `/var/log/messages` or `/var/log/syslog`.

---

## **📂 2. File System & Storage Management – Answers**

11. **Find large files**: `find / -type f -size +500M`, `du -ah / | sort -rh | head -n 20`.
12. **Directory usage**: `du -sh /var/*`, `ncdu /`.
13. **Inode usage**: `df -i`, important if `df -h` shows free space but you cannot create files.
14. **Mount new disk**: `fdisk /dev/sdb`, `mkfs.ext4 /dev/sdb1`, add to `/etc/fstab`.
15. **Resize partition**: `lvextend -L +10G /dev/volumegroup/lv`, then `resize2fs /dev/volumegroup/lv`.
16. **du -sh vs df -h**: `du -sh` shows directory size, `df -h` shows disk usage by filesystem.
17. **Recover deleted files**: `extundelete`, `testdisk`, or restore from backup.
18. **Rsync migration**: `rsync -avz /source/ /destination/`.
19. **Log cleanup**: Configure `logrotate` or cron: `find /var/log -type f -mtime +7 -delete`.
20. **Disk I/O performance**: `iostat -x 2`, `iotop`, `vmstat 2`.

---

## **🔍 3. Networking & Connectivity – Answers**

21. **Service unreachable**: `curl -v localhost:PORT`, `systemctl status service`, `firewall-cmd --list-all`.
22. **Check port reachability**: `telnet IP PORT`, `nc -zv IP PORT`, `curl IP:PORT`.
23. **DNS issues**: `nslookup domain.com`, `dig domain.com`, check `/etc/resolv.conf`.
24. **Active connections**: `ss -tulnp`, `netstat -tulnp`.
25. **Bandwidth monitoring**: `iftop`, `nload`, `vnstat`.
26. **Packet loss**: `ping -c 10 IP`, `mtr IP`.
27. **Add static route**: `ip route add 10.0.0.0/24 via 192.168.1.1`, persist in `/etc/network/interfaces` or `/etc/sysconfig/network-scripts/`.
28. **Firewall troubleshooting**: `iptables -L -v -n`, `firewall-cmd --list-all`.
29. **Assign IP**: `ip addr add 192.168.1.100/24 dev eth0`, permanent via `/etc/netplan/` or network-scripts.
30. **Latency issues**: `ping`, `traceroute`, `mtr`, check MTU issues, network load, firewall rules.

---

## **⚡ 4. User & Permission Management – Answers**

31. **Directory access**: `ls -ld /path`, `chmod/g` to fix permissions.
32. **New sudo user**: `adduser username`, `usermod -aG sudo username`.
33. **chmod 4755**: SUID bit set, allows execution as file owner (used for `passwd`).
34. **Logged-in users**: `w`, `who`, `last`.
35. **Restrict user**: `chroot`, `rbash` or set command in `.bash_profile`.
36. **Cron permission issues**: Check user’s environment variables, `PATH`, and script permissions.
37. **Restore `/etc` permissions**: Use backup or reinstall packages.
38. **Find files by user**: `find / -user username`.
39. **Password expiry**: `chage -l username`, configure `/etc/login.defs`.
40. **2FA**: `Google Authenticator PAM module`, configure SSH.

---

## **📝 5. Logs & Monitoring – Answers**

41. **Analyze huge logs**: `less`, `grep`, `awk`, `tail -f`.
42. **Search errors**: `grep -i "error" /var/log/*`.
43. **Log rotation**: Use `logrotate`, configure `/etc/logrotate.d/appname`.
44. **Unresponsive server**: Check `/var/log/syslog`, `dmesg`, `journalctl -xe`.
45. **Monitor resources**: Use `Grafana + Prometheus` or `Glances`.
46. **Real-time alert**: Configure `monit`, `nagios`, or use `systemd` service watchers.
47. **journalctl vs /var/log/messages**: `journalctl` is structured binary log, `messages` is plaintext.
48. **Historical usage**: `sar -u`, `sar -r`, or `collectl`.
49. **Kernel panic**: `dmesg | less`, `journalctl -k`.
50. **Random reboot**: Check `/var/log/syslog`, `last -x`, `dmesg`.

---

## **⚙️ 6. Package Management & Updates – Answers**

51. **Install on multiple servers**: Use `ansible -m yum -a "name=package state=present"`.
52. **Check package**: `dpkg -l package` (Debian), `rpm -qa | grep package` (RHEL).
53. **Rollback package**: `yum downgrade package` or use snapshot.
54. **Safe updates**: `yum update --security`, `apt update && apt upgrade`.
55. **Dependency issues**: `yum deplist package`, `apt --fix-broken install`.
56. **Custom repo**: Add `.repo` file in `/etc/yum.repos.d/` or `sources.list`.
57. **Remove unused packages**: `yum autoremove`, `apt autoremove`.
58. **Verify package**: `rpm -V package`.
59. **Create custom package**: Use `rpmbuild` or `dpkg-deb --build`.
60. **Unattended updates**: `apt install unattended-upgrades`, configure `/etc/apt/apt.conf.d/50unattended-upgrades`.

---

## **🔧 7. Shell Scripting & Automation – Answers**

61. **CPU monitor script**:

```bash
#!/bin/bash
CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
if (( $(echo "$CPU>80" | bc -l) )); then
  echo "High CPU $CPU%" | mail -s "CPU Alert" admin@example.com
fi
```

62. **Automate backup**: `0 2 * * * tar -czf /backup/dir_$(date +\%F).tar.gz /data`.
63. **Script args**: `$1`, `$2`, `$@` for positional parameters.
64. **Debug script**: `bash -x script.sh` or check environment variables.
65. **Automate log cleanup**: Use `find /var/log -type f -mtime +7 -delete` in cron.
66. **Run at reboot**: Add cron `@reboot /path/to/script.sh`.
67. **Error handling**: Use `set -e`, check `$?`, trap signals.
68. **Count log files**: `find /var/log -name "*.log" | wc -l`.
69. **Check service in script**:

```bash
if ! systemctl is-active --quiet nginx; then systemctl restart nginx; fi
```

70. **Secure credentials**: Store in `.env` file with 600 permissions or use Vault.

---

## **💻 8. System Security – Answers**

71. **Identify malicious processes**: `top`, `ps aux`, check unusual ports, `chkrootkit`.
72. **Audit user activity**: `auditd`, `ausearch`, `last`, `lastb`.
73. **Disable SSH password**: `PasswordAuthentication no` in `/etc/ssh/sshd_config`.
74. **World-writable files**: `find / -type f -perm -o+w`.
75. **Check sudo users**: `getent group sudo`, `visudo`.
76. **Fail2ban**: Configure jail for SSH, monitor logs, block IPs automatically.
77. **Verify integrity**: `sha256sum file`, `rpm -V package`.
78. **Secure service**: Restrict firewall, run as non-root, patch regularly.
79. **Encryption**: `LUKS` for disk, `openssl` for data in transit.
80. **Trace unauthorized changes**: `auditd`, check file timestamps, compare backups.

---

## **⚡ 9. Backup, Recovery & High Availability – Answers**

81. **Database restore**: Use `mysqldump` or `pg_restore`.
82. **Automated backup**: `cron` or `systemd timers` with scripts.
83. **Incremental backup**: `rsync --link-dest`, `tar --listed-incremental`.
84. **Recover `/home`**: Restore from backup or use `extundelete` if not overwritten.
85. **Test backup**: Restore on test server and verify.
86. **RAID**: `mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sd[b-c]`.
87. **Replication**: `rsync -avz`, `GlusterFS`, `DRBD`, or database replication.
88. **Disk failure**: Replace disk, add to RAID, rebuild, check logs.
89. **Snapshot**: LVM: `lvcreate -L1G -s -n snap /dev/vg/lv`.
90. **Verify backup**: `tar -tzf backup.tar.gz` or checksum compare.

---

## **📦 10. Containers, Docker & DevOps Workflows – Answers**

91. **Container fails**: `docker logs container`, `docker inspect`, check volumes and networks.
92. **Persist data**: Use `docker volumes` or bind mount `-v /host:/container`.
93. **Monitor container resources**: `docker stats`, `cAdvisor`.
94. **Clean unused objects**: `docker system prune -a`.
95. **Deploy interdependent services**: Use `docker-compose` or Kubernetes manifests.
96. **Networking issues**: `docker network ls`, `docker exec -it container ping`.
97. **Auto-restart**: `--restart unless-stopped` or systemd service.
98. **Optimized image**: Use small base (`alpine`), multi-stage builds, remove caches.
99. **Log rotation**: Configure `logrotate` or `docker logging driver`.
100. **Secure container**: Run non-root, minimal privileges, scan images with `trivy`.

---

This guide is **ready for interview prep**, real-world Linux scenarios, and hands-on DevOps usage.

I can also **make a 1-page printable cheat sheet** with **all 100 questions + key commands** for rapid revision if you want.

Do you want me to do that next?
