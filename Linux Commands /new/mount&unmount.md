mount 
NAME          MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
zram0         253:0    0  407M  0 disk [SWAP]
nvme0n1       259:0    0    8G  0 disk 
├─nvme0n1p1   259:1    0    8G  0 part /
├─nvme0n1p127 259:2    0    1M  0 part 
└─nvme0n1p128 259:3    0   10M  0 part /boot/efi
nvme1n1       259:4    0    2G  0 disk 
Perfect 👍 — you’ve shared your current disk layout.

Let’s understand it first:

```
nvme0n1  → main 8 GB system disk (root mounted at /)
nvme1n1  → new 2 GB disk (unmounted — this is what you’ll mount)
```

So you’ll mount **`/dev/nvme1n1`** (not `/dev/sdf` in your case).

---

## 🧩 Steps to Mount `/dev/nvme1n1`

### **1. Create a partition on it**

```bash
sudo fdisk /dev/nvme1n1
```

Inside fdisk:

```
n    → new partition  
p    → primary  
1    → partition number  
Enter → default first sector  
Enter → default last sector (use whole 2G)  
w    → write and exit  
```

Then verify:

```bash
lsblk
```

You should now see `/dev/nvme1n1p1`.

---

### **2. Format the partition**

```bash
sudo mkfs -t ext4 /dev/nvme1n1p1
```

---

### **3. Create a mount point**

```bash
sudo mkdir /mnt/data
```

---

### **4. Mount the volume**

```bash
sudo mount /dev/nvme1n1p1 /mnt/data
```

Check if mounted:

```bash
df -h
```

✅ You should see `/mnt/data`.

---

### **5. Make it permanent (after reboot)**

Get the partition UUID:

```bash
sudo blkid /dev/nvme1n1p1
```

You’ll get something like:

```
/dev/nvme1n1p1: UUID="abcd1234-5678-9ef0-1122-334455667788" TYPE="ext4"
```

Now edit fstab:

```bash
sudo vim /etc/fstab
```

Add this line at the end:

```
UUID=abcd1234-5678-9ef0-1122-334455667788   /mnt/data   ext4   defaults,nofail   0   2
```

Save and test:

```bash
sudo mount -a
```

No errors → done ✅

---

### **6. (Optional) Change permissions**

```bash
sudo chown ec2-user:ec2-user /mnt/data
sudo chmod 755 /mnt/data
```

---

Would you like me to show how to **expand this 2 GB volume later** if you increase its size in AWS (or using `lvextend` / `growpart`)?


unmount 

Perfect 👍 — since you already **unmounted** `/dev/nvme1n1p1`, now let’s **remove the partition** safely from `/dev/nvme1n1`.

---

## 🧱 **1. Verify current partitions**

```bash
lsblk
```

You should see something like:

```
nvme1n1      2G
└─nvme1n1p1  2G
```

---

## ⚙️ **2. Open fdisk on the disk**

```bash
sudo fdisk /dev/nvme1n1
```

---

## ✂️ **3. Inside fdisk — delete the partition**

Type these commands inside fdisk prompt:

```
d   → delete a partition
1   → partition number (if only one, just press Enter)
w   → write changes and exit
```

---

## 🧩 **4. Confirm**

Run again:

```bash
lsblk
```

Now you should see:

```
nvme1n1      2G
```

✅ No more `nvme1n1p1` → partition removed successfully.

---

## ⚠️ Optional: wipe filesystem signature

If you want to clean the disk completely:

```bash
sudo wipefs -a /dev/nvme1n1
```

(This erases any filesystem or partition table info)

---

Would you like to **recreate a new partition** and format it again (fresh mount)?
