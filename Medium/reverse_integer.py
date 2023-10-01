"""
https://leetcode.com/problems/reverse-integer/
"""


class Solution:

    def reverse(self, x: int) -> int:
        x = str(x)
        if int(x) not in range(-2**31, 2**31):
            k = 0
        else:
            if int(x) >= 0:
                k = int(x[::-1])
                if k > 2**31-1:
                    k = 0
            else:
                n = x[1:]
                k = int(x[0]+n[::-1])
                if k < -2**31:
                    k = 0
        return k
