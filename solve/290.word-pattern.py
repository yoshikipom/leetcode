#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        d = {}
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d and d[pattern[i]] != words[i]:
                return False
            d[pattern[i]] = words[i]
        return len(d) == len(set(d.values()))
        
# @lc code=end
