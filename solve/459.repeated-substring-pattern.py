#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        substrs = []
        for i in range(1,len(s)//2+1):
            substrs.append(s[:i])
        # print(substrs)
        for substr in substrs:
            if len(s) % len(substr) != 0:
                continue
            if substr * (len(s)//len(substr)) == s:
                return True
        return False
        
# @lc code=end
