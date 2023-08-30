#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        b = 0
        for c in s:
            b ^= ord(c)
        for c in t:
            b ^= ord(c)
        return chr(b)
        
# @lc code=end
