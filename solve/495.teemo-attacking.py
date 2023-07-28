#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        if len(timeSeries) == 1:
            return duration
        
        result = duration
        for i in range(len(timeSeries)-1)[::-1]:
            result += min(duration, timeSeries[i+1] - timeSeries[i])
        return result
            
            
        
# @lc code=end
