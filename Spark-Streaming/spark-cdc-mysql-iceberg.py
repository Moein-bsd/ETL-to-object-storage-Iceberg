
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, lit, current_timestamp, coalesce
from pyspark.sql.types import StructType, StructField, StringType, IntegerType ,  BooleanType, TimestampType, DoubleType , LongType
from pyspark.sql import functions as F



financial_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("credit_card", StringType(), True),
    StructField("credit_card_type", StringType(), True),
    StructField("iban", StringType(), True),
    StructField("currency_code", StringType(), True),
    StructField("money_amount", StringType(), True)
])

cdc_schema = StructType([
    StructField("payload", StructType([
        StructField("before", financial_schema, True),
        StructField("after", financial_schema, True),
        StructField("op", StringType(), True),
        StructField("ts_ms", LongType(), True)
        
    ]), True)
])


def process_batch(batch_df, batch_id):
    """Process each batch of CDC events"""
    if batch_df.count() == 0:
        return




 

    operational_df = batch_df.select(
        coalesce(col("after.id"), col("before.id")).alias("id"),
        coalesce(col("after.first_name"), col("before.first_name")).alias("first_name"),
        coalesce(col("after.last_name"), col("before.last_name")).alias("last_name"),
        coalesce(col("after.credit_card"), col("before.credit_card")).alias("credit_card"),
        coalesce(col("after.credit_card_type"), col("before.credit_card_type")).alias("credit_card_type"),
        coalesce(col("after.iban"), col("before.iban")).alias("iban"),
        coalesce(col("after.currency_code"), col("before.currency_code")).alias("currency_code"),
        coalesce(col("after.money_amount"), col("before.money_amount")).alias("money_amount"),
        col("op")  # Keep the operation type
        )
    #####################################################
    # Check processed operational data
    print("=== Operational Data ===")
    operational_df.show(truncate=False)
    print(f"Operational row count: {operational_df.count()}")
    #####################################################################

    #operational_df.printSchema()

    spark = batch_df.sparkSession


    operational_df.createOrReplaceTempView("updates")
    # Perform DML MERGE
    spark.sql("""
    MERGE INTO iceberg.fin_schema.financial_tbl AS target
    USING (
        SELECT 
            id, 
            first_name, 
            last_name, 
            credit_card, 
            credit_card_type, 
            iban, 
            currency_code, 
            money_amount,
            op
        FROM updates
        ) AS s
        ON  target.id = s.id
        WHEN MATCHED AND s.op = 'd' THEN DELETE
        WHEN MATCHED AND s.op = 'u' THEN 
        UPDATE SET
            target.id = s.id,
            target.first_name = s.first_name,
            target.last_name = s.last_name,
            target.credit_card = s.credit_card,
            target.credit_card_type = s.credit_card_type,
            target.iban = s.iban,
            target.currency_code = s.currency_code,
            target.money_amount = s.money_amount
        WHEN NOT MATCHED AND s.op = 'c'
        THEN INSERT  (id,first_name, last_name, credit_card, credit_card_type, iban, currency_code, money_amount) 
        VALUES (s.id, s.first_name, s.last_name, s.credit_card, s.credit_card_type, s.iban, s.currency_code, s.money_amount )        
        """)






def main():
    spark = SparkSession.builder \
        .appName("MySQL-CDC-to-Iceberg") \
        .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")\
        .config("spark.sql.catalog.iceberg", "org.apache.iceberg.spark.SparkCatalog") \
        .config("spark.sql.catalog.iceberg.type", "hive") \
        .config("spark.sql.catalog.iceberg.uri", "thrift://192.168.16.244:9083") \
        .config("spark.sql.catalog.iceberg.s3.endpoint", "http://node5:1000") \
        .config("spark.sql.catalog.iceberg.warehouse", "s3a://bronze/") \
        .config("spark.sql.catalog.iceberg.io-impl", "org.apache.iceberg.aws.s3.S3FileIO") \
        .config("spark.sql.catalog.iceberg.s3.path-style-access", "true") \
	    .getOrCreate()

    # Read from Kafka
    kafka_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "node1:9092,node2:9092,node3:9092") \
        .option("subscribe", "mysql-perfix.source1.financial_tbl") \
        .option("startingOffsets", "earliest") \
        .load()



    # Parse the CDC JSON payload
    parsed_df = kafka_df.select(
        from_json(col("value").cast("string"), cdc_schema).alias("data")
        ).select("data.payload.*")




    # Process the stream
    query = parsed_df.writeStream \
        .foreachBatch(process_batch) \
        .option("checkpointLocation", "s3a://bronze/checkpoints/financial_cdc") \
        .trigger(processingTime="20 seconds") \
        .start()

    query.awaitTermination()


if __name__ == "__main__":
    main()







