"""
https://leetcode.com/problems/duplicate-emails/?lang=pythondata
"""

import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person[person.duplicated(['email'])].drop('id', axis=1)
    return df.drop_duplicates()


"""
https://leetcode.com/problems/delete-duplicate-emails/?lang=pythondata
"""

# Modify Person in place


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset=['email'], inplace=True)
