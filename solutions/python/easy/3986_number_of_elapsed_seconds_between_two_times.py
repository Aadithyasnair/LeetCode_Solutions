"""
Problem ID :3986
Title      : Number of Elapsed Seconds Between Two Times
Language   : Python
Solved Date: 2026-07-18
"""
from datetime import datetime

class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        return int((datetime.strptime(endTime, "%H:%M:%S") - datetime.strptime(startTime, "%H:%M:%S")).total_seconds())