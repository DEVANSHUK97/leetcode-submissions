class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            if len(set(word) - set(allowed)) == 0:
                ans = ans + 1
        return ans
