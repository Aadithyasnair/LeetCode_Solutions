"""
Problem ID : 3174
Title      : Clear Digits
Language   : Python
Solved Date: 2026-08-02
"""
class Solution:
    def clearDigits(self, s: str) -> str:
        sl=[]
        for i in s:
            if i.isdigit():
                sl.pop()
            else:
                sl.append(i)
        return "".join(sl)