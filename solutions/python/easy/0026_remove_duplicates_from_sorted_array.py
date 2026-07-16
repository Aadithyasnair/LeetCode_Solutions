"""
Problem ID : 0026
Title      : Remove Duplicates from Sorted Array
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i!=len(nums)-1:
            print(nums[i],nums[i+1])
            if (nums[i]==nums[i+1]):
                nums.pop(i+1)
                continue
            i=i+1
        return len(nums)