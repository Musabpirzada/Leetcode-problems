import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Get the sales_ids of salespersons who have orders related to company "RED"
    sales_ids_with_orders = orders[orders['com_id'].isin(company[company['name'] == 'RED']['com_id'])]['sales_id']

    # Filter salespersons who do not have orders related to company "RED"
    result = sales_person[~sales_person['sales_id'].isin(sales_ids_with_orders)]

    # Select only the 'name' column as output
    result = result[['name']]

    return result

# Example usage
sales_person_data = {'sales_id': [1, 2, 3, 4, 5],
                    'name': ['John', 'Amy', 'Mark', 'Pam', 'Alex'],
                    'salary': [100000, 12000, 65000, 25000, 5000],
                    'commission_rate': [6, 5, 12, 25, 10],
                    'hire_date': ['4/1/2006', '5/1/2010', '12/25/2008', '1/1/2005', '2/3/2007']}

company_data = {'com_id': [1, 2, 3, 4],
                'name': ['RED', 'ORANGE', 'YELLOW', 'GREEN'],
                'city': ['Boston', 'New York', 'Boston', 'Austin']}

orders_data = {'order_id': [1, 2, 3, 4],
               'order_date': ['1/1/2014', '2/1/2014', '3/1/2014', '4/1/2014'],
               'com_id': [3, 4, 1, 1],
               'sales_id': [4, 5, 1, 4],
               'amount': [10000, 5000, 50000, 25000]}

sales_person_df = pd.DataFrame(sales_person_data)
company_df = pd.DataFrame(company_data)
orders_df = pd.DataFrame(orders_data)

result = sales_person(sales_person_df, company_df, orders_df)
print(result)
