"""
Problem ID : 2855
Title      : Minimum Right Shifts to Sort the Array
Language   : Python
Solved Date: 2026-07-27
"""
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        nsor=sorted(nums)
        count=0
        while nums!=nsor and count<len(nsor):
            le=nums.pop()
            nums.insert(0,le)
            count+=1
        if nums==nsor:
            return count
        else:
            return -1