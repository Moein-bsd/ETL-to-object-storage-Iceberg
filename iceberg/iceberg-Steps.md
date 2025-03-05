### Steps to create and iceberg table format on MinIO cluster:

1-Create Related SCHEMA:
```
CREATE SCHEMA iceberg.fin_schema  WITH (location='s3a://bronze/financial');
CREATE SCHEMA iceberg.info_schema  WITH (location='s3a://bronze/information');

show schemas from  iceberg ;

```
2-Create Related Tables :
```
create table iceberg.fin_schema.financial_tbl
(
	id INT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	credit_card VARCHAR(50),
	credit_card_type VARCHAR(50),
	iban VARCHAR(50),
	currency_code VARCHAR(50),
	money_amount VARCHAR(50)

)
WITH (
 format = 'PARQUET'
);

create table iceberg.info_schema.information_tbl
(
	id INT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	email VARCHAR(50),
	gender VARCHAR(50),
	ip_address VARCHAR(20),
	car_company VARCHAR(50)

)
WITH (
 format = 'PARQUET'
);




```

