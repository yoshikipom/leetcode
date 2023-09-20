#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cur = (0,0)
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        dir_index = 0
        result = []
        seen = set()
        seen.add((0,0))
        while True:
            i,j = cur
            dx,dy = dirs[dir_index]
            result.append(matrix[i][j])
            if (i+dx, j+dy) in seen or not 0 <=i+dx<len(matrix) or not 0 <=j+dy<len(matrix[0]):
                dir_index = (dir_index+1) % 4
                dx,dy = dirs[dir_index]
                if (i+dx,j+dy) in seen or not 0 <=i+dx<len(matrix) or not 0 <=j+dy<len(matrix[0]):
                    return result
            seen.add((i+dx, j+dy))
            cur = (i+dx, j+dy)
            
# @lc code=end
