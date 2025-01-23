

### steps to deploy and config postgresql (as Data Source):

1-Install Prerequisites on Linux
```
sudo apt install  -y gcc build-essential zlib1g-dev libreadline6-dev libicu-dev pkg-config libssl-dev libsystemd-dev

```
2-Download and install MYSQL source package :

```
sudo mkdir  -p  /opt/postgresql/
cd /opt/postgresql/

sudo wget https://ftp.postgresql.org/pub/source/v16.6/postgresql-16.6.tar.gz

sudo tar -xzf postgresql-16.6.tar.gz
cd postgresql-16.6/

ll


# --with-systemd This option enables integration with systemd, allowing PostgreSQL to use systemd features for managing the service.
# --with-openssl  This option enables support for SSL

sudo ./configure --with-openssl  --with-systemd

make
sudo make install
```
3-create postgres user :

```
sudo useradd postgres
sudo passwd postgres
```

4-set Data directory:

```
sudo mkdir -p /opt/postgresql/data
sudo mkdir -p /opt/postgresql/
touch /opt/postgresql/logfile
sudo chown  postgres: /opt/postgresql/logfile
sudo chmod 600 /opt/postgresql/logfile
sudo chown -R postgres: /opt/postgresql/data
```

5- init database :

```
su postgres
/usr/local/pgsql/bin/initdb -D /opt/postgresql/data -U postgres -W


/usr/local/pgsql/bin/pg_ctl -D  /opt/postgresql/data  start
#or
su postgres -c "/usr/local/pgsql/bin/pg_ctl -D  /opt/postgresql/data  start"

```

6-use systemd for create service **:

```
sudo nano /usr/lib/systemd/system/postgresql.service

#copy my postgresql.service

```
7-config Network postgresql :

```
su postgres -c "nano /opt/postgresql/data/postgresql.conf"
#modify listen_addresses = 'yourt_IP'     # what IP address(es) to listen on;


su postgres -c  "nano /opt/postgresql/data/pg_hba.conf "
#copy my pg_hba.conf



```

8- run:

```
sudo systemctl daemon-reload
sudo systemctl status  postgresql
sudo systemctl start  postgresql
```

9- connect to Postgres and create source database :
```
psql -Upostgres

CREATE DATABASE source2;
CREATE USER psq  WITH PASSWORD '123';
\c source2;
CREATE SCHEMA info;
GRANT ALL PRIVILEGES ON DATABASE source2 TO psq;
GRANT ALL PRIVILEGES ON SCHEMA info TO psq;



```



