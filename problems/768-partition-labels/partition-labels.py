class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurance = {char: i for i, char in enumerate(s)}
        partition = []
        start = end = 0
        
        for idx, char in enumerate(s):
            end = max(end, last_occurance[char])

            if idx == end:     
                partition.append(end - start + 1)
                start = idx + 1

        return partition 