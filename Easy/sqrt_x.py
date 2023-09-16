"""
https://leetcode.com/problems/sqrtx/
"""
from math import floor


class Solution:

    def mysqrt(self, x: int) -> int:
        return floor(x**(1/2))
