#
# @lc app=leetcode id=598 lang=python3
#
# [598] Range Addition II
#

# @lc code=start
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_a = m
        min_b = n
        for a, b in ops:
            min_a = min(a, min_a)
            min_b = min(b, min_b)
        return min_a * min_b
 
        
        
# @lc code=end
