#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        index = 0
        for op in operations:
            if op == '+':
                arr.append(arr[index-2] + arr[index-1])
            elif op =='D':
                arr.append(arr[index-1] * 2)
            elif op =='C':
                arr.pop()
            else:
                arr.append(int(op))
        return sum(arr)
                
        
# @lc code=end
