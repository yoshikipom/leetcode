#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        prev = None
        for c in s:
            if prev != c:
                groups.append(0)
            groups[-1] += 1
            prev = c
            
        result = 0
        # print(groups)
        for i in range(1, len(groups)):
            result += min(groups[i-1], groups[i])
        
        return result
        
# @lc code=end
