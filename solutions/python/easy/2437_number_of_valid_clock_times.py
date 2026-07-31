"""
Problem ID : 2437
Title      : Number of Valid Clock Times
Language   : Python
Solved Date: 2026-07-31
"""
class Solution:
    def countTime(self, time: str) -> int:
        if time[0] == '?' and time[1] == '?':
            hours = 24
        elif time[0] == '?':
            hours = 3 if time[1] < '4' else 2
        elif time[1] == '?':
            hours = 4 if time[0] == '2' else 10
        else:
            hours = 1
        if time[3] == '?' and time[4] == '?':
            minutes = 60
        elif time[3] == '?':
            minutes = 6
        elif time[4] == '?':
            minutes = 10
        else:
            minutes = 1
        return hours * minutes