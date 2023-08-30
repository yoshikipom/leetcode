#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for i in range(len(nums))]
        dp[0]=nums[0]
        dp[1]=max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        # print(dp)
        return max(dp[-1], dp[-2])
            
        
# @lc code=endA
