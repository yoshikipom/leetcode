#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        for i, word in enumerate(list1):
            d[word] = i
            
        result = []
        min_index_sum = len(list1) + len(list2)
        for j, word in enumerate(list2):
            if word not in d:
                continue
            index_sum = d[word] + j
            if index_sum < min_index_sum:
                min_index_sum = index_sum
                result = [word]
            elif index_sum == min_index_sum:
                result.append(word)
                
            
        return result
            
        
# @lc code=end
