class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = ""
        n = len(S)
        i = 0
        while i < n - 1:
            if S[i] == '(' and S[i + 1] == '(':
                ans.append(S[i])
                i = i + 1
            elif S[i] == ')' and S[i + 1] == ')':
                ans.append(S[i])
                i = i + 1
            else:
                ans.append(S[i])
            i = i + 1
        return ans
