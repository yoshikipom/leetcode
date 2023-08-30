#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        s = s.replace('-', '')
        remainder = len(s) % k
        arr = []
        if remainder != 0:
            arr.append(s[:remainder])
        for i in range(len(s)//k):
            arr.append(s[remainder+i*k:remainder+(i+1)*k])
            
        return '-'.join(arr)
            
        
        
# @lc code=end
