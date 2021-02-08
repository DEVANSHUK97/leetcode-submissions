def abs(x):
    if x < 0:
        return -x
    return x
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        curr = points[0]
        for i in points[1:]:
            ans = ans + max(abs(i[0]-curr[0]), abs(i[1]-curr[1]))
            curr = i
        return ans
