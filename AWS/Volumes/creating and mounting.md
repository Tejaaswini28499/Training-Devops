1. Take a new volume
2. and have to take the volume same as Instance Availability Zone
3. attach to the instance
4. do fdisk you can see the new volume
5. after that you need to do partation 
6. do the format

Note: volumes it should be in the same region and Availability Zone as the Instance 

df -h
  711  fdisk
  712  fdisk -l
  713  sudo fdisk -l- to see the disk available

  714  sudo fdisk /dev/nvme1n1- doing the partation
 After typing this command you need to give m, 
 next n- to do partation
 enter, enter, enter, enter, give w to save

  715  sudo fdisk -l
  716  mkfs (tab tab)
  after mkfs click on tab twice.
  
  718  mkfs.ext4 /dev/nvme1n1 - To format
  719  sudo mkfs.ext4 /dev/nvme1n1
  --------------------
Repeat
  720  ls
  721  fdisk -l
  722  sudo fdisk -l
  723  sudo fdisk /dev/nvme2n1
  724  sudo fdisk -l
  725  mkfs.ext4 /dev/nvme2n1
  726  sudo mkfs.ext4 /dev/nvme2n1
  727  sudo fdisk -l
  -----------------------------
  creating the new directory called image-backup in tmp 
  728  cd /var/www/html/images/
  729  ls
  730  cd ..
  731  ls
  732  mkdir /tmp/image-backup
  733  sudo fdisk -l
  734  cd /tmp/image-backup/
  735  ls
  736  cd /var/www/html
  737  ls
 ------------------------------
 moving the images in the images folder from root volume to tmp 
  755  sudo rsync -av --remove-source-files images/* /tmp/image-backup/
  756  ls
  757  cd images
  758  ls
  759  cd class
  760  ls
  761  cd ..
  762  ls
  763  cd /tmp/image-backup/
  764  ls
  765  cd class/
  766  ls
  ----------------------------------
mount is nothing but telling OS there is a new storage available.
  767  mount /dev/nvme2n1 /var/www/html/images
  768  sudo mount /dev/nvme2n1 /var/www/html/images - mount is nothing but telling OS there is a new storage available.
  810  sudo umount /var/www/html/images -- unmount 

  note: until and unless you edit sudo vi /etc/fstab this mount and unmount are temporary.
----------------------------------------
Moving from tmp to new disk /dev/nvme2n1
  769  df -h
  770  cd ..
  771  ls
  772  cd /var/www/html
  773  ls
  774  cd images/
  775  ls
  776 
  778  sudo rsync -av --remove-source-files /tmp/image-backup/* /var/www/html/images/
  779  ls
  780  pwd
  781  ls
  782  cd ..
  783  ls
  784  cd images/
  785  ls
  786  cd class
  787  ls
  788  cd ..
  789  ls
  ----------------------
  If you mount and do not save in sudo vi /etc/fstab file the it will be erased and not able to
  fetch the info again.

  790  df -h
  791  reboot
  792  sudo reboot
  793  df -h
  794  cd /var/www/html
  795  ls
  796  cd images/
  797  ls
  798  class/
  799  ls
  800  cd /tmp/image-b
  801  vi /etc/fstab
  802  sudo vi /etc/fstab
/dev/nvme2n1 tab /var/www/html/images tab ext4 tab defaults tab 0 tab 0
save: wq!

  803  df -h
  804  sudo fdisk -l
  805  sudo vi /etc/fstab
  806  mount -a
  807  sudo mount -a = this command is to apply the changes made in the file.

  doing this it will be saved permanently even if the system restarts the info will be still 
 available but not deleted.

  808  df -h
  809  umount /var/www/html/images
  810  sudo umount /var/www/html/images
  811  df -h
  812  cat /etc/fstab
  813  df -h
  814  sudo reboot
  815  df -h
  816  sudo fdisk -l
  817  sudo vi /etc/fstab
  ----------------------
  818  sudo umount -a
  819  df -h
  820  sudo mount -a
  821  df -h
  822  ls
  823  cd /var/www/html/
  824  ls
  
  849  clear
  850  history | tail -150
  -----------------------


Ubuntu installation.


   1  sudo apt update 
    2  sudo apt install mysql-server
    3  sudo systemctl start mysql
    4  sudo systemctl status mysql
    5  sudo systemctl enable mysql
    6  sudo mysql_secure_installation
    7  sudo fdisk -l
    8  sudo fdisk /dev/nvme1n1
    9  mkfs.ext4 /dev/nvme1n1
   10  sudo mkfs.ext4 /dev/nvme1n1
   11  sudo vi /etc/fstab
   12  sudo fdisk -l
   13  clear
   14  sudo fdisk -l
   15  df -h
   16  sudo vi /etc/fstab
   17  sudo mount -a
   18  sudo fdisk -l
   19  df -h
   20  sudo mkfs.ext4 -L MYSQL  /dev/nvme1n1
   21  sudo mount -a
   22  df -h
   23  cd /var/lib/mysql
   24  ls
   25  cd ~
   26  sudo systemctl status mysql
   27  pws
   28  pwd
   29  cd /var/lib/mysql
   30  ls
   31  ls -a
   32  ls
   33  sudo systemctl status mysql
   34  ls
   35  df -h
   36  history
   37  sudo vi /etc/fstab
   38  sudo mount -a
   39  df -h
   40  sudo reboot
   41  history


## File Types

   mkfs         mkfs.cramfs  mkfs.ext2    mkfs.ext3    mkfs.ext4    mkfs.fat     mkfs.minix   mkfs.msdos   mkfs.vfat    mkfs.xfs
