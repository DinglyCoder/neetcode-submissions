"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i: i.start)
        for i in intervals:
            print(i.start)
        latestMeeting = 0

        for i in range(len(intervals)):
            if (intervals[i].start < latestMeeting):
                print(f"{intervals[i].start}. {latestMeeting}")
                return False

            latestMeeting = max(latestMeeting, intervals[i].end)

        return True
