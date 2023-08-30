#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
V = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = []
        for c in s:
            s_list.append(c)
            
        s = s_list
        
        l = 0
        r = len(s_list) - 1
        n = len(s_list)
        while l < r:
            if s[l] in V and s[r] in V:
                tmp = s[l]
                s[l] = s[r]
                s[r] = tmp
                l+=1
                r-=1
                continue
            while l < n and s[l] not in V:
                l+=1
            while 0 <= r and s[r] not in V:
                r-=1
        return ''.join(s)
        
# @lc code=end
