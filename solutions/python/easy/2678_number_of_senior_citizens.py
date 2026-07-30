"""
Problem ID : 2678
Title      : Number of Senior Citizens
Language   : Python
Solved Date: 2026-07-30
"""
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in details:
            if int(i[11:13])>60:
                count+=1
        return count