import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Count the number of direct reports for each manager
    direct_reports_count = employee.groupby('managerId').size().reset_index(name='reports_count')

    # Filter for managers with at least five direct reports or with None (null) managerId
    result = direct_reports_count[(direct_reports_count['reports_count'] >= 5) | (direct_reports_count['managerId'].isnull())]

    # Merge with the employee table to get manager names
    result = result.merge(employee[['id', 'name']], left_on='managerId', right_on='id', how='left')

    # Select only the 'name' column as output
    result = result[['name']]

    # Filter out rows with empty names
    result = result[result['name'].notnull()]

    return result

# Example usage
employee_data = {'id': [101, 102, 103, 104, 105, 106],
                  'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'],
                  'department': ['A', 'A', 'A', 'A', 'A', 'B'],
                  'managerId': [None, 101, 101, 101, 101, 101]}

employee_df = pd.DataFrame(employee_data)
result = find_managers(employee_df)
print(result)
