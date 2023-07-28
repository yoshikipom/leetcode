#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        comp = 1
        for i in range(31):
            if comp *2 <= num:
                comp *= 2
        return (comp*2-1) ^ num
        
# @lc code=end
