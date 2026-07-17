"""
Problem ID : 3467
Title      : Transform Array by Parity
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        newl=[]
        for i in nums:
            if i%2==0:
                newl.append(0)
            else:
                newl.append(1)
        newl.sort()
        return newl