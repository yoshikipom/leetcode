#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        check_row = matrix[0]
        for i in range(1, min(len(matrix), len(matrix[0]))):
            for j in range(len(matrix[0])-i):
                if matrix[i][i+j] != check_row[j]:
                    return False
        check_colmn = [matrix[i][0] for i in range(len(matrix))]
        for i in range(1, min(len(matrix), len(matrix[0]))):
            for j in range(len(matrix)-i):
                if matrix[i+j][i] != check_colmn[j]:
                    return False
        return True
            
        
# @lc code=end
