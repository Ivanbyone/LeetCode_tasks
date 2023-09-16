"""
https://leetcode.com/problems/big-countries/?lang=pythondata
"""

import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world.drop(columns=['continent', 'gdp'], axis=1, inplace=True)
    return world.loc[((world['area'] >= 3000000) | (world['population'] >= 25000000))]
