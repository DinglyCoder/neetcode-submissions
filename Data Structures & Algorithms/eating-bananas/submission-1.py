class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minK = 1000000001

        while (l <= r):
            k = (l + r) // 2
            hours = 0
            for i in piles:
                hours += -(-i // k)

            if hours > h:
                l = k + 1
            else:
                print(f"k={k} hours={hours}")
                minK = min(minK, k)
                r = k - 1

        return minK

