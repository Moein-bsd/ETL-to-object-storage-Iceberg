
### steps to install and config Kafka Cluster:

1.make kafka directory on each nodes :

```
 mkdir kafka-3.8.1

 cd kafka-3.8.1
```

2.download kafka :

```
 wget  https://downloads.apache.org/kafka/3.8.1/kafka_2.13-3.8.1.tgz
 #scp downloaded kafka to another nodes

 tar -xzf kafka_2.13-3.8.1.tgz
 
 ```
 
 3.change server.properties <on your directory> and copy configs for each associated node:


```
 nano /home/moein/kafka-3.8.1/kafka_2.13-3.8.1/config/kraft/server.properties
 ```
 
 4.add env variables :

 #set /etc/profile

 sudo nano /etc/profile #this
 

 
 5.clustering kafka nodes:

```
 #in kafka node1:

 kafka-storage.sh random-uuid
 
 #in All kafka nodes:
 
 kafka-storage.sh format -t yR2oLObjQlONvUxLxuHSUA <your_UUID> -c  /home/moein/kafka-3.8.1/kafka_2.13-3.8.1/config/kraft/server.properties
 
 ```

 