#
# @lc app=leetcode id=812 lang=python3
#
# [812] Largest Triangle Area
#

# @lc code=start
from typing import List

https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        result = 0
        for i in range(n):
            a = points[i]
            for j in range(i+1, n):
                b = points[j]
                for k in range(j+1, n):
                    c = points[k]
                    area = 1/2 * abs(a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1]))
                    result = max(result, area)
        return result
                    
        
        
# @lc code=end
