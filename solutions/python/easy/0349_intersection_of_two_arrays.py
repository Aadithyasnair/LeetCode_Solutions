"""
Problem ID : 0349
Title      : Intersection of Two Arrays
Language   : Python
Solved Date: 2026-07-19
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return (list(set(nums1).intersection(set(nums2))))
