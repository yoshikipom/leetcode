#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        result.append([1])
        if numRows == 1:
            return result
        result.append([1, 1])
        if numRows == 2:
            return result
        
        for i in range(3, numRows+1):
            tmp = [1]
            prev = result[-1]
            for j in range(1, len(prev)):
                tmp.append(prev[j-1] + prev[j])
            tmp.append(1)
            result.append(tmp)
        
        return result
        
        
# @lc code=end
