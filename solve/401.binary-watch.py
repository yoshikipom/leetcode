#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#
# @lc code=start
from itertools import combinations
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        results = []
        for arr in combinations(list(range(10)),turnedOn):
            time_str = to_str(arr)
            if time_str:
                results.append(time_str)
            # print(to_str(arr))
        return results
        
def to_str(arr: List[int]) -> str:
    minute = 0
    hour = 0
    for turned_on in arr:
        if 0 <= turned_on <= 5:
            minute += 2 ** turned_on
            # minute calc
        else:
            # hour calc
            hour += 2 ** (turned_on-6)
    
    if hour >= 12 or minute >= 60:
        return None
    return str(hour) + ":" + str(minute).zfill(2)
    
            
# @lc code=end
