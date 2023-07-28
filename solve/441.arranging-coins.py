#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        allow = 0
        deny = 2**16
        
        while deny - allow > 1 :
            mid = (allow + deny)//2
            if is_allowed(mid, n):
                allow = mid
            else:
                deny = mid 
                
        return allow
    
def is_allowed(mid, n):
    return (mid * (mid+1))//2 <= n
        
        
    # def arrangeCoins(self, n: int) -> int:
    #     hight = 0
    #     row = 0
    #     while n > 0:
    #         row += 1
    #         if n >= row:
    #             n -= row
    #             hight+=1
    #             continue
    #         else:
    #             break
    #     return hight
            
# @lc code=end
