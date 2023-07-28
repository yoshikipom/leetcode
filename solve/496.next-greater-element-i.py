#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return []
        d = defaultdict(lambda: -1)
        stack = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                popped = stack.pop()
                d[popped] = nums2[i]
            
            stack.append(nums2[i])
        
        result = []
        for a in nums1:
            result.append(d[a])
        return result
            
        
# @lc code=end
