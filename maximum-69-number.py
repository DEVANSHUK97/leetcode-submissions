class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        l = len(s)
        ans = ''
        swaps_remaining = 1
        for i in range(l):
            if s[i]=='6' and swaps_remaining:
                ans = ans + '9'
                swaps_remaining = swaps_remaining - 1
            else:
                ans = ans + s[i]
        return int(ans)
