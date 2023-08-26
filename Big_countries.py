import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    result = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return result[['name', 'population', 'area']]

# Sample data
data = {
    'name': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'],
    'continent': ['Asia', 'Europe', 'Africa', 'Europe', 'Africa'],
    'area': [652230, 28748, 2381741, 468, 1246700],
    'population': [25500100, 2831741, 37100000, 78115, 20609294],
    'gdp': [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
}

world_df = pd.DataFrame(data)

result_df = big_countries(world_df)
print(result_df)


#https://leetcode.com/problems/big-countries/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
