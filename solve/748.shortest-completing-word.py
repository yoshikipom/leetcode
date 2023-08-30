#
# @lc app=leetcode id=748 lang=python3
#
# [748] Shortest Completing Word
#

# @lc code=start
import collections
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        self.d = collections.defaultdict(int)
        licensePlate = licensePlate.lower()
        for c in licensePlate:
            if c.isalpha():
                self.d[c] += 1
               
        result = None 
        for word in words:
            if self.is_acceptable(word):
                if not result:
                    result = word
                else:
                    if len(word) < len(result):
                        result = word
        return result

    def is_acceptable(self, word):
        word = word.lower()
        word_d = collections.defaultdict(int)
        for c in word:
            word_d[c] +=1
        for k, v in self.d.items():
            if k not in word_d:
                return False
            if word_d[k] < v:
                return False
        return True
        
# @lc code=end
