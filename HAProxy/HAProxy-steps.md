
### steps to install HAProxy for Load balancing MinIO Cluster:

1.install HAProxy :
```
sudo apt-get update

sudo apt-get -y install haproxy

```

2.go to haproxy and backup default config:

```
cd /etc/haproxy/

sudo mv haproxy.cfg haproxy.cfg-back

```

3.create new HAproxy config:

```
sudo nano  haproxy.cfg

```



```

frontend http
   stats enable
   stats uri /haproxy?stats
   bind *:1000
   bind *:1001

  # Define the backend for Service 1 (port 80)
   use_backend minio_api  if { dst_port 1000 }

  # Define the backend for Service 2 (port 81)
   use_backend minio_console if { dst_port 1001 }

backend minio_api
  mode http
  balance leastconn
  server minio1 192.168.16.240:10000 check
  server minio2 192.168.16.241:10000 check
  server minio3 192.168.16.242:10000 check
  server minio4 192.168.16.243:10000 check


backend minio_console
  mode http
  balance leastconn
  server minio1 192.168.16.240:10001 check
  server minio2 192.168.16.241:10001 check
  server minio3 192.168.16.242:10001 check
  server minio4 192.168.16.243:10001 check


```

4.create new HAproxy config:

```
sudo systemctl enable haproxy

sudo systemctl start haproxy

sudo systemctl status haproxy

#check exposed port

ss -tupln | grep 1000
ss -tupln | grep 1001


```
