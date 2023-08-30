#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ret = True
        for bit in bits[-2::-1]:
            if bit: ret = not ret
            else: break
        return ret
        
# @lc code=end
