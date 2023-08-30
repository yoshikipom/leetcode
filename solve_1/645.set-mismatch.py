#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        for a in nums:
            if a in s:
                duplicated = a
            s.add(a)
        
        for i in range(1, len(nums)+1):
            if i not in s:
                missing = i
        return [duplicated, missing]
# @lc code=end
