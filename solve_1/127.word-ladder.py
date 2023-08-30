#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i]+"*"+word[i+1:]].append(word)
                
        queue = deque()
        queue.appendleft((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        
        while queue:
            current_word, level = queue.pop()
            for i in range(L):
                mid_word = current_word[:i]+'*'+current_word[i+1:]
                for word in all_combo_dict[mid_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.appendleft((word, level+1))
            all_combo_dict[mid_word] = []
        return 0
        
        
        
# @lc code=end
