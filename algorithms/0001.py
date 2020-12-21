class Solution:
    def twoSum(self, nums, target: int):
        m = {}
        for i in range(len(nums)):
            m[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in m and i != m[complement]:
                result1, result2 = i, m[complement]
                break
        return [result1, result2]


if __name__ == "__main__":
    print(Solution().twoSum([3, 2, 4], 6))
