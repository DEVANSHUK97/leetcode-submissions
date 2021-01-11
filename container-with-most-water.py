class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        left = 0
        right = n-1
        while left <= right:
            vol = min(height[left], height[right]) * (right - left)
            if ans < vol:
                ans = vol
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        return ans
    
