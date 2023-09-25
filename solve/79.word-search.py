#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from collections import deque
from typing import List, Set


dirs = [
        (0,1),
        (1,0),
        (0,-1),
        (-1,0),
        ]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.word = word
        for i in range(self.m):
            for j in range(self.n):
                s = set()
                s.add((i, j))
                if self.board[i][j] != word[0]:
                    continue
                if self.dfs(i, j, 0, s):
                    return True
        return False
                        
    
    def dfs(self, i, j, index, s:Set) -> bool:
        if len(s) == len(self.word):
            return True
        result = False
        for di, dj in dirs:
            next_i = i + di
            next_j = j + dj
            next_index = index + 1
            if next_i < 0 or self.m <= next_i or next_j < 0 or self.n <= next_j:
                continue
            if (next_i, next_j) in s:
                continue
            if self.board[next_i][next_j] == self.word[next_index]:
                s.add((next_i, next_j))
                result = self.dfs(next_i, next_j, next_index, s)
                s.remove((next_i, next_j))
                if result:
                    break
        return result
        
        
        
            
            
        
        
        
# @lc code=end
