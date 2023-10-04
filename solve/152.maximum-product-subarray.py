#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List


class Solution:
    
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]
        max_val = nums[0]
        min_val = nums[0]
        
        for num in nums[1:]:
            max_val, min_val = max([num, num*max_val, num*min_val]), min([num, num*max_val, num*min_val])
            result = max(result, max_val)
        
        return result
                
        
# @lc code=end
