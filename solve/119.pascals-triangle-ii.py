#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex+1
        if numRows == 1:
            return [1]
        if numRows == 2:
            return [1,1]
        result = [1,1]
        for i in range(3, numRows+1):
            prev = result[0]
            for j in range(1, len(result)):
                tmp = result[j]
                result[j] = (prev + result[j])
                prev = tmp
            result.append(1)
        
        return result
        
# @lc code=end
