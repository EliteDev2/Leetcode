class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 0
        diff = float('inf') #max int
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) -1
            while j < k:
                psum = nums[i] + nums[j] + nums[k]
                if psum == target:
                    return psum
                    
                tmp = abs(psum - target)
                if tmp < diff:
                    diff = tmp
                    closest = psum
                if psum < target:
                    j += 1
                else:
                    k -= 1

        return closest

                



        