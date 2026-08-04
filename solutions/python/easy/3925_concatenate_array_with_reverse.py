"""
Problem ID : 3925
Title      : Concatenate Array With Reverse
Language   : Python
Solved Date: 2026-08-04
"""
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums+nums[::-1]