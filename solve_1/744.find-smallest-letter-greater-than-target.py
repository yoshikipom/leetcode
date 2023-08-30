#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        less_or_equal = -1
        greater = len(letters)
        while greater - less_or_equal > 1:
            mid = (less_or_equal + greater) // 2
            if letters[mid] <= target:
                less_or_equal = mid
            else:
                greater = mid
        if greater == len(letters):
            return letters[0]
        else:
            return letters[greater]
        
# @lc code=end
