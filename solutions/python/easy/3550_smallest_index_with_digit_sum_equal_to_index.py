"""
Problem ID : 3550
Title      : Smallest Index With Digit Sum Equal to Index
Language   : Python
Solved Date: 2026-08-07
"""
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        l=-1
        for i in range(len(nums)):
            numsum=0
            for j in str(nums[i]):
                numsum+=int(j)
            if numsum==i and (i<l or l==-1):
                l=i
        return l