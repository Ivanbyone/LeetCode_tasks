"""
https://leetcode.com/problems/palindrome-number/
"""


class Solution:

    def ispalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
