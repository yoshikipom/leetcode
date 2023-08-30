#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while True:
            if n <= 0:
                return False
            if n == 1:
                return True
            if n % 2 != 0:
                return False
            n //= 2
            
        
# @lc code=end
