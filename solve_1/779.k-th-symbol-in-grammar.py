#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
import math
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0 -> 01, 1 -> 10
        # 0
        # 01
        # 0110
        # 0110 1001 (A B)
        # 0110 1001 1001 0110 (A B B A)
        # 0110 1001 1001 0110 1001 0110 0110 1001 (A B B A B A A B)
        # (A B B A B A A B B A A B A B B A)
        # length of n row will be 2^n
        
        if n == 1:
            return 0

        tmp = self.kthGrammar(n-1, (k+1)//2)
        if tmp == 0:
            return 1 - k%2
        else:
            return k%2
        
# @lc code=end
