#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List

class UF:
    def __init__(self, n: int):
        self.parents = [-1 for i in range(n)]
        self.len = n
        self.group_size = [1 for i in range(n)]
        
    def union(self, a: int, b: int):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        a, b = min(a, b), max(a, b)
        self.parents[b] = a
        self.group_size[a] += self.group_size[b]
        self.len -= 1

        
    def find(self, a: int) -> int:
        cur = a
        while True:
            if self.parents[cur] == -1:
                break
            else:
                cur = self.parents[cur]
        return cur

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                continue
            d[num] = i
        
        uf = UF(len(nums))
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                continue
            seen.add(num)
            # print(i, num, uf.parents)
            if num-1 in d:
                uf.union(d[num-1], i)
        # print(uf.parents)
        # print(nums)
        # print(uf.group_size)
        return max(uf.group_size)
            
        
        
# @lc code=end
