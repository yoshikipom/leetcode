#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        num_of_ilands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0' or (i, j) in seen:
                    continue
                
                num_of_ilands += 1
                queue = deque()
                queue.appendleft((i, j))
                seen.add((i, j))
                while queue:
                    cur_i, cur_j = queue.pop()
                    for di, dj in directions:
                        new_i = cur_i+di
                        new_j = cur_j+dj
                        if not 0<=new_i<len(grid) or not 0<=new_j<len(grid[0]):
                            continue
                        if (new_i, new_j) in seen:
                            continue
                        if grid[new_i][new_j] == '0':
                            continue
                        queue.appendleft((new_i, new_j))
                        seen.add((new_i, new_j))
        return num_of_ilands

                    
# @lc code=end
