"""
Problem ID : 0383
Title      : Ransom Note
Language   : Python
Solved Date: 2026-07-20
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        un=set(ransomNote)
        for i in un:
            if ransomNote.count(i)>magazine.count(i):
                return False
        return True