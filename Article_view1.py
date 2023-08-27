import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter views where author_id is equal to viewer_id
    self_views = views[views['author_id'] == views['viewer_id']]

    # Get unique author_ids from self_views
    unique_author_ids = self_views['author_id'].unique()

    # Create a DataFrame with the unique_author_ids
    result = pd.DataFrame({'id': unique_author_ids})

    # Sort the result by id in ascending order
    result = result.sort_values(by='id')

    return result

# Sample input data
data = {
    'article_id': [1, 1, 2, 2, 4, 3, 3],
    'author_id': [3, 3, 7, 7, 7, 4, 4],
    'viewer_id': [5, 6, 7, 6, 1, 4, 4],
    'view_date': ['2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02', '2019-07-22', '2019-07-21', '2019-07-21']
}

views_df = pd.DataFrame(data)

# Call the function with the input DataFrame
result_df = article_views(views_df)

# Print the result
print(result_df)
