class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxlen = 1
        i = 1

        while i < len(nums):
            length = 1
            if nums[i] > nums[i - 1]:
                while i < len(nums) and nums[i] > nums[i - 1]:
                    length += 1
                    i+= 1
            elif nums[i] < nums[i - 1]:
                while i < len(nums) and nums[i] < nums[i - 1] :
                    length += 1
                    i+= 1
            else:
                i += 1
                continue
            maxlen = max(maxlen, length)
        
        return maxlen