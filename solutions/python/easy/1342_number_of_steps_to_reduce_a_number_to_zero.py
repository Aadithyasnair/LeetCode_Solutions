"""
Problem ID : 1342
Title      : Number of Steps to Reduce a Number to Zero
Language   : Python
Solved Date: 2026-07-21
"""
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps=0
        while num!=0:
            if num%2==0:
                num=num/2
                steps+=1
            else:
                num=num-1
                steps+=1
        return steps