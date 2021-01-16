class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        diff = arr[0] - arr[1]
        ans = True
        n = len(arr)
        for i in range(n-1):
            if diff != arr[i] - arr[1+i]:
                return False
        return True            
