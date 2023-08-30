#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        kk = 2*k
        for i in range(len(s)//kk+1):
            target = s[i*kk:(i+1)*kk]
            result += target[:k][::-1] + target[k:]
        return result
            
        
# @lc code=end
