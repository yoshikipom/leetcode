class Solution:
    def maxArea(self, li: List[int]) -> int:
        l = 0
        r = len(li)-1
        result = 0

        while l < r:
            tmp = min(li[l], li[r]) * (r - l)
            result = max(result, tmp)

            if li[l] < li[r]:
                l += 1
            else:
                r -= 1
        return result
