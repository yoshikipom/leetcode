#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] <= nums[-1]:
            idx = bisect.bisect_left(nums, target)
            if idx < len(nums) and target == nums[idx]:
                return idx
            else:
                return -1
        
        l = 1
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid-1] > nums[mid]:
                start = mid
                break
            if nums[mid] > nums[0]:
                l = mid+1
            else:
                r = mid-1
        
        # print(start)
        if target <= nums[-1]:
            idx = bisect.bisect_left(nums, target, lo=start, hi=len(nums)-1)
            if idx < len(nums) and target == nums[idx]:
                return idx
            else:
                return -1
        else:
            idx = bisect.bisect_left(nums, target, lo=0, hi=start-1)
            if idx < len(nums) and target == nums[idx]:
                return idx
            else:
                return -1
        
        
# @lc code=end
