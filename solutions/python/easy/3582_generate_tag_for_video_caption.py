"""
Problem ID : 3582
Title      : Generate Tag for Video Caption
Language   : Python
Solved Date: 2026-07-27
"""
class Solution:
    def generateTag(self, caption: str) -> str:
        clist=list(caption.title())
        caption1="".join(char for char in clist if char.isalpha())
        try:
            ans="".join(caption1[0].lower())+"".join(caption1[1:])
            return '#'+ans[:99]
        except IndexError:
            return '#'