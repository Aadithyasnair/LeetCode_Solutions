"""
Problem ID : 0001
Title      : Two Sum
Language   : Python
Solved Date: 2026-07-16
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        ro=True
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i]+nums[j])==target:
                    return [i,j]
                    ro=False
                    break