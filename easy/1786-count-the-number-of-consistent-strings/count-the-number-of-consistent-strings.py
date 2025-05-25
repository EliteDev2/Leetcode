class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # return sum([True for word in words for char in word if char in allowed])
        count = 0
        for word in words:
            for char in word:
                if char not in allowed:
                    count += 1
                    break
        return len(words) - count
            

        