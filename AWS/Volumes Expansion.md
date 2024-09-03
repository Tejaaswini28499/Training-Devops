## how to extent volume in ubuntu machine after expanding in EBS

```
expand the volume in AWS as requried
extent volume in ubuntu machine: to do this follow below steps 
    1. lsblk - Verify the New Size of the EBS Volume
    2. df -h - Check the filesystem
    3. sudo growpart /dev/nvme0n1p1 - Extend the Partition
    4. sudo resize2fs /dev/xvdf1 - Extend the Filesystem
    ```

    Note: you cannot decrease the volume you can only increase it.


