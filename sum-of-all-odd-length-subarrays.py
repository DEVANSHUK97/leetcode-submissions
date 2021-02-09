class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        size = 1
        while size<=n:
            for i in range(n-size + 1):
                ans = ans + sum(arr[i:i+size])
            size = size + 2
        return ans
