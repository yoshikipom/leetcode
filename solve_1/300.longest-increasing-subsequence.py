#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        arr.append(nums[0])
        for num in nums:
            index = bisect.bisect_left(arr, num)
            if index == len(arr):
                arr.append(num)
            else:
                arr[index] = num
        return len(arr)
            
               
        
        
# @lc code=end
