class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        ans_n = -1
        n = len(s)
        for i in range(n):
            j = 0
            while i-j >= 0 and i+j < n:
                if s[i-j] != s[i+j]:
                    break
                if 2*j + 1 > ans_n:
                    ans_n = 2*j + 1
                    ans = s[i-j:i+j+1]
                j = j + 1
        for i in range(n):
            j = i + 1
            if j==n:
                break
            k = 0
            while i-k >= 0 and j+k < n:
                if s[i-k] != s[j+k]:
                    break
                if 2*k + 2 > ans_n:
                    ans_n = 2*k + 2
                    ans = s[i-k:j+k+1]
                k = k + 1
        return ans


    
