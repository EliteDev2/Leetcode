class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        max_count = 0
        for val in range(1, n+1):
            sum = 0
            while val > 0:
                sum += val % 10
                val //= 10
            count[sum] += 1
            max_count = max(max_count, count[sum])
        
        ans = 0
        for key in count:
            ans += count[key] == max_count # True resolved to 1 , False -> 0
        return ans
            