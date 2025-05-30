class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        num = n
        def digitProduct(num):
            product_of_digits = 1
            while num != 0:
                product_of_digits = product_of_digits * (num % 10)
                num //= 10
            return product_of_digits

        while num >= n:
            if digitProduct(num) % t == 0:
                return num
            num += 1
