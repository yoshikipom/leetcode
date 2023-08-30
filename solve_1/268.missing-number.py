#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        tmp = (l+1) * l // 2
        return  tmp - sum(nums)
            
        
# @lc code=end
