#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        negative = False
        if num < 0:
            negative = True
            num = num * (-1)
        result = ''
        while num != 0:
            result += str(num % 7)
            num //= 7
        if negative:
            return '-' + result[::-1]
        else:
            return result[::-1]
            
        
# @lc code=end
