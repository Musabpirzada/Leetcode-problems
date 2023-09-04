import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Group by actor_id and director_id and count the number of occurrences
    counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')

    # Filter for pairs with at least three cooperations
    result = counts[counts['cooperation_count'] >= 3][['actor_id', 'director_id']]

    return result

# Example usage
data = {'actor_id': [1, 1, 1, 1, 1, 2, 2],
        'director_id': [1, 1, 1, 2, 2, 1, 1],
        'timestamp': [0, 1, 2, 3, 4, 5, 6]}

actor_director_df = pd.DataFrame(data)
result = actors_and_directors(actor_director_df)
print(result)
