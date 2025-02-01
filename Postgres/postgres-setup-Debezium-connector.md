
### Some Postgres setup tasks are required before you can install and run a Debezium connector:

1-Connect to PostgreSQL as a superuser and Create a user with replication privileges:

```
psql -h node8 -Upostgres -d source2

CREATE ROLE debezium WITH REPLICATION LOGIN PASSWORD '123';
GRANT SELECT ON ALL TABLES IN SCHEMA info TO debezium;
GRANT USAGE ON SCHEMA info TO debezium;


```

2-create publications for specific schemas and tables:
```
CREATE PUBLICATION dbz_publication FOR TABLE info.information_tbl ;
#or 
#CREATE PUBLICATION dbz_publication FOR ALL TABLES IN SCHEMA info ;

ALTER PUBLICATION dbz_publication
DROP TABLE info.information_tbl;

```

3-Checking Publication Details:
```
SELECT * FROM pg_publication;
SELECT * FROM pg_publication_tables;

```