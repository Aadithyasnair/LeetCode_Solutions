"""
Problem ID : 0492
Title      : Construct the Rectangle
Language   : Python
Solved Date: 2026-07-18
"""
import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mind=math.inf
        l=w=0

        for i in range(1,int(math.sqrt(area))+1):
            if area%i==0:
                j=area//i
                if j-i<mind:
                    mind=j-i
                    l=j
                    w=i
        return [l,w]