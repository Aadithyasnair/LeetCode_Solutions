"""
Problem ID : 3848
Title      : Check Digitorial Permutation
Language   : Python
Solved Date: 2026-08-20
"""

import math
class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        sumfac = 0

        for i in str(n):
            sumfac += math.factorial(int(i))

        return sorted(str(sumfac)) == sorted(str(n))