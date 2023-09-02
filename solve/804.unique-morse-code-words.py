#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start
import string
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = dict(zip(string.ascii_lowercase, range(26)))
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        for word in words:
            s.add(''.join(tuple(map(lambda c: morse[d[c]], word))))
        return len(s)
            
# @lc code=end
