class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        ans = 2*0 + start
        for i in range(1,n):
            ans = ans ^ (2*i + start)
        return ans
