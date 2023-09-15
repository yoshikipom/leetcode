#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)
        count = 0
        digit = s[0]
        result = ''
        for c in s:
            if digit != c:
                result += str(count)+digit
                count = 0
                digit = c
            count += 1
        if count:
            result += str(count)+digit
        return result
        
            
        
# @lc code=end
