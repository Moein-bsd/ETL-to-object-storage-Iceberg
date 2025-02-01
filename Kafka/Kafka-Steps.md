
### steps to install and config Kafka Cluster:

1- Make kafka directory on each nodes :

```
 mkdir kafka-3.8.1

 cd kafka-3.8.1
```

2- Download kafka :

```
 wget  https://downloads.apache.org/kafka/3.8.1/kafka_2.13-3.8.1.tgz
 #scp downloaded kafka to another nodes

 tar -xzf kafka_2.13-3.8.1.tgz
 
 ```
 
 3- Change server.properties <on your directory> and copy configs for each associated node:


```
 nano /home/moein/kafka-3.8.1/kafka_2.13-3.8.1/config/kraft/server.properties
 ```
 
 4- Add env variables :

 #set /etc/profile

 sudo nano /etc/profile #this
 

 
 5- Clustering kafka nodes:

```
 #in kafka node1:

 kafka-storage.sh random-uuid
 
 #in All kafka nodes (node2,node3 ):
 
 kafka-storage.sh format -t yR2oLObjQlONvUxLxuHSUA <your_UUID> -c  /home/moein/kafka-3.8.1/kafka_2.13-3.8.1/config/kraft/server.properties
 
 ```

6- Create systemd Service for Kafka:

```
sudo nano /etc/systemd/system/kafka.service
#copy my kafka.service


sudo systemctl daemon-reload
sudo systemctl enable kafka.service && systemctl start kafka.service

```

7-Check service state and serice log :

```
sudo systemctl status kafka.service
journalctl -xu  kafka -e -n 100 -f
```



#### steps to install and config JMX Exporter Agent on Kafka Cluster (node1-3) :

1-download JMX Exporter Agent and yaml config:

```
 cd kafka-3.8.1

 wget https://github.com/prometheus/jmx_exporter/releases/download/1.1.0/jmx_prometheus_javaagent-1.1.0.jar

 wget https://raw.githubusercontent.com/prometheus/jmx_exporter/refs/heads/main/examples/kafka-kraft-3_0_0.yml

```

2-Add Environment in kafka systemd service file (like my kafka.service ):
```
Environment="KAFKA_OPTS=-javaagent:/home/moein/kafka-3.8.1/jmx_prometheus_javaagent-1.1.0.jar=8090:/home/moein/kafka-3.8.1/kafka-kraft-3_0_0.yml"
```
3-Test Metrics :
```

curl node1:8090/metrics
curl node2:8090/metrics
curl node3:8090/metrics

```


 