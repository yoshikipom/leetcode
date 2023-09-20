#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable_max = 0
        for i in range(len(nums)-1):
            if i <= reachable_max:
                reachable_max = max(reachable_max, i+nums[i])
            else:
                return False
        
        return len(nums) - 1 <= reachable_max
            
                
            
            
        
        
# @lc code=end
