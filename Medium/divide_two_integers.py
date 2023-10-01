"""
https://leetcode.com/problems/divide-two-integers/
"""


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        result = int(dividend / divisor)
        if result not in range(-2**31, 2**31-1):
            if result > 0:
                result = 2**31-1
            elif result < 0:
                result = -2**31

        return result
