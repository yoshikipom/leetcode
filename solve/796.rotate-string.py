#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # for shift in range(len(s)):
        #     for i in range(len(s)):
        #         if s[(shift+i)%len(s)] != goal[i]:
        #             break
        #     else:
        #         return True
        # return False
        return s in goal+goal
                    
# @lc code=end
