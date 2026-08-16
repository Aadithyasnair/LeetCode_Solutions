"""
Problem ID : 1716
Title      : Calculate Money in Leetcode Bank
Language   : Python
Solved Date: 2026-08-16
"""
class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        for i in range(n):
            res += i // 7 + i % 7 + 1
        return res