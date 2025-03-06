### steps to deploy and config  Spark Streaming:

1-Download Requirement Jar Files:
```
cd /home/spark/spark-3.5.1-bin-hadoop3/jars

rm guava-14.0.1.jar

wget https://repo1.maven.org/maven2/com/google/guava/guava/27.0-jre/guava-27.0-jre.jar
wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-dynamodb/1.12.778/aws-java-sdk-dynamodb-1.12.778.jar
wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-core/1.12.778/aws-java-sdk-core-1.12.778.jar
wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-s3/1.12.778/aws-java-sdk-s3-1.12.778.jar
wget https://repo1.maven.org/maven2/joda-time/joda-time/2.1/joda-time-2.1.jar


wget https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.6.1/iceberg-spark-runtime-3.5_2.12-1.6.1.jar

wget https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.1/spark-sql-kafka-0-10_2.12-3.5.1.jar

wget https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.8.1/kafka-clients-3.8.1.jar

wget https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.5.1/spark-token-provider-kafka-0-10_2.12-3.5.1.jar

wget https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.12.1/commons-pool2-2.12.1.jar

wget https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-aws-bundle/1.6.1/iceberg-aws-bundle-1.6.1.jar



```

2-Run Spark Sreaming :
```
export AWS_REGION="us-east-1"
export AWS_ACCESS_KEY_ID="Ye20hXPlsCGTV4wQYJm8"
export AWS_SECRET_ACCESS_KEY="ndWDf6BiGPE1ikjwLmCN8UXHUzrHFYDr09484eCU"


spark-submit --conf "spark.log.level=WARN"   spark-cdc-mysql-iceberg.py

spark-submit --conf "spark.log.level=WARN" spark-cdc-postgres-iceberg.py
```


















