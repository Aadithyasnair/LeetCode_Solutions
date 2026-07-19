"""
Problem ID : 0350
Title      : Intersection of Two Arrays II
Language   : Python
Solved Date: 2026-07-20
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret=[]
        for i in nums1:
            if i in nums2:
                ret.append(i)
                nums2.remove(i)
        return ret