#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        target_color = image[sr][sc]
        if color == target_color:
            return image
        
        def dfs(i, j):
            if i < 0 or r <= i or j < 0 or c <= j:
                return
            if image[i][j] == target_color:
                image[i][j] = color
                for di, dj in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
                    dfs(i+di, j+dj)
        
        dfs(sr, sc)
        return image
        
        
# @lc code=end
