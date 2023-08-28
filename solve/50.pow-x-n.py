#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def _pow(x: float, n: int) -> float:
            if n == 1:
                return x
            if n % 2 == 0:
                return _pow(x*x, n//2)
            else:
                return x * _pow(x*x, (n-1)//2)        
        
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        return _pow(x, n)    
        
# @lc code=end
