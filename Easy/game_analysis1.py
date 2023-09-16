"""
https://leetcode.com/problems/game-play-analysis-i/?lang=pythondata
"""

import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.drop(columns=['device_id', 'games_played'], axis=1, inplace=True)
    activity.sort_values(by='event_date', ascending=True, inplace=True)
    activity.drop_duplicates(subset=['player_id'], inplace=True)
    activity.sort_values(by='player_id', inplace=True)
    activity = activity.rename(columns={'event_date': 'first_login'})
    return activity
