
chmod u+r file1.txt 
chmod ug-rx teju

chmod - change mode
u/g/o - of user/group/others
+ /- - add or remove
r/w/x - read write execute
file name/directory name  - mention the filename(file1.txt)/directory(teju) as given above.

eg: chmod u+rwx file1.txt, chmod g+rw file1.txt, chmod ug+rwx file1.txt, chmod u-rx

## another way to change the File permision is using numbers 4,2,1

chomd 777 file1.txt 

4- read permission
2- Write permission
1- execute permission

u- if the user wants all the permission then that should be 7 
group- wants all permission then that should be 7
others- wants all permsiion then it should be 7 

eg: chmod 770 file1.txt, chmod 421 file1.txt, chmod 124 teju

