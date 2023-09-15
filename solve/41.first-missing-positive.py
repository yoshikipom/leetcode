#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums.count(1) == 0:
            return 1
        
        for i in range(len(nums)):
            if nums[i] <= 0 or len(nums) < nums[i]:
                nums[i] = 1
        
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            nums[idx] = -abs(nums[idx])
            
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        return len(nums)+1
        
        
# @lc code=end
