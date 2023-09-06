import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = accounts[accounts['income'] < 20000]
    low_salary_result = pd.DataFrame({'category': ['Low Salary'], 'accounts_count': [len(low_salary)]})

    average_salary = accounts[(20000 <= accounts['income']) & (accounts['income'] <= 50000)]
    average_salary_result = pd.DataFrame({'category': ['Average Salary'], 'accounts_count': [len(average_salary)]})

    high_salary = accounts[accounts['income'] > 50000]
    high_salary_result = pd.DataFrame({'category': ['High Salary'], 'accounts_count': [len(high_salary)]})

    result = pd.concat([low_salary_result, average_salary_result, high_salary_result], ignore_index=True)
    return result

# Example usage
data = {'income': [15000, 30000, 45000, 10000, 55000, 60000, 25000]}
accounts_df = pd.DataFrame(data)
result = count_salary_categories(accounts_df)
print(result)
