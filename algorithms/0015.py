import bisect
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def exist(nums, num, i, j):
            index = bisect.bisect_left(nums, num)
            if index == len(nums):
                return False
            if nums[index] != num or index == i or index == j:
                return False
            return True

        nums.sort()
        results = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if exist(nums, -nums[i]-nums[j], i, j):
                    results.add(
                        tuple(sorted((nums[i], nums[j], -nums[i]-nums[j]))))

        return list(map(lambda x: list(x), results))


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
