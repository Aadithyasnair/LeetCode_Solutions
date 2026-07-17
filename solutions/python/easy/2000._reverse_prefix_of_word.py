"""
Problem ID : 2000
Title      : Reverse Prefix of Word
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        neww=''
        for i in range(len(word)):
            if word[i]==ch:
                break
            i=-1
        if i==-1:
            return word
        else:
            return word[0:i+1][::-1]+word[i+1:len(word)]