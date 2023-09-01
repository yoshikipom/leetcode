#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set()
        for c in jewels:
            s.add(c)
        result = 0
        for c in stones:
            if c in s:
                result += 1
        return result
            
        
# @lc code=end
