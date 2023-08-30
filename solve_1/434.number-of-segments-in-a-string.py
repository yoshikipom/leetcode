#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        after_space = True
        result = 0
        for c in s:
            if c != ' ' and after_space:
                result += 1
                after_space = False
            elif c == ' ':
                after_space = True
            
        return result
        
# @lc code=end
