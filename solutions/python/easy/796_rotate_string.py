"""
Problem ID : 796
Title      : Rotate String
Language   : Python
Solved Date: 2026-08-16
"""
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        dec=False
        if s==goal:
            dec=True
        else:
            s=list(s)
            for i in range(len(s)-1):
                s.insert(len(s)-1,s.pop(0))
                if "".join(s)==goal:
                    dec=True
        return dec