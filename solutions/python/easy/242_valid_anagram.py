"""
Problem ID : 242
Title      : Valid Anagram
Language   : Python
Solved Date: 2026-08-01
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            d1={}
            d2={}
            for i in range(len(s)):
                if s[i] not in d1:
                    d1[s[i]]=1
                elif s[i] in d1:
                    d1[s[i]]+=1
            for j in range(len(t)):
                if t[j] not in d2:
                    d2[t[j]]=1
                elif t[j] in d2:
                    d2[t[j]]+=1
        else:
            return False
        return d1==d2