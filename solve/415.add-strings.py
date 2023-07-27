#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_l = max(len(num1), len(num2))
        num1=num1.zfill(max_l)
        num2=num2.zfill(max_l)
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        carry = 0
        result = ''
        for i in range(max_l):
            total = int(num1[i]) + int(num2[i]) + carry
            result += str(total % 10)
            carry = total // 10
        
        if carry:
            result += str(carry)
        
        return result[::-1]
        
# @lc code=end
