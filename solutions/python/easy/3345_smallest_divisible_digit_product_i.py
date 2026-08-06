"""
Problem ID : 3345
Title      : Smallest Divisible Digit Product I
Language   : Python
Solved Date: 2026-08-06
"""
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            pro=1
            for i in str(n):
                pro*=int(i)
            if pro%t==0:
                return n
            n+=1
