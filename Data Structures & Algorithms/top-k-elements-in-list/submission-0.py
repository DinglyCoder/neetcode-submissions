class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        print(counts)

        ret = []

        counts = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)

        for i in range(k):
            ret.append(counts[i])

        return ret