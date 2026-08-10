"""
Problem ID : 1941
Title      : Check if All Characters Have Equal Number of Occurrences
Language   : Python
Solved Date: 2026-08-10
"""
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        l=list(s)
        s=set(l)
        cnt=[]
        for i in s:
            cnt.append(l.count(i))
        if cnt.count(cnt[0])==len(cnt):
            return True
        else:
            return False