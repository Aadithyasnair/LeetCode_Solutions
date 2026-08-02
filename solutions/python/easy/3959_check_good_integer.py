"""
Problem ID : 3959
Title      : Check Good Integer
Language   : Python
Solved Date: 2026-08-02
"""
class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitsum=0
        squaresum=0
        for i in str(n):
            digitsum+=int(i)
            squaresum+=(int(i)**2)
        return ((squaresum-digitsum)>=50)