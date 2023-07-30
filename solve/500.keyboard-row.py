#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        
        result = []
        for word in words:
            tmp = word.lower()
            all_in_row1 = all([c in row1 for c in tmp])
            if all_in_row1:
                result.append(word)
                continue
            all_in_row2 = all([c in row2 for c in tmp])
            if all_in_row2:
                result.append(word)
                continue
            all_in_row3 = all([c in row3 for c in tmp])
            if all_in_row3:
                result.append(word)
                continue
                
        return result
                
        
        
# @lc code=end
