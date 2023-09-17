"""
https://leetcode.com/problems/article-views-i/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
"""

import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views.loc[(views['author_id'] == views['viewer_id'])]
    df.drop(columns=['article_id', 'viewer_id', 'view_date'], axis=1, inplace=True)
    df = df.rename(columns={'author_id': 'id'})
    df = df.sort_values(by='id')
    return df.drop_duplicates()
