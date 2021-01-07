class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        first = s[0]
        if first == '+':
            number = ''
            for i in s[1:]:
                if i not in [str(i) for i in range(10)]:
                    break
                else:
                    number = number + i
            if len(number) > 0:
                if int(number) > 2**31 - 1:
                    ans = 2**31  -1
                else:
                    ans = int(number)
            else:
                ans = 0
        elif first == '-':
            number = ''
            for i in s[1:]:
                if i not in [str(i) for i in range(10)]:
                    break
                else:
                    number = number + i
            if len(number) > 0:
                if int(number) > 2**31:
                    ans = -1*2**31
                else:
                    ans = -1*int(number)
            else:
                ans = 0
        elif first in [str(i) for i in range(10)]:
            number = ''
            for i in s:
                if i not in [str(i) for i in range(10)]:
                    break
                else:
                    number = number + i
            if len(number) > 0:
                if int(number) > 2**31 - 1:
                    ans = 2**31 - 1
                else:
                    ans = int(number)
            else:
                ans = 0
        else:
            ans = 0
        return ans
