#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        current = 0
        for a in nums:
            if a == 1:
                current += 1
                result = max(result, current)
            else:
                current = 0
        return result
        
# @lc code=end
