#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            if s[i] != s[j]:
                return False
            if i >= j:
                return True
            return check_palindrome(s, i+1, j-1)
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return check_palindrome(s, l+1, r) or check_palindrome(s, l, r-1)
        
        return True
            
            
            
            
        
# @lc code=end
