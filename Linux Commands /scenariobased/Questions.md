Absolutely! Since you want **scenario-based Linux questions for a DevOps engineer with 5 years of experience**, I’ll structure them to test **practical problem-solving, real-world Linux administration, and DevOps workflows**. I’ll divide them into **10 categories** for easier learning and interview preparation.

---

## **🖥️ 1. Linux System & Process Management**

1. A critical process is consuming 100% CPU, but `top` shows it’s stuck in uninterruptible sleep. How do you handle it?
2. A user complains that their process is running slow. How do you identify CPU vs I/O bottleneck?
3. You notice zombie processes accumulating. How do you clean them?
4. Explain how you would limit a user’s CPU usage using `nice` and `cgroups`.
5. Your server is running out of memory; how do you identify which process is the culprit?
6. How do you check which process is listening on a specific port?
7. How would you kill a process that refuses to terminate with `kill -9`?
8. A process has hung during startup. How do you debug it using system logs?
9. How do you monitor real-time CPU and memory usage for a high-load application?
10. A daemon is not restarting after failure. How do you debug it in `systemd`?

---

## **📂 2. File System & Storage Management**

11. Disk space is running out. How do you find large files across directories?
12. Explain how to identify which directory is consuming the most disk space.
13. How would you check inode usage and why is it important?
14. A new disk is attached to the server. How do you mount it persistently?
15. How do you resize an existing partition without downtime?
16. Explain how `du -sh` differs from `df -h` in usage and output.
17. How would you recover accidentally deleted critical files?
18. Describe a scenario to use `rsync` for disk migration.
19. A log directory fills up every night. How would you automate cleanup?
20. How do you check disk I/O performance and bottlenecks?

---

## **🔍 3. Networking & Connectivity**

21. Users cannot connect to your web service. How do you troubleshoot?
22. How do you check if a port is reachable from a remote server?
23. Your server is not resolving domain names. How do you debug DNS issues?
24. Explain how to check all active network connections and listening ports.
25. How do you monitor network bandwidth usage in real-time?
26. You suspect network packet loss. Which tools do you use and why?
27. How do you add a static route to a Linux server?
28. Explain how to check firewall rules and troubleshoot blocked traffic.
29. Your application server needs a new IP address. How do you assign it temporarily and permanently?
30. How would you troubleshoot latency issues between two Linux servers?

---

## **⚡ 4. User & Permission Management**

31. A user cannot access a shared directory. How do you troubleshoot permissions?
32. How do you set up a new Linux user with sudo access but limited permissions?
33. Explain `chmod 4755` and when you might use it.
34. How do you check which users are currently logged in and what they’re doing?
35. How would you restrict a user to a single command or directory?
36. Explain how to troubleshoot `Permission denied` errors for scripts executed via cron.
37. A user accidentally changed permissions on `/etc`. How do you restore it?
38. How do you find all files owned by a specific user?
39. Explain how to configure password expiration policies.
40. How do you enforce two-factor authentication for Linux users?

---

## **📝 5. Logs & Monitoring**

41. Application logs are huge. How do you analyze them efficiently?
42. Explain how to search for a specific error in multiple log files.
43. How do you monitor log growth and rotate logs automatically?
44. A server suddenly becomes unresponsive. Which logs do you check first?
45. How do you monitor disk, memory, and CPU usage in a single dashboard?
46. How do you get notified in real-time if a service fails?
47. Explain how `journalctl` is different from `/var/log/messages`.
48. You need to check historical resource usage trends. How would you do it?
49. How do you troubleshoot kernel panics using logs?
50. Your system keeps rebooting randomly. How would you debug it?

---

## **⚙️ 6. Package Management & Updates**

51. You need to install software on multiple servers at once. How do you automate it?
52. How do you check if a package is installed and its version?
53. Explain how to roll back a package update in Linux.
54. How do you update all servers safely without downtime?
55. A package installation fails due to dependency issues. How do you resolve it?
56. How do you manage software from a custom repository?
57. Explain how to remove unused packages and free space.
58. How do you verify the integrity of an installed package?
59. How would you create a custom `.rpm` or `.deb` package?
60. How do you configure unattended security updates?

---

## **🔧 7. Shell Scripting & Automation**

61. Write a script to monitor CPU usage and alert if >80%.
62. How would you automate backups of a directory using cron?
63. Explain how to pass arguments to a Bash script.
64. A script works on one server but fails on another. How do you debug it?
65. How would you automate log cleanup using shell scripting?
66. Explain how to schedule a script to run at server reboot.
67. How do you handle errors and exit codes in scripts?
68. Write a one-liner to count all `.log` files in `/var/log`.
69. How do you check if a service is running inside a script and restart it if needed?
70. How do you securely store credentials for scripts that run automatically?

---

## **💻 8. System Security**

71. A server is compromised. How do you identify malicious processes?
72. Explain how to audit user activity in Linux.
73. How do you configure SSH to disable password login?
74. How do you find world-writable files and directories?
75. How do you check which users have sudo privileges?
76. Explain how to set up `fail2ban` to prevent brute-force attacks.
77. How do you verify file integrity using checksums?
78. How do you prevent a service from being exploited via a network?
79. Explain how to encrypt data at rest and in transit.
80. A Linux server shows unauthorized file changes. How do you trace it?

---

## **⚡ 9. Backup, Recovery & High Availability**

81. Your database crashed. How do you restore from a backup?
82. How do you schedule automated backups using cron or systemd timers?
83. Explain how to take an incremental backup of `/etc`.
84. How would you recover from accidental deletion of `/home`?
85. How do you test a backup to ensure it works before disaster?
86. How do you set up RAID for data redundancy?
87. How do you replicate data between two servers for HA?
88. Your server disk failed. How do you rebuild it with minimal downtime?
89. How do you take a snapshot of a live filesystem safely?
90. How would you verify that backup files are not corrupted?

---

## **📦 10. Containers, Docker & DevOps Workflows**

91. You deployed a Docker container, but it fails to start. How do you debug?
92. Explain how to persist data from a container.
93. How do you monitor container resource usage on a Linux host?
94. How do you clean unused images, volumes, and networks?
95. You need to deploy multiple services with interdependencies. How do you automate it?
96. How do you troubleshoot networking issues inside containers?
97. How do you ensure containers restart automatically on host reboot?
98. Explain how to build a container image optimized for production.
99. How do you handle log rotation for containers?
100. A container is exposing sensitive data. How do you secure it?

---

✅ These **100 scenario-based questions** cover **Linux internals, system administration, troubleshooting, automation, networking, security, and DevOps practices**. They’re exactly what a 5-year DevOps engineer would encounter in real interviews.

If you want, I can also **create an answer guide for all 100 questions** with **commands, step-by-step troubleshooting, and examples**, so it becomes a complete preparation sheet.

Do you want me to do that next?
