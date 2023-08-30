#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        target = n
        while target not in history:
            if target == 1:
                return True
            history.add(target)
            tmp = 0
            for c in str(target):
                tmp += int(c) ** 2
            target = tmp
        return False
        
# @lc code=end
