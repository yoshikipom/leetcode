#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_cur = 0
        for i, num in enumerate(nums):
            if num == 0:
                continue
            nums[write_cur] = num
            write_cur += 1
        for i in range(write_cur, len(nums)):
            nums[write_cur] = 0
            write_cur += 1
            
            
        
# @lc code=end
