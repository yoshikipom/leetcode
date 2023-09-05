#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_val = float('inf')
        for price in prices:
            if min_val < price:
                result = max(result, price-min_val)
            min_val = min(min_val, price)
        return result
            
        
# @lc code=end
