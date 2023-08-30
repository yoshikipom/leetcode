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
            if num in d:
                if num * 2 == target:
                    return [d[num], i]
                else:
                    continue
            else:
                d[num] = i
        
        for i, num in enumerate(nums):
            if target - num in d and d[target-num]!=i:
                return [d[target-num], i]
        
        raise Exception("shouldn't reach here")
        
            
        
# @lc code=end
