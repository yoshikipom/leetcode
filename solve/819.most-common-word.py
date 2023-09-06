#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
from collections import defaultdict
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = set(banned)
        d = defaultdict(int)
        pattern = r'[^a-zA-Z]'
        for word in re.split(pattern, paragraph):
            if not word:
                continue
            word = word.lower()
            if word not in s:
                d[word] += 1
                
        result = None
        max_count = 0
        for k, v in d.items():
            if max_count < v:
                max_count = v
                result = k
        return result
            
        
# @lc code=end
