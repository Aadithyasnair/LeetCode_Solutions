"""
Problem ID : 2864
Title      : Maximum Odd Binary Number
Language   : Python
Solved Date: 2026-07-19
"""
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        oc=s.count("1")
        zc=len(s)-oc
        return ("1"*(oc-1))+("0"*(zc))+"1"