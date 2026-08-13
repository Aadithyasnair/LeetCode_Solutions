"""
Problem ID : 3516
Title      : Find Closest Person
Language   : Python
Solved Date: 2026-08-13
"""
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z-x)>abs(z-y):
            return 2
        elif abs(z-x)==abs(z-y):
            return 0
        else:
            return 1    