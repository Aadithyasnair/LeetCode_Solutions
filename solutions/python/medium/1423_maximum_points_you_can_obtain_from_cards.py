"""
Problem ID : 1423
Title      : Maximum Points You Can Obtain from Cards
Language   : Python
Solved Date: 2026-07-23
"""
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        total = sum(cardPoints)
        window = sum(cardPoints[:n-k])
        ans = window

        for i in range(n-k, n):
            window += cardPoints[i] - cardPoints[i-(n-k)]
            ans = min(ans, window)

        return total - ans