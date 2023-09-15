#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        # l_index = bisect.bisect_left(nums, target)
        # r_index = bisect.bisect_right(nums, target)
        
        less = -1
        eq_or_greater = len(nums)
        while eq_or_greater - less > 1:
            mid = (less+eq_or_greater)//2
            if nums[mid] < target:
                less = mid
            else:
                eq_or_greater = mid
        l_index = eq_or_greater          
        
        less_or_eq = -1
        greater = len(nums)
        while greater - less_or_eq > 1:
            mid = (less_or_eq+greater)//2
            if nums[mid] <= target:
                less_or_eq = mid
            else:
                greater = mid
        r_index = greater    
        
        
        if l_index < len(nums) and nums[l_index] == target:
            return l_index, r_index-1
        else:
            return -1, -1
        
        
        
# @lc code=end
