#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = map(lambda x: x[::-1], s.split())
        return ' '.join(arr)
        
        
# @lc code=end
