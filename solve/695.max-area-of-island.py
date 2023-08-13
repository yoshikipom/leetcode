#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        done = set()
        for i in range(len(grid)):
            grid[i] = [0] + grid[i] + [0]
        grid = [[0]*len(grid[0])] + grid + [[0]*len(grid[0])]
        
        def calc_area(start_i: int, start_j: int):
            directions = [(-1, 0),(1, 0),(0, -1),(0, 1),]
            area = 0
            queue = deque()
            queue.appendleft((start_i, start_j))
            while queue:
                i, j = queue.pop()
                if grid[i][j] == 0 or (i, j) in done:
                    continue
                done.add((i,j))
                area += 1
                for di, dj in directions:
                    queue.appendleft((i+di, j+dj))
            return area
            
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 1:
                    result = max(result, calc_area(i, j))
        
        return result        
                
                
# @lc code=end
