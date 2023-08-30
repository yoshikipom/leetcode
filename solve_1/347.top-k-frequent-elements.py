#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        t = []
        for val, count in c.items():
            t.append((-count, val))
        # t.sort(reverse=True)
            
        # result = []
        # for i in range(k):
        #     result.append(t[i][1])
        # return result
        
        heapq.heapify(t)
        result = []
        for i in range(k):
            count, val = heapq.heappop(t)
            result.append(val)
        return result
        
        
# @lc code=end
