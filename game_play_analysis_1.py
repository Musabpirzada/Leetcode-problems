import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Group by player_id and select the minimum event_date
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    result = result.rename(columns={'player_id': 'player_id', 'event_date': 'first_login'})

    return result

# Example input
data = {'player_id': [1, 1, 2, 3, 3],
        'device_id': [2, 2, 3, 1, 4],
        'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
        'games_played': [5, 6, 1, 0, 5]}

activity_table = pd.DataFrame(data)

# Call the function and print the result
result = game_analysis(activity_table)
print(result)
