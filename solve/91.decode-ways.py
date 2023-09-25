#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]== '0':
            return 0
        
        dp = [[0 for j in range(2)] for i in range(len(s))]
        
        # initial condition
        dp[0][1] = 1
        
        for i in range(len(s)-1):
            digit = s[i]
            next_digit = s[i+1]
            
            # x -> xy
            if 10<=int(digit+next_digit)<=26:
                dp[i+1][0] = dp[i][1]
                
            # xx -> xx,y or x -> x,y
            if next_digit != '0':
                dp[i+1][1] = dp[i][0] + dp[i][1]
        
        return sum(dp[-1])
        
# @lc code=end
