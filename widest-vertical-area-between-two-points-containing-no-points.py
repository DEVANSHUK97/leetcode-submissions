class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xes = [loc[0] for loc in points]
        ans = 0
        xes = sorted(xes)
        n = len(xes)
        for i in range(1,n):
            if xes[i] - xes[i - 1] > ans:
                ans = xes[i] - xes[i - 1]
        return ans
            
