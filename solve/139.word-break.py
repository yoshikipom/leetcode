#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     word_set = set(wordDict)
    #     q = deque()
    #     q.appendleft(0)
    #     seen = set()
        
    #     while q:
    #         start = q.pop()
    #         if start == len(s):
    #             return True
    #         for end in range(start+1, len(s)+1):
    #             if end in seen:
    #                 continue
    #             if s[start:end] in word_set:
    #                 q.append(end)
    #                 seen.add(end)
    #     return False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[usage of word dict][feasibity of sub str of s]
        dp = [False for j in range(len(s)+1)]
        dp[0] = True
        
        for j in range(len(s)+1):
            for i in range(len(wordDict)):
                word = wordDict[i]
                # print(i, j)
                if j < len(word):
                    continue
                if dp[j-len(word)] == True and s[j-len(word):j] == word:
                    dp[j] = True
        
        # print(*dp)
        
        if dp[-1] == True:
            return True
        return False
        
# @lc code=end
