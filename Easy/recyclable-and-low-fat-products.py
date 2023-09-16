"""
https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
"""

import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products = products.loc[((products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'))]
    products.drop(columns=['low_fats', 'recyclable'], axis=1, inplace=True)
    products.sort_values(by='product_id', inplace=True)
    return products
