#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#

# @lc code=start
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        consumed = 0
        line = 1
        for c in s:
            c_index = ord(c)-ord('a')
            c_len = widths[c_index]
            if 100 < consumed + c_len:
                line += 1
                consumed = c_len
            else:
                consumed += c_len
        return [line, consumed]
        
# @lc code=end
