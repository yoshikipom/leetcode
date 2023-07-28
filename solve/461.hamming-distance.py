#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        bx = bin(x)[2:]
        by = bin(y)[2:]
        l = max(len(bx), len(by))
        bx = bx.zfill(l)[::-1]
        by = by.zfill(l)[::-1]
        # print(bx, by)
        for i in range(l):
            if bx[i] != by[i]:
                result += 1
        return result
            
        
# @lc code=end
