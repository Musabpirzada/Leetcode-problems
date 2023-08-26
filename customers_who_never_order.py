import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
  """
  Finds all customers who never order anything.

  Args:
    customers: A Pandas DataFrame of customers.
    orders: A Pandas DataFrame of orders.

  Returns:
    A Pandas DataFrame of customers who never order anything.
  """

  # Add the customerId column to the customers DataFrame.
  customers['customerId'] = customers['id']

  # Add the orderId column to the orders DataFrame.
  orders['orderId'] = orders['id']

  # Left join the customers and orders tables on the customer ID column.
  joined_df = customers.merge(orders, on='customerId', how='left')

  try:
    # Filter for customers where the order ID is null.
    customers_who_never_ordered = joined_df[joined_df['orderId'].isnull()]
  except KeyError as err:
    print(f"The {err} column does not exist in the joined DataFrame.")

  # Select and rename the 'name' column to 'Customers'.
  return customers_who_never_ordered[['name']].rename(columns={'name': 'Customers'})
