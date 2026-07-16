"""
Problem ID : 1450
Title      : Number of Students Doing Homework at a Given Time
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        c=0
        for i in range(len(startTime)):
            if startTime[i]<=queryTime<=endTime[i]:
                c+=1
        return c