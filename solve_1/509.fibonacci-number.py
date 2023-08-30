#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
import functools


class Solution:
    def fib(self, n: int) -> int:
        @functools.cache
        def f(i):
            if i == 0:
                result = 0
            elif i == 1:
                result = 1
            else:
                result = f(i-2) + f(i-1)
            return result
        return f(n)
        
# @lc code=end
