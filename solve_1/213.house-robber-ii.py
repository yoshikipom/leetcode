#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        
        nums1 = nums[:-1]
        nums2 = nums[1:]
        
        def max_rob(nums: List[int])->int:
            dp = [0 for i in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            return dp[-1]
        
        return max(max_rob(nums1), max_rob(nums2))
            
        
# @lc code=end
