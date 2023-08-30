#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        index = nums.index(m)
        nums.pop(index)
        
        for num in nums:
            if m < num * 2:
                return -1
            
        return index
        
# @lc code=end
