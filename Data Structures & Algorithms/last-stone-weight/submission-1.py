class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [i * -1 for i in stones]
        heapq.heapify(maxHeap)

        print(maxHeap)

        while len(maxHeap) > 1:
            stoneOne = -1 * heapq.heappop(maxHeap)
            stoneTwo = -1 * heapq.heappop(maxHeap)

            if stoneOne > stoneTwo:
                stoneOne = stoneOne - stoneTwo
                heapq.heappush(maxHeap, -1 * stoneOne)
            elif stoneTwo > stoneOne:
                stoneTwo = stoneTwo - stoneOne
                heapq.heappush(maxHeap, -1 * stoneTwo)

        if len(maxHeap) > 0:
            return -1 * maxHeap[0]
        return 0