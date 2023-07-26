#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start



def numArray(s):
    done = {}
    num_array = []
    index = 0
    for c in s:
        if c in done:
            num_array.append(done[c])
        else:
            num_array.append(index)
            done[c] = index
            index += 1
    return num_array


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return numArray(s) == numArray(t)
        
# @lc code=end
