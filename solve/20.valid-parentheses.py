#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
dict = {
    '(': ')',
    '{': '}',
    '[': ']',
}
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                if not stack:
                    return False
                if dict[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0


# @lc code=end
