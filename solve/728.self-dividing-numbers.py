#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right+1):
            possible = True
            if '0' in str(num):
                continue
            for c in str(num):
                digit = int(c)
                if num % digit != 0:
                    possible = False
            if possible:
                result.append(num)
        return result
                
        
# @lc code=end
