import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)  # Sort by id to ensure the smallest id is kept
    person.drop_duplicates(subset='email', keep='first', inplace=True)

# Example usage
data = {'id': [2, 1],
        'email': ['abc@efg.com', 'abc@efg.com']}
person_df = pd.DataFrame(data)
print("Before:")
print(person_df)
delete_duplicate_emails(person_df)
print("After:")
print(person_df)
