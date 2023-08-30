#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         d = dict()
#         for c in magazine:
#             if c not in d:
#                 d[c] = 0
#             d[c] += 1
        
#         for c in ransomNote:
#             if c not in d or d[c] == 0:
#                 return False
#             d[c] -= 1
#         return True
    
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        print(c1)
        print(c2)
        print(c1&c2)
        return c1 & c2 == c1
            
        

# @lc code=end
