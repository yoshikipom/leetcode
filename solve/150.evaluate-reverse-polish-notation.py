#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
import math
from typing import List


class Solution:
    def isnum(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
            
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isnum(token):
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                elif token == '/':
                    stack.append(math.trunc(a/b))
                else:
                    raise Exception(f'unknown token {token}')
        return stack.pop()
        
# @lc code=end
