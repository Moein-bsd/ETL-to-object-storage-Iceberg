
### steps to deploy and config MYSQL (as Data Source and HMS Database):

1-Download and install MYSQL source package :

```
sudo mkdir -p  /opt/mysql
cd /opt/mysql

sudo wget https://downloads.mysql.com/archives/get/p/23/file/mysql-server_8.4.0-1ubuntu22.04_amd64.deb-bundle.tar

sudo tar -xvf mysql-server_8.4.0-1ubuntu22.04_amd64.deb-bundle.tar

#set root password
#user: root
#Password: P@ssw0rd

sudo dpkg-preconfigure mysql-community-server_*.deb

sudo dpkg -i mysql-{common,community-client-plugins,community-client-core,community-client,client,community-server-core,community-server,server}_*.deb

```

2-create user and database for HMS:

```
mysql -u root -p

CREATE USER 'hive'@'node5' IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON *.* TO 'hive'@'node5' WITH GRANT OPTION;

create database hive_meta;

```


