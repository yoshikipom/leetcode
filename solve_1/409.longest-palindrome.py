#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        c = Counter(s)
        for k, v in c.items():
            # print(k, v)
            result += (v // 2) * 2
            
        if not result == len(s) or len(s) == 1:
            result += 1
        return result
            
        
# @lc code=end
