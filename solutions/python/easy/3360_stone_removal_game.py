"""
Problem ID : 3360
Title      : Stone Removal Game
Language   : Python
Solved Date: 2026-08-06
"""
class Solution:
    def canAliceWin(self, n: int) -> bool:
        count=10
        turn='A'
        while True:
            if n<count:
                if turn=='A':
                    return False
                else:
                    return True
            else:
                n=n-count
                count-=1
                if turn=='A':
                    turn='B'
                else:
                    turn='A'