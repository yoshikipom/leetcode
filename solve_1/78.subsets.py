#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
import itertools
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        # for i in range(len(nums)+1):
        #     for c in list(itertools.combinations(nums,i)):
        #         result.append(list(c))
        # return result

        tmp_arr = []
        def backtrack(first:int):
            '''
            Add candidates to `result`
            '''
            if len(tmp_arr) == n:
                result.append(tmp_arr[:])    
                return
            
            for i in range(first, len(nums)):
                tmp_arr.append(nums[i])
                backtrack(i+1)
                tmp_arr.pop()
                
        for n in range(len(nums)+1):
            # print(n, tmp_arr)
            backtrack(0)
            # print(result)
        return result
        
        
        
# @lc code=end
