#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower():
            return True
        if word.isupper():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False
        
# @lc code=end
