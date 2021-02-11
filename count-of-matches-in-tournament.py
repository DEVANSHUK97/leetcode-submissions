class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        x = n
        while x != 1:
            if x%2 == 1:
                x = x - 1
                x = x / 2
                ans = ans + x
                x = x + 1
            else:
                x = x / 2
                ans = ans + x
        return int(ans)
