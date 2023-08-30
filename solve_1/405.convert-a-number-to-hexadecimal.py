#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        
        if num < 0:
            num = 2 ** 32 + num
        
        chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        result = ''
        while num != 0:
            remainder = num % 16
            result = chars[remainder] + result
            num //= 16
        return result
        
# @lc code=end
