#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = float('INF')
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(total - target) < abs(min_diff):
                    min_diff = total - target
                if total < target:
                    l += 1
                else:
                    r -= 1
                    
        return min_diff + target
        
# @lc code=end
