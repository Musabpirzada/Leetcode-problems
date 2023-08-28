import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()  # Capitalize the first character and convert the rest to lowercase
    return users.sort_values(by='user_id')  # Sort the result by user_id

# Example usage
data = {'user_id': [1, 2],
        'name': ['aLice', 'bOB']}
users_df = pd.DataFrame(data)
result = fix_names(users_df)
print(result)
