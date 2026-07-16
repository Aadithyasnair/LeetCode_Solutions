"""
Problem ID : 0067
Title      : Add Binary
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a, 2) + int(b, 2):b}"