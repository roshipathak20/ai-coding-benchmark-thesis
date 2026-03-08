# Task: Pandas data aggregation
# Write a Python function total_sales_per_product(df)
#
# The dataframe contains columns:
# product, amount
#
# The function should group the dataframe by product
# and calculate the total sales amount per product.
#
# Example:
# product amount
# A       10
# B       20
# A       5
#
# Output:
# product amount
# A       15
# B       20

def total_sales_per_product(df):
    return df.groupby('product')['amount'].sum().reset_index()      