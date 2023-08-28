import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Use a regular expression to filter out valid emails based on the given criteria
    valid_emails_mask = users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$')
    return users[valid_emails_mask]

# Example usage
data = {'user_id': [1, 2, 3, 4, 5, 6, 7],
        'name': ['Winston', 'Jonathan', 'Annabelle', 'Sally', 'Marwan', 'David', 'Shapiro'],
        'mail': ['winston@leetcode.com', 'jonathanisgreat', 'bella-@leetcode.com', 'sally.come@leetcode.com', 'quarz#2020@leetcode.com', 'david69@gmail.com', '.shapo@leetcode.com']}
users_df = pd.DataFrame(data)
result = valid_emails(users_df)
print(result)
