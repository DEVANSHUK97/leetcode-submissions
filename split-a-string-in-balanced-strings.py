class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        ans = []
        i = 0
        while i < n:
            r_l_counts = {}
            start = s[i]
            r_l_counts['L'] = 0
            r_l_counts['R'] = 0
            r_l_counts[s[i]] = 1
            for j in range(i+1,n):
                r_l_counts[s[j]] = r_l_counts.get(s[j], 0) + 1
                if r_l_counts['R'] == r_l_counts['L']:
                    i = j+1
                    ans.append(s[i:j+1])
                    break
        return len(ans)
            
