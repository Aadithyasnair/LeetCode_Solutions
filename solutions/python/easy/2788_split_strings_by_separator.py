"""
Problem ID : 2788
Title      : Split Strings by Separator
Language   : Python
Solved Date: 2026-07-29
"""
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        newlist=[]
        for i in words:
            c=i.split(separator)
            for j in c:
                if j!="":
                    newlist.append(j)
        return newlist