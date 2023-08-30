#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
import bisect
from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        A = list(accumulate([0]+nums))
        result = 0
        # print(A)
        d = defaultdict(int)
        for i, num in enumerate(A):
            if num - k in d:
                result += d[num - k]
            d[num] += 1
            
        return result
                    
        
        
# @lc code=end
