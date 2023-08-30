#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while True:
            mid = (l+r) // 2
            g = guess(mid)
            if g == -1:
                r = mid - 1
            elif g == 1:
                l = mid + 1
            else:
                return mid
# @lc code=end

def guess(num: int) -> int:
    pass
