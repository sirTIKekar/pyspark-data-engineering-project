from pyspark.sql.functions import col

def clean_sales_data(df):
    df = df.dropna()
    df = df.filter(col("quantity") > 0)
    df = df.filter(col("price") > 0)
    return df
