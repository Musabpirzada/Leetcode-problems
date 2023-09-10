import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Initialize an empty list to store the rearranged data
    rearranged_data = []

    # Iterate through each row in the original table
    for index, row in products.iterrows():
        product_id = row['product_id']

        # Check if the product is available in each store
        if not pd.isnull(row['store1']):
            rearranged_data.append((product_id, 'store1', row['store1']))
        if not pd.isnull(row['store2']):
            rearranged_data.append((product_id, 'store2', row['store2']))
        if not pd.isnull(row['store3']):
            rearranged_data.append((product_id, 'store3', row['store3']))

    # Create a new DataFrame from the rearranged data
    result_df = pd.DataFrame(rearranged_data, columns=['product_id', 'store', 'price'])
    return result_df

# Example input
data = {'product_id': [0, 1],
        'store1': [95, 70],
        'store2': [100, None],
        'store3': [105, 80]}

products_table = pd.DataFrame(data)

# Call the function and print the result
result = rearrange_products_table(products_table)
print(result)
