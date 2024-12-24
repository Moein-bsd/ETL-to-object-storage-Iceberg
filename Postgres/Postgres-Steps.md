

### steps to deploy and config MUSQL (as Data Source):

1-Install Prerequisites on Linux
```
sudo apt install gcc build-essential zlib1g-dev libreadline6-dev libicu-dev pkg-config

```
2-Download and install MYSQL source package :

```
sudo mkdir  -p  /opt/postgresql/
cd /opt/postgresql/

wget https://ftp.postgresql.org/pub/source/v16.6/postgresql-16.6.tar.gz

tar -xzf postgresql-16.6.tar.gz
cd postgresql-16.6/

ll

sudo ./configure
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
sudo chown -R postgres: /opt/postgresql/data
```

5- add postgres to PATH :

```
sudo sh -c "echo 'export PATH=$PATH:/usr/local/pgsql/bin' > /etc/profile.d/postgres.sh"
source /etc/profile.d/postgres.sh
```

5- init database :

```
su postgres
/usr/local/pgsql/bin/initdb -D /opt/postgresql/data -U postgres -W
nano /opt/postgresql/data/postgresql.conf

#or

su postgres -c "nano /opt/postgresql/data/postgresql.conf"

/usr/local/pgsql/bin/pg_ctl -D  /opt/postgresql/data -l /opt/postgresql/logfile start
#or
su postgres -c "/usr/local/pgsql/bin/pg_ctl -D  /opt/postgresql/data  -l /opt/postgresql/logfile start"

```

6-use systemd for create service :

```
sudo nano /usr/lib/systemd/system/postgresql.service

```

```
// if you wanna use systemd create service file in 
-> /usr/lib/systemd/system/ with this command
4. sudo nano /usr/lib/systemd/system/postgresql.service
5. fill the file with this script

[Unit]
Description=PostgreSQL database server
Documentation=man:postgres(1)
After=network-online.target
Wants=network-online.target

[Service]
Type=notify
User=postgres
ExecStart=/usr/local/pgsql/bin/postgres -D  /opt/postgresql/data  -l /opt/postgresql/logfile
ExecReload=/bin/kill -HUP $MAINPID
ExecStop=/usr/local/pgsql/bin/pg_ctl stop -D  /opt/postgresql/data  -l /opt/postgresql/logfile

KillMode=mixed
KillSignal=SIGINT
TimeoutSec=infinity
RuntimeDirectory=postgresql

[Install]
WantedBy=multi-user.target
```
6. run:
sudo systemctl daemon-reload