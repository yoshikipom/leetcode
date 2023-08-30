#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_is_zero = n % 2 == 0
        n //= 2
        while n:
            remainder = n % 2
            n //= 2
            if prev_is_zero and remainder == 0:
                return False
            if not prev_is_zero and remainder == 1:
                return False
            prev_is_zero = not prev_is_zero
        return True
            
        
# @lc code=end
