"""
Problem ID : 3099
Title      : Harshad Number
Language   : Python
Solved Date: 2026-07-27
"""
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sd=0
        for i in str(x):
            sd+=int(i)
        return sd if x%sd==0 else -1