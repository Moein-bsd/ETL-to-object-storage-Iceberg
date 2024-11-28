
### steps to deploy and config MinIO Cluster(Do it On All MinIO Nodes):


1.Add new disk to each MinIO Node:

> [!IMPORTANT]
> For simplicity in a straightforward MinIO setup,using the entire disk without partitioning  is perfectly fine.


2-format new added Drive(s):

 ```
sudo mkfs.xfs /dev/sdb -L miniodriver1
sudo mkdir -p /mnt/disk1/minio
sudo mount /dev/sdb /mnt/disk1/minio
lsblk -f /dev/sdb 
sudo nano /etc/fstab

#add following in fstab

LABEL=miniodriver1      /mnt/disk1/minio     xfs     defaults,noatime  0       2

  ```

3-create user and group minio:

```
sudo groupadd -r minio-grp
sudo useradd -M -r -g minio-grp minio-user
sudo chown minio-user:minio-grp /mnt/disk1/minio
```

4-download and install minio.deb :

```

wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio_20241107005220.0.0_amd64.deb -O minio.deb
sudo dpkg -i minio.deb

```

5-changing  minio.servic config :
```
sudo nano /lib/systemd/system/minio.service
=------mofify

User=minio-user
Group=minio-grp
```

6-change MinIO EnvironmentFile :

```
sudo  nano /etc/default/minio

MINIO_VOLUMES="http://minio-0{1...4}:10000/mnt/disk1/minio"
MINIO_OPTS="--console-address :10001 --address :10000"
MINIO_ROOT_USER=adminminio
MINIO_ROOT_PASSWORD=adminminio
#set Erasure coding
#MINIO_STORAGE_CLASS_STANDARD="EC:1"
```

7-start MiniO service on All MinIO nodes:

```

sudo systemctl enable minio.service
sudo systemctl start minio.service
sudo systemctl status minio.service

```