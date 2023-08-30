#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = list(set(nums))
        l.sort()
        if len(l) < 3:
            return l[-1]
        else:
            return l[-3]
    
        
# @lc code=end
