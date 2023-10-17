#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums)-1)

    def search(self, nums, l, r):
        if l == r:
            return l
        mid = (l+r)//2
        if nums[mid] > nums[mid+1]:
            return self.search(nums, l, mid)
        else:
            return self.search(nums, mid+1, r)
# @lc code=end
