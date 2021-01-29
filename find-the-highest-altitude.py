class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        running_sum = 0
        for i in gain:
            running_sum += i
            ans = max(ans, running_sum)
        return ans
