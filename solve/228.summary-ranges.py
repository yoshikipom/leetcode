#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(-1)
        prev = nums[0]
        result =[]
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                continue
            else:
                if prev == nums[i-1]:
                    result.append(str(prev))
                else:
                    result.append(f'{prev}->{nums[i-1]}')
                prev = nums[i]
        return result
                
            
            
        
# @lc code=end
