#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from collections import deque
from typing import List


dirs = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0),
]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        can_remain = set()
        m = len(board)
        n = len(board[0])
        
        def search(i, j):
            if (i, j) in can_remain:
                return
            if board[i][j] == 'X':
                return
            
            q = deque()
            q.appendleft((i,j))
            while q:
                # print(q)
                ii, jj = q.pop()
                if (ii,jj) in can_remain:
                    continue
                can_remain.add((ii,jj))
                for di,dj in dirs:
                    if not 0<=ii+di<m or not 0<=jj+dj<n:
                        continue
                    if board[ii+di][jj+dj] == 'O':
                        q.appendleft((ii+di,jj+dj))
                        
        for j in range(n):
            search(0, j)
            search(m-1, j)
        for i in range(m):
            search(i, 0)
            search(i, n-1)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in can_remain:
                    board[i][j] = 'X'
        # print(can_remain)
                    
        
# @lc code=end
