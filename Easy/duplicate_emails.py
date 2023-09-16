"""
https://leetcode.com/problems/duplicate-emails/?lang=pythondata
"""

import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person[person.duplicated(['email'])].drop('id', axis=1)
    return df.drop_duplicates()
