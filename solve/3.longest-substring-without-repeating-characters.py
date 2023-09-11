#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        r = 0
        result = 0
        
        while r < len(s):
            if s[r] in d and l <= d[s[r]]:
                # duplicated
                l = d[s[r]]+1
                d.pop(s[r])
                continue
            
            result = max(result, r-l+1)
            # print(l, r, result, d)
            d[s[r]] = r
            r += 1
            
        return result

        
# @lc code=end
