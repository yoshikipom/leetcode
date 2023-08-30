#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for num in nums1:
            if num not in d:
                d[num] = 0
            d[num] += 1
        
        result = []
        for num in nums2:
            if num in d:
                result.append(num)
                d[num] -= 1
                if d[num] == 0:
                    del d[num]
        return result
                
            
        
# @lc code=end
