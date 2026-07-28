"""
Problem ID : 3024
Title      : Type of Triangle
Language   : Python
Solved Date: 2026-07-28
"""
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0]+nums[1]<=nums[2]:
            return 'none'
        else:
            if nums[0]==nums[1]==nums[2]:
                return 'equilateral'
            elif nums[0]==nums[1] or nums[1]==nums[2] or nums[0]==nums[2]:
                return 'isosceles'
            else:
                return 'scalene'