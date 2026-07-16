"""
Problem ID : 0027
Title      : Remove Element
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
                continue
            i+=1
        return len(nums)