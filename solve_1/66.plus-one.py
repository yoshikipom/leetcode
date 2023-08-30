#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry_flag = True
        for i in range(len(digits))[::-1]:
            digit = digits[i]
            if carry_flag:
                if digits[i] == 9:
                    digit = 0
                    carry_flag = True
                else:
                    digit = digits[i] + 1
                    carry_flag = False
            else:
                digit = digits[i]
            result.append(digit)
        if carry_flag:
            result.append(1)
        return result[::-1]
        
# @lc code=end
