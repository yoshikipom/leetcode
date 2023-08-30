#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_pointer = 0
        for num in nums:
            if num != val:
                nums[insert_pointer] = num
                insert_pointer += 1
        return insert_pointer
            
        
# @lc code=end
