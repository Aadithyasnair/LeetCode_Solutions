"""
Problem ID : 1089
Title      : Duplicate Zeros
Language   : Python
Solved Date: 2026-08-05
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arrlen=len(arr)
        for i in range(arrlen-1,-1,-1):
            print(i)
            if arr[i]==0:
                arr.insert(i+1,0)
        arr[:]=arr[:arrlen]