#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score: List[int] = sorted(score)
        
        rank_str = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + [f'{x}' for x in range(4, len(score)+1)]
        
        output = []
        for num in score:
            index = bisect.bisect_left(sorted_score, num)
            rank = len(score) - 1 - index # 0-indexed
            # print(rank)
            output.append(rank_str[rank])
        return output

        
# @lc code=end
