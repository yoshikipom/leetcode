#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
import collections
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        for a in nums:
            d[a] += 1
            
        result = 0
        for k in list(d.keys()):
            if d[k+1] == 0:
                continue
            result = max(result, d[k] + d[k+1])
        
        return result
        
# @lc code=end
