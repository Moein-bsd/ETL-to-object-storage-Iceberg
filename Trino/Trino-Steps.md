
### steps to deploy and config Trino cluster:
#### Do  Steps 1 to 4 in node6 , node7 , node8


> [!IMPORTANT]
> Trino requires a 64-bit version of Java 23, with a minimum required version of 23.0.0 and a recommendation to use the latest patch version. So we should config Java 23 on Trino cluster.
>For  Linux X64 [Java 23.0.1 Linux X64 ](https://github.com/adoptium/temurin23-binaries/releases/download/jdk-23.0.1%2B11/OpenJDK23U-jdk_x64_linux_hotspot_23.0.1_11.tar.gz/) 
 




1-Download and extrct it :
```
 sudo mkdir /opt/trino
 sudo chown moein:moein trino
 cd /opt/trino

wget https://repo1.maven.org/maven2/io/trino/trino-server/455/trino-server-455.tar.gz

sudo tar -xzf trino-server-455.tar.gz

 
```
2-create a symbolic link for python :
```
sudo ln -s /usr/bin/python3 /usr/bin/python

```

3-download  Trino cli file :
```
sudo wget https://repo1.maven.org/maven2/io/trino/trino-cli/455/trino-cli-455-executable.jar



```

4-start Trino :
```

launcher start

```

5-connect to trino (node Coordinator):

```
java  -jar /opt/trino/trino-cli-455-executable.jar  --server http://node6:8080 

```