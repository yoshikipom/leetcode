#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        divs = []
        for i in range(1, int(area ** (1/2))+1):
            if area % i == 0:
                divs.append(i)
        
        min_diff = area
        result = [1, area]
        for l in divs:
            w = area // l
            if abs(l-w) < min_diff:
                min_diff = abs(l-w)
                result = [l, w]
        return sorted(result)[::-1]
            
        
        
# @lc code=end
