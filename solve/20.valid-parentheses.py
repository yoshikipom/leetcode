#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        for c in s:
            if c in ('(','{','['):
                stack.append(c)
            else:
                if not stack or stack[-1] != d[c]:
                    return False
                else:
                    stack.pop()
        return not stack
        
# @lc code=end
