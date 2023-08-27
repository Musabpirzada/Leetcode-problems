import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter tweets where content length is greater than 15
    invalid_tweets = tweets[tweets['content'].apply(len) > 15]

    # Select only the 'tweet_id' column
    result = invalid_tweets[['tweet_id']]

    return result

# Sample input data
data = {
    'tweet_id': [1, 2],
    'content': ['Vote for Biden', 'Let us make America great again!']
}

tweets_df = pd.DataFrame(data)

# Call the function with the input DataFrame
result_df = invalid_tweets(tweets_df)

# Print the result
print(result_df)
