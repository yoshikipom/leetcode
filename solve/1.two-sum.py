#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            d[num] = i
        for i, num in enumerate(nums):
            if target - num in d:
                if i == d[target-num]:
                    continue
                return i, d[target-num]
        raise Exception("result was not found")
        
# @lc code=end
