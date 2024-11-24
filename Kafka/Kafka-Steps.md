

 mkdir kafka-3.8.1
 cd kafka-3.8.1
 wget  https://downloads.apache.org/kafka/3.8.1/kafka_2.13-3.8.1.tgz
 tar -xzf kafka_2.13-3.8.1.tgz
 
 #set /etc/profile
 sudo nano /etc/profile #this
 
 change server.properties:
 nano /home/moein/kafka-3.8.1/kafka_2.13-3.8.1/config/kraft/server.properties
 
 
 
 

 
 
 in node1:
 kafka-storage.sh random-uuid
 
 in All kafka nodes:
 
 kafka-storage.sh format -t yR2oLObjQlONvUxLxuHSUA <your_UUID> -c  /home/moein/kafka-3.8.1/kafka_2.13-3.8.1/config/kraft/server.properties