import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Group by customer_number and count the number of orders
    customer_order_counts = orders.groupby('customer_number')['order_number'].count().reset_index()

    # Find the customer with the maximum count of orders
    result = customer_order_counts[customer_order_counts['order_number'] == customer_order_counts['order_number'].max()]

    return result[['customer_number']]

# Example input
data = {'order_number': [1, 2, 3, 4],
        'customer_number': [1, 2, 3, 3]}

orders_table = pd.DataFrame(data)

# Call the function and print the result
result = largest_orders(orders_table)
print(result)
