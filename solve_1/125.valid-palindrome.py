#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ''
        for c in s:
            if c.isalpha() or c.isdigit():
                tmp += c.lower()
        return tmp == tmp[::-1]
        
# @lc code=end
