from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

def create_spark_session():
    return SparkSession.builder \
        .appName("Sales ETL Pipeline") \
        .getOrCreate()

def read_data(spark, path):
    return spark.read.csv(path, header=True, inferSchema=True)

def transform_data(df):
    df = df.withColumn("total_amount", col("quantity") * col("price"))
    
    aggregated_df = df.groupBy("customer_id") \
        .agg(sum("total_amount").alias("total_spent"))
    
    return aggregated_df

def main():
    spark = create_spark_session()
    df = read_data(spark, "data/sample_sales.csv")
    result_df = transform_data(df)
    result_df.show()

if __name__ == "__main__":
    main()
