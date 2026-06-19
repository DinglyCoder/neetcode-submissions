"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        running = []
        maxRooms = 0

        intervals.sort(key =lambda x: x.start)

        for i in range(len(intervals)):

            j = 0
            while j < len(running):
                if running[j].end <= intervals[i].start:
                    running.pop(j)
                else:
                    j += 1
            
            running.append(intervals[i])
            maxRooms = max(maxRooms, len(running))

        return maxRooms

        