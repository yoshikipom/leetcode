#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        expanded = []
        for row in mat:
            for a in row:
                expanded.append(a)
        if len(expanded) != r * c:
            return mat
        
        result = [[None for j in range(c)] for i in range(r)]
        for i, a in enumerate(expanded):
            row = i // c
            colmun = i % c
            result[row][colmun] = a
        return result
        
# @lc code=end
