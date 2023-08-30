#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
        
        result = []
        # print(nums)
        for i, num in enumerate(nums):
            if num > 0:
                result.append(i+1)
        return result
# @lc code=end
