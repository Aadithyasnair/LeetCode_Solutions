"""
Problem ID : 0258
Title      : Add Digits
Language   : Python
Solved Date: 2026-07-19
"""
class Solution:
    def addDigits(self, num: int) -> int:
        def rec(num):
            total = 0
            for i in str(num):
                total += int(i)
            return total
        while len(str(num)) > 1:
            num = rec(num)
        return num