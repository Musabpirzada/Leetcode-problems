import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # Group by date_id, make_name, and calculate the number of unique lead_id and partner_id
    grouped = daily_sales.groupby(['date_id', 'make_name']).agg({'lead_id': 'nunique', 'partner_id': 'nunique'}).reset_index()

    # Rename columns to match the expected output format
    grouped.rename(columns={'date_id': 'date_id', 'make_name': 'make_name', 'lead_id': 'unique_leads', 'partner_id': 'unique_partners'}, inplace=True)

    return grouped

# Example usage
data = {'date_id': ['2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7'],
        'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota', 'honda', 'honda', 'honda', 'honda', 'honda'],
        'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
        'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]}

daily_sales_df = pd.DataFrame(data)
result = daily_leads_and_partners(daily_sales_df)
print(result)
