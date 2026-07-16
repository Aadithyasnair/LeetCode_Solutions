"""
Problem ID : 0008
Title      : String to Integer (atoi)
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        sign = 1
        if s and s[0] == '-':
            sign = -1
            s = s[1:]
        elif s and s[0] == '+':
            s = s[1:]
        
        num = 0
        
        for i in s:
            if not i.isdigit():
                break
            num = num * 10 + int(i)
        
        num *= sign
        
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1
        
        return num