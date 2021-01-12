class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        ans = ''
        n_min = min([len(s) for s in strs])
        for i in range(n_min):
            char = strs[0][i]
            mismatch = False
            for j in range(1,len(strs)):
                if strs[j][i] != char:
                    mismatch = True
                    break
            if not mismatch:
                ans = ans + char
            else:
                break
        return ans

                
