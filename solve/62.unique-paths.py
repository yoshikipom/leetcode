#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
from functools import cache
import sys


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        sys.setrecursionlimit(1000)
        l = 1
        #(m+n)C(m)
        @cache
        def factorial(a:int)->int:
            
            if a==0 or a==1:
                return 1
            return a * factorial(a-1)
        return factorial(m-1+n-1)//(factorial(m-1)*factorial(n-1))
# @lc code=end
