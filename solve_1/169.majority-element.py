#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            print(num)
            if num not in d:
                d[num] = 0
            d[num]+=1
            if d[num] > len(nums)//2:
                return num
        
# @lc code=end
