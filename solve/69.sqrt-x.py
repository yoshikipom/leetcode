#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start

def f(x):
    return x * x

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = 2 ** 31
        while low <= high:
            mid = (low + high) // 2
            if x < f(mid):
                high = mid - 1
            elif x == mid:
                return mid
            else:
                low = mid + 1
        return min(low, high)
                
        
# @lc code=end
