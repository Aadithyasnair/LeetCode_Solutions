"""
Problem ID : 1431
Title      : Kids With the Greatest Number of Candies
Language   : Python
Solved Date: 2026-08-06
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        for i in candies:
            High=True
            for j in candies:
                if i+extraCandies < j:
                    High=False
            l.append(High)
        return l