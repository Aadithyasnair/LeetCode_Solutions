"""
Problem ID : 0367
Title      : Valid Perfect Square
Language   : Python
Solved Date: 2026-07-20
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low=1
        high=num
        while low<=high:
            mid=(low+high)//2
            square=mid*mid
            if square==num:
                return True
            elif square<num:
                low=mid+1
            else:
                high=mid-1
        return False