Groups in Linux

## Types of Groups:
```
Primary Group: Every user is assigned a primary group, which is typically their own username. Files created by the user will have this group ownership by default.

Secondary Groups: A user can also belong to additional groups (secondary groups) to share access to files and directories with other users.
```

## Group Management Commands:
```
groupadd groupname: Adds/Create a new group.
groupdel groupname: Deletes a group.
gpasswd: Administers group membership and passwords.
usermod -aG groupname username: Adds a user to a secondary group.
groups username: Displays the groups a user belongs to.
chgrp groupname filename: Changes the group ownership of a file or directory.
```

## Group-Related Files:
```
/etc/group: Contains group definitions, including group names, Group IDs (GIDs), and members.
```

## Example of Group and User Interaction
```
Let’s say you have a user tejaaswini and a group called developers:

Create a user: useradd tejaaswini
Create a group: groupadd developers
Add the user to the group: usermod -aG developers tejaaswini
Change the group ownership of a file: chgrp developers project.txt
Set permissions: chmod g+rw project.txt (allows the group to read and write to the file).
sudo groupdel groupname : To delete a group, use the groupdel command
sudo groupmod -n new_groupname old_groupname: Renaming the group


This setup allows users in the developers group to have access to project.txt.
```

## Important Notes
```
Deleting a User: Deleting a user does not automatically delete all the files owned by that user in other parts of the system (e.g., files outside the home directory). You may need to manually handle those files.

Renaming a User or Group: When you rename a user or group, the UID or GID (User/Group ID) associated with them remains the same, meaning file ownership and permissions are retained.

Backup: It's a good practice to backup or carefully assess any files and permissions before deleting or renaming users and groups, especially on multi-user systems.
```

