class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        strs.sort(key=lambda x: len(x))
        prefix = ''
        done = False
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != c:
                    done = True
                    break
            if done:
                break
            else:
                prefix += c

        return prefix
