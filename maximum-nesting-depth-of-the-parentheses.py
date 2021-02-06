class Solution:
    def maxDepth(self, s: str) -> int:
        total = 0
        ans = 0
        for i in s:
            if i == '(':
                ans = ans + 1
            elif i == ')':
                ans = ans - 1
            total = max(ans, total)
        return total
