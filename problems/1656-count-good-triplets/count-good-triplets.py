class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        triplets = 0
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):

                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):

                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            triplets += 1
                            
        return triplets
        