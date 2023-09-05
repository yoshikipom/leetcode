#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1 # less than target
        r = len(nums) # greater than or equal to target
        while r - l > 1:
            mid = (l+r)//2
            if target <= nums[mid]:
                r = mid
            else:
                l = mid
        return r
            
        
# @lc code=end
