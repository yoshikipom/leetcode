#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current_list = []
        n = len(s)
        def backtrack(start):
            # print(start, current_list)
            if start == n:
                result.append(current_list[:])
                return
            for end in range(start+1, n+1):
                word = s[start:end]
                if word == word[::-1]:
                    current_list.append(word)
                    backtrack(end)
                    current_list.pop()
                    
        backtrack(0)
        return result
     
                    
                    
        
# @lc code=end
