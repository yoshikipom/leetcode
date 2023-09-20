#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        r1 = n//2 + n%2
        r2 = n//2
        for i in range(r1):
            for j in range(r2):
                # v1 = matrix[i][j]
                # v2 = matrix[j][n-1-i]
                # v3 = matrix[n-1-i][n-1-j]
                # v4 = matrix[n-1-j][i]
                # matrix[i][j] = v4
                # matrix[j][n-1-i] = v1
                # matrix[n-1-i][n-1-j] = v2
                # matrix[n-1-j][i] = v3
                # for row in matrix:
                    # print(*row)
                matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i]=matrix[n-1-j][i],matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j]
# @lc code=end
