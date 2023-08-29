import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = sorted(set(employee['salary']), reverse=True)

    second_highest = unique_salaries[1] if len(unique_salaries) > 1 else None

    result_df = pd.DataFrame({"SecondHighestSalary": [second_highest]})
    return result_df

# Example usage
data = {'id': [1, 2],
        'salary': [100, 100]}
employee_df = pd.DataFrame(data)
result = second_highest_salary(employee_df)
print(result)
