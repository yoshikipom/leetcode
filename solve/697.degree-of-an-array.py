#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_val = []
        max_frequency = max(c.values())
        for k, v in c.items():
            if v == max_frequency:
                max_val.append(k)
        
        # print(max_val)
        
        result = len(nums)
        for val in max_val:
            l = 0
            while True:
                if nums[l] == val:
                    break
                l+=1 
            r = len(nums) - 1
            while True:
                if nums[r] == val:
                    break
                r-=1
            result = min(result, r-l+1)
        
        return result
        
# @lc code=end
