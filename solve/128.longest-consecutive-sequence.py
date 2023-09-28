#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List

# class UF:
#     def __init__(self, n: int):
#         self.parents = [-1 for i in range(n)]
#         self.len = n
#         self.group_size = [1 for i in range(n)]
        
#     def union(self, a: int, b: int):
#         a = self.find(a)
#         b = self.find(b)
#         if a == b:
#             return
#         a, b = min(a, b), max(a, b)
#         self.parents[b] = a
#         self.group_size[a] += self.group_size[b]
#         self.len -= 1

        
#     def find(self, a: int) -> int:
#         cur = a
#         while True:
#             if self.parents[cur] == -1:
#                 break
#             else:
#                 cur = self.parents[cur]
#         return cur

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # nums = list(set(nums))
        # d = {}
        # for i, num in enumerate(nums):
        #     d[num] = i
        
        # uf = UF(len(nums))
        # for i, num in enumerate(nums):
        #     # print(i, num, uf.parents)
        #     if num-1 in d:
        #         uf.union(d[num-1], i)
        # # print(uf.parents)
        # # print(nums)
        # # print(uf.group_size)
        # return max(uf.group_size)
        
        result = 0
        num_set = set(nums)
        for num in num_set:
            
            # start a streak only from minimum value in the sequence.
            if num-1 not in num_set:
                current_num = num
                current_streak = 0
                while current_num in num_set:
                    current_streak += 1
                    current_num += 1
                    
                result = max(result, current_streak)
                
        return result
                    
                
            
        
        
# @lc code=end
