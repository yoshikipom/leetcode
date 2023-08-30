#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        def backtrack(arr: List[int], seen: Set[int]):
            if len(arr) == len(nums):
                self.result.append(arr[:])
            
            for i in range(len(nums)):
                if i in seen:
                    continue
                seen.add(i)
                arr.append(nums[i])
                backtrack(arr, seen)
                seen.discard(i)
                arr.pop()
        backtrack([], set())
        return self.result
            
        
# @lc code=end
