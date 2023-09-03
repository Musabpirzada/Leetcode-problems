import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # Group by sell_date and aggregate product names as a sorted list without spaces after commas
    grouped = activities.groupby('sell_date')['product'].apply(lambda x: ','.join(sorted(set(x)))).reset_index()

    # Calculate the number of different products sold
    grouped['num_sold'] = grouped['product'].apply(lambda x: len(x.split(',')))

    # Reorder columns to match the expected output format
    grouped = grouped.rename(columns={'sell_date': 'sell_date', 'num_sold': 'num_sold', 'product': 'products'})
    grouped = grouped[['sell_date', 'num_sold', 'products']]

    return grouped

# Example usage
data = {'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30'],
        'product': ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-Shirt']}

activities_df = pd.DataFrame(data)
result = categorize_products(activities_df)

# Print the result in the specified format
print(result.to_string(index=False, col_space={'products': 30}))
