#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        def backtrack(arr: List[int], total: int, last_index: int):
            # print(arr, total)
            if total == target:
                self.result.append(arr[:])
                return
            if total > target:
                return
            for i in range(last_index, len(candidates)):
                num = candidates[i]
                arr.append(num)
                backtrack(arr, total+num, i)
                arr.pop()
        backtrack([], 0, 0)
        return self.result
        
# @lc code=end
