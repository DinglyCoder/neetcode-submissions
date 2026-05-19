class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        print(counts)

        ret = []

        # counts = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        counts = counts.most_common(k)

        for num, count in counts:
            ret.append(num)

        return ret