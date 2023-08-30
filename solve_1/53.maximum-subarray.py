#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from itertools import accumulate
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        result = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum+num)
            result = max(result, current_sum)
        return result
            
            
        
# @lc code=end
