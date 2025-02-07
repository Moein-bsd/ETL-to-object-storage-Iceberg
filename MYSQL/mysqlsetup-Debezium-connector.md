
### Some MySQL setup tasks are required before you can install and run a Debezium connector:


1-Create the MySQL user and  Grant the required permissions to the user:

```
CREATE USER 'debezium'@'node1' IDENTIFIED BY '123';
CREATE USER 'debezium'@'node2' IDENTIFIED BY '123';
CREATE USER 'debezium'@'node3' IDENTIFIED BY '123';

GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'debezium'@'node1';
GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'debezium'@'node2';
GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'debezium'@'node3';

FLUSH PRIVILEGES;

```

2-Check whether the log-bin option is enabled:

```

SELECT VARIABLE_NAME,variable_value as "BINARY LOGGING STATUS (log-bin) ::" FROM performance_schema.global_variables WHERE variable_name like 'log_bin';

SELECT VARIABLE_NAME,variable_value as "BINARY LOGGING STATUS (log-bin) ::" FROM performance_schema.global_variables WHERE variable_name like 'binlog_format';

```
