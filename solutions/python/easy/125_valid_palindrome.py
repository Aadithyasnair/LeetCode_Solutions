"""
Problem ID : 125
Title      : Valid Palindrome
Language   : Python
Solved Date: 2026-08-01
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        fs=''
        for i in s:
            if i.isalpha() or i.isdigit():
                fs=fs+i.lower()
        return(fs==fs[::-1])