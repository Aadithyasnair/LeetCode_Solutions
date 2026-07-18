"""
Problem ID : 1837
Title      : Sum of Digits in Base K
Language   : Python
Solved Date: 2026-07-18
"""
import numpy as np
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        lee=np.base_repr(n,base=k)
        sum=0
        for i in lee:
            sum=sum+int(i)
        return sum