"""
Problem ID : 1464
Title      : Maximum Product of Two Elements in an Array
Language   : Python
Solved Date: 2026-07-27
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)