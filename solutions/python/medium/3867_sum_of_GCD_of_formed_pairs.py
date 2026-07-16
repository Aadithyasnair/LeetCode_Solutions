"""
Problem ID : 3867
Title      : Sum of GCD of Formed Pairs
Language   : Python
Solved Date: 2026-07-16
"""
import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd=[]
        mx=0
        for x in nums:
            mx=max(mx,x)
            prefixGcd.append(math.gcd(x,mx))
        prefixGcd.sort()
        left=0
        right=len(prefixGcd)-1
        ans=0
        while left<right:
            ans+=math.gcd(prefixGcd[left],prefixGcd[right])
            left+=1
            right-=1
        return ans