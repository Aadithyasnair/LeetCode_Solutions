"""
Problem ID : 3931
Title      : Check Adjacent Digit Differences
Language   : Python
Solved Date: 2026-07-18
"""
class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        mx=0
        for i in range(len(s)-1):
            ss=abs(int(s[i])-int(s[i+1]))
            if ss>mx:
                mx=ss
        return True if mx<=2 else False