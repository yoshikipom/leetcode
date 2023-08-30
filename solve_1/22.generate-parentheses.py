#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        m = n*2
        def backtrack(arr: List[str], left_cnt: int, right_cnt:int):
            if len(arr) == m:
                self.result.append(''.join(arr))
                return
            if left_cnt < n:
                arr.append('(')
                backtrack(arr, left_cnt+1, right_cnt)
                arr.pop()
            if left_cnt > right_cnt:
                arr.append(')')
                backtrack(arr, left_cnt, right_cnt+1)
                arr.pop()
        backtrack([], 0, 0)
        return self.result
                

    
    # def generateParenthesis(self, n: int) -> List[str]:
    #     result = []
    #     m = n * 2
    #     for bit in range(1<<m):
    #         if bin(bit).count('1') != n:
    #             continue
    #         if not self.is_acceptable(bit, m):
    #             continue
    #         result.append(self.to_parentheses(bit, m))
    #     return result
    
    # def is_acceptable(self, bit: int, n: int)-> bool:
    #     # print(bit, n)
    #     stack = []
    #     for i in range(n):
    #         # print(stack)
    #         if bit>>i & 1:
    #             # case for ')'
    #             if not stack:
    #                 return False
    #             else:
    #                 stack.pop()
    #         else:
    #             # case for '('
    #             stack.append(i)
                
    #     # print('result stack: ', stack)
        
    #     if stack:
    #         return False
    #     else:
    #         return True
    
    # def to_parentheses(self, bit: int, n: int)-> str:
    #     str = ''
    #     for i in range(n):
    #         if bit>>i & 1:
    #             str += ')'
    #         else:
    #             str += '('
    #     return str
                
        
# @lc code=end
