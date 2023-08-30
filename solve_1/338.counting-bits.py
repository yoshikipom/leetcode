#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)
        x = 0
        b = 1
        while b <= n:
            while x < b and x + b <= n:
                result[x+b] = result[x] + 1
                x+=1
            x = 0
            b <<= 1
            
        return result
            
        
# @lc code=end
