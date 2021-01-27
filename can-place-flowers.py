class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], num: int) -> bool:
        n = len(flowerbed)
        ans = 0

        if flowerbed == [0]:
            return True

        for i in range(n):
            if flowerbed[i] == 1:
                continue

            if i == 0:
                if i+1 <= n-1 and flowerbed[i+1] == 0:
                    ans = ans + 1
                    flowerbed[i] = 1
            elif i == n-1:
                if i-1 >= 0 and flowerbed[i-1] == 0:
                    ans = ans + 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    ans = ans + 1
                    flowerbed[i] = 1
        # print(flowerbed)
        return ans >= num
