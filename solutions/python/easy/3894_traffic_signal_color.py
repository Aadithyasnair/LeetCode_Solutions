"""
Problem ID : 3894
Title      : Traffic Signal Color
Language   : Python
Solved Date: 2026-07-25
"""
class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer == 0:
            return "Green"
        elif timer == 30:
            return "Orange"
        elif 30 < timer <= 90:
            return "Red"
        else:
            return "Invalid"