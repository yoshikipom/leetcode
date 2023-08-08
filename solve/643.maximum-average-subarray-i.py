#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        tmp = total
        for i in range(k, len(nums)):
            tmp -= nums[i-k]
            tmp += nums[i]
            total = max(total, tmp)
        return total/k
            
        
# @lc code=end
