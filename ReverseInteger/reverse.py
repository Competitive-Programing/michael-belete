class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        reverse = 0
        while num > 0:
             lastDigit = num % 10  
             reverse = (reverse * 10) + lastDigit  
             num = num // 10
        if(x < 0):
            reverse = -reverse

        if (reverse >= -2147483648) and (reverse <= 2147483647):
            return reverse
        else:
            return 0