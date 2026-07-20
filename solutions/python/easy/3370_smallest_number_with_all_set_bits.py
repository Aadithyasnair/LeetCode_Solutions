"""
Problem ID : 3370
Title      : Smallest Number With All Set Bits
Language   : Python
Solved Date: 2026-07-20
"""
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (int('1'*len(bin(n)[2:]),2))