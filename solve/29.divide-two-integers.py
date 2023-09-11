#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0:
            dividend = -dividend
            sign = -sign
        if divisor < 0:
            divisor = -divisor
            sign = -sign
            
        if divisor == 1:
            if sign < 0:
                return  sign * min(dividend, 2**31)
            return sign * min(dividend, 2**31-1)
        
        result = 0
        sub = divisor
        div_count = 1
        arr = [(sub, div_count)]
        while sub + sub <= dividend:
            sub = sub + sub
            div_count = div_count + div_count
            arr.append((sub, div_count))
            
        for sub, div_count in arr[::-1]:
            if dividend == 0:
                break
            if sub <= dividend:
                dividend -= sub
                result += div_count
                
        # while divisor <= dividend:
        #     sub = divisor
        #     div_count = 1
        #     while sub + sub <= dividend:
        #         sub = sub + sub
        #         div_count = div_count + div_count
        #     dividend -= sub
        #     result += div_count
        
        if sign < 0:
            return  sign * min(result, 2**31)
        return sign * min(result, 2**31-1)        
        
            
            
        
# @lc code=end
