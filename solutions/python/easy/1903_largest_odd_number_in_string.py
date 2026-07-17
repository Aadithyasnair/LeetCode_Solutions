"""
Problem ID : 1903
Title      : Largest Odd Number in String
Language   : Python
Solved Date: 2026-07-16
"""
class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=len(num)
        for i in range(n-1,-1,-1):
            if int(num[i])%2==0:
                continue
            return num[:i+1]
            break
        return ""