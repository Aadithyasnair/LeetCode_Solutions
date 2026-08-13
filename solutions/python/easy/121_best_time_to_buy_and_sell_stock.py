"""
Problem ID : 121
Title      : Best Time to Buy and Sell Stock
Language   : Python
Solved Date: 2026-08-13
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        for price in prices:
            low = min(low, price)
            profit = max(profit, price - low)
        return profit