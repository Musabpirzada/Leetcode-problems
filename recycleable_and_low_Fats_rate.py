import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.query('low_fats == "Y" & recyclable == "Y"')[['product_id']]

# Sample data
data = {
    'product_id': [0, 1, 2, 3, 4],
    'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
    'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
}

products_df = pd.DataFrame(data)

result_df = find_products(products_df)
print(result_df)


https://leetcode.com/studyplan/30-days-of-pandas/
