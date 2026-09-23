class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals.sort()

        curr = intervals[0]

        for i in range(1, len(intervals)):

            if curr[1] >= intervals[i][0]:
                curr[1] = max(curr[1], intervals[i][1])
            else:
                ret.append(curr)
                curr = intervals[i]
        
        ret.append(curr)

        return ret