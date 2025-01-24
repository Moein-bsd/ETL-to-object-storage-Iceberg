
### steps to config Kafka Cluster + debeziu :

1-setup kafka connect :

 ```
cd /home/moein/kafka-3.8.1/kafka_2.13-3.8.1/
mkdir plugins

cd plugins


wget https://repo1.maven.org/maven2/io/debezium/debezium-connector-mysql/3.0.7.Final/debezium-connector-mysql-3.0.7.Final-plugin.tar.gz

https://repo1.maven.org/maven2/io/debezium/debezium-connector-postgres/3.0.7.Final/debezium-connector-postgres-3.0.7.Final-plugin.tar.gz

tar -xzf debezium-connector-mysql-3.0.7.Final-plugin.tar.gz
tar -xzf debezium-connector-postgres-3.0.7.Final-plugin.tar.gz

nano ../config/connect-distributed.properties
#copy configs for each associated node

 ```

> [!IMPORTANT]
> check Debezium version Compatibility with your MySQL version ( for me =mysql versiom is 8.4 and postgresql is 16.6  ;) ).
> https://debezium.io/releases/


2- Run kafka connect and verify that:

 ```
connect-distributed.sh connect-distributed.properties

curl http://node1:8083/ 

#Verify the Connector is Loaded
curl -s http://node1:8083/connector-plugins | jq


[
  {
    "class": "io.debezium.connector.mysql.MySqlConnector",
    "type": "source",
    "version": "3.0.7.Final"
  },
  {
    "class": "io.debezium.connector.postgresql.PostgresConnector",
    "type": "source",
    "version": "3.0.7.Final"
  },
  {
    "class": "org.apache.kafka.connect.mirror.MirrorCheckpointConnector",
    "type": "source",
    "version": "3.8.1"
  },
  {
    "class": "org.apache.kafka.connect.mirror.MirrorHeartbeatConnector",
    "type": "source",
    "version": "3.8.1"
  },
  {
    "class": "org.apache.kafka.connect.mirror.MirrorSourceConnector",
    "type": "source",
    "version": "3.8.1"
  }
]

 ```

3- create connection :

```
curl -X POST -H "Content-Type: application/json" --data @mysql-connector.json http://node1:8083/connectors
curl -X POST -H "Content-Type: application/json" --data @postgres-connector.json http://node1:8083/connectors

```

4- get list all connectors:
```
 curl -s http://node1:8083/connectors | jq


[
  "mysql-connector-source1"
]


```
5- Delete connection(Just for knowledge): 
```
curl -X DELETE http://node1:8083/connectors/mysql-connector-source1


```

6-Create topics for mysql source table and postres:
```
kafka-topics.sh --bootstrap-server node1:9092,node2:9092,node3:9092 --create  --topic mysql-perfix.source1.financial_tbl --replication-factor 3 --partitions 3

kafka-topics.sh --bootstrap-server node1:9092,node2:9092,node3:9092 --create   --topic psq-perfix.info.information_tbl  --replication-factor 3 --partitions 3


```

7-list your topics:
```
kafka-topics.sh --bootstrap-server node1:9092,node2:9092,node3:9092 --list
```
