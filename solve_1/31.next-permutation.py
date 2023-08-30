#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        increase_point = len(nums) -2
        while 0 <= increase_point:
            if nums[increase_point] < nums[increase_point+1]:
                break
            increase_point -= 1
        else:
            l = 0
            r = len(nums) - 1
            while l<r:
                nums[l], nums[r] = nums[r], nums[l] 
                l+=1
                r-=1
            return 
        
        cur = len(nums) -1
        while True:
            if nums[increase_point] < nums[cur]:
                break
            cur-=1
        nums[increase_point], nums[cur] = nums[cur], nums[increase_point]
        l = increase_point+1
        r = len(nums) - 1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l] 
            l+=1
            r-=1
        
            
            
        
# @lc code=end
