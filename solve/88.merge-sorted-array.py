#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur1 = m - 1
        cur2 = n - 1
        insert_cur = m + n - 1
        while 0 <= insert_cur:
            if cur1 < 0:
                value = nums2[cur2]
                cur2 -= 1
            elif cur2 < 0:
                value = nums1[cur1]
                cur1 -= 1
            elif nums1[cur1] < nums2[cur2]:
                value = nums2[cur2]
                cur2 -= 1
            else:
                value = nums1[cur1]
                cur1 -= 1
            nums1[insert_cur] = value
            insert_cur -= 1
            


# @lc code=end
