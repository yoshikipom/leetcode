#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
import bisect


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        d = dict()
        for i, c in enumerate(t):
            if c not in d:
                d[c] = []
            d[c].append(i)
        
        cur = 0
        for i, c in enumerate(s):
            if c not in d:
                return False
            arr = d[c]
            index = bisect.bisect_left(arr, cur)
            if index >= len(arr):
                return False
            cur = arr[index] + 1
        return True
        
# @lc code=end
