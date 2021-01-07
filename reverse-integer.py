class Solution:
    def reverse(self, x: int) -> int:
        sign = '+'
        if x < 0:
            sign = '-'
            ans = int((str(-1*x))[::-1])
            if (ans) > 2**31:
                return 0
            return -1*ans
        else:
            ans = int((str(x))[::-1])
            if (ans) > 2**31 - 1:
                return 0
            return ans
