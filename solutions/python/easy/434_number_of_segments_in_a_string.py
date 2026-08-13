"""
Problem ID : 434
Title      : Number of Segments in a String
Language   : Python
Solved Date: 2026-08-13
"""
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())