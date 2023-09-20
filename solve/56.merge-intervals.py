#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []
        result.append(intervals[0])
        for start, end in intervals[1:]:
            prev_start, prev_end = result[-1]
            if start <= prev_end:
                result[-1][1] = max(prev_end, end)
            else:
                result.append([start,end])
        return result
        
# @lc code=end
