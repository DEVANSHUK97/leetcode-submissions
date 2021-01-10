class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x%10 == x:
            return True
        y = x
        digits = 0
        while y:
            most_significant = y%10
            y = y//10
            digits = digits + 1
        z = x
        for i in range(digits):
            leftmost = (z//(10**(digits - i - 1)))%10
            rightmost = (z//(10**(i)))%10
            # print(digits, leftmost, rightmost)
            if leftmost != rightmost:
                return False
        return True
        
