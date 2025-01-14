
### steps to deploy and config MYSQL (as Data Source and HMS Database):

1-Download and install MYSQL source package :

```
sudo mkdir -p  /opt/mysql-deb
cd /opt/mysql-deb

sudo wget https://downloads.mysql.com/archives/get/p/23/file/mysql-server_8.4.0-1ubuntu22.04_amd64.deb-bundle.tar

sudo tar -xvf mysql-server_8.4.0-1ubuntu22.04_amd64.deb-bundle.tar

#set root password
#user: root
#Password: P@ssw0rd

sudo dpkg-preconfigure mysql-community-server_*.deb

sudo dpkg -i mysql-{common,community-client-plugins,community-client-core,community-client,client,community-server-core,community-server,server}_*.deb

```

2-change default MySQL data directory to another path :

```
sudo systemctl status mysql.service

sudo systemctl stop  mysql.service

sudo mkdir -p /opt/mysql/data

sudo chown -R mysql:mysql /opt/mysql

sudo rsync -av /var/lib/mysql/ /opt/mysql/data/

sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
#change datadir to :datadir         = /opt/mysql/data



#Update AppArmor Configuration (Linux security module that restricts programs):

sudo nano /etc/apparmor.d/usr.sbin.mysqld

#Add the following lines  and comment old data directory
/opt/mysql/data/ r,
/opt/mysql/data/** rwk,

sudo systemctl reload apparmor

sudo systemctl reload apparmor


sudo systemctl start mysql.service

rm -rf /var/lib/mysql
```




3-create user and database for HMS:

```
mysql -u root -p

CREATE USER 'hive'@'node5' IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON hive_meta.* TO 'hive'@'node5' WITH GRANT OPTION;

create database hive_meta;

```


