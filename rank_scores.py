import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
  """
  Rank scores from highest to lowest.

  Args:
    scores: A Pandas DataFrame with two columns: `id` and `score`.

  Returns:
    A Pandas DataFrame with two columns: `score` and `rank`. The scores are ranked
    from highest to lowest, and ties are broken by assigning the same rank to all
    tied scores. The id column is removed.
  """

  # Sort scores in descending order
  scores = scores.sort_values(by=['score'], ascending=False)

  # Rank scores
  scores['rank'] = scores['score'].rank(method='dense', ascending=False)

  # Remove id column
  scores = scores[['score', 'rank']]

  return scores
