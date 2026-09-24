class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0 
        print(intervals)
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < curr[1]:
                count += 1
                # remove 1 and keep the one with the smaller end time
                if curr[1] > intervals[i][1]:
                    curr = intervals[i]
            else:
                curr = intervals[i]

        return count

