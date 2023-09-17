"""
https://leetcode.com/problems/invalid-tweets/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
"""

import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets = tweets.loc[tweets['content'].str.len() > 15]
    tweets.pop('content')
    return tweets
