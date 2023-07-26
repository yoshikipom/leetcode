#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start

import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ABC = string.ascii_uppercase
        result = ""
        while True:
            remain = columnNumber % 26
            result = ABC[remain-1] + result
            # print(columnNumber, columnNumber // 26)
            columnNumber = columnNumber // 26
            if remain == 0:
                columnNumber -= 1
            if columnNumber == 0:
                break
            
        return result
            
        
        
# @lc code=end
