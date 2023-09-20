#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        INF = float('inf')
        for i in range(len(matrix)):
            row = matrix[i]
            if 0 in row:
                for j in range(len(row)):
                    if row[j] != 0:
                        row[j] -= INF
        
        for j in range(len(matrix[0])):
            has_zero = False
            for i in range(len(matrix)):
                if matrix[i][j] == 0:
                    has_zero = True
                    break
            if has_zero:
                for i in range(len(matrix)):
                    if matrix[i][j] != 0:
                        matrix[i][j] -= INF
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] <= -INF:
                    matrix[i][j] = 0

                
            
        
        
# @lc code=end
