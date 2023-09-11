class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        result = []
        for num in nums:
            if lower < num:
                result.append([lower, num-1])
                lower = num + 1
            elif lower == num:
                lower = num + 1
            else:
                raise Exception('unexpected')
            
        if lower <= upper:
            result.append([lower, upper])
        
        return result
                
            