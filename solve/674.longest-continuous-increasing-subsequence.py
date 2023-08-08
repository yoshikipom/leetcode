#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        result = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                count += 1
                result = max(result, count)
            else:
                count = 1
        return result
                
            
            
            
            
        
# @lc code=end
