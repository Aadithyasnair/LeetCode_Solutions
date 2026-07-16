"""
Problem ID : 0664
Title      : Strange Printer
Language   : Python
Solved Date: 2026-07-17
"""
from functools import cache

class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def solve(i, j):
            if i >= j:
                return 1 if i == j else 0
            
            res = solve(i, j - 1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    res = min(res, solve(i, k) + solve(k + 1, j - 1))
            return res

        return solve(0, len(s) - 1)
