class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        dp = [None] * n
        dp[0] = k
        dp[1] = k * k
        for i in range(2, n):
            case1 = (k-1) * dp[i-1]
            case2 = (k-1) * dp[i-2]
            dp[i] = case1 + case2
        return dp[-1]
        
