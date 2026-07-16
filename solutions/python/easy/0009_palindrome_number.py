"""
Problem ID : 0009
Title      : Palindrome Number
Language   : Python
Solved Date: 2026-07-16
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x)==str(x)[::-1] else False