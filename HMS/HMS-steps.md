
### steps to install and config Hive Meta Store :

1-Download hive 3.1.3 and extract it :
```
cd /opt
sudo wget https://archive.apache.org/dist/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz

sudo tar -xzf apache-hive-3.1.3-bin.tar.gz
```

2-config HMS:

```
#copy my my config files:

#hive-site.xml
#hive-env.sh

```

3-Add essential jar files in lib hive directory  :
```
cd /opt/apache-hive-3.1.3-bin/lib

#we have Mysql version 8.4.0 so we download 8.4.0 version connector :

sudo wget https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.4.0/mysql-connector-j-8.4.0.jar

ll  | grep mysql

sudo wget https://repo1.maven.org/maven2/com/google/guava/guava/27.0-jre/guava-27.0-jre.jar

 ll  | grep guava
 
```

4- initialize HMS database :

```
#first test your connection to node7(MYSQL Server) --- 3306 is default port mysql

nc -zv node7 3306

cd /opt/apache-hive-3.1.3-bin/bin

./schematool -dbType mysql -initSchema  --verbose

#At the end you will get this msg:

#Initialization script completed
#schemaTool completed

```


