"""
Problem ID : 1389
Title      : Create Target Array in the Given Order
Language   : Python
Solved Date: 2026-08-02
"""
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target