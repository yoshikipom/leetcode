#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # search capacity range by binary search
        lo = -1
        hi = sum(weights)
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if has_enough_capacity(weights, days, mid):
                hi = mid
            else:
                lo = mid
        return hi
            
def has_enough_capacity(weighs: List[int], limit_days: int, capacity: int) -> bool:
    ship_days = 1
    weight_on_cargo = 0
    for weight in weighs:
        if capacity < weight:
            return False
        if capacity < weight_on_cargo + weight:
            ship_days += 1
            weight_on_cargo = 0
        weight_on_cargo += weight
    return ship_days <= limit_days
        
        
# @lc code=end
