class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x^y
        ans = 0
        while z:
            ans = ans + z%2
            z = z//2
        return ans
