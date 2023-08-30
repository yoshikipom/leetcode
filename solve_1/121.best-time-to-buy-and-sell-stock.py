#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        for price in prices[1:]:
            low = min(low, price)
            profit = max(profit, price - low)
        return profit
            
        
# @lc code=end
