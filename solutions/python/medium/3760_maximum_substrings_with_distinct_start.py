"""
Problem ID : 3760
Title      : Maximum Substrings With Distinct Start
Language   : Python
Solved Date: 2026-07-20
"""
class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))