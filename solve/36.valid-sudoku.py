#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for i in range(9):
            s = set()
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in s:
                    # print(s, num)
                    # print('row')
                    return False
                s.add(num)
        
        
        # colmn
        for j in range(9):
            s = set()
            for i in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in s:
                    # print('colmun')
                    return False
                s.add(num)
        
        
        # box
        base = [
            (0, 0), (0, 3), (0,6),
            (3, 0), (3, 3), (3,6),
            (6, 0), (6, 3), (6,6),
        ]
        for base_i, base_j in base:
            s = set()
            for di in range(3):
                for dj in range(3):
                    num = board[base_i+di][base_j+dj]
                    if num == '.':
                        continue
                    if num in s:
                        # print('box')
                        return False
                    s.add(num)
        
        return True
        
# @lc code=end
