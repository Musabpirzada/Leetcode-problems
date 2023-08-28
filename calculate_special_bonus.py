import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Apply bonus calculation based on conditions
    employees['bonus'] = employees.apply(lambda row: row['salary'] if row['employee_id'] % 2 != 0 and not row['name'].startswith('M') else 0, axis=1)

    # Sort the DataFrame by employee_id
    result = employees.sort_values(by='employee_id')

    # Select only the 'employee_id' and 'bonus' columns
    result = result[['employee_id', 'bonus']]

    return result

# Sample input data
data = {
    'employee_id': [2, 3, 7, 8, 9],
    'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
    'salary': [3000, 3800, 7400, 6100, 7700]
}

employees_df = pd.DataFrame(data)

# Call the function with the input DataFrame
result_df = calculate_special_bonus(employees_df)

# Print the result
print(result_df)
