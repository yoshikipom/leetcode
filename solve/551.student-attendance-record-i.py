#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        a_cnt = 0
        l_cnt = 0
        for c in s:
            if c == 'L':
                l_cnt += 1
                if 3 <= l_cnt:
                    return False
                continue
            else:
                l_cnt = 0
                
            if c == 'P':
                continue
            
            if c == 'A':
                a_cnt += 1
                if 2 <= a_cnt:
                    return False
            else:
                raise Exception("input is invalid")
        return True
                
            
        
# @lc code=end
