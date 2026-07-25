"""
Problem ID : 3908
Title      : Valid Digit Number
Language   : Python
Solved Date: 2026-07-25
"""
class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        return str(n)[0]!=str(x) and  list(str(n)).count(str(x))>=1