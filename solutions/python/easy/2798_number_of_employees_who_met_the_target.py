"""
Problem ID : 2798
Title      : Number of Employees Who Met the Target
Language   : Python
Solved Date: 2026-07-31
"""
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(1 for i in hours if i>=target)