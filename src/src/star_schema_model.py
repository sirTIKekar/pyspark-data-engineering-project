def create_fact_table(df):
    fact_sales = df.select(
        "order_id",
        "customer_id",
        "product_id",
        "quantity",
        "price",
        "order_date"
    )
    return fact_sales

def create_dim_customer(df):
    dim_customer = df.select("customer_id").distinct()
    return dim_customer

def create_dim_product(df):
    dim_product = df.select("product_id").distinct()
    return dim_product
