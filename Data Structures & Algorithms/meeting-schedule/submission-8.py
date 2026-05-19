"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #meeting rooms 1
        #given an array of time interval conssitng of start and end times
        #determine if a person can add all meetings to schedule
        intervals.sort(key = lambda i: i.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True