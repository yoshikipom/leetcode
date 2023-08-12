#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
from itertools import accumulate
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a = list(accumulate(nums))
        b = list(accumulate(nums[::-1]))
        
        if len(nums) == 1:
            return 0
        if b[-2] == 0:
            return 0
        
        for i in range(1, len(nums)-1):
            # a_num + b_num + 1 = len(nums)
            # b_num = len(nums) - 1 - a_num(i+1)
            # print(i-1, len(nums)-1-i-1)
            if a[i-1] == b[len(nums)-1-i-1]:
                return i
 
        if a[-2] == 0:
            return len(nums) - 1
        
        return -1
            
                
            
        
            
        
# @lc code=end
