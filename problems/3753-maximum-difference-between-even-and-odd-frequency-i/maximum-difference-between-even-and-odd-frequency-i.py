class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd = 0
        even = len(s)
        for val in freq.values():
            if val % 2 == 0:
                even = min(even, val)
            else:
                odd = max(odd, val)
        return odd - even
        