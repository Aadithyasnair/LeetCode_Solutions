"""
Problem ID : 2525
Title      : Categorize Box According to Criteria
Language   : Python
Solved Date: 2026-08-02
"""
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulk=False
        heavy=False
        if length>=10**4 or width>=10**4 or height>=10**4 or length*width*height>=10**9:
            bulk=True
        if mass>=100:
            heavy=True
        if bulk and heavy:
            return 'Both'
        if not bulk and not heavy:
            return 'Neither'
        if bulk and not heavy:
            return 'Bulky'
        if not bulk and heavy:
            return 'Heavy'