#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        tmp = 1
        for i in range(2, int(num**(1/2)) + 1):
            if num % i == 0:
                # print(i, num//i)
                tmp += i + num//i
        return num == tmp
        
# @lc code=end
