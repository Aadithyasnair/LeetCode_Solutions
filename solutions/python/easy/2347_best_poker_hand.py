"""
Problem ID : 2347
Title      : Best Poker Hand
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        count = {}
        for r in ranks:
            count[r] = count.get(r, 0) + 1
        mx = max(count.values())
        if len(set(suits)) == 1:
            return "Flush"
        elif mx >= 3:
            return "Three of a Kind"
        elif mx == 2:
            return "Pair"
        else:
            return "High Card"