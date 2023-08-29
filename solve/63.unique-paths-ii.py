#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])
        dp = [[0 for j in range(w)] for i in range(h)]
        dp[0][0] = 1 -  obstacleGrid[0][0]
        for i in range(h):
            for j in range(w):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    continue
                if j != 0:
                    from_left = dp[i][j-1]
                else:
                    from_left = 0
                if i != 0:
                    from_up = dp[i-1][j]
                else:
                    from_up = 0
                dp[i][j] = from_left + from_up
        # for row in dp:
            # print(*row)
        return dp[-1][-1]
        
# @lc code=end
