#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        result = []
        
        def dfs(index:int, path:List[str]):
            if len(path) == len(digits):
                result.append(''.join(path))
                return
                
            for c in letters[digits[index]]:
                path.append(c)
                dfs(index+1, path)
                path.pop()
        
        dfs(0, [])
        return result
        
# @lc code=end
