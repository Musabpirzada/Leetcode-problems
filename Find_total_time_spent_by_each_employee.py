import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate the total time spent by each employee on each day
    employees['total_time'] = employees['out_time'] - employees['in_time']

    # Group by emp_id and event_day, and sum the total_time
    result = employees.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    result = result.rename(columns={'event_day': 'day', 'emp_id': 'emp_id', 'total_time': 'total_time'})

    return result

# Example input
data = {'emp_id': [1, 1, 1, 2, 2],
        'event_day': ['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09'],
        'in_time': [4, 55, 1, 3, 47],
        'out_time': [32, 200, 42, 33, 74]}

employees_table = pd.DataFrame(data)

# Call the function and print the result
result = total_time(employees_table)
print(result)
