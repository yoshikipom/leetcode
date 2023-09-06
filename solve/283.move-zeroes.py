#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[last_non_zero], nums[cur] = nums[cur], nums[last_non_zero]
                last_non_zero += 1
            
        
# @lc code=end
