"""
Problem ID : 0070
Title      : Climbing Stairs
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        return round((((1 + sqrt(5)) / 2) ** (n + 1) - ((1 - sqrt(5)) / 2) ** (n + 1)) / sqrt(5))