#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        else:
            l = 0
            r = len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1]
                if nums[mid-1] > nums[mid]:
                    return nums[mid]
                
                if nums[0] < nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
# @lc code=end
