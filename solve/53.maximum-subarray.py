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
        A = [0] + list(accumulate(nums))
        min_val = 0
        result = max(nums)
        for a in A[1:]:
            result = max(result, a - min_val)
            min_val = min(min_val, a)
        return result
            
            
        
# @lc code=end
