#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        for word in s.split(sep=' '):
            if word == '':
                continue
            result = len(word)
        return result
        
# @lc code=end
