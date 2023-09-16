"""
https://leetcode.com/problems/rank-scores/?lang=pythondata
"""

import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.drop(['id'], axis=1, inplace=True)
    scores = scores.sort_values(by='score', ascending=False)
    s = list(scores['score'].unique())
    r = [int(i) for i in range(1, len(s)+1)]
    d = dict(zip(s, r))
    scores['rank'] = scores['score'].replace(d)
    return scores
