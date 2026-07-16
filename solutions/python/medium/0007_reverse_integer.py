"""
Problem ID : 0007
Title      : Reverse Integer
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0]=='-':
            k=int('-'+str(x)[1:][::-1])
        else:
            k=int(str(x)[::-1])
        if -2**31 <= k <= 2**31 - 1:
            return k
        else:
            return 0