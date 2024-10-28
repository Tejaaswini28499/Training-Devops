## Package commads

1. Top -The top command displays real-time information about system processes, including CPU and memory usage. It's an interactive tool that gives you a dynamic view of your system's performance.This will open the top interface, where you can see a live view of running processes. You can press q to exit, or press other keys (like k to kill a process or h for help) to interact with it.


2. ps aux -The ps aux command shows a detailed list of all running processes on the system, including processes not associated with your terminal.This command will give you a snapshot of all the processes running on the system, not limited to the current user or terminal session. 


3. ps -ef - The ps -ef command is another way to view a list of all running processes, but with a slightly different format compared to ps aux. It uses standard syntax for UNIX-like systems.
This command will list all running processes with details about the user, parent process, and more.

4. ps -ef | grep 2918 - This command uses ps -ef to list all processes, but the grep command is used to filter the results to show only processes that contain the string 2918 (likely a process ID in this case).

Explanation:
 ps -ef: Lists all running processes.
|: This is a pipe, which passes the output of ps -ef as input to grep.
grep 2918: Filters the output to show only lines that contain the string "2918".
Use Case: This command is typically used to check if a process with a specific PID (in this case, 2918) is running, or to look for processes related to that PID.

5. kill "PID" - Kill the ProcessID mentioned.(this will slowly kill with all parent PID and others)
6. kill -9 "PID" - this will force kill the processID (This will Kill only the PID mentioned) -9(force kill)