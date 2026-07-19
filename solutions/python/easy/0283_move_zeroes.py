"""
Problem ID : 0283
Title      : Move Zeroes
Language   : Python
Solved Date: 2026-07-19
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zc=nums.count(0)
        nums[:]=[x for x in nums if x!=0]
        nums.extend([0]*zc)