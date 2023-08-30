#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
import collections
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        c = collections.Counter(candyType)
        return min(len(c), len(candyType)//2)
        
# @lc code=end
