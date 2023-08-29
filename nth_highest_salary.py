import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    distinct_salaries = employee['salary'].unique()
    distinct_salaries.sort()

    nth_highest = None
    if N <= len(distinct_salaries):
        nth_highest = distinct_salaries[-N]

    result_df = pd.DataFrame({"getNthHighestSalary(" + str(N) + ")": [nth_highest]})
    return result_df

# Example usage
data = {'id': [1],
        'salary': [100]}
employee_df = pd.DataFrame(data)
N = 2
result = nth_highest_salary(employee_df, N)
print(result)
