#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        dp = [INF for j in range(amount+1)]
        dp[0] = 0
        for i in range(len(coins)):
            val = coins[i]
            for j in range(val, amount+1):
                dp[j] = min(dp[j], dp[j-val]+1)
        return dp[-1] if dp[-1] != INF else -1
                
        
# @lc code=end
