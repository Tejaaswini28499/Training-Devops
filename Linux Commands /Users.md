## Types of Users:
```
Root User: This is the superuser with unrestricted access to all commands and system files. The root user can modify any part of the system, including creating, deleting, and configuring user accounts.

Regular Users: These are standard user accounts created for individuals or services. Regular users have restricted access to certain system resources.

System Users: These users are typically created by the system for running specific services (like nobody, www-data, etc.), and they usually don't have login privileges.
```
## User Management Commands:
```
useradd username: Adds a new user.
passwd username: Changes the password for the user.
usermod: Modifies an existing user’s attributes (e.g., changing the shell or adding the user to a group).
userdel username: This deletes the user account but keeps their home directory and files intact.
sudo userdel -r username :Delete user and their home directory:
id username: Displays the user ID, group ID, and group memberships of the user.
whoami: Shows the current logged-in user.
sudo usermod -l new_username old_username: Renaming a User. This will change the username but not the user’s home directory.
sudo usermod -l new_username -d /home/new_username -m old_username :If you also want to change the home directory to match the new username, use:

```

## User-Related Files:
```
1. cat /etc/passwd - Contains basic user account information, such as username, UID, home directory, and default shell.
eg: 
ec2-user:x:1000:1000:EC2 Default User:/home/ec2-user:/bin/bash
teju:x:1001:1001::/home/teju:/bin/bash
yogi:x:1002:1003::/home/yogi:/bin/bash

ec2-user: username
x: password link
1000: userid
1000: groupid
/home/ec2-user : path
/bin/bash: 


2. cat /etc/shadow: Stores encrypted passwords and password-related information (only accessible by root).
eg:
ec2-user:!!:19920:0:99999:7:::
teju:$6$VFTdZ4CCDsaID.PP$yy9WbJY1xtq89GW0t97yuD.IkrY7c.lUunOcNWTlqRVsE9fkUHORTLjPMWm0WplvzoF9ko1S/asNHRoDrIcRo1:19970:0:99999:7:::
yogi:$6$Oo8baXhvu/W1KgC/$X7FOBPlqEExRIUYaWqc49T8PDC/C8nnJxKx65iDyHdw1PhgaFw3o5EEX6j6ajdFLY/HI2bPuONImuHfcvTx9d1:19970:0:99999:7:::

3./home/username: The default home directory for users where personal files are stored.
```
note: If you are inside the user and asking for password and you dont know then exit and then you will be the root user.

stat file1 : This way, you can quickly identify the owner (user) and group of any file.
File: file1
  Size: 21              Blocks: 8          IO Block: 4096   regular file
Device: 10301h/66305d   Inode: 506116      Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/ec2-user)   Gid: ( 1006/ project)
Context: unconfined_u:object_r:user_home_t:s0
Access: 2024-09-03 06:16:20.284776363 +0000
Modify: 2024-09-03 06:16:20.284776363 +0000
Change: 2024-09-05 07:51:52.205392517 +0000
 Birth: 2024-09-03 06:16:20.284776363 +0000


## Managing Permissions Using Users and Groups
```
Permissions for files and directories in Linux are divided into three categories:

Owner (user): The user who owns the file or directory.
Group: The group associated with the file or directory.
Others: All other users on the system.

chmod: Changes the permission of a file or directory.
chown: Changes the ownership of a file or directory (both user and group).
```