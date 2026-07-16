"""
Problem ID : 0088
Title      : Merge Sorted Array
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        new = []
        for i in range(m):
            new.append(nums1[i])
        for i in range(n):
            new.append(nums2[i])
        new.sort()
        nums1[:] = new