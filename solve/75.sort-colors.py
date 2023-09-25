#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt = 0
        non_two_cnt = 0
        for i in range(len(nums)):
            # print(nums[:i], zero_cnt, non_two_cnt)
            num = nums[i]
            if num == 0:
                nums[zero_cnt], nums[i] = nums[i], nums[zero_cnt]
                if nums[i] == 1:
                    nums[non_two_cnt], nums[i] = nums[i], nums[non_two_cnt]
                zero_cnt += 1
                non_two_cnt += 1
            elif num == 1:
                nums[non_two_cnt], nums[i] = nums[i], nums[non_two_cnt]
                non_two_cnt += 1
            else:
                continue

        # print(nums, zero_cnt, non_two_cnt)
                
            
        
# @lc code=end
