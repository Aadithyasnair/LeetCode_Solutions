"""
Problem ID : 0985
Title      : Sum of Even Numbers After Queries
Language   : Python
Solved Date: 2026-07-17
"""
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]):
        evenSum = 0
        for x in nums:
            if x % 2 == 0:
                evenSum += x
        ans = []
        for val, index in queries:
            if nums[index] % 2 == 0:
                evenSum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                evenSum += nums[index]
            ans.append(evenSum)
        return ans