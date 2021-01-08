class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = {}
        destn = 0
        direction = 'down'
        for char in s:
            ans[destn] = ans.get(destn,'') + char
            if destn == 0:
                destn = (destn+1)%numRows
                direction = 'down'
            elif destn == numRows - 1:
                destn = (destn-1)%numRows
                direction = 'up'
            else:
                if direction == 'up':
                    destn = (destn-1)%numRows
                else:
                    destn = (destn+1)%numRows

        return ''.join([ans.get(i,'') for i in range(numRows)])


        
