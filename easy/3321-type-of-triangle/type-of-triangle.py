class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b, c = nums
        # Check if the three sides can form a triangle using the triangle inequality: a + b > c
        if a + b <= c: 
            return "none"
        if a == b == c:
            return 'equilateral'
        elif a == b or b == c or a == c:
            return 'isosceles'
        else:
            return 'scalene'
        
        