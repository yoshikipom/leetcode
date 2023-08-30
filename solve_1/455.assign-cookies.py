#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_cur = 0
        cookie_cur = 0
        result = 0
        while child_cur < len(g) and cookie_cur < len(s):
            if g[child_cur] <= s[cookie_cur]:
                result += 1
                child_cur += 1
                cookie_cur += 1
                continue
            else:
                cookie_cur += 1
        return result
                
            
        
            
# @lc code=end
