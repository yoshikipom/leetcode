#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
import string


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 0
        result = 0
        ABC = string.ascii_uppercase
        d = {}
        for i, abc in enumerate(ABC):
            d[abc] = i+1
        for c in columnTitle[::-1]:
            result += d[c] * (26 ** base)
            base += 1
            
        return result
            
            
        
# @lc code=end
