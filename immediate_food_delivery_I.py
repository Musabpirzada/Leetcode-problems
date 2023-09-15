import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # Calculate the total number of immediate orders
    immediate_orders = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]
    immediate_order_count = len(immediate_orders)

    # Calculate the total number of orders
    total_order_count = len(delivery)

    # Calculate the percentage of immediate orders
    immediate_percentage = (immediate_order_count / total_order_count) * 100

    # Create a DataFrame with the result
    result_df = pd.DataFrame({'immediate_percentage': [round(immediate_percentage, 2)]})
    return result_df

# Example input
data = {'delivery_id': [1, 2, 3, 4, 5, 6],
        'customer_id': [1, 5, 1, 3, 4, 2],
        'order_date': ['2019-08-01', '2019-08-02', '2019-08-11', '2019-08-24', '2019-08-21', '2019-08-11'],
        'customer_pref_delivery_date': ['2019-08-02', '2019-08-02', '2019-08-11', '2019-08-26', '2019-08-22', '2019-08-13']}

delivery_table = pd.DataFrame(data)
delivery_table['order_date'] = pd.to_datetime(delivery_table['order_date'])
delivery_table['customer_pref_delivery_date'] = pd.to_datetime(delivery_table['customer_pref_delivery_date'])

# Call the function and print the result
result = food_delivery(delivery_table)
print(result)
