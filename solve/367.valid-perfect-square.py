#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid + 1
            else:
                right = mid - 1
        return False    
# @lc code=end

def main():
    val = Solution().isPerfectSquare(14)
    assert(val==False)
    val = Solution().isPerfectSquare(16)
    assert(val==True)


if __name__ == '__main__':
    main()
