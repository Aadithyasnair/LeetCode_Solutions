"""
Problem ID : 3300
Title      : Minimum Element After Replacement With Digit Sum
Language   : Python
Solved Date: 2026-08-13
"""
class Solution:
    def minElement(self, nums: List[int]) -> int:
        l1=[]
        for i in nums:
            sum=0
            for j in str(i):
                sum+=int(j)
            l1.append(sum)
        return min(l1)