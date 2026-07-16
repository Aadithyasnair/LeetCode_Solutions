"""
Problem ID : 0069
Title      : Sqrt(x)
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        while (i*i)<=x:
            i+=1
        return i-1 