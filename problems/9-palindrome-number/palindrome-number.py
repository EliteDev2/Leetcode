class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        reversed_half = 0

        while x > reversed_half:
            last_digit = x % 10 
            reversed_half = reversed_half * 10 + last_digit
            x //= 10
        # For Even | For ODD
        return x == reversed_half or x == reversed_half // 10


        