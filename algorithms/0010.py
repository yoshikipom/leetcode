class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[i, j]

            if j == len(pattern):
                memo[i, j] = i == len(text)
                return memo[i, j]

            first_match = i < len(text) and pattern[j] in {text[i], '.'}
            if j+1 < len(pattern) and pattern[j+1] == '*':
                ans = dp(i, j+2) or first_match and dp(i+1, j)
            else:
                ans = first_match and dp(i+1, j+1)
            memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
