"""
Problem ID : 0066
Title      : Plus One
Language   : Python
Solved Date: 2026-07-16
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new=[]
        digit=0
        for i in digits:
            digit=digit*10+i
        digit=digit+1
        while digit>0:
            k=digit%10
            digit=digit//10
            new.append(k)
        return new[::-1]