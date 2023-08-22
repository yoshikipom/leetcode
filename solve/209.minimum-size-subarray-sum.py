#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
import bisect
import itertools
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        A = [0]+list(itertools.accumulate(nums))
        if A[-1] < target:
            return 0
        
        result = len(nums)
        for l in range(len(A)):
            # for r in range(l+1, len(A)):
            #     if target <= A[r] - A[l]:                
            #         result = min(result, r-l)
            #         break
            r = bisect.bisect_left(A, target+A[l])
            if 0 <= r < len(A) and l < r:
                result = min(result, r-l)
        
        return result
        
# @lc code=end
