import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Merge the Employees and EmployeeUNI tables using a left join
    merged = employees.merge(employee_uni, on='id', how='left')

    # Rename columns to match the expected output format
    merged['unique_id'] = merged['unique_id'].apply(lambda x: None if pd.isnull(x) else int(x))
    result = merged[['unique_id', 'name']]

    return result

# Example usage
employees_data = {'id': [1, 7, 11, 90, 3],
                  'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']}
employee_uni_data = {'id': [3, 11, 90],
                     'unique_id': [1, 2, 3]}

employees_df = pd.DataFrame(employees_data)
employee_uni_df = pd.DataFrame(employee_uni_data)
result = replace_employee_id(employees_df, employee_uni_df)
print(result)
