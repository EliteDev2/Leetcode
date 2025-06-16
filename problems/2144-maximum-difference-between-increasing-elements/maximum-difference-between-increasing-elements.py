class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxdif = -1

        min_num = nums[0]

        for i in range(len(nums)):
            maxdif = max( maxdif, nums[i] - min_num)
            min_num = min(min_num, nums[i])

        return maxdif if maxdif != 0 else -1
        