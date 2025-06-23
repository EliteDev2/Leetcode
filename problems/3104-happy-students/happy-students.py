class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        if nums[0] > 0:
            res += 1
        if nums[-1] < len(nums):
            res += 1
        
        for i in range(len(nums) - 1):
            st = i + 1
            if nums[i] < st and nums[i + 1] > st:
                res += 1
        return res