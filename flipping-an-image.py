class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            ans = []
            for j in range(n):
                ans.append(1 - image[i][n-j-1])
            image[i] = ans
        return image
