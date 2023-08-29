import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge Employee and Department tables based on departmentId
    merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id')

    # Group by department and find the employee with the highest salary in each group
    highest_salary_df = merged_df.groupby('name_y').apply(lambda x: x[x['salary'] == x['salary'].max()])

    # Rename columns and select required columns for the output
    result_df = highest_salary_df.rename(columns={'name_y': 'Department', 'name_x': 'Employee'}).reset_index(drop=True)
    result_df = result_df[['Department', 'Employee', 'salary']]

    return result_df

# Example usage
employee_data = {'id': [1, 2, 3, 4, 5],
                 'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
                 'salary': [70000, 90000, 80000, 60000, 90000],
                 'departmentId': [1, 1, 2, 2, 1]}
employee_df = pd.DataFrame(employee_data)

department_data = {'id': [1, 2],
                   'name': ['IT', 'Sales']}
department_df = pd.DataFrame(department_data)

result = department_highest_salary(employee_df, department_df)
print(result)
