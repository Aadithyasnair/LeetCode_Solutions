"""
Problem ID : 1805
Title      : Number of Different Integers in a String
Language   : Python
Solved Date: 2026-07-18
"""
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        neww = ""
        for ch in word:
            if ch.isalpha():
                neww += " "
            else:
                neww += ch
        nums = neww.split()
        nums = [int(x) for x in nums]
        return len(set(nums))