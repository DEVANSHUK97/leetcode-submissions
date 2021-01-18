class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        n = len(command)
        for i in range(n):
            if command[i] == 'G':
                ans = ans + 'G'
            elif command[i] == '(':
                if i + 1 == n:
                    break
                if command[i+1] == ')':
                    ans = ans + 'o'
                elif i + 3 >= n:
                    break
                elif (command[i + 1], command[i + 2], command[i + 3]) \
                == ('a','l',')'):
                    ans = ans + 'al'
            else:
                pass
        return ans
            
