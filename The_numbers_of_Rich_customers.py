import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame to keep only rows with amount greater than 500
    rich_customers = store[store['amount'] > 500]

    # Count the number of unique customer IDs in the filtered DataFrame
    rich_count = rich_customers['customer_id'].nunique()

    # Create a DataFrame with the result
    result_df = pd.DataFrame({'rich_count': [rich_count]})
    return result_df

# Example input
data = {'bill_id': [6, 8, 4, 11, 13],
        'customer_id': [1, 1, 2, 3, 3],
        'amount': [549, 834, 394, 657, 257]}

store_table = pd.DataFrame(data)

# Call the function and print the result
result = count_rich_customers(store_table)
print(result)
