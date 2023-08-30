#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start

directions = ((1,0),(-1,0),(0,1),(0,-1))
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h = len(grid)+2
        w = len(grid[0])+2
        perimiter = 0
        for i in range(len(grid)):
            grid[i] = [0] + grid[i] + [0]
        grid = [[0] * w] + grid + [[0] * w]
        # print(grid)
        
        for i in range(1, h-1):
            for j in range(1, w-1):
                if grid[i][j] == 0:
                    continue
                for dx, dy in directions:
                    if grid[i+dx][j+dy] == 0:
                        perimiter += 1
                        # print(i, j, dx, dy)
                        
        return perimiter
                    
                
                
        
        
# @lc code=end
