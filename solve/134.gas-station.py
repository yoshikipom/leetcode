#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
from itertools import accumulate
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        arr = []
        for i in range(n):
            arr.append(gas[i] - cost[i])
            
        # print(arr)
        
        if sum(arr) < 0:
            return -1
        
        val = 0
        min_val = float('inf')
        for i in range(n):
            val += arr[i]
            min_val = min(min_val, val)
        
        if 0 <= min_val:
            return 0
        
        for start in range(1, n):
            min_val -= arr[start-1]
            if 0 <= min_val:
                return start
        
        return -1
            
        
        
# @lc code=end
