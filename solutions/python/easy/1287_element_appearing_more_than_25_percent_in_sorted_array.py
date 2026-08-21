"""
Problem ID : 1287
Title      : Element Appearing More Than 25% In Sorted Array
Language   : Python
Solved Date: 2026-08-21
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in arr:
            if (arr.count(i)>(len(arr)*0.25)):
                return i