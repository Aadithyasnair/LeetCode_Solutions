"""
Problem ID : 3798
Title      : Largest Even Number
Language   : Python
Solved Date: 2026-07-26
"""
class Solution:
    def largestEven(self,s: str) -> str:
        s1=list(s)
        if '2' in s1:
            if s1.index('2')==(len(s)-1):
                return s
            else:
                del s1[len(s1)-s1[::-1].index("2"):]
            return "".join(s1)
        else:
            return ''