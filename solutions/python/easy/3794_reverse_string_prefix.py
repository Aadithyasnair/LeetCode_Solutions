"""
Problem ID : 3794
Title      : Reverse String Prefix
Language   : Python
Solved Date: 2026-07-26
"""
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1]+s[k:]