
### steps to install and config Hive Meta Store :

1-Download hive 4.0.0 and extract it :
```
cd /opt

sudo wget https://archive.apache.org/dist/hive/hive-4.0.0/apache-hive-4.0.0-bin.tar.gz

sudo tar -xzf apache-hive-4.0.0-bin.tar.gz

sudo chown -R moein:moein  apache-hive-4.0.0-bin/   
```

2-Config HMS:

```
#copy my my config files:

#hive-site.xml
#hive-env.sh

```


> [!IMPORTANT]
> Add env variables HADOOP_HOME (USE hadoop-3.3.6 Version) to  /etc/profile ot bashrc file 



3-Add essential jar files in lib hive directory  :
```
cd /opt/apache-hive-4.0.0-bin/lib

#we have Mysql version 8.4.0 so we download 8.4.0 version connector :

wget https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.4.0/mysql-connector-j-8.4.0.jar

ll  | grep mysql

wget https://repo1.maven.org/maven2/com/google/guava/guava/27.0-jre/guava-27.0-jre.jar

 ll  | grep guava


#AWS SDK v1 JARs

wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.6/hadoop-aws-3.3.6.jar
wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.778/aws-java-sdk-bundle-1.12.778.jar

 
```

4- Initialize HMS database :

```
#first test your connection to node7(MYSQL Server) --- 3306 is default port mysql

nc -zv node7 3306

cd /opt/apache-hive-4.0.0-bin/bin

./schematool -dbType mysql -initSchema  --verbose

#At the end you will get this msg:

#Initialization script completed
#schemaTool completed

```

5- Start Hive Metastore

```
/opt/apache-hive-4.0.0-bin/bin/hive --service metastore  -v


```















