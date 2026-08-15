"""
Problem ID : 997
Title      : Find the Town Judge
Language   : Python
Solved Date: 2026-08-15
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        for i in range(1, n + 1):
            if all(a != i for a, b in trust) and sum(b == i for a, b in trust) == n - 1:
                return i
        return -1