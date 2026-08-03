"""
Problem ID : 3697
Title      : Compute Decimal Representation
Language   : Python
Solved Date: 2026-08-03
"""
class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        pointer=0
        ls=[]
        while pointer<len(str(n)):
            if str(n)[pointer]!='0':
                ls.append(int(str(n)[pointer]+('0'*(len(str(n))-pointer-1))))
            pointer+=1
        return ls